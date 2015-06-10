import csv
import json

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
                           "title": row[1]
                       }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
    outfile.write(json.dumps(movies))

print("Converting ratings...")
ratings = []
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for idx, row in enumerate(reader):
        ratings.append({"model": "moviebase.Rating",
                        "pk": idx + 1,
                        "fields": {
                            "rater": row[0],
                            "movie": row[1],
                            "rating": row[2]
                        }})

with open("movieratings/fixtures/ratings.json", "w") as outfile:
    outfile.write(json.dumps(ratings))