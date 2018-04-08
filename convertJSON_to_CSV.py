# Created at 2018/4/8 Sunday 11:09 by HenrySHE
# Aims to format Json file
import json
import csv
f = open('rgame.json')
data = json.load(f)
# data = json.dumps(f)
# print(data)
keys = data.keys()
# print (data["578080"])
# print (data["10"]["name"])
f = open("test.csv", "w")
f1 = csv.writer(f)
f1.writerow(["appid", "name", "developer", "publisher", "score_rank","positive","negative","userscore","owners","owners_variance","players_forever","players_forever_variance","players_2weeks","players_2weeks_variance","average_forever","average_2weeks","median_forever","median_2weeks","price"])

for i in keys:
    # print(i)
    tmp = str(i)
    # print(data[tmp]["appid"])
    f1.writerow([data[tmp]["appid"],
                 data[tmp]["name"],
                 data[tmp]["developer"],
                 data[tmp]["publisher"],
                 data[tmp]["score_rank"],
                 data[tmp]["positive"],
                 data[tmp]["negative"],
                 data[tmp]["userscore"],
                 data[tmp]["owners"],
                 data[tmp]["owners_variance"],
                 data[tmp]["players_forever"],
                 data[tmp]["players_forever_variance"],
                 data[tmp]["players_2weeks"],
                 data[tmp]["players_2weeks_variance"],
                 data[tmp]["average_forever"],
                 data[tmp]["average_2weeks"],
                 data[tmp]["median_forever"],
                 data[tmp]["median_2weeks"],
                 data[tmp]["price"]
                ])
    
# print(data.keys())
f.close()