import api
import requests
import urllib.parse as urllib

fileName = 'Localizable.strings'

def textToCleanDic(fileName):
    file = open(fileName)
    dc = []
    for line in file:
        if '=' in line:
            raw = line[0:len(line)-3].split('=')
            eng = raw[0].strip('"')
            eng = eng.strip(' ')
            eng = eng.strip('"')
            ch = raw[1].strip('"')
            ch = ch.strip(' ')
            ch = ch.strip('"')
            dc.append((eng,ch))
    file.close()
    return dc

authToken = api.authenticate()
translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
enZHdictionary = textToCleanDic(fileName)

def translateDic(dic):
    index = len(dic)

    for i in range(0,index):

        key = dic[i]
        eng = key[0]

        translation_args = {
            "from" : "en",
            "to" : "zh",
            "text" : eng
        }
        translation_result = requests.get(translation_url+urllib.urlencode(translation_args)
                                          ,headers=authToken)
        decoded = translation_result.content.decode('UTF-8')
        decoded = decoded.strip('"')
        newTupe = (eng,decoded)
        dic[i] = newTupe

    return dic

def writeToFile(fileName):

    dic = translateDic(enZHdictionary)
    with open(fileName, 'w') as file:
        for key in dic:
            line = "\"" + key[0] + "\" =  \"" + key[1] + "\";\n"
            file.write(line)

        file.close()


writeToFile("raw2")



