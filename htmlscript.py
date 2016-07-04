import requests
import json
import urllib.parse as urllib

args = {
    "client_id" : "topdoxtranslate",
    'client_secret' : 'YrmVQT+NoubAlrZOqRqUg03DaUl09ab30i3oiwVp/No=',
    'scope' : 'http://api.microsofttranslator.com',
    'grant_type' :  'client_credentials'
}

oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
pre_oauth_junk = (requests.post(oauth_url,data=urllib.urlencode(args)).content).decode('utf-8')

oauth_junk = json.loads(pre_oauth_junk)

translation_args = {
        'text': "hello",
        'to': 'ru',
        'from': 'en'
        }
headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
print (translation_result.content.decode('UTF-8'))