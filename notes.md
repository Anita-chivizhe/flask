# /movies -> movies

@app.get("/movies")
def get_all_movies(): # Auto converts data -> JSON (Flask)
return movies

# /movies/100 - <id> -> Variable

@app.get("/movies/<id>")
def get_movie_by_id(id): # Auto converts data -> JSON (Flask)
for movie in movies:
if movie["id"] == id:
return movie
return {"message": "Movie not found"}, HTTP_NOT_FOUND

@app.delete("/movies/<id>")
def delete_movie_by_id(id): # Auto converts data -> JSON (Flask)
for movie in movies:
if movie["id"] == id:
movies.remove(movie)
return {"message": f"{id}Movie deleted successfully"}, 200
return {"message": "Movie not found"}, HTTP_NOT_FOUND

@app.post("/movies")

# def generate_movie_id():

# highest_id = max(movie["id"] for movie in movies)

# return highest_id + 1

def create_movies():
new_movie = request.get_json()
print(new_movie)
ids = [int(movie["id"]) for movie in movies]
new_movie["id"] = str(max(ids) + 1)
movies.append(new_movie)
return {"message": "Movie created successfully"}

@app.put("/movies/<id>")
def update_movie_by_id(id):
body = request.get_json()
pprint(body)
print(id)
for movie in movies:
if movie["id"] == id:
movie.update(body)
return {"message": f"{id}Movie updated successfully"}, 200
return {"message": "Movie not found"}, HTTP_NOT_FOUND
