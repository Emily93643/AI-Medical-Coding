from flask import Flask, render_template, jsonify, request
from coding import get_coded_term
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test1.html')

@app.route('/coding', methods=['POST'])
def get_coding():
    if request.method == 'POST':
      term = request.form['term']
      dict = request.form['dict']
      top_k = request.form['top_k']
       
      # check for empty string/string only spaces
      if not bool(dict.strip()):
        dict = "meddra26_1"

      if not bool(term.strip()):
         return render_template('index.html')

      coding_data = get_coded_term(dict, term, top_k)
    #   return jsonify(data=coding_data.to_json(orient="records"))
      return jsonify(data=coding_data)
    else:
        return 'Only POST requests are allowed.'     

if __name__ == "__main__":
    print("\n *** Server started!: localhost:8000 ***\n")
    serve(app, host="0.0.0.0", port=8000)
    
