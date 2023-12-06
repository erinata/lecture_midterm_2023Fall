import urllib.request
import os

if not os.path.exists("html_files"):
  os.mkdir("html_files")

f = open("html_files/charcoalpaper.html", "wb")
response = urllib.request.urlopen("http://www.charcoalpaper.com/exams/github/user/dataset")
html = response.read()
f.write(html)
f.close()


