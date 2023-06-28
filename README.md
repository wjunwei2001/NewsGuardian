# NewsGuardian
~ Description of project ~

# Data Processing
The dataset used for training the models was obtained from Kaggle's Fake and Real News Dataset (https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). The dataset consists of texts which centred around political news.

During the data processing phase, the dataset was cleaned and preprocessed to remove any irrelevant information and perform text normalization techniques such as tokenization, stemming, and stop-word removal using NLTK library. This step ensured that the data was in a suitable format for training the machine learning models.

# Feature Engineering


# Model Training
To identify the best performing model for the fake news detection task, multiple machine learning models were trained and evaluated. The following models were included in the experimentation process: 

1) **Gaussian Naive Bayes Classifier**

This model is a variant of Naive Bayes that follows Gaussian normal distribution and is known for its efficiency with high-dimensional data. It is a supervised machine learning classification algorithm based on the Bayes theorem. 

Accuracy: 0.948

2) **Support Vector Classifier**

This classifier uses support vectors to create decision boundaries between classes. It aims to maximise the margin between the classes, making it effective for classification tasks.

Accuracy: 0.995

3) **Passive Aggressive Classifier**

Passive Aggressive classifier is a type of online learning algorithm that can be used for classification tasks. The algorithm works by maintaining a weight vector that represents the model's parameters. When presented with a new training example, the classifier makes a prediction based on the current model and compares it to the true label. If the prediction is correct, the model remains unchanged (passive). However, if the prediction is incorrect, the model is updated aggressively to correct the mistake.

Accuracy: 0.995

4) **Ensemble model**

The ensemble model combines the prediction of the three models above to make a final prediction. Given that each model has its own strengths and weaknesses, this method leverages the diversity of the individual models to improve overall performance and robustness. In this ensemble model, bootstrap aggregating is adopted. The three models above are trained on different bootstrap samples from the training data. Each model is trained independently, and predictions are aggregated using majority voting.

Accuracy: 0.989

5) **Deep learning - Neural Network**

# Development of Web-based application
NewsGuardian is developed as a web-based solution using the following technologies:

FrontEnd: React

Backend: Flask

# Deployment of app
