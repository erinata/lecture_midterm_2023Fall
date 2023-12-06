import pandas
import os
import math
import requests
import json
import time

  
f = open("token", "r")
token = f.read()
f.close()
  
  
github_session = requests.Session()
github_session.auth = ( "erinata", token)
  
  
github_data = pandas.read_csv("parsed_files/github_data.csv")

starred_url_list = github_data['starred_url']


# print(starred_url_list)
df = pandas.DataFrame()

for starred_url in starred_url_list:
  print(starred_url)
  if (starred_url=="missing"):
    starred_count = "missing"
  else:
    starred_url = starred_url.replace("{/owner}", "").replace("{/repo}", "")
    starred_count = 0 
    for i in range(1000):
      starred_url_with_page = starred_url + "?page=" + str(i+1)
      response_text = github_session.get(starred_url).text
      json_text = json.loads(response_text)
      starred_count = starred_count + len(json_text)
      if len(json_text)  == 0:
        break
      time.sleep(0.1)
  df = pandas.concat([df,
  pandas.DataFrame.from_records([{
    'starred_count': str(starred_count)
    }])
  ])
  time.sleep(0.1)
  
df.to_csv("parsed_files/github_data_starred.csv", index =False)

  
  