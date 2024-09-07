<div align="center">
    <h1>Rastreamento Automatizado de Preços na Amazon</h1>
  
  <div align="center">
      <img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" />
      <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"></a>
      <a href="#"><img alt="Requests" src="https://img.shields.io/badge/Requests-FF6F00?style=for-the-badge&logo=requests&logoColor=white"></a>
      <a href="#"><img alt="BeautifulSoup" src="https://img.shields.io/badge/BeautifulSoup-FFD700?style=for-the-badge&logo=beautifulsoup&logoColor=black"></a>
  </div>

<h3>Amazon Web Scraper Project</h3>
  
<p>Este projeto cria um web scraper em Python para extrair e monitorar preços de produtos na Amazon. Utilizando BeautifulSoup e Requests, o scraper coleta o título e o preço do produto, armazena em CSV e atualiza periodicamente as informações.</p>

</div>


## <a name="table">Súmario</a>

1. [Introdução](#introdução)
2. [Web Scraping](#web-scraping)
3. [Funcionamento](#funcionamento)
4. [Motivação/Objetivo](#motivação-objetivo)
5. [Contexto](#contexto)
6. [Limitações](#limitações)
7. [Fontes](#fontes)

## <a name="introdução">Introdução</a>

<body>
    <p style="text-align: justify;">
        Este projeto visa criar um web scraper em Python para extrair informações de preços de um produto específico na Amazon. Utilizando as bibliotecas BeautifulSoup e Requests, o código se conecta ao site da Amazon, recupera o título e o preço do produto e os armazena em um arquivo CSV. Além disso, é implementada uma função para verificar periodicamente o preço do produto e atualizar o arquivo CSV com os dados mais recentes.
    </p>
</body>

## <a name="web-scraping">Web Scraping</a>

O processo de web scraping é realizado utilizando as seguintes bibliotecas:

- **BeautifulSoup**: Para parsear e extrair dados do HTML.
- **Requests**: Para realizar requisições HTTP e recuperar o conteúdo da página.

## <a name="funcionamento">Funcionamento</a>

- **Coleta de Dados**: O scraper acessa a página do produto na Amazon e extrai o título e o preço do produto.
- **Armazenamento**: Os dados extraídos são armazenados em um arquivo CSV.
- **Atualização Periódica**: O scraper é configurado para verificar periodicamente o preço do produto e atualizar o arquivo CSV com as informações mais recentes.

## <a name="motivação-objetivo">Motivação/Objetivo</a>

- **Acompanhamento de Preços**: Monitorar e registrar os preços de um produto específico na Amazon ao longo do tempo, permitindo aos usuários acompanhar flutuações de preço e tomar decisões informadas sobre quando comprar.
- **Automação e Eficiência**: Automatizar o processo de monitoramento de preços, economizando tempo e esforço, e fornecendo atualizações regulares sem necessidade de verificação manual.

## <a name="contexto">Contexto</a>

O código desenvolvido é aplicável a uma ampla variedade de produtos vendidos na Amazon. Ele oferece uma solução eficiente para usuários interessados em monitorar e analisar os preços de produtos específicos ao longo do tempo, fornecendo insights valiosos para tomada de decisões de compra.

## <a name="limitações">Limitações</a>

- **Variação de Preços**: Os preços dos produtos na Amazon podem variar frequentemente devido a promoções, descontos sazonais e outros fatores. Portanto, os dados coletados refletem os preços no momento da extração e podem não representar o preço final de compra.
- **Dependência de Conexão com a Internet**: O funcionamento adequado do web scraper depende da disponibilidade de conexão com a internet e da acessibilidade do site da Amazon. Interrupções na conexão ou mudanças na estrutura do site podem afetar a capacidade do scraper de coletar dados com precisão.

## <a name="fontes">Fontes</a>

- **Storytelling with Data: A Data Visualization Guide for Business Professionals** (Book)
