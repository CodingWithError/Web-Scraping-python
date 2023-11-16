import requests
from bs4 import BeautifulSoup

def scrape_flipcart_product(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' , "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_name = soup.find('span', {'class': 'B_NuCI'}).text.strip()
        product_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.strip()
        
        print('Product Name:', product_name)
        print('Product Price:', product_price)
    except Exception as e:
        print('Error:', str(e))

if __name__ == "__main__":
    url ="https://www.flipkart.com/vbuyz-women-kurta-trouser-set/p/itma73b456672d89?pid=SWDG3TVW9WJBVHVG&lid=LSTSWDG3TVW9WJBVHVGEHSOAX&marketplace=FLIPKART&store=clo%2Fcfv&srno=b_1_1&otracker=browse&fm=organic&iid=en_ZJ8VXo0qkuIsTYsMPPFIndOvp-m0NJNnjARFM4kfEvEbDDBGnvUZozjGuqH0uhUIHztMFYTb3fTQaowFn1lMLw%3D%3D&ppt=browse&ppn=browse&ssid=xlwjsj1i9s0000001699096661063"
    #Paste the product URL of the Flipcart.
    scrape_flipcart_product(url)