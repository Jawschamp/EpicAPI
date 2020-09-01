from EpicTest import *
from FortEndpoints import URLs

def DataminePak(Season_Patch, pakchunk):
    Pak = URLs.ThirdParties.NiteStats.FortniteFiles + Season_Patch + "/" + pakchunk + "-WindowsClient.pak.json"
    GetPak = r.get(Pak).json()
    print(GetPak)

DataminePak(Season_Patch="13.3", pakchunk="pakchunk1006")
