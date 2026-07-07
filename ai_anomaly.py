import anthropic
import json
import pandas as pd 
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

stats = 'London avg 12.3C rain 45mm vs 7day average avg 11.8C rain 38mm. Manchester avg 9.1C rain 68mm vs average 10.2C rain 52mm. Edinburgh avg 6.8C rain 82mm vs average 8.1C rain 61mm. Birmingham avg 10.5C rain 41mm vs average 10.1C rain 39mm.'

response = client.messages.create(
model='claude-opus-4-5',
max_tokens=512,
messages=[{'role': 'user', 'content': 'You are a data monitoring system. Analyse these UK weather readings versus 7-day averages. Flag any significant anomalies and generate a brief monitoring report with specific cities and values: ' + stats}]
)

report = "No anomalies detected"
for block in response.content: 
    if block.type == "text": 
        report = block.text 
        break 
# report = response.content[0].text
print('Anomaly Report:') 
print(report)

with open('anomaly_log.json', 'a') as f:
    json.dump({'timestamp': str(pd.Timestamp.now()), 'report': report}, f)
    f.write('\n')
print('Report saved to anomaly_log.json')