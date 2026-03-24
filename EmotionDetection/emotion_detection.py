import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text) #I am confused for there is no such thing as 'emotion scores' in the json

    # Extract emotion scores from the response
    emotion_scores = formatted_response.get('documentSentiment', {}).get('emotionScores', {})
    anger_score = emotion_scores.get('anger', 0)
    disgust_score = emotion_scores.get('disgust', 0)
    fear_score = emotion_scores.get('fear', 0)
    joy_score = emotion_scores.get('joy', 0)
    sadness_score = emotion_scores.get('sadness', 0)

        # Determine the dominant emotion
    emotions = {
        'joy': joy_score,
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare the response with emotion scores and the dominant emotion
    response_data = {
        'joy': joy_score,
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    # Return the response data as a JSON string
    return json.dumps(response_data)