from transform_weather import daily

output_path = 'daily_weather.csv' 
daily.to_csv(output_path, index=False) 
print('Loaded ' + str(len(daily)) + ' rows to ' + output_path) 
print(daily.head())
