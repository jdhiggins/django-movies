import csv
import json
from datetime import datetime

print("Converting users...")
users = []
with open("data/ml-1m/users.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        users.append({"model": "moviebase.Rater",
                      "pk": row[0],
                      "fields": {
                          "gender": row[1],
                          "age": row[2],
                          "job": row[3],
                          "zip_code": row[4]
                      }})

with open("movieratings/fixtures/users.json", "w") as outfile:
    outfile.write(json.dumps(users))

print("Converting movies...")
movies = []
with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        movies.append({"model": "moviebase.Movie",
                       "pk": row[0],
                       "fields": {
                           "title": row[1],
                       }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
    outfile.write(json.dumps(movies))

print("Converting ratings...")
ratings = []
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for idx, row in enumerate(reader):
        posted_at = datetime.fromtimestamp(int(row[3])).strftime('%Y-%m-%d %H:%M:%S')
        ratings.append({"model": "moviebase.Rating",
                        "pk": idx + 1,
                        "fields": {
                            "rater": row[0],
                            "movie": row[1],
                            "rating": row[2],
                            "posted_at": posted_at,
                        }})

with open("movieratings/fixtures/ratings.json", "w") as outfile:
    outfile.write(json.dumps(ratings))


print("Converting genres...")
genres = []
with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        genre_row_values = row[2].split("|")
        for genre_value in genre_row_values:
            genres.append({"model": "moviebase.Genre",
                            "": genre_value,
                            "fields": {
                                "movie": row[0],
                            }})


with open("movieratings/fixtures/genres.json", "w") as outfile:
    outfile.write(json.dumps(genres))


