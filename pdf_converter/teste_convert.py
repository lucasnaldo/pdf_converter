import pdftables_api
import datetime
import easygui
import os

arquivo = easygui.fileopenbox()
inputFilepath = arquivo
filename_w_ext = os.path.basename(inputFilepath)
filename, file_extension = os.path.splitext(filename_w_ext)
saida = (filename + '_Corrigido.xlsx')

c = pdftables_api.Client('jnutwuhlq3r5')
# dt = str(datetime.datetime.now().strftime("%Y%m%d"))
# filename = '{}_convertido.xlsx'.format(dt)

c.xlsx(arquivo, saida) 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML