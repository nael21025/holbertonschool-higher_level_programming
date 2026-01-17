#!/usr/bin/python3
def uppercase(str):
    out = ""
    for ch in str:
        o = ord(ch)
        if 97 <= o <= 122:
            out += chr(o - 32)
        else:
            out += ch
    print("{}".format(out))
