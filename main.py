import unicodedata
import string as s

def no_accent_char(char):
    """Retire l'accent d'un caractère"""
    table_correspondance = {192: 65,
                            193: 65,
                            194: 65,
                            195: 65,
                            196: 65,
                            197: 65,
                            198: 65,
                            199: 67,
                            200: 69,
                            201: 69,
                            202: 69,
                            203: 69,
                            204: 73,
                            205: 73,
                            206: 73,
                            207: 73,
                            208: 68,
                            209: 78,
                            210: 79,
                            211: 79,
                            212: 79,
                            213: 79,
                            214: 79,
                            216: 79,
                            217: 85,
                            218: 85,
                            219: 85,
                            220: 85,
                            221: 89,
                            224: 97,
                            225: 97,
                            226: 97,
                            227: 97,
                            228: 97,
                            229: 97,
                            230: 97,
                            231: 99,
                            232: 101,
                            233: 101,
                            234: 101,
                            235: 101,
                            236: 105,
                            237: 105,
                            238: 105,
                            239: 105,
                            240: 111,
                            241: 110,
                            242: 111,
                            243: 111,
                            244: 111,
                            245: 111,
                            246: 111,
                            248: 111,
                            249: 117,
                            250: 117,
                            251: 117,
                            252: 117,
                            253: 121

                            }

    if 192 <= ord(char) <= 214 or 216 <= ord(char) <= 253:
        return chr(table_correspondance[ord(char)])
    else:
        return char

    return new_string

import os
def no_accent_word(string):
    """Retire tous les accents d'un mot"""
    new_string = ""
    for char in string:
        new_string += no_accent_char(char)

    return new_string


def create_menu(self, tab: int, lst: list):
    menu_tab = " " * tab * 4
    menu = """"""
    for i in lst:
        number = lst.index(i) + 1
        menu += f"{menu_tab}[{number}] {i}\n"
    return menu



