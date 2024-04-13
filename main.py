# Importando Modulos

from bs4 import BeautifulSoup
import requests


def get_product_price():
    url = 'https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/ref=bmx_dp_5kl4ezon_d_sccl_3_1/139-0810955-0548326?pd_rd_w=PDZ4r&content-id=amzn1.sym.628e3119-8afd-4af2-be6b-18415b51e649&pf_rd_p=628e3119-8afd-4af2-be6b-18415b51e649&pf_rd_r=1J9HBCTCPP5A7GJ3RZBX&pd_rd_wg=YulZV&pd_rd_r=b2fa3ebf-3da5-46b0-b9a5-1c2ea86bd7e5&pd_rd_i=1119002257&psc=1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    price = soup.find(class_="a-offscreen").get_text()

    return price


try:
    product_price = get_product_price()
    print(f"O preço do produto é: {product_price}")
except Exception as e:
    print("Ocorreu um erro ao obter o preço do produto:", e)
