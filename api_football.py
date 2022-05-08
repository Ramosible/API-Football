import requests
import json
import sqlite3
key = "43bb2404d29aaf91665c813cc56493c44483e8024294c38cb9a80a8bca69c68b"

#you can use your own key
# key = input("input your key: ")

"""

documentation - https://apifootball.com/documentation/?gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWF8sMnm3SOok8tUJOWmUmp-kqKxsRCyl_0Khmskd9x9RGrDMODVCoaAkBxEALw_wcB

"""




"""
Here i created a dictionary named "leagues" where you have access
on different leauge ids by their name, i have collected more important leagues
here. (here you can see all ids- https://dashboard.api-football.com/soccer/ids)
From the get request which i sent to url named 'url' we got 200 as a status code.
then i took json data ('resp.text') which i had as a string and  make it a list
using loads method from json module. 
then i created a list, named 'list_1' and in it i added touples that 
consists of data. this data is 'team_id', 'team_name' and 'team_badge' of 
a teams participating in championships (you can choose championships from a 'leagues' dictionary)

then i created database (Teams.sqlite3), and in this database i created 
table 'TEAMS'. i keep 'team_id', 'team_name' and 'team_badge' of each team in this table.

I leave the code in the comments.
that's All :)

 """
#
# leagues = {'ucl': 3, 'la liga': 302, 'UEFA Europa League': 4, 'European Championship':1,}
# id = leagues['ucl']
# dictt = {'action': 'get_standings','league_id': id, 'APIkey': key }
# url = "https://apiv3.apifootball.com/"
# resp = requests.get(url, params=dictt)
# # print(resp.url)
# # print(resp.headers)
# # print(resp)
# # print(resp.status_code)
# # print(resp.ok)
# # print(resp.text)
# data = json.loads(resp.text)
# # print(data)
# print(json.dumps(data,indent= 4))
# # print(type(data))
#
# list_1 = []
# for i in range(len(data)):
#     t_id = data[i]['team_id']
#     t_name = data[i]['team_name']
#     t_badge = data[i]['team_badge']
#     i = i+1
#     list_1.append((t_id,t_name,t_badge))
#
# print(list_1)
##team_name, team_badge
#
# conn = sqlite3.connect('Teams.sqlite3')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS TEAMS
#                       (team_id INT,
#                       team_name VARCHAR(50),
#                       team_badge VARCHAR(100))
#                       """)
#
# cursor.executemany("INSERT INTO TEAMS (team_id,team_name,team_badge) VALUES(?,?,?)", list_1)
# conn.commit()


""""
It returns available players  by lastname.
If you do not get the desired player, enter your full name.
AND LAST... you can see images of players. i used for loop  to avoid error,
because not all player pictures are available. and i saved this image in the file.
"""

# player_lastname = input("input player name: ")

# #for example you can try 'messi', 'ronaldo', 'neymar', 'modric' and so on...

# params = {'action':'get_players','player_name':player_lastname,"APIkey":key}
# url_2 = 'https://apiv3.apifootball.com/'
# resp = requests.get(url_2, params= params)
# # print(resp.ok)
# player = json.loads(resp.text)
# print(json.dumps(player, indent=4))
###'Get names:'
# index = 0
# for i in range(len(player)):
#     print(player[index].get('player_name'))
#     index+=1
#


# name = 'Cristiano Ronaldo' #you can choose name from 'Get names' but let's input Ronaldo now..
# dict_2 = {'action': "get_players",'player_name':name , "APIkey":key2}
#
# url = "https://apiv3.apifootball.com"
# response = requests.get(url, params = dict_2)
# r = response.text
# mydict = response.json()
# js = json.dumps(mydict[0], indent=4)
# print(js)
#
# img = mydict[0].get('player_image')
# if img != "":
#     resp2 = requests.get(img)
#     with open("player_img.png", "wb") as f:
#         f.write(resp2.content)
#         print('Image saved! ')
# else:
#     print('sorry, Image  not found :(')


"""
here, we get some information from api, and store it in json file.
i created a dict named 'team_ids', where you can see some popular teams ids.
(but if you want, you can use any number. i leave it in the comments.
you can take the information from api using 'js_dict'. you can see it's structure 
as python string using 'js_str'
then i create database and save some information in the table.

"""
#
# url_3 = "https://apiv3.apifootball.com/"
# team_ids = {'Barcelona':529, 'Real Madrid': 541, 'Atletico Madrid':530,
#             'Manchester United':33, 'Liverpool':40, 'Manchester City':50,
#             'Chelsea': 49, 'Bayern Munich': 157	, ' Borussia Dortmund':165,
#             'Juventus' :496}
#
#
# firstTeam = team_ids['Real Madrid']
# secondTeam = team_ids['Manchester City']
# ##firstTeam = int
# ##firstTeam = int
# dict_3 = {'action':'get_H2H','APIkey': key, 'firstTeamId':firstTeam,'secondTeamId': secondTeam}
# resp = requests.get(url_3, params=dict_3)
# # print(resp.text)
# #here we get information from api and keep in python dictionary - (js_dict)
# with open('h2h.json','w') as file:
#     js_dict = json.loads(resp.text)
#     json.dump(json.loads(resp.text), file, indent=4)
# #here we get information from json file
# with open("h2h.json", 'r') as f:
#     js_str = json.dumps(json.load(f), indent=4)
#     ###js_str is just for beauty
#
# (js_dict.get('firstTeam_lastResults')[0].get('match_id'))
# (js_dict.get('firstTeam_lastResults')[0].get('team_home_badge'))
# (js_dict.get('firstTeam_lastResults')[0].get('league_logo'))
# #for testing
#
#
#
# resp_4 = requests.get('https://apiv3.apifootball.com/badges/logo_leagues/27_wc-qualification-south-america.png')
# print(resp_4.ok)
# ##let's save this photo
# with open('img.png','wb') as filee:
#     filee.write(resp_4.content)
#
# data = []
# for i in range(len(js_dict.get('firstTeam_lastResults'))):
#     data.append((js_dict.get('firstTeam_lastResults')[i].get('match_id'), js_dict.get('firstTeam_lastResults')[i].get('country_name'),
#                  js_dict.get('firstTeam_lastResults')[i].get('match_date'),js_dict.get('firstTeam_lastResults')[i].get('country_logo')))
#
#
# conn = sqlite3.connect('h2h.sqlite3')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS H2H
#                       (matches INT,
#                       countries VARCHAR(50),
#                       match_date VARCHAR(30),
#                       country_logo VARCHAR(100))
#                       """)
#
# cursor.executemany('INSERT INTO H2H (matches,countries,match_date,country_logo) VALUES(?,?,?,?)',data)
# conn.commit()
#
#
#

