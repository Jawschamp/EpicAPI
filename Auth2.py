import requests
from base64 import b64encode
import json
import random
import string

token = None

def getToken():
    global token
    if token != None:
        print("Token already generated, auth code not requiered")
        return token
    authCode = input("Go to this https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code url and get your Auth Code abd insert it here: ")
    id_secret = "ec684b8c687f479fadea3cb2ad83f5c6:e1f31c211f28413186262d37a13fc84d" #fortnitePCGameClient
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Authorization": f"basic {str(b64encode(id_secret.encode('utf-8')), 'utf-8')}"}

    body = {"grant_type": "authorization_code",
            "code": authCode}
    r = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", headers=headers, data=body)
    print(r.text, r.cookies)
    res = json.loads(r.text)
    
    if "access_token" in res:
        token = res["access_token"]
        print(f"Token: {token}\nExpires at: {res['expires_at']}")
        return token
    else:
        if "errorCode" in r:
            print("[ERROR] {r['errorCode']}")
        else:
            print("[ERROR] Unknown error")
        return False

def getEndpoint():
    getToken_result = getToken()
    if getToken_result:
        endpoint = input("Insert endpoint: ")
        
        if endpoint.lower().find("epicgames.com") != -1:
            try:
                headers = {"Authorization": f"bearer {getToken_result}"}
                r = requests.get(endpoint, headers=headers)
                print(r.text)
                print("Do you want to save the response into a json file? Y N")
                saveFile = input()
                if saveFile.lower() == "y" or saveFile.lower() == "yes":
                    random_name = "".join(random.choice(string.ascii_lowercase) for i in range(5))
                    with open(f"{random_name}.json", "x") as f:
                        try:
                            f.write(r.text)
                            print(f"File successfully saved (./{random_name}.json)")
                        except Exception as e:
                            print(f"[ERROR] Couldn't save the file ({e})")
            except:
                print("[ERROR] Something went wrong :(")
        else:
            print("[ERROR] Invalid endpoint, insert a valid Fortnite endpoint")
    getEndpoint()

getEndpoint()
