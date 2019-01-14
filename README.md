# Predicting a beauty brand from its title -> Visualizing with Dash Plotly

Using  sklearn to vectorize beauty product titles and predicting its brand using SGD.

The top 3  most likely brands are visualized using Dash Plotly to build a Flask app with Python only.

Because I wanted to deploy on Heroku, I had to make the model smaller to fit in (free) memory. So I reduced the number of features by adding max_features=10000 to the TFIDF vectorizer. This reduced accuracy on the test set slightly.

Check here: https://brandprediction.herokuapp.com/
