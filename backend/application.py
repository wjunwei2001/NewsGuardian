from flask import Flask, render_template, request, jsonify
import nltk
import re
import pickle 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.models import load_model

app = Flask(__name__)
ps = PorterStemmer()

# loading of the saved model and vectorizer using pickle
model = load_model('nn_model.keras')
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# building the functionalities 
@app.route('/', methods = ['GET'])
def homePage() :
    return render_template('base.html')

def predict(text) : 
    review = re.sub('^[a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in 
              stopwords.words('english')]
    review = ''.join(review)
    review_vector = vectorizer.transform([review]).toarray()
    prediction = 'Fake News' if model.predict(review_vector)[0][0] <= 0.6 else 'Real News'
    return prediction

@app.route('/', methods=['POST'])
def webapp() :
    text = request.form['text']
    prediction = predict(text)
    return render_template('base.html', text = text, result = prediction)


if __name__ == "__main__" :
    app.run()







