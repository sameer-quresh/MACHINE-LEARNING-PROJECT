from flask import Flask, render_template, request, jsonify
# import random
import pickle
app = Flask(__name__)
model = pickle.load(open('model_pickle','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review_text = request.form['reviewText']
    # is_fake = random.random() < 0.5
    prediction = model.predict_proba(review_text)
    output = '{0:.{1}f}'.format(prediction[0][1],2)
    is_real>=0.85
    result = 'This review is likely fake.' if is_real else 'This review is likely genuine.'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)