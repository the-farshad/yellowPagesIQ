"""Scrape company details from yellowpages.com.iq into a CSV file."""

import csv

import bs4
import requests

BASE_URL = "http://www.yellowpages.com.iq/search-result.php?id="
OUTPUT_FILE = "IraqCompanyInformation.csv"
# Unknown company ids redirect back to the index page with this script.
REDIRECT_SCRIPT = "window.location.href='index.php';"


def build_header():
    header = [None] * 30
    header[0:9] = [
        "Company Name", "Category", "Landmark", "Building", "Street",
        "City", "Country", "Mobile", "Mobile", "Email",
    ]
    header[20:] = [
        "Company Name", "Founded", "Mobile", "Phone", "Website", "Email",
        "Views",
    ]
    return header


def scrape():
    session = requests.Session()
    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(build_header())
        company_id = 1
        try:
            for company_id in range(1, 10600):
                page = session.get(BASE_URL + str(company_id))
                soup = bs4.BeautifulSoup(page.content, "lxml")
                if soup.select("script")[0].text == REDIRECT_SCRIPT:
                    continue

                row = [None] * 30
                row[0] = soup.find("h2").text
                row[1] = soup.find("h5").text

                counter = 2
                for span in soup.select("div p span"):
                    text = span.text
                    if not text:
                        continue
                    index = text.find(":")
                    row[counter] = text[index + 1:] if index != -1 else text
                    counter += 1

                counter = 20
                for span in soup.select("div ul li span"):
                    row[counter] = span.text
                    counter += 1

                cleaned = []
                for value in row:
                    if isinstance(value, str):
                        value = value.strip()
                        if value == "---":
                            value = ""
                    cleaned.append(value)
                writer.writerow(cleaned)
                print(company_id)
        except Exception as error:
            # Print the id reached so the run can be resumed from here.
            print(f"Stopped at id={company_id}: {error}")


if __name__ == "__main__":
    scrape()
