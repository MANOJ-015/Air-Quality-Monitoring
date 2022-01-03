from flask import Flask,render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    f = requests.get("https://cloud.boltiot.com/remote/412e23fb-904e-406d-95b0-4b6d25c1032b/analogRead?deviceName=BOLT13169334&pin=A0").json()
    return render_template('index.html',f=f)

# @app.route('/cal')
# def calculate():
#     f = requests.get("https://cloud.boltiot.com/remote/412e23fb-904e-406d-95b0-4b6d25c1032b/analogRead?deviceName=BOLT13169334&pin=A0").json()
#     return f'''<h1> {f} </h1>'''


# makes the app to run

if __name__ == "__main__":
    app.run(debug = True)

