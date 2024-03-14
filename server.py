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
    top_k = int(request.args.get('top_k'))
    
    # check for empty string/string only spaces
    if not bool(dict.strip()):
        dict = "MedDRA"
    if not bool(version.strip()):
        version = "36.1"
    if not bool(term.strip()):
        return render_template('index.html')

    coding_data = get_coded_term(dict, version, term, top_k)
      
  #    if coding_data.empty:
  #       return render_template('code-not-found.html')

    return render_template(
        "coding.html", 
        term=term,
        top_k=top_k,
          json_data = coding_data[['term', 'llt_code', 'llt_name', 'pt_code', 'pt_name', 'soc_name', 'soc_code', 'hlt_name', 'hlt_code', 'hlgt_name', 'hlgt_code']].to_dict(orient='records'),
        #llt_name = coding_data.iloc[0, 3],
        #llt_code = coding_data.iloc[0, 1]
        #context= coding_data.loc[0, 'llt_code']
    )

if __name__ == "__main__":
    print("\n *** Server started!: localhost:8000 ***\n")
    serve(app, host="0.0.0.0", port=8000)
    
