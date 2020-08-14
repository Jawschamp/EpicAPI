from EpicTest import *

class FortniteDATA:
    class Dev:
        def Devplaytest():
            Devplaytest = r.get(URLs.DevVersions.Devplaytest).json()
            cln = Devplaytest["cln"]
            build = Devplaytest["build"]
            print("Devplaytest", "cln", cln, "Build", build)

        def QQTest():
            QQTest = r.get(URLs.DevVersions.QQTest).json()
            cln = QQTest["cln"]
            build = QQTest["build"]
            print("QQTest", "cln", cln, "Build", build)

    class Challenges:
        def Get_Challenges(Week):
            Get_Challenges = r.get(URLs.ThirdParties.FortniteAPIIO.Challenges, headers={"Authorization": APIKEY}).json()
            name = Get_Challenges["weeks"][Week]["name"]
            challenges = Get_Challenges["weeks"][Week]["challenges"]
            for i in challenges:
                title = i["title"]
            print(name, title)

    def Get_Shop():
        GetShop = r.get(URLs.ThirdParties.BenBot.shop).json()["featured"]
        for I in GetShop:
            Names = I["entries"]["items"]
            print(Names)

    def Get_Ingame_News():
        In_Game_News = r.get(URLs.FortniteService.In_Game_News).json()["battleroyalenews"]["news"]
        print(In_Game_News)

    def GetGameModes():
        with open("GameModes.json", "r") as e:
            GetGameModes = json.load(e)["channels"]["client-matchmaking"]["states"]
            for GameModes in GetGameModes:
                LiveModes = GameModes["state"]["region"]["NAW"]["eventFlagsForcedOn"][-1]
                print(LiveModes)

    def GetSACinfo(Code): #param Code is the SAC code you want data on e.g: VastBlast, or Ninja, or mine, Jaws:)
        SAC = r.get(URLs.ThirdParties.Fortnite_API.SAC + f"{Code}").json()["data"]
        Code = SAC["code"]
        account_name = SAC["account"]["name"]
        print(crayons.green("This SAC Code belongs to", account_name))

    def GetFNVersion():
        Version = r.get(URLs.FortniteService.version).json()
        build = Version["build"]
        print(build)
