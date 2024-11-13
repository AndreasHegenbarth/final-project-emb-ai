import requests
import json

def emotion_detector(text_to_analyse):
    print('emotion_detector function')
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  

    
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        predictions = formatted_response['emotionPredictions']
        emotion = predictions[0]['emotion']

        anger = emotion['anger']
        disgust = emotion['disgust']
        joy = emotion['joy']
        fear = emotion['fear']
        sadness = emotion['sadness']
        Keymax = max(zip(emotion.values(), emotion.keys()))[1]
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        anger = ''
        disgust = ''
        joy = ''
        fear = ''
        sadness = ''
        Keymax = ''
   
 
    return {
        'anger': anger, 
        'disgust': disgust,
        'joy': joy,
        'fear': fear,
        'sadness': sadness,
        'dominant_emotion': Keymax
        }