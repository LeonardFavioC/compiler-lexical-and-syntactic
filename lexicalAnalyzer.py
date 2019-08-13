# coding: utf-8

from num import isNum
from id import isId

SPECIALCHAR = [ 'mod', 'pot', '+', '-', '*', '/', '(', ',', ')' ]

def readFile(name):
    try:
        x = open(name, 'r')
        return x
    except:
        return('Something went wrong when reading to the file')
        x.close()

def getTockens():
    try:
        txt = readFile('math.txt')
        lines=[]
        for idx, line in enumerate(txt):
            sentence = ''
            stack=''
            for char in line.replace(" ", "").split('\n')[0]:
                if char in SPECIALCHAR:
                    if stack:
                        if stack in SPECIALCHAR:
                            sentence += stack[0]
                        elif isNum(stack):
                            sentence += 'n'
                        elif isId(stack):
                            sentence += 'i'
                        else:
                            sentence += 'u'
                        stack=''
                    sentence += char
                else:
                    stack += char
            if stack:
                if stack in SPECIALCHAR:
                    sentence += stack[0]
                elif isNum(stack):
                    sentence += 'n'
                elif isId(stack):
                    sentence += 'i'
                else:
                    sentence += 'u'
                stack=''
            lines.append(sentence)
        return lines
        txt.close()
    except Exception as e:
        print(e)

