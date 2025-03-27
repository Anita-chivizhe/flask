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

movies = [
{
"id": "99",
"name": "Vikram",
"poster": "https://m.media-amazon.com/images/M/MV5BMmJhYTYxMGEtNjQ5NS00MWZiLWEwN2ItYjJmMWE2YTU1YWYxXkEyXkFqcGdeQXVyMTEzNzg0Mjkx._V1_.jpg",
"rating": 8.4,
"summary": "Members of a black ops team must track and eliminate a gang of masked murderers.",
"trailer": "https://www.youtube.com/embed/OKBMCL-frPU",
},
{
"id": "100",
"name": "RRR",
"poster": "https://englishtribuneimages.blob.core.windows.net/gallary-content/2021/6/Desk/2021_6$largeimg_977224513.JPG",
"rating": 8.8,
"summary": "RRR is an upcoming Indian Telugu-language period action drama film directed by S. S. Rajamouli, and produced by D. V. V. Danayya of DVV Entertainments.",
"trailer": "https://www.youtube.com/embed/f_vbAtFSEc0",
},
{
"id": "101",
"name": "Iron man 2",
"poster": "https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_FMjpg_UX1000_.jpg",
"rating": 7,
"summary": "With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) faces pressure from all sides to share his technology with the military. He is reluctant to divulge the secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts (Gwyneth Paltrow) and Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront a powerful new enemy.",
"trailer": "https://www.youtube.com/embed/wKtcmiifycU",
},
{
"id": "102",
"name": "No Country for Old Men",
"poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
"rating": 8.1,
"summary": "A hunter's life takes a drastic turn when he discovers two million dollars while strolling through the aftermath of a drug deal. He is then pursued by a psychopathic killer who wants the money.",
"trailer": "https://www.youtube.com/embed/38A__WT3-o0",
},
{
"id": "103",
"name": "Jai Bhim",
"poster": "https://m.media-amazon.com/images/M/MV5BY2Y5ZWMwZDgtZDQxYy00Mjk0LThhY2YtMmU1MTRmMjVhMjRiXkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_FMjpg_UX1000_.jpg",
"summary": "A tribal woman and a righteous lawyer battle in court to unravel the mystery around the disappearance of her husband, who was picked up the police on a false case",
"rating": 8.8,
"trailer": "https://www.youtube.com/embed/nnXpbTFrqXA",
},
{
"id": "104",
"name": "The Avengers",
"rating": 8,
"summary": "Marvel's The Avengers (classified under the name Marvel Avengers\n Assemble in the United Kingdom and Ireland), or simply The Avengers, is\n a 2012 American superhero film based on the Marvel Comics superhero team\n of the same name.",
"poster": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/avengersendgame_lob_crd_05.jpg",
"trailer": "https://www.youtube.com/embed/eOrNdBpGMv8",
},
{
"id": "105",
"name": "Interstellar",
"poster": "https://m.media-amazon.com/images/I/A1JVqNMI7UL._SL1500_.jpg",
"rating": 8.6,
"summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\n of researchers, to find a new planet for humans.",
"trailer": "https://www.youtube.com/embed/zSWdZVtXT7E",
},
{
"id": "106",
"name": "Baahubali",
"poster": "https://flxt.tmsimg.com/assets/p11546593_p_v10_af.jpg",
"rating": 8,
"summary": "In the kingdom of Mahishmati, Shivudu falls in love with a young warrior woman. While trying to woo her, he learns about the conflict-ridden past of his family and his true legacy.",
"trailer": "https://www.youtube.com/embed/sOEg_YZQsTI",
},
{
"id": "107",
"name": "Ratatouille",
"poster": "https://resizing.flixster.com/gL_JpWcD7sNHNYSwI1ff069Yyug=/ems.ZW1zLXByZC1hc3NldHMvbW92aWVzLzc4ZmJhZjZiLTEzNWMtNDIwOC1hYzU1LTgwZjE3ZjQzNTdiNy5qcGc=",
"rating": 8,
"summary": "Remy, a rat, aspires to become a renowned French chef. However, he fails to realise that people despise rodents and will never enjoy a meal cooked by him.",
"trailer": "https://www.youtube.com/embed/NgsQ8mVkN8w",
},
{
"name": "PS2",
"poster": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5MC00NGUyLWJiYWMtZDI3MTQ1MGU4OGY2XkEyXkFqcGdeQXVyNDExMjcyMzA@._V1_.jpg",
"summary": "Ponniyin Selvan: I is an upcoming Indian Tamil-language epic period action film directed by Mani Ratnam, who co-wrote it with Elango Kumaravel and B. Jeyamohan",
"rating": 8,
"trailer": "https://www.youtube.com/embed/KsH2LA8pCjo",
"id": "108",
},
{
"name": "Thor: Ragnarok",
"poster": "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_.jpg",
"summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\\n of researchers, to find a new planet for humans.",
"rating": 8.8,
"trailer": "https://youtu.be/NgsQ8mVkN8w",
"id": "109",
},
]

@app.get("/movie-list")
def movies_page():
return render_template("movie-list.html", movies=movies)

@app.get("/movie-list/<id>")
def movie_details_page(id):
for movie in movies:
if movie["id"] == id:
return render_template("movie-details.html", movie=movie)
return render_template("not-found.html"), 404

<h2>Hobbies</h2>
    <ul>
      {% for hobby in hobbies %}

      <li>{{hobby}}</li>


    <h2>{{name}} loves:</h2>
    <ul>
      <li>{{hobbies[0]}}</li>
      <li>{{hobbies[1]}}</li>
      <li>{{hobbies[2]}}</li>
      <li>{{hobbies[3]}}</li>
      <li>{{hobbies[4]}}</li>
      <li>{{hobbies[5]}}</li>
    </ul>
