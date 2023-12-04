# Tests for your routes go here


# calling POST /albums with album info adds that
# album to the list in GET /albums


def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/music_store.sql")
    post_response = web_client.post(
        "/albums", data={"title": "Voyager", "release_year": "2022", "artist_id": "2"}
    )

    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert (
        get_response.data.decode("utf-8")
        == "Album(1, Demon Days, 2005, 1)\nAlbum(2, Voyager, 2022, 2)"
    )


# calling GET /albums returns a list of albums


def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" "Album(1, Demon Days, 2005, 1)"
