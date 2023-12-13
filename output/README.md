O aplicativo gerará os arquivos de saída nesta pasta:
- Arquivo `%Y-%m.pdf`: contém os crachás para impressão. `%Y` é o ano e `%m`, o mês aos quais os crachás referem-se (geralmente usa-se o aplicativo para gerar os crachás do próximo mês, mas qualquer ano/mês pode ser escolhido na interface gráfica).
- Arquivo `%Y-%m.secrets.xlsx`: contém o segredo, gerado aleatoriamente, associado a cada titular. Esse segredo pode ser lido no _QR code_ e confrontado com essa planilha para identificar fraudes.
