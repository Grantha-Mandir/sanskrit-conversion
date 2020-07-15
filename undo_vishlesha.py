# -*- coding: utf-8 -*-
"""Prepare roman text for conversion to Devanagari

Usage:
  undo_vishlesha.py simple <file_in>
  undo_vishlesha.py elaborate <file_in>

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
        return replace_simple(line)


def replace_elaborate(text):
    text = text.replace('-', '')
    text = text.replace('’', "'") # is this is actually used for avagraha?
    text = text.replace('g a', 'ga')
    text = text.replace('g ā', 'gā')
    text = text.replace('g i', 'gi')
    text = text.replace('g ī', 'gī')
    text = text.replace('g u', 'gu')
    text = text.replace('g ū', 'gū')
    text = text.replace('g ṛ', 'gṛ')
    text = text.replace('g ṝ', 'gṝ')
    text = text.replace('g e', 'ge')
    text = text.replace('g ei', 'gei')
    text = text.replace('g o', 'go')
    text = text.replace('g au', 'gau')

    text = text.replace('ṅ a', 'ṅa')
    text = text.replace('ṅ ā', 'ṅā')
    text = text.replace('ṅ i', 'ṅi')
    text = text.replace('ṅ ī', 'ṅī')
    text = text.replace('ṅ u', 'ṅu')
    text = text.replace('ṅ ū', 'ṅū')
    text = text.replace('ṅ ṛ', 'ṅṛ')
    text = text.replace('ṅ ṝ', 'ṅṝ')
    text = text.replace('ṅ e', 'ṅe')
    text = text.replace('ṅ ei', 'ṅei')
    text = text.replace('ṅ o', 'ṅo')
    text = text.replace('ṅ au', 'ṅau')

    text = text.replace('c c', 'cc')

    text = text.replace('j j', 'jj')

    text = text.replace('ñ a', 'ña')
    text = text.replace('ñ ā', 'ñā')
    text = text.replace('ñ i', 'ñi')
    text = text.replace('ñ ī', 'ñī')
    text = text.replace('ñ u', 'ñu')
    text = text.replace('ñ ū', 'ñū')
    text = text.replace('ñ ṛ', 'ñṛ')
    text = text.replace('ñ ṝ', 'ñṝ')
    text = text.replace('ñ e', 'ñe')
    text = text.replace('ñ ei', 'ñei')
    text = text.replace('ñ o', 'ño')
    text = text.replace('ñ au', 'ñau')

    text = text.replace('ḍ a', 'ḍa')
    text = text.replace('ḍ ā', 'ḍā')
    text = text.replace('ḍ i', 'ḍi')
    text = text.replace('ḍ ī', 'ḍī')
    text = text.replace('ḍ u', 'ḍu')
    text = text.replace('ḍ ū', 'ḍū')
    text = text.replace('ḍ ṛ', 'ḍṛ')
    text = text.replace('ḍ ṝ', 'ḍṝ')
    text = text.replace('ḍ e', 'ḍe')
    text = text.replace('ḍ ei', 'ḍei')
    text = text.replace('ḍ o', 'ḍo')
    text = text.replace('ḍ au', 'ḍau')
    text = text.replace('ḍ ḍ', 'ḍḍ')
    text = text.replace('ḍ y', 'ḍy')
    text = text.replace('ḍ r', 'ḍr')
    text = text.replace('ḍ v', 'ḍv')

    text = text.replace('ṇ a', 'ṇa')
    text = text.replace('ṇ ā', 'ṇā')
    text = text.replace('ṇ i', 'ṇi')
    text = text.replace('ṇ ī', 'ṇī')
    text = text.replace('ṇ u', 'ṇu')
    text = text.replace('ṇ ū', 'ṇū')
    text = text.replace('ṇ ṛ', 'ṇṛ')
    text = text.replace('ṇ ṝ', 'ṇṝ')
    text = text.replace('ṇ e', 'ṇe')
    text = text.replace('ṇ ei', 'ṇei')
    text = text.replace('ṇ o', 'ṇo')
    text = text.replace('ṇ au', 'ṇau')
    text = text.replace('ṇ ṇ', 'ṇṇ') # not included in Demian's macro

    text = text.replace('t t', 'tt')

    text = text.replace('d a', 'da')
    text = text.replace('d ā', 'dā')
    text = text.replace('d i', 'di')
    text = text.replace('d ī', 'dī')
    text = text.replace('d u', 'du')
    text = text.replace('d ū', 'dū')
    text = text.replace('d ṛ', 'dṛ')
    text = text.replace('d ṝ', 'dṝ')
    text = text.replace('d e', 'de')
    text = text.replace('d ei', 'dei')
    text = text.replace('d o', 'do')
    text = text.replace('d au', 'dau')
    text = text.replace('d d', 'dd')
    text = text.replace('d y', 'dy')
    text = text.replace('d r', 'dr')
    text = text.replace('d v', 'dv')

    text = text.replace('n a', 'na')
    text = text.replace('n ā', 'nā')
    text = text.replace('n i', 'ni')
    text = text.replace('n ī', 'nī')
    text = text.replace('n u', 'nu')
    text = text.replace('n ū', 'nū')
    text = text.replace('n ṛ', 'nṛ')
    text = text.replace('n ṝ', 'nṝ')
    text = text.replace('n e', 'ne')
    text = text.replace('n ei', 'nei')
    text = text.replace('n o', 'no')
    text = text.replace('n au', 'nau')
    text = text.replace('n n', 'n')
    text = text.replace('n m', 'nm')

    text = text.replace('b a', 'ba')
    text = text.replace('b ā', 'bā')
    text = text.replace('b i', 'bi')
    text = text.replace('b ī', 'bī')
    text = text.replace('b u', 'bu')
    text = text.replace('b ū', 'bū')
    text = text.replace('b ṛ', 'bṛ')
    text = text.replace('b ṝ', 'bṝ')
    text = text.replace('b e', 'be')
    text = text.replace('b ei', 'bei')
    text = text.replace('b o', 'bo')
    text = text.replace('b au', 'bau')
    text = text.replace('b b', 'b')

    text = text.replace('m a', 'ma')
    text = text.replace('m ā', 'mā')
    text = text.replace('m i', 'mi')
    text = text.replace('m ī', 'mī')
    text = text.replace('m u', 'mu')
    text = text.replace('m ū', 'mū')
    text = text.replace('m ṛ', 'mṛ')
    text = text.replace('m ṝ', 'mṝ')
    text = text.replace('m e', 'me')
    text = text.replace('m ei', 'mei')
    text = text.replace('m o', 'mo')
    text = text.replace('m au', 'mau')

    text = text.replace('y a', 'ya')
    text = text.replace('y ā', 'yā')
    text = text.replace('y i', 'yi')
    text = text.replace('y ī', 'yī')
    text = text.replace('y u', 'yu')
    text = text.replace('y ū', 'yū')
    text = text.replace('y ṛ', 'yṛ')
    text = text.replace('y ṝ', 'yṝ')
    text = text.replace('y e', 'ye')
    text = text.replace('y ei', 'yei')
    text = text.replace('y o', 'yo')
    text = text.replace('y au', 'yau')

    text = text.replace('r a', 'ra')
    text = text.replace('r ā', 'rā')
    text = text.replace('r i', 'ri')
    text = text.replace('r ī', 'rī')
    text = text.replace('r u', 'ru')
    text = text.replace('r ū', 'rū')
    text = text.replace('r ṛ', 'rṛ')
    text = text.replace('r ṝ', 'rṝ')
    text = text.replace('r e', 're')
    text = text.replace('r ei', 'rei')
    text = text.replace('r o', 'ro')
    text = text.replace('r au', 'rau')
    text = text.replace('r g', 'rg')
    text = text.replace('r j', 'rj')
    text = text.replace('r d', 'rd')
    text = text.replace('r n', 'rn')
    text = text.replace('r b', 'rb')
    text = text.replace('r m', 'rm')
    text = text.replace('r y', 'ry')
    text = text.replace('r l', 'rl')
    text = text.replace('r v', 'rv')
    text = text.replace('r h', 'rh')

    text = text.replace('l l', 'll')

    text = text.replace('v a', 'va')
    text = text.replace('v ā', 'vā')
    text = text.replace('v i', 'vi')
    text = text.replace('v ī', 'vī')
    text = text.replace('v u', 'vu')
    text = text.replace('v ū', 'vū')
    text = text.replace('v ṛ', 'vṛ')
    text = text.replace('v ṝ', 'vṝ')
    text = text.replace('v e', 've')
    text = text.replace('v ei', 'vei')
    text = text.replace('v o', 'vo')
    text = text.replace('v au', 'vau')

    text = text.replace('ś c', 'śc')
    text = text.replace('s t', 'st')
    return text


def undo_vishlesha_elaborate(file_in):
    for line in file_in:
        return replace_elaborate(line)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    # print(arguments)
    path_in = arguments['<file_in>']
    if arguments['<file_in>']:
        with open(path_in) as file_in:
            if arguments['simple']:
                print(undo_vishlesha_simple(file_in))
            if arguments['elaborate']:
                print(undo_vishlesha_elaborate(file_in))
