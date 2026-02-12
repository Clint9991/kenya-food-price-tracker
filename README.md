# Kenya Food Price Anomaly Tracker 🇰🇪

### 🚨 Early Warning System for Food Security
This project analyzes **World Food Programme (WFP)** market data to detect "Hunger Hotspots" in Kenya. It uses Python to identify abnormal price spikes in staple foods (Maize) and visualizes them on an interactive geospatial map.

### 🎯 Objective
To assist humanitarian agencies (like WFP and FAO) in shifting from "Reactive" to "Proactive" aid by identifying market stress *before* it becomes a famine.

### 🛠️ Tech Stack
* **Python:** Data cleaning & processing
* **Pandas:** Time-series analysis & statistical modeling (Z-Score)
* **Folium:** Geospatial mapping & visualization
* **WFP Open Data:** Real-time market prices

### 📊 Key Insights
* **Anomaly Detection:** Automatically flags markets where prices exceed **0.5 Standard Deviations** from the rolling average.
* **Geospatial Tracking:** Visualizes crisis vs. stable regions using Red/Green indicators.

---
*Created by Clinton Mwangi *
