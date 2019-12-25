# -*- coding: utf-8 -*-
import os.path
import shutil
import xml.etree.ElementTree as ET


def replace_text(text):
    # todo: Add candrabindu!
    text = text.replace("", "fi")
    text = text.replace("", "fl")
    text = text.replace("ä", "ā")
    text = text.replace("é", "ī")
    text = text.replace("ü", "ū")
    text = text.replace("å", "ṛ")
    text = text.replace("è", "ṝ")
    text = text.replace("ì", "ṅ")
    text = text.replace("ñ", "ṣ")
    text = text.replace("ï", "ñ")
    text = text.replace("ö", "ṭ")
    text = text.replace("ò", "ḍ")
    text = text.replace("ë", "ṇ")
    text = text.replace("ç", "ś")
    text = text.replace("à", "ṁ")
    text = text.replace("ù", "ḥ")
    text = text.replace("ÿ", "ḷ")
    text = text.replace("û", "ḹ")
    text = text.replace("Ä", "Ā")
    text = text.replace("É", "Ī")
    text = text.replace("Ü", "Ū")
    text = text.replace("Å", "Ṛ")
    text = text.replace("È", "Ṝ")
    text = text.replace("Ì", "Ṅ")
    text = text.replace("Ñ", "Ṣ")
    text = text.replace("Ï", "Ñ")
    text = text.replace("Ö", "Ṭ")
    text = text.replace("Ò", "Ḍ")
    text = text.replace("Ë", "Ṇ")
    text = text.replace("Ç", "Ś")
    text = text.replace("À", "Ṁ")
    text = text.replace("Ù", "Ḥ")
    text = text.replace("ß", "Ḷ")
    return text


def xml_to_unicode(tree):
    namespace = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    root = tree.getroot()
    #t.getroot().findall('.//w:t', namespace)
    # TODO: To write back we need the reference to the XML node here.
    # In ElementTree nodes do not have a reference to their parent,
    # thus we have nodes disconnected from the tree when searching with .//w:t
    # => use a different XML library!!!
    for elem in root.getiterator():
        try:
            elem.find('.//w:t', namespace)
            t = replace_text(elem.text)
            elem.text = t

        except AttributeError:
            pass
    return tree


def process_docx(file_path, user_name, file_name, download_folder):
    temp_unzipped = 'temp_unzipped'
    os.getcwd()
    if os.path.exists(temp_unzipped):
        clean_directory(os.path.realpath(temp_unzipped))
    else:
        os.mkdir(temp_unzipped)
    os.chdir(temp_unzipped)
    os.system('unzip ' + os.path.join('..', file_path))
    docx_mapping()
    #pdb.set_trace()
    parts = file_name.split('.')
    file_name = '.'.join(parts[:-1])
    output_path = os.path.join(download_folder, user_name, file_name + '_processed.docx')
    os.system('zip -r ' + output_path + ' *')
    return file_name + '_processed.docx'

def docx_mapping():
    xml_path = 'word'
    document_parts = ['footnotes', 'document']

    filenames = []
    for d_part in document_parts:
        filenames.append(os.path.join(xml_path, d_part + '.xml'))

    for inpath in filenames:
        (folder, fname) = os.path.split(inpath)
        outfile = '_' + fname
        outpath = os.path.join(folder, outfile)

        with open(inpath, encoding='utf8') as f:
            tree = ET.parse(f)
            tree = xml_to_unicode(tree)
            tree.write(outpath, xml_declaration=True,
                       method='xml', encoding="utf8")

        shutil.copy2(outpath, inpath)
        os.remove(outpath)



def clean_directory(folder):
    if not os.path.exists(folder):
        return
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def rezip(docx_path):
    #pdb.set_trace()
    output_docx = os.path.join('..', docx_path + '_rezipped.docx')
    os.system('zip -r ' + output_docx + ' *')


def main(docx_path):
    temp_unzipped = 'temp_unzipped'
    try:
        os.mkdir(temp_unzipped)
    except FileExistsError:
        pass
    os.chdir(temp_unzipped)
    os.system('unzip ' + os.path.join('..', docx_path))
    docx_mapping()
    rezip(docx_path)


if __name__ == '__main__':
    main('docs/HNV_test.docx')



# quick and dirty script
"""
mkdir unzipped
cd unzipped # ??
unzip ../HNV_test.docx
sed 's/ç/ś/g' < word/footnotes.xml > word/_footnotes.xml
sed 's/ä/ā/g' < word/_footnotes.xml > word/footnotes.xml
#...
zip -r ../HNV_test_rezipped.docx *
"""
