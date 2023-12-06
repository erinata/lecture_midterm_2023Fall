
import requests
import json

import pandas
import os
import time

if not os.path.exists("json_files"):
  os.mkdir("json_files")

charcoalpaper_data = pandas.read_csv("../part_1/parsed_files/charcoalpaper.csv")


f = open("token", "r")
token = f.read()
f.close()

github_session = requests.Session()
github_session.auth = ( "erinata", token)

github_api = "https://api.github.com"


# response_text = github_session.get(github_api + "/rate_limit").text
# json_text = json.loads(response_text)
# print(json_text)



github_user_list = charcoalpaper_data['ghid']

print(github_user_list)

for user_id in github_user_list:
  file_name = "json_files/" + user_id
  if os.path.exists(file_name + ".json"):
    print("File exists", user_id)
  else:
    print("Downloading: ", user_id)
    response_text = github_session.get(github_api + "/users/" + user_id).text
    json_text = json.loads(response_text)
    print(json_text)
    f = open(file_name + ".json", "w")
    f.write(json.dumps(json_text))
    f.close()
    time.sleep(0.1)
    
    

     



