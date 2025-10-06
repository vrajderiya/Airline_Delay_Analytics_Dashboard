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
