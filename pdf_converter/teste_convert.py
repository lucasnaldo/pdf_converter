import pdftables_api

c = pdftables_api.Client('jnutwuhlq3r5')
c.xlsx('Fatura.pdf', 'Fatura.xlsx')
# c.csv('Fatura.pdf', 'Fatura.csv')
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML