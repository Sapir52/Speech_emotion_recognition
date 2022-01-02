from flask import Flask, jsonify, render_template, request
import numpy as np
import librosa
import librosa.display
from joblib import load
#from keras.models import load_model
results_dict = {
    "predictedEmotion": [],
    "emotionCategories": [],
    "probabilities": [],
    "predictedGender": [],
    "genderCategories": [],
    "genderProbabilities": []
}

#functions
def input_parser(input_file):
   try:
      X, sample_rate = librosa.load(input_file, res_type='kaiser_fast') 
      mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=128).T,axis=0) 
   except Exception as e:
      print("Error encountered while parsing file: ", input_file)
      return None
   feature = mfccs.tolist()
   print("feature"+str(feature))
   return feature

def get_results_dict_from_svc_model(model, model2, arr2d):
    pred_emotion = model.predict(arr2d)
    probs = model.predict_proba(arr2d)
    emotion_labels = model.classes_
    results_dict["predictedEmotion"] = pred_emotion[0]
    results_dict["emotionCategories"] = emotion_labels.tolist()
    results_dict["probabilities"] = probs[0].tolist()

    pred_gender = model2.predict(arr2d)
    probs_gender = model2.predict_proba(arr2d)
    Gender_labels = ["Male", "Female"]
    if pred_gender[0] == 0:
        label = Gender_labels[0]
    elif pred_gender[0] == 1:
        label = Gender_labels[1]
    results_dict["predictedGender"] = label
    results_dict["genderCategories"] = Gender_labels
    results_dict["genderProbabilities"] = probs_gender[0].tolist()
    return results_dict

def get_results_dict_from_h5_model(model, model2, arr2d):
    # Emotion h5 model
    probs = model.predict(arr2d)
    print("probs[0].tolist()" + str(probs[0].tolist()))
    emotion_labels = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprise']
    pred_emotion = emotion_labels[int(np.amax(probs))]
    results_dict["predictedEmotion"] = pred_emotion
    results_dict["emotionCategories"] = emotion_labels
    results_dict["genderProbabilities"] = probs[0].tolist()

    # Gender h5 model
    probs = model2.predict(arr2d)
    print("probs " + str(probs))
    print("probs[0].tolist()" + str(probs[0].tolist()))
    emotion_labels = ["Male", "Female"]
    pred_emotion = emotion_labels[int(np.amax(probs))]
    results_dict["predictedGender"] = pred_emotion
    results_dict["genderCategories"] = emotion_labels
    results_dict["probabilities"] = probs[0].tolist()

    return results_dict
def model_test(input_file):
    user_file = {'filepath': [input_file]}
    # Import models
    # model = load_model('models/emotion_model.h5')
    # model2 = load_model('models/gender_model.h5')
    model = load('models/RandomForestClassifier_model.sav')
    model2 = load('models/RandomForestClassifier_gender_model.sav')
    # Transforming data into a vector representation
    feature = input_parser(input_file)
    arr = np.array(feature)
    arr2d = np.reshape(arr, (1,128))
    #Evaluation of the models
    results_dict = get_results_dict_from_svc_model(model, model2, arr2d)
    print(results_dict)
    return results_dict




app = Flask(__name__)
app.secret_key = 'upgraded potato'

# App routes
@app.route("/", methods=['GET', 'POST'])
def record_page():
    print("responding to record page route request")
    if request.method == "POST":
        f = request.files['audio_data']
        results = model_test(f)
        print('file uploaded successfully')
        print(results)
        return (results)
    else:
        return render_template('index.html')

@app.route("/data")
def data():
    return(jsonify(results_dict))

if __name__ == "__main__":
    app.run(debug=True)
    


