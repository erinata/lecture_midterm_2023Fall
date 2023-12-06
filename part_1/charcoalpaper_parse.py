from bs4 import BeautifulSoup
import pandas

import os

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")
  
df = pandas.DataFrame()

file_name = "html_files/charcoalpaper.html"
f=open(file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

print(soup)

wrapper_span = soup.find("span", {"id": "wrapper"})
grids = wrapper_span.find_all("div", {"class": "grid"})

# 
for grid in grids:
  user = grid.find("div", {"class": "userid"})
  if user != None:
    ghid = user.text
    ghid = user['ghid'].split("--")[2].replace(" ", "")
    repocount = grid.find("div", {"class": "repocount"})
    if repocount != None:
      repocount = repocount.text
    followercount = grid.find("div", {"class": "followercount"})
    if followercount != None:
      followercount = followercount.text.replace("*", "").replace(" ", "")
    membersince = grid.find("div", {"class": "membersince"})
    if membersince != None:
      membersince = membersince.text.replace("(", "").replace(")", "").replace(" ", "")  

    df = pandas.concat([df,  
      pandas.DataFrame.from_records([{
          "ghid": ghid,
          "repocount": repocount,
          "followercount": followercount,
          "membersince": membersince
        }])
      ])    

df = df[df.duplicated(subset=['ghid'])==False].sort_values(by=['ghid'])

df.to_csv("parsed_files/charcoalpaper.csv", index =False)

  
  



  
  