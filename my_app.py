from flask import Flask

app = Flask(__name__)

@app.route('/')
def web_content():
    return "**** Hello,This is a Git Automated Test Page_From_@dil ****"

if __name__ == "__main__":
    app.run(debug=True)