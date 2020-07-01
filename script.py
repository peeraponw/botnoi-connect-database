import pymongo 
from flask import Flask, jsonify
import json

URI = 'mongodb://heroku_672rlh8s:s18fo4q6ejpm67lmodcn4hqjil@ds161551.mlab.com:61551/heroku_672rlh8s'

client = pymongo.MongoClient(URI)

app = Flask(__name__)

@app.route('/')
def connect_db():
	db = client['heroku_672rlh8s']

	query = {}

	collection = db['covid_stats']

	cursor = collection.find(query, projection={"_id":0})
	results = []
	for doc in cursor:
		results.append(doc)
	print(results)
	return jsonify(results)

if __name__=="__main__":
	app.run(debug=True)

