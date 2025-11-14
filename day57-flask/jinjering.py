from flask import Flask, render_template, json
import random
# from time import da
import datetime
import requests
random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")  # ✅ correct API URL
    response.raise_for_status()  # raises an error for 4xx/5xx responses
    blogs = response.json()  # now safe to parse
    print(blogs)
    return render_template("/index.html", blogs=blogs)
    # rand = random.randint(0, 9)
    # year = datetime.datetime.now().year
    # return render_template("/index.html", num=rand, today=year)

@app.route('/guess/<string:name>')
def guess(name):
    req_age = f"https://api.agify.io?name={name}"
    age_response = requests.get(req_age)
    age = age_response.json().get('age')
    print(age)
    req_gender = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(req_gender)
    gender = gender_response.json().get('gender')
    print(gender)
    print(gender)
    year = datetime.datetime.now().year
    return render_template("/index.html", age=age, gender=gender, name=name)

@app.route('/blog')
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")  # ✅ correct API URL
    response.raise_for_status()  # raises an error for 4xx/5xx responses
    blogs = response.json()  # now safe to parse
    print(blogs)
    return render_template("/index.html", blogs=blogs)

@app.route('/post/<int:id>')
def blog_post(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")  # ✅ correct API URL
    response.raise_for_status()  # raises an error for 4xx/5xx responses
    blogs = response.json()  # now safe to parse
    # find the correct post
    blog = next((post for post in blogs if post["id"] == id), None)
    print(blogs)
    return render_template("/post.html", blog=blog, id=id)
# render_template("/blog.html", blog=blogs)

if __name__ == "__main__":
    app.run(debug=True)