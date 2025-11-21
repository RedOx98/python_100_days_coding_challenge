from flask import Flask, render_template, json, request, jsonify
from flask_mail import Mail, Message
import random
# from time import da
import datetime
import requests
random_number = random.randint(0, 9)


app = Flask(__name__)

# Mail Config
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'olaskeet@gmail.com'
# app.config['MAIL_PASSWORD'] = 'snvjgxxtriwyaion'   # Not gmail password
# app.config['MAIL_DEFAULT_SENDER'] = '<noreply>@gmail.com'
# Mail Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True      # SSL for port 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'olaskeet@gmail.com'
app.config['MAIL_PASSWORD'] = 'snvjgxxtriwyaion'  # App password, correct
app.config['MAIL_DEFAULT_SENDER'] = 'olaskeet@gmail.com'  # MUST be valid


mail = Mail(app)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")  # ✅ correct API URL
    response.raise_for_status()  # raises an error for 4xx/5xx responses
    blogs = response.json()  # now safe to parse
    print(blogs)
    return render_template("/index.html", blogs=blogs)

@app.route('/about')
def about():
    return render_template("/about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    print("inside contact page")
    if request.method == "POST":
        data = request.get_json()  # <-- Use get_json() for safety

        name = data.get("name")
        print(f"name is {name}")
        email = data.get("email")
        print(f"email is {email}")
        phone = data.get("phone")
        print(f"phone is {phone}")
        message_text = data.get("message")
        print(f"message is {message_text}")

        try:
            msg = Message(
                subject=f"New Contact Form Message from {name}",
                recipients=["bulqcommerce@gmail.com"],
                body=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message_text}
"""
            )
            mail.send(msg)
            return jsonify({"status": "success"}), 200

        except Exception as e:
            print("Email error:", e)
            return jsonify({"status": "error"}), 500

    # GET → Return contact page
    return render_template("contact.html")


# @app.route('/guess/<string:name>')
# def guess(name):
#     req_age = f"https://api.agify.io?name={name}"
#     age_response = requests.get(req_age)
#     age = age_response.json().get('age')
#     print(age)
#     req_gender = f"https://api.genderize.io/?name={name}"
#     gender_response = requests.get(req_gender)
#     gender = gender_response.json().get('gender')
#     print(gender)
#     print(gender)
#     year = datetime.datetime.now().year
#     return render_template("/index.html", age=age, gender=gender, name=name)

# @app.route('/blog')
# def blog():
#     response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")  # ✅ correct API URL
#     response.raise_for_status()  # raises an error for 4xx/5xx responses
#     blogs = response.json()  # now safe to parse
#     print(blogs)
#     return render_template("/index.html", blogs=blogs)

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