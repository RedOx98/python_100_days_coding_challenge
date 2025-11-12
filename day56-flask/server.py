from flask import Flask, render_template
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)