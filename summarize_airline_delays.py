
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_airline_delays.csv')

# Average delay per airline
avg_delay_by_carrier = df.groupby('carrier_name')['arr_delay'].mean().sort_values(ascending=False)
print('\nTop Airlines by Average Arrival Delay:')
print(avg_delay_by_carrier.head(10))

# Monthly total delays
monthly_delays = df.groupby(['year', 'month'])['arr_delay'].sum().reset_index()
monthly_delays['year_month'] = monthly_delays['year'].astype(str) + '-' + monthly_delays['month'].astype(str).str.zfill(2)
print('\nMonthly Total Delays:')
print(monthly_delays[['year_month', 'arr_delay']].head(12))

# Top airports by delay ratio
top_airports = df.groupby('airport_name')['delay_ratio'].mean().sort_values(ascending=False)
print('\nTop Airports by Average Delay Ratio:')
print(top_airports.head(10))

# Delay causes summary
delay_causes = df[['carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']].sum().sort_values(ascending=False)
print('\nTotal Delay Minutes by Cause:')
print(delay_causes)

# Save results to CSV files
avg_delay_by_carrier.head(10).to_csv('summary_avg_delay_by_carrier.csv')
monthly_delays.to_csv('summary_monthly_delays.csv', index=False)
top_airports.head(10).to_csv('summary_top_airports.csv')
delay_causes.to_csv('summary_delay_causes.csv')

print('\nSummary reports saved as CSV files.')
