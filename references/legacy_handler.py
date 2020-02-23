import re


class Legacy():
    def __init__(self, mapping_file):

        def read_mapping(mapping_file):
            map_dict = dict()
            with open(mapping_file) as f:
                for line in f:
                    kruti, uni = line.strip().split('\t')
                    map_dict[kruti] = uni
            return map_dict

        self.mapping_dict = read_mapping(mapping_file) if isinstance(mapping_file,str)  else mapping_file

    def replace_text(self, text):
        ignore = {'', ' ', '  '}
        for ch in self.mapping_dict:
            if ch not in ignore:
                text = text.replace(ch, self.mapping_dict[ch])
        return text

    def xml_to_unicode(self, tree):
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        root = tree.getroot()
        # t.getroot().findall('.//w:t', namespace)
        # TODO: To write back we need the reference to the XML node here.
        # In ElementTree nodes do not have a reference to their parent,
        # thus we have nodes disconnected from the tree when searching with .//w:t
        # => use a different XML library!!!

        for elem in root.getiterator():
            try:
                if elem.text is not None:
                    elem.find('.//w:t', namespace)
                    t = self.replace_text(elem.text)
                    elem.text = t
            except AttributeError:
                pass
        return tree


class Krutidev(Legacy):
    def __init__(self, mapping_file):
        super().__init__(mapping_file)

    def xml_to_unicode(self, tree):
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        root = tree.getroot()
        for elem in root.getiterator():
            try:
                if elem.text is not None:
                    elem.find('.//w:t', namespace)
                    t = self.replace_text(elem.text)
                    t = self.special_cases(t)
                    elem.text = t
            except AttributeError:
                pass
        return tree

    def special_cases(self, text):
        #apply case 1 (Code for Glyph1 : ± (reph+anusvAr))
        text = text.replace("±","Zं")
        return text

class Balaram(Krutidev):
        def __init__(self):
            # todo: Add candrabindu!
            mapping_dict = {"": "fi", "": "fl", "ä": "ā", "é": "ī", "ü": "ū", "å": "ṛ", "è": "ṝ",
                       "ì": "ṅ", "ñ": "ṣ", "ï": "ñ", "ö": "ṭ", "ò": "ḍ", "ë": "ṇ", "ç": "ś",
                       "à": "ṁ", "ù": "ḥ", "ÿ": "ḷ", "û": "ḹ", "Ä": "Ā", "É": "Ī", "Ü": "Ū",
                       "Å": "Ṛ", "È": "Ṝ", "Ì": "Ṅ", "Ñ": "Ṣ", "Ï": "Ñ", "Ö": "Ṭ", "Ò":
                           "Ḍ", "Ë": "Ṇ", "Ç": "Ś", "À": "Ṁ", "Ù": "Ḥ", "ß": "Ḷ"}

            super().__init__(mapping_dict)