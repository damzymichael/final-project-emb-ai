"""
Flask server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Receives text via a GET request parameter ('textToAnalyze'),
    runs emotion analysis, handles invalid inputs, and returns 
    the formatted emotion response string or error message.
    """
    # Retrieve the text argument from the request
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Incorporate error handling when the dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return formatted string conforming to the required output structure
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application web interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
