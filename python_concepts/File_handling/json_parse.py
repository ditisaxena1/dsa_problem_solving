import json

# JSON string
json_string = '''
{
  "quiz": {
    "sport": {
      "q1": {
        "question": "Which one is correct team name in NBA?",
        "options": [
          "New York Bulls",
          "Los Angeles Kings",
          "Golden State Warriors",
          "Huston Rocket"
        ],
        "answer": "Huston Rocket"
      }
    }
  }
}
'''

# Load JSON string into a dictionary
data = json.loads(json_string)

# Extract the question
question = data['quiz']['sport']['q1']['question']

print(f"Question: {question}")