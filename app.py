from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

ourstory = Story(["name", "noun", "person", "verb", "second person", "color", "second noun", "city/state", "second verb", "third verb", "fourth verb", "third noun", "food", "name of school"], "Hi! My name is {name} and I have a secret to share with you. I'm a normal kid by day, but a {noun} by night. Only you and my best friend {person} know my secret. You may be wondering how this happened? Well, one night I was {verb} at home, and then BOOM! The lights went out and {second person} appeared. In a booming voice, they said 'because your favorite color is {color} you have been chosen to be a {noun}'. My mission is to save the people of {city/state} by doing my favorite things: {second verb}, {third verb}, and {fourth verb}. This may sound easy, but it's no walk in the park. It requires hard work and {second noun}. My weakness is eating {food} - it's gross! Keep that away from me!! I save the world every night, but when I wake up in the morning, I go back to my normal life at {name of school}.")

@app.route('/')
def index():
    prompts = ourstory.prompts
    return render_template('index.html', prompts=prompts)

@app.route('/story')
def story():
    storytext = ourstory.generate(request.args)
    return render_template('story.html', text=storytext)