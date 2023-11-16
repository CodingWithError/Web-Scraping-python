import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_amazon_product(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
        }
        status_code = 503

        while status_code != 200:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                product_name = soup.find('span', class_='a-size-large product-title-word-break')
                price_element = soup.find('span', class_='a-price-whole')
                if price_element:
                    return product_name.get_text().strip()[:50], price_element.get_text().strip()

    except Exception as e:
        return None, str(e)

def scrape_snapdeal_product(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_name = soup.find('h1', {'class': 'pdp-e-i-head'}).text.strip()
        product_price = soup.find('span', {'class': 'payBlkBig'}).text.strip()
        return product_name[:50], product_price

    except Exception as e:
        return None, str(e)


def scrape_flipkart_product(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        product_name_element = soup.find("span", {"class": "B_NuCI"})
        product_price_element = soup.find("div", {"class": "_30jeq3 _16Jk6d"})

        name_flipkart = product_name_element.text.strip() if product_name_element else None
        price_flipkart = product_price_element.text.strip() if product_price_element else None

        if price_flipkart:
            price_flipkart = price_flipkart.replace('₹', '').replace(',', '')

        return name_flipkart[:50], price_flipkart
    except Exception as e:
        return None, str(e)

# Get Amazon, Snapdeal, and Flipkart URLs from the user
amazon_url = input("Enter the Amazon product URL: ")
snapdeal_url = input("Enter the Snapdeal product URL: ")
flipkart_url = input("Enter the Flipkart product URL: ")

# Scrape data from all three websites
amazon_product_name, amazon_product_price = scrape_amazon_product(amazon_url)
snapdeal_product_name, snapdeal_product_price = scrape_snapdeal_product(snapdeal_url)
flipkart_product_name, flipkart_product_price = scrape_flipkart_product(flipkart_url)

# Calculate the lowest price and the corresponding website
if amazon_product_price and snapdeal_product_price:
    amazon_price = float(amazon_product_price.replace(',', ''))
    snapdeal_price = float(snapdeal_product_price.replace(',', ''))

    if flipkart_product_price:
        try:
            flipkart_price = float(flipkart_product_price.replace(',', ''))
        except ValueError:
            flipkart_price = float('inf')
    else:
        flipkart_price = float('inf')

    min_price = min(amazon_price, snapdeal_price, flipkart_price)
    if min_price == amazon_price:
        lowest_price_website = "Amazon"
    elif min_price == snapdeal_price:
        lowest_price_website = "Snapdeal"
    else:
        lowest_price_website = "Flipkart"
else:
    lowest_price_website = "N/A"

# Create a list of lists with the data for all three websites
table_data = [
    ['Website', 'Product Name', 'Product Price'],
    ['Amazon', amazon_product_name, amazon_product_price],
    ['Snapdeal', snapdeal_product_name, snapdeal_product_price],
    ['Flipkart', flipkart_product_name, flipkart_product_price],
    ['Comparison', '', f'Lowest Price: {lowest_price_website}']
]

# Use tabulate to format the table with wrapped text within the cells
table = tabulate(table_data, headers='firstrow', tablefmt='grid')

# Display the table
print(table)