import pickle
from flask import Flask, request

app = Flask(__name__)
model = pickle.load(open('sentiment.pkl', 'rb'))

@app.route('/analyze', methods=['GET'])
def analyze():
    if "text" in request.args:
        text = request.args.get('text')
    else:
        return "No string to analyze"

    score = model.predict_proba([text])[0][1]
    return str(score)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')