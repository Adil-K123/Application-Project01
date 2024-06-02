from flask import Flask

app = Flask(__name__)

@app.route('/')
def web_content():
    return "**** Yes,it is working!!!!!!!!!!! ****"

if __name__ == "__main__":
    app.run(debug=True)