# yellowPagesIQ

Scrape company details from the Iraqi business directory
[yellowpages.com.iq](http://www.yellowpages.com.iq) into a CSV file.

For each company the scraper collects the name, category, address fields and
contact details.

## Requirements

- Python 3

Install the dependencies:

```sh
pip install -r requirements.txt
```

## Usage

```sh
python main.py
```

Results are appended to `IraqCompanyInformation.csv`. If a run is interrupted,
the last processed id is printed so it can be resumed.

## License

Released under the [GPL-3.0](LICENSE.md) license.
