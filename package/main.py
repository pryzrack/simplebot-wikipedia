import wikipediaapi
from flask import Flask, render_template


wiki_wiki = wikipediaapi.Wikipedia(
        language='es',
    extract_format=wikipediaapi.ExtractFormat.HTML
)

p_wiki = wiki_wiki.page("python")

app = Flask(__name__)
# home route
@app.route("/")
def hello():
    return p_wiki.text

app.run(debug = True)
