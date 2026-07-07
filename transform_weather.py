# Import raw hourly weather data extracted from Open-Meteo API 
import pandas as pd
from extract_weather import df

# Aggregate hourly data to daily level per city
daily = df.groupby(['city', df['datetime'].str[:10]]).agg(avg_temp=('temp_c','mean'), max_temp=('temp_c','max'), min_temp=('temp_c','min'), total_rain=('rain_mm','sum')).reset_index()
# Rename columns to match target schema naming conventions
daily.columns = ['city','date','avg_temp_c','max_temp_c','min_temp_c','total_rain_mm']
# Add audit timestamp — when this record was processed
daily['loaded_at'] = pd.Timestamp.now()
print('Daily rows:', len(daily))
print(daily.head())