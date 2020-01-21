# -*- coding: utf-8 -*-
import os.path
import shutil
import xml.etree.ElementTree as ET



def get_balaram_mapping():
    # todo: Add candrabindu!
    balaram_map = {"": "fi", "": "fl", "ä": "ā","é": "ī","ü": "ū","å": "ṛ","è":"ṝ",
                   "ì":"ṅ","ñ": "ṣ" ,"ï": "ñ", "ö": "ṭ","ò": "ḍ","ë": "ṇ","ç": "ś",
                   "à": "ṁ","ù": "ḥ", "ÿ":"ḷ","û": "ḹ","Ä": "Ā","É": "Ī","Ü": "Ū",
                   "Å": "Ṛ","È": "Ṝ", "Ì": "Ṅ","Ñ": "Ṣ","Ï":"Ñ","Ö": "Ṭ","Ò":
                       "Ḍ","Ë": "Ṇ","Ç":"Ś","À":"Ṁ","Ù":"Ḥ","ß":"Ḷ" }
    return balaram_map

def read_ruchi_mapping():
    mappings = [dict(), dict(), dict()]
    with open(os.path.abspath('../ruchi_mapping.tsv')) as f:
        for count,line in enumerate(f):
            parts = line.strip().split('\t')
            if len(parts)<5 or count==0:
                continue
            if parts[4]=='':
                continue
            cols = parts[1:4]
            for count,c in enumerate(cols):
                mappings[count][c] = parts[4]
    return mappings


#ToDo: Memoize this
def get_kruti_mapping():
    mappings = read_ruchi_mapping()
    return mappings[1]

#ToDo: Memoize this
def get_wc901_mapping():
    mappings = read_ruchi_mapping()
    return mappings[2]

#ToDo: Memoize this
def get_rmd_mapping():
    mappings = read_ruchi_mapping()
    return mappings[0]


def xml_to_unicode(tree, map_name):
    def replace_text(text, mapping):
        ignore = {''}
        for ch in mapping:
            if ch not in ignore:
                text = text.replace(ch, mapping[ch])
        return text

    namespace = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    root = tree.getroot()
    #t.getroot().findall('.//w:t', namespace)
    # TODO: To write back we need the reference to the XML node here.
    # In ElementTree nodes do not have a reference to their parent,
    # thus we have nodes disconnected from the tree when searching with .//w:t
    # => use a different XML library!!!

    if map_name=='balaram':
        mapping = get_balaram_mapping()
    elif map_name=='krutidev':
        mapping = get_kruti_mapping()
    elif map_name=='wc901':
        mapping = get_wc901_mapping()
    elif map_name=='rm_devanagiri':
        mapping = get_rmd_mapping()
    else:
        raise NotImplementedError(f'{map_name} not implmented.')

    for elem in root.getiterator():
        try:
            elem.find('.//w:t', namespace)
            t = replace_text(elem.text, mapping)
            elem.text = t

        except AttributeError:
            pass
    return tree


def process_docx(file_path, user_name, file_name, download_folder, map_name='balaram'):
    temp_unzipped = 'temp_unzipped'
    os.getcwd()
    if os.path.exists(temp_unzipped):
        clean_directory(os.path.realpath(temp_unzipped))
    else:
        os.mkdir(temp_unzipped)
    os.chdir(temp_unzipped)
    os.system('unzip ' + os.path.join('..', file_path))
    docx_mapping(map_name)
    #pdb.set_trace()
    parts = file_name.split('.')
    file_name = '.'.join(parts[:-1])
    output_path = os.path.join(download_folder, user_name, file_name + '_processed.docx')
    os.system('zip -r ' + output_path + ' *')
    os.chdir(os.path.abspath('../'))
    return file_name + '_processed.docx'

def docx_mapping(map_name):
    xml_path = 'word'
    document_parts = ['footnotes', 'document']

    filenames = []
    for d_part in document_parts:
        filenames.append(os.path.join(xml_path, d_part + '.xml'))

    for inpath in filenames:
        (folder, fname) = os.path.split(inpath)
        outfile = '_' + fname
        outpath = os.path.join(folder, outfile)
        if not os.path.exists(inpath):
            continue
        with open(inpath, encoding='utf8') as f:
            tree = ET.parse(f)
            tree = xml_to_unicode(tree, map_name)
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
    docx_mapping(map_name='balaram')
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
