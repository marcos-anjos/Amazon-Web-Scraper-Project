"""
Módulo para obter o preço de um produto na Amazon.

Este módulo contém uma função para obter o preço de um produto na Amazon usando web scraping.

Funções:
    get_product_price(): Obtém o preço do produto na Amazon.

Exemplo:
    try:
        product_price = get_product_price()
        print(f"O preço do produto é: {product_price}")
    except Exception as e:
        print("Ocorreu um erro ao obter o preço do produto:", e)
"""

from bs4 import BeautifulSoup
import requests

def get_product_price():
    """
    Obtém o preço de um produto na Amazon.

    Retorna:
        str: O preço do produto.
        
    Raises:
        Exception: Se houver um erro ao obter o preço do produto.
    """
    # URL do produto na Amazon
    url = 'https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/ref=bmx_dp_5kl4ezon_d_sccl_3_1/139-0810955-0548326?pd_rd_w=PDZ4r&content-id=amzn1.sym.628e3119-8afd-4af2-be6b-18415b51e649&pf_rd_p=628e3119-8afd-4af2-be6b-18415b51e649&pf_rd_r=1J9HBCTCPP5A7GJ3RZBX&pd_rd_wg=YulZV&pd_rd_r=b2fa3ebf-3da5-46b0-b9a5-1c2ea86bd7e5&pd_rd_i=1119002257&psc=1'
    
    # Cabeçalhos da solicitação HTTP
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }

    # Envia uma solicitação GET para a URL usando os cabeçalhos especificados
    response = requests.get(url, headers=headers)
    
    # Analisa o conteúdo HTML da resposta usando BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")

    # Encontra o elemento HTML que contém o preço do produto
    price = soup.find(class_="a-offscreen").get_text()

    return price

# Tenta obter o preço do produto e imprime na tela
try:
    product_price = get_product_price()
    print(f"O preço do produto é: {product_price}")
# Captura e imprime qualquer erro que ocorra durante a obtenção do preço do produto
except Exception as e:
    print("Ocorreu um erro ao obter o preço do produto:", e)

