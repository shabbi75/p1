import slate
import re
import glob
from os.path import basename, splitext, join


def main():
    for pdf in glob.glob('./data/*.pdf'):
        name = splitext(basename(pdf))[0]
        save_text(join('..', 'data', name + '.txt'), get_text(pdf))

def save_text(filepath, text):
    with open(filepath, 'w+') as fout:
        fout.write(text)

def get_text(filepath):
    fulltext = ''
    with open(filepath) as f:
        doc = slate.PDF(f)
        for text in doc:
            pattern=re.compile("[^\w']")
            fulltext += pattern.sub(' ', text)
    return fulltext








if __name__ == "__main__":
    main()
