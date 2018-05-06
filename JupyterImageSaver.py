import sys
import re
import codecs
import base64
import hashlib

from bs4 import BeautifulSoup

regex_base64src = re.compile("data:image\/([a-zA-Z]*);base64,(.*=)")

def main(notebook, outdir="./images"):

    notebook = codecs.open(notebook, 'r', 'utf-8')
    soup = BeautifulSoup(notebook.read(), "html.parser")

    fileid = 0

    for image in soup.findAll("img"):

        base64match = regex_base64src.search(image["src"])

        if base64match:
            image_format = base64match.group(1)
            image_data = base64match.group(2).replace('%0A','')

            filename = '{}/base64-img-{}.{}'.format(outdir, fileid, image_format)
            filedata = base64.b64decode(image_data)
            with open(filename, 'wb') as f:
                f.write(filedata)
        else:
            filename = image["src"]

        print(filename)
        fileid = fileid + 1

if __name__ == '__main__':
    main(sys.argv[1])