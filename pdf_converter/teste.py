import io
import json
import os
import csv
import codecs

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    # for xxx in fp:
    #     print(xxx)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                #   password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filename = ('teste.csv')
    # out_csv = ('teste2.csv')
    f = open(filename, 'wt', encoding='utf-8', newline='')
    f.write(u'\uFEFF')
    for line in text:
        if text.find == None    :
            f.write(u'\uFEFF')
        else:
            f.write(line)
    # print(type(text))
    # print(text)
    # result = text.find('') 
    # print ("Substring found at index:", result )
    f.close()
    fp.close()
    # with open(path,'r') as fin:
    #     dr = csv.DictReader(fin, delimiter='\t')

    # # dr.fieldnames contains values from first row of `f`.
    # with open(out_csv,'wb') as fou:
    #     dw = csv.DictWriter(fou, delimiter='\t', fieldnames=dr.fieldnames)
    #     headers = {} 
    #     for n in dw.fieldnames:
    #         headers[n] = n
    #     dw.writerow(headers)
    #     for row in dr:
    #         dw.writerow(row)
    
    # fou.close()
    device.close()
    retstr.close()
    return text


if __name__ == '__main__':
    pdf_path = ('Fatura.pdf')
    convert_pdf_to_txt(pdf_path)
