# -*- coding: utf-8 -*-
"""Prepare roman text for conversion to Devanagari

Usage:
  undo_vishlesha.py <file_in>
  undo_vishlesha.py (-h | --help)
"""

from docopt import docopt


def replace_simple(text):
    text = text.replace('-', '')
    text = text.replace('g ', 'g')
    text = text.replace('c c', 'cc')
    text = text.replace('j j', 'jj')
    text = text.replace('d ', 'd')
    text = text.replace('m ', 'm')
    text = text.replace('y ', 'y')
    text = text.replace('r ', 'r')
    text = text.replace('ś c', 'śc')
    text = text.replace('s t', 'st')
    return text


def undo_vishlesha_simple(file_in):
    for line in file_in:
        for x in line:
            return replace_simple(line)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    # print(arguments)
    path_in = arguments['<file_in>']
    if arguments['<file_in>']:
        with open(path_in) as file_in:
            print(undo_vishlesha_simple(file_in))
