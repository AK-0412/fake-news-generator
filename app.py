from flask import Flask, render_template
import random

app = Flask(__name__)

# lists used for making random news
people = ["Scientists", "Government", "Researchers", "Tech companies","Researchers", "Celebrities", "Doctors", "AI Robots"]
actions = ["discover", "announce", "reveal", "launch", "investigate", "announce", "secretly develop"]
things = [
     "a secret city under the ocean",
    "a device that controls weather",
    "a hidden alien base on the moon",
    "a technology that reads minds",
    "a cure that can stop aging",
    "a plan to control the internet"
]
locations = ["in India", "in Antarctica", "on Mars", "in a secret lab","in America", "in Iran"]


# function to create random news
def make_news():
    p = random.choice(people)
    a = random.choice(actions)
    t = random.choice(things)
    l = random.choice(locations)

    news_line = p + " " + a + " " + t + " " + l
    return news_line


@app.route("/")
def home():
    line = make_news()
    return render_template("index.html", news=line)


if __name__ == "__main__":
    app.run(debug=True)

