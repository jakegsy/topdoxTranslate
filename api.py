import requests
import json
import urllib.parse as urllib

def authenticate():
    args = {
        "client_id" : "topdoxtranslate",
        'client_secret' : 'YrmVQT+NoubAlrZOqRqUg03DaUl09ab30i3oiwVp/No=',
        'scope' : 'http://api.microsofttranslator.com',
        'grant_type' :  'client_credentials'
    }

    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    pre_oauth_junk = (requests.post(oauth_url,data=urllib.urlencode(args)).content).decode('utf-8')
    oauth_junk = json.loads(pre_oauth_junk)
    headers = {'Authorization': 'Bearer ' + oauth_junk['access_token']}
    return headers



