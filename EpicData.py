import requests
import json


from base64 import b64encode

#Local files
#from Auth import authenticate
r = requests.Session()

def Printinfo(Info):
    print(Info)

class URLs:
    class ThirdParties:
        class BenBot:
            cosmetics = "https://benbotfn.tk/api/v1/cosmetics/br"
            shop = "https://benbotfn.tk/api/v1/shop/br"

        class Fortnite_API:
            PlayerStats = "https://fortnite-api.com/v1/stats/br/v2"
            SAC = "https://fortnite-api.com/v2/creatorcode?name="
    class EventService:
        BASE_URL_LIVE = "https://events-public-service-live.ol.epicgames.com/" #params gameID Fortnite, accountID, regionId, Platform Windows
    
    class AccountService:
        BASE_URL_PROD = "https://account-public-service-prod.ol.epicgames.com/account/"
        BASE_URL_PROD_ALT = "https://account-public-service-prod.ak.epicgames.com/account/" 
        BASE_URL_STAGE = "https://account-public-service-stage.ol.epicgames.com/account/"

        MetaData = "https://account-public-service-prod03.ol.epicgames.com/account/api/accounts/:accountId/metadata"

    class CatalogService:
        BASE_URL_PROD = "https://catalog-public-service-prod06.ol.epicgames.com/catalog/"
        BASE_URL_PROD_ALT = "https://catalog-public-service-prod06.ak.epicgames.com/catalog/"
        BASE_URL_STAGE = "https://catalogv2-public-service-stage.ol.epicgames.com/catalog/"
        class URLS:
            Bulk_Items = "https://catalog-public-service-prod06.ol.epicgames.com/catalog/" + "api/shared/bulk/items"
    
    class ChannelService:
        BASE_URL_PROD = "https://channels-public-service-prod.ol.epicgames.com/"
        BASE_URL_STAGE = "https://channels-public-service-stage.ol.epicgames.com/"

    class FortniteService:
        version = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/version"
        BASE_URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/"
        In_Game_News = "https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game"

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

def Bulk_Items():
    URL = r.get(URLs.CatalogService.URLS.Bulk_Items)
    print(URL, URLs.CatalogService.URLS.Bulk_Items)
Bulk_Items()

def AccountMetaData():
    print(URLs.AccountService.MetaData)


class GetEpicData:
    def Get_Shop():
        GetShop = r.get(URLs.ThirdParties.BenBot.shop).json()["featured"]
        for I in GetShop:
            Names = I["entries"]["items"]
            print(Names)

    def GetSACinfo(Name):
        SAC = r.get(URLs.ThirdParties.Fortnite_API.SAC + f"{Name}").json()["data"]
        Code = SAC["code"]
        account_name = SAC["account"]["name"]
        print(Printinfo("SAC Code"), Code)

    def GetFNVersion():
        Version = r.get(URLs.FortniteService.version).json()
        build = Version["build"]
        print(build)

    def Get_News():
        Get_News = r.get(URLs.FortniteNews.News).json()["blogList"]
        for News_Feed in Get_News:
            title = News_Feed["title"]
            author = News_Feed["author"]
            date = News_Feed["date"]
            image = News_Feed["image"]
            banner = News_Feed["trendingImage"]
            description = News_Feed["shareDescription"]
            #content = News_Feed["content"]
            #GetContent = content.strip("></")
            print(title, author)

    def GetIngameNews():
        In_Game_News = r.get(URLs.FortniteService.In_Game_News).json()["battleroyalenews"]["news"]
        print(In_Game_News)

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


#GetEpicData.GetSACinfo(Name="VastBlast")
#GetEpicData.GetFNVersion()
#GetEpicData.Get_Shop()
#GetEpicData.GetIngameNews()
#GetEpicData.GetGameModes()
#GetEpicData.Get_News()
#GetEpicData.Get_Free_Game_Info()

class Stats:
    def GetPlayerStats(PlayerName):
        GetPlayerStats = r.get(URLs.ThirdParties.Fortnite_API.PlayerStats + f"?name={PlayerName}").json()["data"]
        AccountName = GetPlayerStats["account"]["name"]
        BattlePassLevel = GetPlayerStats["battlePass"]["level"]
        Stat = GetPlayerStats["stats"]["all"]
        print(AccountName, BattlePassLevel)

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

#Stats.GetPlayerStats("Tfue")
#Stats.SearchByEmail(Email="officialstaticbots@gmail.com")
#Stats.SearchAccountIDByName(Name="Ninja")
#Stats.Test(accountID="d4d0142cc75141ff841b1b41b40bed3a")
#import Auth2

def currencies():
    e = r.get(URLs.CatalogService.BASE_URL_PROD + "api/shared/bulk/offers", headers={"Authorization": FN_ACCESS_TOKEN})
    print("currencies() function: ", e)

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
