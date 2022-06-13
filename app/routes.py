from app import app
from flask import render_template
from flask import Blueprint
import requests as r
from marvel import Marvel 
# m=Marvel("58a542f44f06c07f2cd106c20a53ea37","2a38bb0597f9942fea16b293c9a92e72505fdc41")
# all_character=character.all()
# install requests and Marvel so I can make api calls
@app.route('/')
def home():
    greeting = 'Hello!'
    print(greeting)
    return render_template('index.html')
# about page setup
@app.route('/about')
def about():
    return render_template('about.html')

# api call to Marvel api for character info
@app.route('/characters')
def marvelcharacters():
    # try:
    # except:
    data = r.get('http://gateway.marvel.com/v1/public/characters?ts=1&apikey=58a542f44f06c07f2cd106c20a53ea37&hash=aee49f3b70e753445ae9f599ac2c9767')

    if data.status_code == 200:
        data = data.json()
    return render_template('marvel.html', data=data)



