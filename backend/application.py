from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import nltk
import re
import pickle 
custom_nltk_data_path = "/opt/render/nltk_data"
nltk.data.path.append(custom_nltk_data_path)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.models import load_model

app = Flask(__name__)
CORS(app)
ps = PorterStemmer()

# loading of the saved model and vectorizer using pickle
model = load_model('nn_model.keras')
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# building the functionalities 
@app.route('/', methods = ['GET'])
def homePage() :
    return render_template('base.html')

def get_prediction(text) : 
    review = re.sub('^[a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in 
              stopwords.words('english')]
    review = ''.join(review)
    review_vector = vectorizer.transform([review]).toarray()
    if model.predict(review_vector)[0][0] > 0.7:
        prediction = "Real News"
    elif 0.4 < model.predict(review_vector)[0][0] <= 0.7:
        prediction = "Suspicious piece of news. Please check the credibility of the source"
    else:
        prediction = "Fake News"
    return prediction

@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction = get_prediction(text)
    return render_template('base.html', text=text, result=prediction)

@app.route('/predict/', methods=['GET','POST'])
def predict() :
    data = request.get_json()
    text = data['text']
    prediction = get_prediction(text)
    return jsonify({'result': prediction})

# import time
# @app.route('/time')
# def get_current_time():
#     return {'time': time.time()}

if __name__ == "__main__" :
    app.run()







