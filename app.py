import json
from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    image_count = 65  # Number of images you have (e.g., img01.jpg to img10.jpg)
    unique_random_numbers = random.sample(range(1, image_count + 1), image_count)
    images = [f'img{i:02}.jpg' for i in unique_random_numbers]
    with open("song.json",'r') as file:
        data = json.load(file)
    songs = data['songs']
    qoutes = data['qoutes']

    today = datetime.date.today()
    # Format the date as MMDD (e.g., 0312 for March 12)
    date_str = today.strftime('%d')
    dayImg = f'img{date_str:02}.jpg'
    songId = int(date_str)
    song = next(song for song in songs if song['id'] == songId)
    koute = next(qoute for qoute in qoutes if qoute['id'] == songId)

    return render_template('index.html', images=images,songLink=song['link'],dayImg = dayImg,songMessage = song['message'],qoute=koute['koute'])

if __name__ == '__main__':
    app.run(debug=True)
