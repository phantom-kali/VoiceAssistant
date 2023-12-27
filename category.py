import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load data from JSON
with open('commands_data.json', 'r') as file:
    data = json.load(file)

# Extract commands and categories from JSON
commands = []
categories = []

for entry in data['tasks']:
    category = entry['category']
    commands.extend(entry['commands'])
    categories.extend([category] * len(entry['commands']))

# Create a classifier pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(commands, categories)

# Function to predict category for a new command
def predict_category(command):
    return(model.predict([command])[0])

