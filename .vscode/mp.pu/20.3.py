import json

def save_feedback(feedbacks, filename='feedback.json'):
    with open(filename, 'w') as file:
        json.dump(feedbacks, file)

def load_feedback(filename='feedback.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_feedback(feedbacks, feedback):
    feedbacks.append(feedback)
    save_feedback(feedbacks)
