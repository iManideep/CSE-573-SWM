from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import pandas as pd

PATH = r'C:\Users\manid\Downloads\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('log-level=3')

# l = ['elonmusk', 'sama', 'BillGates', 'realDonaldTrump', 'Cristiano', 'rihanna', 'BarackObama', 'justinbieber', 'katyperry', \
#      'taylorswift13', 'narendramodi', 'selenagomez', 'britneyspears', 'akshaykumar', 'realmadrid', 'BeingSalmanKhan', 'iamsrk',
#      'JLo', 'jimmyfallon','onedirection', 'BrunoMars', 'Eminem', 'kanyewest', 'LeoDiCaprio', 'maroon5', 'KylieJenner',
#      'deepikapadukone', 'iHrithik', 'tomhanks', 'nickjonas', 'imVkohli', 'BigSean', 'elissakh', 'LittleMix', 'shahidkapoor', 'ciara']

ans = []

driver = webdriver.Chrome(options)

df1 = pd.read_csv('userNames.csv')
for user in df1['twitter']:
    target_url = "https://twitter.com/"+user
    driver.get(target_url)
    time.sleep(2)
    resp = driver.page_source
    
    profileDetails = {"Profile Banner":"","Profile Image":"","User Description":"","Joined":"","User Name":"","Twitter Handle":"","Subscriptions":"","Following":"","Followers":""}
    res = set()
    soup = BeautifulSoup(resp,'html.parser')

    try:
        profile = soup.find("div", {"data-testid" : "UserName"}).find("span",{"class":"css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"})
        profile.text
    except:
        continue

    header_photo = soup.find("a",{"href":"/"+user+"/header_photo"})
    if header_photo and header_photo.find("img"):
        profileDetails['Profile Banner'] = header_photo.find("img")['src']
    profile_photo = soup.find("a",{"href":"/"+user+"/photo"})
    if profile_photo and profile_photo.find("img"):
        profileDetails['Profile Image'] = profile_photo.find("img")['src']

    UserDescription = soup.find("div", {"data-testid" : "UserDescription"})
    if UserDescription and UserDescription.find("span"):
        profileDetails["User Description"] = UserDescription.find("span").text

    profileDetails["User Name"] = profile.text
    for i in range(100):
        profile = profile.find_next()
        o = profile.text
        res.add(o)
    
    for i in res:
        if "@" in i:
            profileDetails["Twitter Handle"] = "@"+user
        if re.match(r"^[,0-9]+\sSubscriptions$", i.strip()):
            profileDetails["Subscriptions"] = i.strip().split(" ")[0]
        if re.match(r"[,0-9]+[\.]?[0-9]?[A-Z]?\sFollowing", i.strip()):
            profileDetails["Following"] = i.strip().split(" ")[0]
        if re.search(r"[,0-9]+(?:\.[0-9]+)?[KMGT]? Followers", i.strip()):
            profileDetails["Followers"] = re.search(r"[,0-9]+(?:\.[0-9]+)?[KMGT]? Followers", i.strip()).group().split(" ")[0]
        if "Joined" in i:
            profileDetails["Joined"] = i.split("Joined ")[1]
    ans.append(profileDetails)
    
driver.close()

df = pd.DataFrame(ans)
df = df[["User Name", "Twitter Handle", "User Description", "Joined", "Following", "Followers", "Profile Image", "Profile Banner", "Subscriptions"]]
df.to_csv("twitter.csv")