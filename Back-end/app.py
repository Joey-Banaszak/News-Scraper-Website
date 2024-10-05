from flask import Flask, render_template, request
from newsapi import NewsApiClient
import requests

app = Flask(__name__, static_folder='public')

API_URL = "https://newsapi.org/v2/everything"
API_KEY = "7f4b76d59b4f49ff94d3fa7b473a5d23"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search.html')
def search():
    query = request.args.get("q")
    if query:
        search_results = news_search(query)
        return render_template("search.html", articles=search_results)
    else:
        return render_template("index.html")


def news_search(query):
    parameters = {"q": query, "apiKey": API_KEY, "language": "en", "pageSize": 20}
    news = []
    res = requests.get(API_URL, params = parameters)
    if(res.status_code == 200):
        news = res.json().get("articles", [])
    return news

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
