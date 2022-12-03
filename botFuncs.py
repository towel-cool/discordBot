import json
import requests
import random

def getLyrics(songTitle):
    # Code from https://github.com/5ifty/Genius/blob/master/index.py

    url = f"https://some-random-api.ml/lyrics?title={songTitle}"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    if ('error' not in parsed):
        title = parsed["title"]
        lyrics = parsed["lyrics"]
        artist = parsed["author"]
        return [title, lyrics, artist]
    else:
        return [parsed["error"]]

def getImage():
  imageID = random.randrange(0,1084)
  image = f"https://picsum.photos/id/{imageID}/900"
  return image