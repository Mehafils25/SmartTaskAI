import joblib

model = joblib.load("task_classifier.pkl")

def predict_category(task):

    prediction = model.predict([task])

    return prediction[0]