import requests
from bs4 import BeautifulSoup

def scrape_snapdeal_product(url):
    try:
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_name = soup.find('h1', {'class': 'pdp-e-i-head'}).text.strip()
        product_price = soup.find('span', {'class': 'payBlkBig'}).text.strip()
        
        print('Product Name:', product_name)
        print('Product Price:', product_price)
    except Exception as e:
        print('Error:', str(e))

if __name__ == "__main__":
    url ="https://www.snapdeal.com/product/veirdo-green-half-sleeve-tshirt/639827458615"
    #Paste the product URL of the snapdeal.
    scrape_snapdeal_product(url)
