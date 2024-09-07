# Amazon Web Scraper Project

## Introdução

Este projeto visa criar um web scraper em Python para extrair informações de preços de um produto específico na Amazon. Utilizando as bibliotecas BeautifulSoup e Requests, o código se conecta ao site da Amazon, recupera o título e o preço do produto e os armazena em um arquivo CSV. Além disso, é implementada uma função para verificar periodicamente o preço do produto e atualizar o arquivo CSV com os dados mais recentes.

## Web Scraping

O processo de web scraping é realizado utilizando as seguintes bibliotecas:

- **BeautifulSoup**: Para parsear e extrair dados do HTML.
- **Requests**: Para realizar requisições HTTP e recuperar o conteúdo da página.

### Funcionamento

1. **Coleta de Dados**: O scraper acessa a página do produto na Amazon e extrai o título e o preço do produto.
2. **Armazenamento**: Os dados extraídos são armazenados em um arquivo CSV.
3. **Atualização Periódica**: O scraper é configurado para verificar periodicamente o preço do produto e atualizar o arquivo CSV com as informações mais recentes.

## Motivação/Objetivo

- **Acompanhamento de Preços**: Monitorar e registrar os preços de um produto específico na Amazon ao longo do tempo, permitindo aos usuários acompanhar flutuações de preço e tomar decisões informadas sobre quando comprar.
- **Automação e Eficiência**: Automatizar o processo de monitoramento de preços, economizando tempo e esforço, e fornecendo atualizações regulares sem necessidade de verificação manual.

## Contexto

O código desenvolvido é aplicável a uma ampla variedade de produtos vendidos na Amazon. Ele oferece uma solução eficiente para usuários interessados em monitorar e analisar os preços de produtos específicos ao longo do tempo, fornecendo insights valiosos para tomada de decisões de compra.

## Limitações

- **Variação de Preços**: Os preços dos produtos na Amazon podem variar frequentemente devido a promoções, descontos sazonais e outros fatores. Portanto, os dados coletados refletem os preços no momento da extração e podem não representar o preço final de compra.
- **Dependência de Conexão com a Internet**: O funcionamento adequado do web scraper depende da disponibilidade de conexão com a internet e da acessibilidade do site da Amazon. Interrupções na conexão ou mudanças na estrutura do site podem afetar a capacidade do scraper de coletar dados com precisão.

## Fontes

- [Storytelling with Data: A Data Visualization Guide for Business Professionals](link)
- [Book](link)

