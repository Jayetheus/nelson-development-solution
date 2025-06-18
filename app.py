from flask import Flask, request, jsonify, render_template

#THIS IS MY SOLUTION FOR jayastro10@gmail.com
app = Flask(__name__)


app.config['SECRET_KEY'] = 'this_is_my_secret_key'



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/process-word", methods=['POST'])
def process_word():
    data = request.get_json()
    word = data["data"]

    letters = [letter for letter in word]
    letters.sort(key=None)

    return jsonify({"word" : letters})

  

app.run(debug=True)