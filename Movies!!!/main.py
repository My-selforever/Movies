import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

f = open('Movies.csv',encoding="utf-8")

r = csv.reader(f)

data = list(r)

allMovies = []
allMovies = data[1:]

Liked = []

Disliked = []

Unwatched = []


@app.route('/get-all-movies')
def getMov():
    return jsonify({
        'data': allMovies[0],
        'status': 'Success'
    })


if (__name__ == "__main__"):
    app.run()
