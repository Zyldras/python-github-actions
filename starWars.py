import requests
import json


def getMoviesWithLuke ():
	l = []
	luke = requests.get("https://swapi.py4e.com/api/people/1/").json()

	print(luke)

	for film in luke["films"]:
		title = requests.get(film).json()["title"]
		l.append(title)

	return l


# print(swapi.json())

print(getMoviesWithLuke())