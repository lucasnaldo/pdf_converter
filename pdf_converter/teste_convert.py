import pdftables_api
import datetime
import easygui
import os
import PyPDF2
import json

arquivo = easygui.fileopenbox()
# filename_w_ext = os.path.basename(arquivo)
# filename, file_extension = os.path.splitext(filename_w_ext)
# saida = (filename + '_Corrigido.csv')

read_pdf = PyPDF2.PdfFileReader(arquivo)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
# page_content
# print(page_content)


data = json.dumps(page_content)
formatj = json.loads(data)
print (formatj)
# def get_data(page_content):
#     _dict = {}
#     page_content_list = page_content.splitlines()
#     for line in page_content_list:
#         if ':' not in line:
#             continue
#         key, value = line.split(':')
#         _dict[key.strip()] = value.strip()
#     return _dict

# print(json.dumps(get_data(page_content), indent=4))






"""
c = pdftables_api.Client('jnutwuhlq3r5')
# dt = str(datetime.datetime.now().strftime("%Y%m%d"))
# filename = '{}_convertido.xlsx'.format(dt)

c.csv(arquivo, saida) 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

"""