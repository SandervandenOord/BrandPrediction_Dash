# Predicting a beauty brand from its title -> Visualizing with Dash Plotly

Using  sklearn to vectorize beauty product titles and predicting its brand using SGD.

The top 4 most likely brands are visualized using Dash Plotly.

Because I wanted to deploy on Heroku, I had to make the model smaller to fit in (free) memory. So I reduced the number of features by adding max_features=10001 to the TFIDF vectorizer.

Check here: https://brandprediction.herokuapp.com/
