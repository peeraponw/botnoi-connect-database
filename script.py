from bs4 import BeuatifulSoup
import requests
import pymongo
from flask import Flask

URI = 'mongodb://heroku_672rlh8s:s18fo4q6ejpm67lmodcn4hqjil@ds161551.mlab.com:61551/heroku_672rlh8s'

client = pymongo.MongoClient(URI)

@app.route('/')
def connect_db():
	db = client['heroku_672r1h8s']

	query = {}

	collection = db['covid_stats']

	cursor = collection.find(query)

	results = []
	for doc in cursor:
		results.append(doc)
	return jsonify(results)

if __name__=="__main__":
	app.run()

