# Web Scraping Project

This project contains Python scripts for scraping product information from three popular e-commerce websites: Amazon, Flipkart, and Snapdeal. The scripts retrieve product names and prices, and then compare them to determine the lowest price among the three platforms.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Scripts Overview](#scripts-overview)
  - [DatascrapingofAmazon.py](#datascrapingofamazonpy)
  - [DatascrapingofFlipcart.py](#datascrapingofflipcartpy)
  - [DatascrapingofSnapdeal.py](#datascrapingofsnapdealpy)
  - [endproduct.py](#endproductpy)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `tabulate` library (for table formatting)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

## Installation

2. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 tabulate
   ```

# Scripts Overview
### DatascrapingofAmazon.py
This script scrapes product names and prices from a specified Amazon product URL. It utilizes BeautifulSoup to parse the HTML content and retrieves relevant product details.

### DatascrapingofFlipcart.py
This script retrieves product names and prices from a specified Flipkart product URL. It also uses BeautifulSoup for HTML parsing and displays the product information.

### DatascrapingofSnapdeal.py
This script is designed to scrape product names and prices from a specified Snapdeal product URL, using BeautifulSoup for HTML content extraction.

### endproduct.py
This script combines the scraping functionality for Amazon, Flipkart, and Snapdeal into one cohesive script. It prompts the user to input product URLs for each site, retrieves the product names and prices, and then compares the prices to determine the lowest among the three platforms. The results are displayed in a formatted table using the tabulate library.

## Usage
To run any of the individual scripts, execute them in your terminal or command prompt:

```bash
python DatascrapingofAmazon.py
```

```bash
python DatascrapingofFlipcart.py
```

```bash
python DatascrapingofSnapdeal.py
```

## To run the complete price comparison script, execute:
```bash
python endproduct.py
```

-You will be prompted to enter the product URLs for Amazon, Flipkart, and Snapdeal. The script will then output the product names and prices, along with the lowest price among the three.
