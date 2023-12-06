import pandas
import os

import matplotlib.pyplot as pyplot
import numpy


if not os.path.exists('graph'):
  os.mkdir('graph')
  
dataset = pandas.read_csv("data_output/dataset.csv")


print(sum((dataset["ghid"] != dataset['ghid_charcoalpaper'])*1))
print(sum((dataset["public_repos"] != dataset['repocount_charcoalpaper'])*1))
print(sum((dataset["followers"] != dataset['followercount_charcoalpaper'])*1))






pyplot.scatter( numpy.log(dataset['followers']) , numpy.log(dataset['following']), c=numpy.log(dataset['public_repos'] ) )
pyplot.title("Relationship between followers and following")
pyplot.xlabel("followers")
pyplot.ylabel("following")
pyplot.colorbar()
pyplot.savefig("graph/plot_followers_following.png")
pyplot.close()




dataset["created_at_date"] = [d.split("T")[0] for d in dataset['created_at']]
print(dataset["created_at_date"])

dataset["created_at_year"] = [int(d.split("-")[0]) for d in dataset['created_at']]
print(dataset["created_at_year"])



pyplot.scatter( numpy.log(dataset['followers']) , numpy.log(dataset['following']), c=dataset['created_at_year'] ) 
pyplot.title("Relationship between followers and following by year")
pyplot.xlabel("followers")
pyplot.ylabel("following")
pyplot.colorbar()
pyplot.savefig("graph/plot_followers_following_by_year.png")
pyplot.close()


