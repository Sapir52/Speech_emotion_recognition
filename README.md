# Speech_emotion_recognition

Speech Emotions Predictor is an application that allows users to record, and playback short audio file and its built-in super cool Machine Learning model will predict the range of emotions and the gender of the audio clip. 

There are options to compare the frequencies and other attributes for various emotions to see how they show up on a scale. 

The application uses 8 types of emotions:
natural, calm, happy, sad, angry, scared, disgust, surprised.

In addition, allows to identify the gender of the user: male, female.

# Pipeline

- Data from CSV files of audio voices.
- Used librosa package to convert audio files into 128 Features including low-level feature extraction, such as chromograms, Mel spectrogram, MFCC, and various other spectral and rhythmic features
Used Pandas to provide the feature data for emotions and gender as input to the models.
- Using different classifiers and deep learning model to find the best model.
- Development of recording and playback functionality: Its output allows the prediction of emotions and gender of the recorded audio.

# The application
The Speech Emotion Predictor runs as a client-side flask application.

The application works by using the built-in functionality of HTML5 to allow the users browser to record and store the audio file, the file once recorded to passed into the FLASK app. 

Method where the file can then be run thru the audio parser, breaking it into features and then thru the model. 

The application uses two different models, one for emotion and one for Male/Female, this production as well as the probability of each emotion and gender is then passed into a JSON file as a dictionary that is used to generate the plotly bar chart of emotions and gender.

# Using Random Forest Classifier
![home_page](https://user-images.githubusercontent.com/63209732/147882296-4597d2d9-9ed8-4c58-a075-cdc669f2b504.png)

![speech_predict](https://user-images.githubusercontent.com/63209732/147882484-02b72166-9d98-440c-8f44-329ded9c5cdb.png)


# Run Flask App
python app.py to launch site
