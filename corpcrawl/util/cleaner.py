import re

def clean_name(name):
    if name:
        remove = ["(Filer)"]
    for r in remove:
        name = name.replace(r, "")
    name = name.strip()
    name = first_letter_caps(name)
    return name


def clean_addr(addr):
    return first_letter_caps(addr)


def first_letter_caps(word):
    def repl(m):
        return m.group(0).upper()                                                                                     
    return re.sub('^[a-z]|\s[a-z]', repl, word.lower())