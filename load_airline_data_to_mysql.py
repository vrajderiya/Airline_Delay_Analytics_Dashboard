
import pandas as pd
import pymysql

# Load cleaned data
df = pd.read_csv('cleaned_airline_delays.csv')

# Connect to MySQL using pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='airline_dw',
    autocommit=True
)
cursor = conn.cursor()

# Load distinct dimension tables
dim_time = df[['year', 'month']].drop_duplicates().reset_index(drop=True)
dim_airport = df[['airport', 'airport_name']].drop_duplicates().reset_index(drop=True)
dim_carrier = df[['carrier', 'carrier_name']].drop_duplicates().reset_index(drop=True)

# Insert into dim_time
for _, row in dim_time.iterrows():
    cursor.execute("""
        INSERT INTO dim_time (year, month) VALUES (%s, %s)
    """, (row['year'], row['month']))

# Insert into dim_airport
for _, row in dim_airport.iterrows():
    cursor.execute("""
        INSERT INTO dim_airport (airport_code, airport_name) VALUES (%s, %s)
    """, (row['airport'], row['airport_name']))

# Insert into dim_carrier
for _, row in dim_carrier.iterrows():
    cursor.execute("""
        INSERT INTO dim_carrier (carrier_code, carrier_name) VALUES (%s, %s)
    """, (row['carrier'], row['carrier_name']))

# Create mapping dictionaries
cursor.execute("SELECT * FROM dim_time")
time_map = {(row[1], row[2]): row[0] for row in cursor.fetchall()}

cursor.execute("SELECT * FROM dim_airport")
airport_map = {row[1]: row[0] for row in cursor.fetchall()}

cursor.execute("SELECT * FROM dim_carrier")
carrier_map = {row[1]: row[0] for row in cursor.fetchall()}

# Insert into fact table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fact_flight_delays (
            time_id, airport_id, carrier_id,
            arr_flights, arr_del15, arr_cancelled, arr_diverted,
            arr_delay, carrier_delay, weather_delay, nas_delay,
            security_delay, late_aircraft_delay,
            delay_ratio, cancel_ratio, divert_ratio, total_delay_causes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        time_map[(row['year'], row['month'])],
        airport_map[row['airport']],
        carrier_map[row['carrier']],
        row['arr_flights'], row['arr_del15'], row['arr_cancelled'], row['arr_diverted'],
        row['arr_delay'], row['carrier_delay'], row['weather_delay'], row['nas_delay'],
        row['security_delay'], row['late_aircraft_delay'],
        row['delay_ratio'], row['cancel_ratio'], row['divert_ratio'], row['total_delay_causes']
    ))

cursor.close()
conn.close()
print("Data loaded into MySQL successfully using pymysql.")
