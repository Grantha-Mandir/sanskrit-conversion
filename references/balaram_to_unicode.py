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


def main(docx_path):
    temp_unzipped = 'temp_unzipped'
    try:
        os.mkdir(temp_unzipped)
    except FileExistsError:
        pass
    os.chdir(temp_unzipped)
    os.system('unzip ' + os.path.join('..', docx_path))

    xml_path = 'word'
    document_parts = ['footnotes']#, 'footnotes', 'document']

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

    import pdb; pdb.set_trace()
    output_docx = os.path.join('..', docx_path + '_rezipped.docx')
    os.system('zip -r ' + output_docx + ' *')


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
