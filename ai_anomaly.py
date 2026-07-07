import anthropic
import json
import pandas as pd 
import os

# Initialise Anthropic client using API key from environment variable
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Weather statistics summary passed to Claude for anomaly analysis
stats = 'London avg 12.3C rain 45mm vs 7day average avg 11.8C rain 38mm. Manchester avg 9.1C rain 68mm vs average 10.2C rain 52mm. Edinburgh avg 6.8C rain 82mm vs average 8.1C rain 61mm. Birmingham avg 10.5C rain 41mm vs average 10.1C rain 39mm.'

# Send weather data to Claude AI for intelligent anomaly detection
# Claude acts as the AI transformation layer in our pipeline
response = client.messages.create(
model='claude-opus-4-5',
max_tokens=512,
messages=[{'role': 'user', 'content': 'You are a data monitoring system. Analyse these UK weather readings versus 7-day averages. Flag any significant anomalies and generate a brief monitoring report with specific cities and values: ' + stats}]
)

 # Extract text report from Claude API response
report = "No anomalies detected"
for block in response.content: 
    if block.type == "text": 
        report = block.text 
        break 
print('Anomaly Report:') 
print(report)

# Append anomaly report to JSON log file with timestamp
with open('anomaly_log.json', 'a') as f:
    json.dump({'timestamp': str(pd.Timestamp.now()), 'report': report}, f)
    f.write('\n')
# Newline separates each JSON entry for readability
print('Report saved to anomaly_log.json')