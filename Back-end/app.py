from flask import Flask, render_template, request, jsonify
import requests
from DAO import PrevSearch


app = Flask(__name__, static_folder='public')

#API stuff
API_URL = "https://newsapi.org/v2/everything"
API_KEY = "7f4b76d59b4f49ff94d3fa7b473a5d23"

#route to default homepage
@app.route('/')
def index():
    return render_template('index.html')

#function to collect all users previous seraches
@app.route('/previous_searches', methods=['GET'])
def previous_searches():
    #finds the search queries in chronological order
    searches = PrevSearch.get_all_searches()
    #returns the queries back to the html
    return jsonify({"previous_searches": [search[0] for search in searches]})

#finds user searches
@app.route('/search.html')
def search():
    #collects user search from URL
    query = request.args.get("q")
    if query:
        #set the query as a database entry and save it
        search = PrevSearch(query)
        search.save()
        #collect API results 
        search_results = news_search(query)
        #send the user to the search page with the articles listed
        return render_template("search.html", articles=search_results)
    #otherwise default to the homepage
    else:
        return render_template("index.html")

#search result finder function
@app.route('/get_previous_searches', methods=['GET'])
def get_previous_searches():
    #attempt to retrieve all searches from the database
    try:
        previous_searches = PrevSearch.get_all_searches()
        #return all searches back into the index.html
        return jsonify([search[0] for search in previous_searches])
    #otherwise assume error
    except Exception as e:
        return jsonify({'error': str(e)})
    
#news searching function
def news_search(query):
    #formats the search parameters
    parameters = {"q": query, "apiKey": API_KEY, "language": "en", "pageSize": 20}
    news = []
    #gets a response from the NewsAPI
    res = requests.get(API_URL, params = parameters)
    #returns a search if the API is successful
    if(res.status_code == 200):
        news = res.json().get("articles", [])
    return news

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

