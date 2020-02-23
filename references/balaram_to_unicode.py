# -*- coding: utf-8 -*-
import os.path
import shutil
import xml.etree.ElementTree as ET
from references.legacy_handler import Krutidev, Balaram



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

    if map_name== 'balaram':
        mapper = Balaram()
    elif map_name=='wc901':
        mapper = Krutidev('../kruti_unicode_map.tsv')
    else:
        raise NotImplementedError(f"{map_name} not implemented")

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
            tree = mapper.xml_to_unicode(tree)
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
