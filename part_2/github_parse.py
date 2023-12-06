import json
import pandas
import glob
import os


if not os.path.exists('parsed_files'):
  os.mkdir('parsed_files')

df = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):
  print(json_file_name)
  # json_file_name = "json_files/erinata.json"
  f = open(json_file_name, "r")
  json_data = json.load(f)
  f.close()

  print(json_data)


  try:
    ghid = json_data['login']
    number_id = json_data['id']
    avatar_url = json_data['avatar_url']
    url = json_data['url']
    followers = json_data['followers']
    following = json_data['following']
    name = json_data['name']
    company = json_data['company']
    blog = json_data['blog']
    location = json_data['location']
    email = json_data['email']
    hireable = json_data['hireable']
    bio = json_data['bio'].replace("\r","").replace("\n","")
    created_at = json_data['created_at']
    updated_at = json_data['updated_at']
    public_repos = json_data['public_repos']
    public_gists = json_data['public_gists']
    twitter_username = json_data['twitter_username']
    starred_url = json_data['starred_url']
    followers_url = json_data['followers_url']
    following_url = json_data['following_url']
    gists_url = json_data['gists_url']
    repos_url = json_data['repos_url']
  except:
    ghid = json_file_name.replace("json_files/","").replace(".json","").replace(" ","")
    number_id = "missing"
    avatar_url = "missing"
    url = "missing"
    followers = "missing"
    following = "missing"
    name = "missing"
    company = "missing"
    blog = "missing"
    location = "missing"
    email = "missing"
    hireable = "missing"
    bio = "missing"
    created_at = "missing"
    updated_at = "missing"
    public_repos = "missing"
    public_gists = "missing"
    twitter_username = "missing"
    starred_url = "missing"
    followers_url = "missing"
    following_url = "missing"
    gists_url = "missing"
    repos_url = "missing"


  df = pandas.concat([df,  
    pandas.DataFrame.from_records([{
        'ghid': ghid,
        'number_id': number_id,
        'avatar_url': avatar_url,
        'url': url,
        'followers': followers,
        'following': following,
        'name': name,
        'company': company,
        'blog': blog,
        'location': location,
        'email': email,
        'hireable': hireable,
        'bio': bio,
        'created_at': created_at,
        'updated_at': updated_at,
        'public_repos': public_repos,
        'public_gists': public_gists,
        'twitter_username': twitter_username,
        'starred_url': starred_url,
        'followers_url': followers_url,
        'following_url': following_url,
        'gists_url': gists_url,
        'repos_url': repos_url
      }])
    ])

df = df.sort_values(by=['ghid'])
df.to_csv("parsed_files/github_data.csv", index =False)

