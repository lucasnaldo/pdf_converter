from slate import PDF
from tempfile import mktemp
...

output_name = mktemp() + ".txt"

with open(url, 'rb') as pdf_file, open(output_name, 'wt') as output:
    doc = PDF(pdf_file)
    for page in doc:
        output.write(page + '\n')