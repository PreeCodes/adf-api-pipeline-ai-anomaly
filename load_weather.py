# Import transformed daily weather data from transformation layer
from transform_weather import daily

# Define output file path for CSV target
output_path = 'daily_weather.csv' 
# Write DataFrame to CSV without row index
daily.to_csv(output_path, index=False) 
 # Audit log — confirm row count loaded successfully 
print('Loaded ' + str(len(daily)) + ' rows to ' + output_path) 
print(daily.head())
