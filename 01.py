from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return '''
        <form action = "/login" method = "post">
        Password: <input type="text"><br>
        <input type = "submit">
        </form>
        '''
    if request.method == "POST":
        return "logged in"



if __name__ == "__main__":
    app.run(debug=True)