# ADF Weather Pipeline with Claude AI Anomaly Detection

## What this project does
Azure Data Factory pipeline that extracts live weather data for 4 UK cities daily, loads incrementally to Azure Synapse Analytics, then runs Claude AI anomaly detection to flag unusual patterns automatically.

## Tech stack
- Python, requests, pandas
- Azure Data Factory (Daily Trigger at 7AM)
- Azure Synapse Analytics (incremental loading)
- Claude AI anomaly detection

## Architecture
Open-Meteo API → Python → Azure Synapse incremental → ADF trigger → Claude AI report

## Dataset
**Source:** Open-Meteo API (free, no API key required) 
**Frequency:** Daily extractions 
**Storage:** Azure Data Lake Gen2 

## Anomaly Report (Sample AI anomaly report)
# UK Weather Monitoring Report

**Report Generated:** Current Period vs 7-Day Average

---

## 🔴 ANOMALIES FLAGGED

### **Manchester**
- **Rainfall:** 68mm vs 52mm avg → **+30.8% above normal** ⚠️
- **Temperature:** 9.1°C vs 10.2°C avg → **-1.1°C below normal**

### **Edinburgh**
- **Rainfall:** 82mm vs 61mm avg → **+34.4% above normal** ⚠️
- **Temperature:** 6.8°C vs 8.1°C avg → **-1.3°C below normal**

---

## 🟢 WITHIN NORMAL PARAMETERS

### **London**
- Temperature: +0.5°C | Rainfall: +18.4% *(minor elevation)*

### **Birmingham**
- Temperature: +0.4°C | Rainfall: +5.1% *(stable)*

---

## Summary

| City | Temp Δ | Rain Δ | Status |
|------|--------|--------|--------|
| Edinburgh | -1.3°C | +34.4% | **FLAG** |
| Manchester | -1.1°C | +30.8% | **FLAG** |
| London | +0.5°C | +18.4% | Monitor |
| Birmingham | +0.4°C | +5.1% | Normal |

**Assessment:** Northern regions experiencing cooler, significantly wetter conditions. Rainfall anomalies >30% in Manchester and Edinburgh warrant continued monitoring for potential flooding risk.

## Setup 
1. **Clone repository** bash git clone https://github.com/yourusername/adf-weather-anomaly 
2. **Install dependencies** pip install anthropic pandas requests
3. **Configure Anthropic API key** - Get API key from console.anthropic.com - Replace YOUR_KEY in ai_anomaly.py 
4. **Configure Azure credentials** - Set up Azure Synapse connection string - Set up Azure Data Lake storage account 
5. **Configure ADF pipeline** - Import pipeline JSON to Azure Data Factory - Set up daily trigger at 06:00 UTC 

## How to run
1. python extract_weather.py
2. python transform_weather.py
3. python load_weather.py
4. python ai_anomaly.py
