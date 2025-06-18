from flask import Flask, request, jsonify

#THIS IS MY SOLUTION FOR jayastro10@gmail.com
app = Flask(__name__)


app.config['SECRET_KEY'] = 'this_is_my_secret_key'


@app.route("/api/process_word", methods=['POST'])
def process_word():
    data = request.get_json()
    word = data.data

    letters = [letter for letter in word]
    letters.sort(key=None)
    
    return jsonify({"word" : letters})
