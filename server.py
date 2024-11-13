from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detector():
    print('emotion_detector')
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)

    response = emotion_detector(text_to_analyze)

    print(response)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    if dominant_emotion is '':
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness':{}.<br /><br /> The dominant emotion is <b>{}</b> ".format(anger, disgust, fear, joy, sadness, dominant_emotion)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)