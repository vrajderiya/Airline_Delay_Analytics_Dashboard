
import pandas as pd

# Load the raw dataset
df = pd.read_csv('ot_delaycause1_DL/airline_ontime_delay_2020_2024.csv')

# Step 1: Basic cleaning - remove rows with missing or invalid delay data
df_cleaned = df.dropna(subset=[
    'arr_flights', 'arr_del15', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
])

# Step 2: Feature Engineering
df_cleaned['total_delay_causes'] = (
    df_cleaned['carrier_delay'] + df_cleaned['weather_delay'] +
    df_cleaned['nas_delay'] + df_cleaned['security_delay'] +
    df_cleaned['late_aircraft_delay']
)

df_cleaned['delay_ratio'] = df_cleaned['arr_del15'] / df_cleaned['arr_flights']
df_cleaned['cancel_ratio'] = df_cleaned['arr_cancelled'] / df_cleaned['arr_flights']
df_cleaned['divert_ratio'] = df_cleaned['arr_diverted'] / df_cleaned['arr_flights']

# Step 3: Normalize carrier and airport names (lowercase, no trailing spaces)
df_cleaned['carrier_name'] = df_cleaned['carrier_name'].str.strip().str.title()
df_cleaned['airport_name'] = df_cleaned['airport_name'].str.strip().str.title()

# Step 4: Save cleaned file
df_cleaned.to_csv('cleaned_airline_delays.csv', index=False)
df_cleaned.to_parquet('cleaned_airline_delays.parquet')

print("ETL Process Complete. Files saved as 'cleaned_airline_delays.csv' and 'cleaned_airline_delays.parquet'.")
