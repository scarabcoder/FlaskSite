from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    users = [
    {
    'nickname': 'Nicholas',
    'handle': 'ScarabCoder',
    'image': 'https://pbs.twimg.com/profile_images/670654474776526848/oEzEzDV__400x400.jpg'
    },
    {
    'nickname': "Jonathan",
    'handle': 'johntastic',
    'image': 'static/jonathan.jpg'
    },
    {
    'nickname': "Simeon",
    'handle': 'StarWarsGeek_'
    }
    ]
    user = users[0]  # fake user
    posts = [
        {
        'author': users[1],
        'body': "Having fun making my jeep run!",
        'tags': ''
        },
        {
        'author': users[2],
        'body': "Anyone wanna play #Minecraft with me?",
        'tags': 'minecraft'
        },
        {
        'author': users[0],
        'body': "Programming with Flask and Python"
        }
    ]
    return render_template('index.html',
                            title = 'Scarab\'s blog',
                           user=user,
                           posts=posts)
