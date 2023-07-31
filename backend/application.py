from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import nltk
import re
import pickle 
custom_nltk_data_path = "backend/"
nltk.data.path.append(custom_nltk_data_path)
import spacy
sp = spacy.load('en_core_web_sm')
spacy_stopwords = sp.Defaults.stop_words

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.models import load_model, model_from_json

app = Flask(__name__)
CORS(app)
ps = PorterStemmer()

# loading of the saved model and vectorizer using pickle
# model = load_model('nn_model.keras')
# with open('model_json', 'r') as json_file:
#     loaded_model_json = json_file.read()
# loaded_model = model_from_json(loaded_model_json)
# loaded_model.load_weights("model.h5")

loaded_model = pickle.load(open('pac_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# building the functionalities 
@app.route('/', methods = ['GET'])
def homePage() :
    return render_template('base.html')

def get_prediction(text) : 
    review = re.sub('^[a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in spacy_stopwords]
    review = ''.join(review)
    review_vector = vectorizer.transform([review]).toarray()
    # prediction_value = loaded_model.predict(review_vector)
    # print(prediction_value)
    # if prediction_value > 0.7:
    #     prediction = "Real News"
    # elif 0.4 < prediction_value <= 0.7:
    #     prediction = "Suspicious piece of news. Please check the credibility of the source"
    # else:
    #     prediction = "Fake News"
    prediction = 'FAKE' if loaded_model.predict(review_vector) == 0 else 'REAL'
    # prediction = "Testing"
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







