""" Emotion Detection """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """ Render Template """

    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detector():
    """Get emotion result from input textfield"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion != '':
        return f"""For the given statement, the system response is
        'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness':{sadness}.
        <br /><br /> The dominant emotion is <b>{dominant_emotion}</b>
        """

    return "Invalid input! Try again."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
