from flask import Flask
app = Flask(__name__)

@app.route("/index")
def indexku ():
    return "halo sayang"

if __name__ == "__main__":
    app.run(debug=True)