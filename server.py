from flask import Flask, render_template, request
from coding import get_coded_term
from waitress import serve
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/coding')
def get_coding():
    dict = request.args.get('dict')
    version = request.args.get('version')
    term = request.args.get('term')

    # check for empty string/string only spaces
    if not bool(dict.strip()):
        dict = "MedDRA"
    if not bool(version.strip()):
        version = "36.1"
    if not bool(term.strip()):
        return render_template('index.html')

    coding_data = get_coded_term(dict, version, term)
   
    # city is not found by API
    if not bool(coding_data.strip()):
        return render_template('code-not-found.html')

    return render_template(
        "coding.html", 
        coded_term = coding_data['data'][0]
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
