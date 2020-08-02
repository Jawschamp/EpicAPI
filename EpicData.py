import requests
import json


from base64 import b64encode

#Local files
#from Auth import authenticate
r = requests.Session()


class AuthTypes:
    def Get_FN_Access_Token():
        with open("Auth.json", "r") as f:
            global FN_ACCESS_TOKEN
            FN_ACCESS_TOKEN = json.load(f)["Token"]
    #Get_FN_Access_Token()

    
    def Get_Auth_Client_ID():
        Client_ID = "ec684b8c687f479fadea3cb2ad83f5c6:e1f31c211f28413186262d37a13fc84d"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": f"basic {str(b64encode(Client_ID.encode('utf-8')), 'utf-8')}"}
        print(headers)
        
        body = {"grant_type": "authorization_code",
                "code": Client_ID}

        cookies = {"XSRF-TOKEN": "016aa9abb2204da88f35f6ce6579e65c"}
        GetClientID = r.post("https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code", headers=headers, data=body)
        global redirectUrl
        redirectUrl = GetClientID.json()
        print(redirectUrl)


class URLs:
    class EventService:
        BASE_URL_LIVE = "https://events-public-service-live.ol.epicgames.com/" #params gameID Fortnite, accountID, regionId, Platform Windows
    
    class AccountService:
        BASE_URL_PROD = "https://account-public-service-prod.ol.epicgames.com/account/"
        BASE_URL_PROD_ALT = "https://account-public-service-prod.ak.epicgames.com/account/" 
        BASE_URL_STAGE = "https://account-public-service-stage.ol.epicgames.com/account/"

    class CatalogService:
        BASE_URL_PROD = "https://catalog-public-service-prod06.ol.epicgames.com/catalog/"
        BASE_URL_PROD_ALT = "https://catalog-public-service-prod06.ak.epicgames.com/catalog/"
        BASE_URL_STAGE = "https://catalogv2-public-service-stage.ol.epicgames.com/catalog/"
    
    class ChannelService:
        BASE_URL_PROD = "https://channels-public-service-prod.ol.epicgames.com/"
        BASE_URL_STAGE = "https://channels-public-service-stage.ol.epicgames.com/"

    class FortniteService:
        BASE_URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/"

    class EpicGamesSite:
        redeem_code = "https://www.epicgames.com/account/v2/ajax/redemption/validate-redemption-code"
        
        class GraphQL:
            backend_GraphQL = "https://www.epicgames.com/store/backend/graphql-proxy"
    
    class EpicGamesStore:
        FreeGames = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=GB&allowCountries=GB,US"
    
    class FortniteEventFlag:
        calendar = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/calendar/v1/timeline"

    class AccountStatus:
        Generic_Account_HTTP_Staus = "https://www.epicgames.com/account/v2/retrieve-info/status"
        Reputation = "https://www.epicgames.com/id/api/reputation"
        Time_Played_On_Fortnite = "https://www.epicgames.com/account/v2/order/playtime?orderId=A1910052308012206" #I wanna put this in a better spot
    
    class Friends:
        Send_Friend_Request = "https://accounts.launcher-website-prod07.ol.epicgames.com/launcher/sendFriendRequest"

    class FortniteNews:
        News = "http://www.epicgames.com/fortnite/api/blog/getPosts?category=&postsPerPage=0&offset=0&locale=en-US&rootPageSlug=blog"

def Get_Shop():
    Req = r.get("https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/storefront/v2/catalog")

class GetEpicData:
    def Get_News():
        Get_News = r.get(URLs.FortniteNews.News).json()["blogList"]
        for News_Feed in Get_News:
            title = News_Feed["title"]
            author = News_Feed["author"]
            date = News_Feed["date"]
            image = News_Feed["image"]
            banner = News_Feed["trendingImage"]
            description = News_Feed["shareDescription"]
            print(title, author, description)

    def Get_Free_Game_Info():
        FreeGames = r.get(URLs.EpicGamesStore.FreeGames).json()["data"]["Catalog"]["searchStore"]["elements"]
        for Info in FreeGames:
            title = Info["title"]
            description = Info["description"]
            effectiveDate = Info["effectiveDate"]
            print(title, description, effectiveDate)
 

    def GetGameModes():
        with open("GameModes.json", "r") as e:
            GetGameModes = json.load(e)["channels"]["client-matchmaking"]["states"]
            for GameModes in GetGameModes:
                LiveModes = GameModes["state"]["region"]["NAW"]["eventFlagsForcedOn"][-1]
                print(LiveModes)
                
GetEpicData.GetGameModes()
GetEpicData.Get_News()
GetEpicData.Get_Free_Game_Info()

class Stats:
    def Test(accountID):
        global IDKE
        IDKE = URLs.ChannelService.BASE_URL_PROD + f"api/v1/user/d4d0142cc75141ff841b1b41b40bed3a?type=all"
        idk = r.get(URLs.ChannelService.BASE_URL_PROD + f"api/v1/user/{accountID}?type=all")
        print(idk)
        print(URLs.ChannelService.BASE_URL_PROD + f"api/v1/user/{accountID}?type=all")

    def SearchAccountIDByName(Name):
        URL = URLs.AccountService.BASE_URL_PROD + f"api/public/account/displayName/{Name}"
        GetAccountID = r.get(URL)
        print(GetAccountID)
        print(URL)

    def SearchByEmail(Email):
        URL = URLs.AccountService.BASE_URL_PROD + f"api/public/account/email/{Email}"
        print(URL)

    def GetStatsForAccountID():
        URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/statsv2/account/"
Stats.SearchByEmail(Email="fngqfn@gmail.com")
Stats.SearchAccountIDByName(Name="Ninja")
Stats.Test(accountID="d4d0142cc75141ff841b1b41b40bed3a")
import Auth2

def currencies():
    e = r.get(URLs.CatalogService.BASE_URL_PROD + "api/shared/bulk/offers", headers={"Authorization": FN_ACCESS_TOKEN})
    print("currencies() function: ", e)
#currencies()


def Send_Friend_Request_HTTP():
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Authorization": FN_ACCESS_TOKEN}
    Send_Friend_Request_To = r.post(URLs.Friends.Send_Friend_Request, headers=headers) #Friends take a FORTNITE_ACCESS_TOKEN
    print(Send_Friend_Request_To.status_code)
#Send_Friend_Request_HTTP()


def Get_Amount_Of_Time_User_Has_Played():
    Time_Played = r.get(URLs.AccountStatus.Time_Played_On_Fortnite)
    print(Time_Played)


def Redeem_Code(code):
    Try_Code = {"redeem-code": code}
    redeem = r.post(URLs.EpicGamesSite.redeem_code, params=Try_Code)
    print(redeem.status_code, Try_Code)
#Redeem_Code(code="JAWS")


def Exchange_Test():
    exchange_get = r.get(AuthTypes.exchange_get_idk)
#Get_Amount_Of_Time_User_Has_Played()
