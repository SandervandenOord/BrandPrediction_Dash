import numpy as np
from joblib import load


beauty_brand_model = load('./model_training/beauty_brand_model.joblib')

dict_brand_id_to_brandname = load('./model_training/brand_id_to_brandname.joblib')


def predict_top3_brands(title):
    probas = beauty_brand_model.predict_proba(title).ravel()
    top3_index = np.argsort(probas)[::-1][:3]
    top3_brandids = beauty_brand_model.named_steps['sgd'].classes_[top3_index]
    top3_probas = probas[top3_index].round(3)
    top3_brand_id_to_proba = dict(zip(top3_brandids, top3_probas))

    top3_predictions = {}
    for brand_id in top3_brandids:
        top3_predictions[brand_id] = {
            'brandname': dict_brand_id_to_brandname[brand_id],
            'probability': top3_brand_id_to_proba[brand_id]
        }

    return top3_predictions
