import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)


@app.route("/test")
def test_route():
    return "Test route works!"


@app.route("/albums", methods=["POST"])
def post_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = Album(
        None,
        request.form["title"],
        request.form["release_year"],
        request.form["artist_id"],
    )
    repo.create(album)
    return "", 200


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    return "\n".join(f"{album}" for album in repo.all())


@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    return "\n".join(f"{artist}" for artist in repo.all())


@app.route("/artists", methods=["POST"])
def post_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = Artist(None, request.form["artist"])
    repo.create(artist)
    return "", 200


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes

apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
