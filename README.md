# ✈️ Airline Delay Analytics Dashboard

An end-to-end **Airline Delay Analytics Dashboard** project for exploring and visualizing U.S. flight delay trends.  
This project integrates **data extraction, cleaning, transformation, relational modeling, and Tableau visualization** to uncover key insights into airline reliability, delay causes, and airport performance.

---

## 📊 Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Architecture & Components](#architecture--components)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Setup & Installation](#setup--installation)  
   - [Running the Data Pipeline](#running-the-data-pipeline)  
   - [Launching the Tableau Dashboard](#launching-the-tableau-dashboard)  
5. [Folder / File Structure](#folder--file-structure)  
6. [Data Model](#data-model)  
7. [Usage / Workflow](#usage--workflow)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact / Author](#contact--author)  

---

## 🧭 Project Overview

**Airline Delay Analytics Dashboard** is designed to help analyze and visualize flight delay patterns across U.S. airlines and airports.  
Using **Python, SQL, and Tableau**, the project cleans raw flight data, builds a star-schema database, summarizes delays by multiple dimensions, and delivers interactive dashboards for business insights.

🔗 **Repository:** [github.com/vrajderiya/Airline_Delay_Analytics_Dashboard](https://github.com/vrajderiya/Airline_Delay_Analytics_Dashboard)

---

## 🚀 Features

✅ Data cleaning and preprocessing using Python (Pandas, NumPy)  
✅ SQL-based star schema for airline delay data  
✅ Automated ETL pipeline for data ingestion  
✅ Summary tables for monthly, carrier, and airport-level analysis  
✅ Interactive Tableau dashboards for visual storytelling  
✅ Drill-down capabilities to explore trends by delay cause, route, or airline  

---

## 🧩 Architecture & Components

**Technologies Used:**
- Python (ETL & preprocessing)
- MySQL (database & relational modeling)
- Tableau (visualization)
- Pandas, SQLAlchemy, MySQL Connector

**Main Components:**
- `etl_airline_delay.py` → Cleans and transforms raw data  
- `load_airline_data_to_mysql.py` → Loads processed data into MySQL  
- `summarize_airline_delays.py` → Creates aggregated summary tables  
- `mysql_star_schema_airline_delays.sql` → Defines database schema  
- `Final Project.twbx` → Tableau dashboard file  

---

## ⚙️ Getting Started

### Prerequisites
Ensure the following are installed:
- Python 3.x  
- MySQL Server  
- Tableau Desktop or Tableau Reader  
- Python libraries:
  ```bash
  pip install pandas sqlalchemy mysql-connector-python

---

## 📸 Screenshots

<img width="1000" height="800" alt="Dashboard 1" src="https://github.com/user-attachments/assets/267b3056-a4c2-4fcd-b463-ea4a306441ce" />
<img width="1894" height="926" alt="Total Flights by Airline" src="https://github.com/user-attachments/assets/26fd40e3-b4ad-494f-8ace-f1ea65f0b72b" />
<img width="1921" height="947" alt="Delayed Flight Share by Airline - 1" src="https://github.com/user-attachments/assets/871d2c81-71f2-477c-a65d-41ad346d451f" />
<img width="1956" height="947" alt="Delay In Minutes By Various Causes For Each Airline" src="https://github.com/user-attachments/assets/21f70345-88cb-45e4-b905-85f49b44c52c" />
<img width="1894" height="926" alt="Delay Rate by Airline" src="https://github.com/user-attachments/assets/1b1e73b8-20f6-48a5-a608-0e096be71dba" />
<img width="1000" height="800" alt="Dashboard 2" src="https://github.com/user-attachments/assets/6654f0fe-2cb6-47d7-91bc-1afac84af219" />
<img width="958" height="947" alt="Top 15 Airports by Total Delayed Time (All causes)-2" src="https://github.com/user-attachments/assets/e16a5d3f-1027-4928-9fac-874d9e29ba30" />
<img width="1845" height="947" alt="Average Delay Rate by Airport" src="https://github.com/user-attachments/assets/7c3b863f-919a-454f-bc7c-74b55d7c9203" />
<img width="1873" height="265" alt="Top 10 Airports by Cancellation Rate" src="https://github.com/user-attachments/assets/a3f92205-64a5-4fa6-bb10-db9eed669183" />
<img width="1845" height="947" alt="Geographic Hotspots of Flight Delays by Airport-2" src="https://github.com/user-attachments/assets/6e9556f9-91d3-4b4c-a7e7-f05206e1aabc" />
<img width="952" height="511" alt="Delay Rate by Airport and Carrier-2" src="https://github.com/user-attachments/assets/cab89eef-9902-4fa8-b23d-6ad295fb7dce" />

---
