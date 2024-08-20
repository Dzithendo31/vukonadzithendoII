import json
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    image_count = 60  # Number of images you have (e.g., img01.jpg to img10.jpg)
    unique_random_numbers = random.sample(range(1, image_count + 1), image_count)
    images = [f'img{i:02}.jpg' for i in unique_random_numbers]
    with open("song.json",'r') as file:
        data = json.load(file)
    songs = data['songs']
    songId = 1
    song = next(song for song in songs if song['id'] == songId)
    return render_template('index.html', images=images,song=song)

if __name__ == '__main__':
    app.run(debug=True)
