

giantDick = {}

def textToCleanDick(fileName):

    file = open(fileName)
    dc = {}
    for line in file:
        if '=' in line:

            raw = line[0:len(line)-3].split('=')

            eng = raw[0].strip('"')
            ch = raw[1].strip('"')
            dc[eng] = ch


    file.close()
    return dc


def dickToText(fileName,dick):



