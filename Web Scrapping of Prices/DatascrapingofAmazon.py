import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' , "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}
        status_code=503
        while(status_code!=200):
            response = requests.get(url, headers=headers)
            if response.status_code==200:
                soup = BeautifulSoup(response.content, 'html.parser')
                product_name=soup.find('span', class_='a-size-large product-title-word-break')
                price_element =soup.find('span', class_='a-price-whole')
                if price_element:
                    print(product_name.get_text().strip())
                    print(price_element.get_text().strip())
                    break
                    
    except Exception as e:
        return f"Error: {str(e)}"

Url='https://www.amazon.in/Amazon-Brand-Symbol-Length-_SY-A23-MNA-SKT-343_Mustard_XL/dp/B0CG225R9F/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.4c4afd42-5285-4b7a-8785-767d6ff21e87&pd_rd_r=c573bb7e-a38e-42f3-8d4a-52b36284113a&pd_rd_w=7Eh9x&pd_rd_wg=NHouZ&pf_rd_p=4c4afd42-5285-4b7a-8785-767d6ff21e87&pf_rd_r=EDWG5J02JVNY8E874HVX&qid=1699098383&refinements=p_85%3A10440599031%2Cp_n_pct-off-with-tax%3A27060456031&rnid=2665398031&rps=1&s=apparel&sr=1-2'
#Enter the URl of the product.
scrape_amazon_product(Url)