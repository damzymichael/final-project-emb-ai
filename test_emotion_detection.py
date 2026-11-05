"""
This module acts as the Flask web server for the Emotion Detection application.
It handles incoming HTTP requests, processes text using the EmotionDetection package,
and returns the formatted analysis results to the user interface.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Receives text via the 'textToAnalyze' query parameter,
    runs the emotion detection function, checks for blank/invalid inputs,
    and returns the formatted result string or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Handle error case when dominant_emotion is None (blank entries)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index web page for the application interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)