from collections import OrderedDict
import operator, json
import re

class Legacy():

    def __init__(self, mapping_file):
        '''
        mapping file can be either a file or the actually mapping dictionary
        :param mapping_file:
        '''
        def read_mapping_json(mapping_file):
            with open(mapping_file) as f:
                map_dict = json.load(f)
            return map_dict

        def read_mapping_tsv(mapping_file):
            len_map = list()
            un_sorted_map_dict = OrderedDict()
            with open(mapping_file, encoding='utf8') as f:
                for line in f:
                    parts = line.strip().split('\t')
                    if len(parts)<=1 or parts[0]=='':
                        continue
                    kruti, uni = parts
                    un_sorted_map_dict[kruti] = uni
                    len_map.append((kruti, len(kruti)))
            len_map_sorted = sorted(len_map, key = operator.itemgetter(1), reverse=True)
            sorted_map_dict = OrderedDict()
            for elem in len_map_sorted:
                sorted_map_dict[elem[0]] = un_sorted_map_dict[elem[0]]
            return sorted_map_dict
        if isinstance(mapping_file,str):
            f_type = mapping_file.split('.')[-1]
            read_func = read_mapping_json if f_type == 'json' else read_mapping_tsv
            self.mapping_dict = read_func(mapping_file)
        else:
            self.mapping_dict =  mapping_file # this is not a file but an actual dictionary

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


class WalkmanChanakya(Legacy):
    def __init__(self):
        mapping_file = '../wc905_unicode.json'
        super().__init__(mapping_file)


    def xml_to_unicode(self, tree):
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        root = tree.getroot()
        for elem in root.getiterator():
            try:
                if elem.text is not None and len(elem.text.strip())>0:
                    elem.find('.//w:t', namespace)
                    t = self.replace_text(elem.text)
                    t = self.replace_special_symbols(t)
                    elem.text = t
            except AttributeError:
                pass
        return tree

    def replace_special_symbols(self, text):
        '''
        This is needed for processing patterns of symbols

        :param text:
        :return: text after replacing some patterns
        '''

        text = re.sub(r'([ेैुूं]+)्र',r'्र\1', text) #replace( /([ेैुूं]+)्र/g , "्र$1" )
        text = re.sub(r'ं([ाेैुू]+)',r'\1ं',text) #replace( /ं([ाेैुू]+)/g , "$1ं" )
        text = re.sub(r'([ \n])ा',r'\1श',text)  #replace( /([ \n])ा/g , "$1श" )
        text = re.sub(r'¯',r'f', text) #replace( /¯ / g, "f");
        text = re.sub(r'Ł',r'र्f', text) #text = text.replace('Ł','र्f')#replace( / Ł / g, "र्f");
        text = re.sub(r'([fŻ])([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])',r'\2\1', text) #replace( / ([fŻ])([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष]) / g, "$2$1" )
        text = re.sub(r'([fŻ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])',r'\2\3\1', text) #replace( / ([fŻ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष]) / g, "$2$3$1" )
        text = re.sub(r'([fŻ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])',r'\2\3\1',text) #replace( /([fŻ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])/g , "$2$3$1" )
        text = re.sub(r'f',r'ि', text) #replace( /f/g , "ि")
        text = re.sub(r'Ż',r'िं', text) #replace( /Ż/g , "िं")
        # following three statements for adjusting position of reph ie, half r.
        text = re.sub(r'±',r'Zं', text) #replace( /± / g, "Zं" )
        text = re.sub(r'([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([ािीुूृेैोौंँ] *)([Z])',r'\3\1\2', text) #replace( / ([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([ािीुूृेैोौंँ] *)([Z]) / g, "$3$1$2" )
        text = re.sub(r'([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([्])([Z])',r'\3\1\2',text) #replace( / ([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([्])([Z]) / g, "$3$1$2" )
        text = self.case5(text)
        #text = re.sub(r'Z',r'र्', text) #replace( / Z / g, "र्" )
        return text

    def case5(self, text):
        '''
         Eliminating reph "Z" and putting 'half - r' at proper position for this.
        :param text:
        :return:
        '''
        matra_set =  {"अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ",
                      "ा", "ि", "ी ","ु", "ू", "ृ", "े", "ै", "ो", "ौ","ं" ":"," ँ"," ॅ",'ी',
                      'ी','ा','ाा','"ाु','"ा','"िा',"ाु"}
        r_index = text.find("Z")
        while r_index>0 and r_index<len(text)-1:
            hlf_r_pos = r_index-1
            hlf_r = text[hlf_r_pos]
            # trying to find non-maatra position left to current O (ie, half -r).
            while hlf_r in matra_set:
                hlf_r_pos = hlf_r_pos -1
                hlf_r = text[hlf_r_pos]
            replace_char = text[hlf_r_pos:r_index]
            new_string  = "र्" + replace_char
            replace_char = replace_char + 'Z'
            text = text.replace(replace_char,new_string)
            r_index = text.find("Z")
        return text


class Krutidev(Legacy):
    def __init__(self):
        mapping_file ='../kruti_ruchi_hybrid.tsv'
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
        matra_set =  {"अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ",
                      "ा", "ि", "ी ","ु", "ू", "ृ", "े", "ै", "ो", "ौ","ं" ":"," ँ"," ॅ",'ी',
                      'ी','ा','ाा','"ाु','"ा','"िा',"ाु"}
        r_index = text.find("Z")
        while r_index>0 and r_index<len(text)-1:
            hlf_r_pos = r_index-1
            hlf_r = text[hlf_r_pos]
            # trying to find non-maatra position left to current O (ie, half -r).
            while hlf_r in matra_set:
                hlf_r_pos = hlf_r_pos -1
                hlf_r = text[hlf_r_pos]
            replace_char = text[hlf_r_pos:r_index]
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
        while ee_index != -1 and ee_index<len(text)-2:
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
        while fa_index != -1 and fa_index<len(text)-1:
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
        while f_index!=-1 and f_index<len(text)-1:
            next_char = text[f_index+1]
            replace_char = "f" + next_char
            text = text.replace(replace_char, next_char+"ि")
            f_index = text.find('f', f_index + 1 )
            #search for f ahead of the current position.
        return text

class Balaram(Legacy):
        def __init__(self):
            # todo: Add candrabindu!
            mapping_dict = {"": "fi", "": "fl", "ä": "ā", "é": "ī", "ü": "ū", "å": "ṛ", "è": "ṝ",
                       "ì": "ṅ", "ñ": "ṣ", "ï": "ñ", "ö": "ṭ", "ò": "ḍ", "ë": "ṇ", "ç": "ś",
                       "à": "ṁ", "ù": "ḥ", "ÿ": "ḷ", "û": "ḹ", "Ä": "Ā", "É": "Ī", "Ü": "Ū",
                       "Å": "Ṛ", "È": "Ṝ", "Ì": "Ṅ", "Ñ": "Ṣ", "Ï": "Ñ", "Ö": "Ṭ", "Ò":
                           "Ḍ", "Ë": "Ṇ", "Ç": "Ś", "À": "Ṁ", "Ù": "Ḥ", "ß": "Ḷ"}

            super().__init__(mapping_dict)