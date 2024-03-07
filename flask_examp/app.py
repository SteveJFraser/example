from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def index():
    
    home_page_links = {"Google": "https://google.com/", "pypy, packaging, python": "https://pypi.org/project/packaging/"}
        
    return render_template("index.html", home_page_links=home_page_links)


if __name__ == "__main__":
    app.run(debug=True)