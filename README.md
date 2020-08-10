This is a shitty file i put together that does stupid things

Auth File made by https://github.com/Londiuh/FN-endpoint-get

To run this, run EpicData.py
and follow what it says, unfortunately I don't have a working Auth that I can add to my EpicData.py file so, you have to do it manually IK it sucks I've looked into it but if you know how to fix it please dm me or open a pull request!
The Problem:
* I can't seem to figure out how Epic knows your logged in, I'm assuming it's a cookie, but I don't know witch one

Description oon what this does:
* It will give you the news from the Website for Fortnite Fortnite
* It will give you Item Shop Data
* It will give you Free Games that Epic is giving away!
* It gives you Live modes, (Only for NAW) for now
Added Commit #3:
Added the following Functions GetFNVersion, GetSACinfo
Added some Third Parties partiaclly because my auth won't work.

Tested functions:
```py
from EpicTest import *


GetEpicData.GET_WEBSITE_FN_NEWS()
GetEpicData.Get_Free_Game_Info()

FortniteDATA.Challenges.Get_Challenges("3") #Returns the challenges for week# e.g: 4

FortniteDATA.Get_Ingame_News()
FortniteDATA.GetGameModes()
FortniteDATA.GetSACinfo("Ninja") #Returns data for the inserted parameter
FortniteDATA.GetFNVersion()

Stats.GetPlayerStats("Ninja")```
