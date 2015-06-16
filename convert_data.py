import csv
import json
from datetime import datetime
from datetime import timezone

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


print("Converting ratings...")
ratings = []
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for idx, row in enumerate(reader):
        posted_at = datetime.fromtimestamp(int(row[3]), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
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


print("Converting movies...")
movies = []
genres_dict = {'Action': 1, 'Adventure': 2, 'Animation': 3, '''Children's''': 4, 'Comedy': 5,
'Crime': 6, 'Documentary': 7,'Drama': 8, 'Fantasy': 9, 'Film-Noir': 10, 'Horror': 11, 'Musical': 12, 'Mystery': 13,
'Romance': 14, 'Sci-Fi':15, 'Thriller': 16, 'War': 17, 'Western': 18}

with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
   reader = csv.reader((line.replace("::", "_") for line in infile),
                       delimiter="_")
   for row in reader:
       genres_list = row[2].split("|")
       genres_keys = [genres_dict[g] for g in genres_list]
       movies.append({"model": "moviebase.Movie",
                      "pk": row[0],
                      "fields": {
                          "title": row[1],
                          "genre": genres_keys
                      }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
   outfile.write(json.dumps(movies))




print("Converting genres...")
genres = []
for k, v in genres_dict.items():
   genres.append({"model": "moviebase.Genre",
                       "pk": v,
                       "fields": {
                           "genre": k,
                       }})

with open("movieratings/fixtures/genres.json", "w") as outfile:
   outfile.write(json.dumps(genres))
