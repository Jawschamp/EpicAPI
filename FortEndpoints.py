class URLs:
    class Replays:
        Replay_URL = "https://pastebin.com/raw/mY744kZV"

    class Creative:
        CreativeIslandPicture = "https://links-public-service-live.ol.epicgames.com/links/api/fn/mnemonic/"
    
    class DevVersions:
        Devplaytest = "https://fortnite-public-service-devplaytest-prod12.ol.epicgames.com/fortnite/api/version"
        QQTest = "https://fortnite-service-epicreleasetesting.fortnite.qq.com/fortnite/api/version"
        Extqadevtesting = "https://fortnite-public-service-extqadevtesting-prod.ol.epicgames.com/fortnite/api/version"
        Stage = "https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version"
        Devplaytesto = "https://fortnite-public-service-devplaytesto-prod.ol.epicgames.com/fortnite/api/version"

    class ThirdParties:
        class FortniteAPIIO:
            Challenges = "https://fortniteapi.io/v1/challenges?season=current&lang=en"
            Map = "https://media.fortniteapi.io/images/map.png"

        class BenBot:
            cosmetics = "https://benbotfn.tk/api/v1/cosmetics/br"
            shop = "https://benbotfn.tk/api/v1/shop/br"

        class Fortnite_API:
            PlayerStats = "https://fortnite-api.com/v1/stats/br/v2"
            SAC = "https://fortnite-api.com/v2/creatorcode?name="
            News = "https://fortnite-api.com/v2/news"

    class CatalogService:
        BASE_URL_PROD = "https://catalog-public-service-prod06.ol.epicgames.com/catalog/"
        BASE_URL_PROD_ALT = "https://catalog-public-service-prod06.ak.epicgames.com/catalog/"
        BASE_URL_STAGE = "https://catalogv2-public-service-stage.ol.epicgames.com/catalog/"
    
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
