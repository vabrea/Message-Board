from flask import Flask


app = Flask(__name__)




@app.get("/aboutme")
def index():
    me = {
        "first_name": "Von",
        "last_name": "Abrea",
        "hobbies": "Snowboarding"
    }
    return me

