@movies_bp.put("/<id>")
def update_movie_by_id(id):
body = request.get_json() # body
movie = Movie.query.get(id) # None if no movie

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

    # data = movie.to_dict()  # copy of the data
    # data.update(body)  # updating copy
    # print(data)

    try:
        movie.update(body)
        db.session.commit()
        return movie.to_dict()

    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]

@movies_bp.put("/<id>")
def update_movie_by_id(id):
body = request.get_json() # body
movie = Movie.query.get(id)
for movie in movies:
if movie["id"] == id:
movie.update(body)
return {"message": "Movie updated successfully", "data": movie}
return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]
