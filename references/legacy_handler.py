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
                if elem.text is not None and len(elem.text.strip())>0:
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
        text = self.case2(text)
        text = self.case3(text)
        text = self.case4(text)
        text = self.case5(text)
        return text

    def case5(self, text):
        '''
         Eliminating reph "Z" and putting 'half - r' at proper position for this.
        :param text:
        :return:
        '''
        matra_set = set_of_matras = {"अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ", "ा", "ि", "ी ","ु", "ू", "ृ", "े", "ै", "ो", "ौ","ं" ":"," ँ"," ॅ"}
        r_index = text.find("Z")
        while r_index>0:
            prob_pos_hlf_r = r_index-1
            prob_hlf_r = text[prob_pos_hlf_r]
            # trying to find non-maatra position left to current O (ie, half -r).
            while prob_hlf_r in matra_set:
                prob_pos_hlf_r = prob_hlf_r -1
                prob_hlf_r = text[prob_pos_hlf_r]
            replace_char = text[prob_pos_hlf_r:(r_index-prob_pos_hlf_r)]
            new_string  = "र्" + replace_char
            replace_char = replace_char + 'Z'
            text = text.replace(replace_char,new_string)
            r_index = text.find("Z")
        return text


    def case4(self, text):
        '''
        Glyph5: Ê, code for replacing "h" with "ी"  and correcting its position too.(moving it one positions forward)
        :param text:
        :return:
        '''
        text.replace("Ê", "ीZ") #t some places  Ê  is  used eg  in "किंकर".
        #following loop to eliminate 'chhotee ee kee maatraa' on half-letters as a result of above transformation.
        ee_index = text.find("ि्")
        while ee_index != -1:
            next_consonant = text[ee_index+2]
            replace_char = "ि्" + next_consonant
            text = text.replace(replace_char,"्" + next_consonant+"ि")
            ee_index = text.find('"ि्"', ee_index + 2)
        return text

    def case3(self, text):
        '''
        Glyph3 & Glyph4: Ç  É
        code for replacing "fa" with "िं"  and correcting its position too.(moving it two positions forward)
        :param text:
        :return:
        '''
        text = text.replace( "Ç" , "fa" ) #at some places  Ç  is  used eg  in "किंकर".
        text = text.replace("É" , "र्fa") # // at some places  É  is  used eg  in "शर्मिंदा"

        fa_index = text.find('fa')
        while fa_index != -1:
            next_char = text[fa_index + 2]
            replace_char = "fa" + next_char
            text = text.replace(replace_char, next_char + "िं")
            fa_index = text.find('fa',fa_index+2)
        return text

    def case2(self, text):
        '''
        Glyp2: Æ
        code for replacing "f" with "ि" and correcting its position too.(moving it one position forward)
        :param text:
        :return:
        '''
        text = text.replace("Æ","र्f")
        f_index = text.find("f")
        while f_index!=-1:
            next_char = text[f_index+1]
            replace_char = "f" + next_char
            text = text.replace(replace_char, next_char+"f")
            f_index = text.find('f', f_index + 1 )
            #search for f ahead of the current position.
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