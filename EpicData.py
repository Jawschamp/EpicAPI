import requests
import json
import crayons


from FortEndpoints import URLs
APIKEY = "57f6c9c8-35e080e2-dee6c4bb-567dc7d4"

r = requests.Session()

print(crayons.green("This was a trash app I made there are alot of people i wanna thank, Terbau#8523, This Nils#0001 and of course Jaws#1100"))
print(crayons.green("This Nils#0001 - Replay Parser made in shitty Node"))


class Auth():
    def DeviceAuth(device_id, account_id, secret):
        device_id = ""
        account_id = ""
        secret = ""

class ReplayData:
    def GetReplayData():
        print(crayons.yellow("This is just a test for now. - This Nils#0001"))
        ReplayParse = r.get("https://pastebin.com/raw/mY744kZV").json()["eliminations"]
        for elems in ReplayParse:
            PlayerID = elems["eliminated"]
            Killer = elems["eliminator"]
            WasKillerABot = elems["eliminator"]["isBot"]
        print("Was Killer a Bot?", WasKillerABot, "The Killer was", Killer)

def AccountMetaData():
    print(URLs.AccountService.MetaData)

class GetEpicData:
    def GET_WEBSITE_FN_NEWS():
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

    def GetStatsForAccountID():
        URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/statsv2/account/"


class CreativeData:
    def Get_Map_Data(IslandCode): #The IslandCode param, is used for getting data on a specific map for e.g: "1512-1011-3409"
        GetPic = r.get(URLs.Creative.CreativeIslandPicture + f"{IslandCode}").json()
        #GetIslandData = [GetPic["accountId"], GetPic["mnemonic"]]
        print(GetPic)

def Get_Amount_Of_Time_User_Has_Played():
    Time_Played = r.get(URLs.AccountStatus.Time_Played_On_Fortnite)
    print(Time_Played)

def Redeem_Code(code):
    Try_Code = {"redeem-code": code}
    redeem = r.post(URLs.EpicGamesSite.redeem_code, params=Try_Code)
    print(redeem.status_code, Try_Code)

