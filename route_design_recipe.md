# music_web_app Route Design Recipe

    Your test should assert that the new album is present in the list of records returned by GET /albums

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

```

## 2. Create Examples as Tests


```python

# POST Request to Add an Album
# Endpoint: POST /albums
# Parameters (in request body):
#     - title: "Voyage"
#     - release_year: 2022
#     - artist_id: 2

# Expected Response:
#     - Status Code: 200 OK
#     - Response Body: No content

"""
returns - no content
adds album to list (database)
"""

# GET /albums
# Response 200 OK

"""
returns - 
Album('Demon Days', 2005, 1)
Album('Voyager', 2022, 2)

"""

```

## 3. Test-drive the Route

```python

"""
POST /albums
  Parameters:
    title: Voyager
    release_year: 2022
    artist_id: 2
  Expected response (200 OK)
"""
def test_post_submit(web_client):
    response = web_client.post('/albums', data={'title': 'Voyager', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```
