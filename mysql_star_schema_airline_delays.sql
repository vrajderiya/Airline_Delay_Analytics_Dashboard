CREATE DATABASE airline_dw;
-- Use the database (ensure it's created beforehand)
USE airline_dw;

-- Dimension: Time
CREATE TABLE dim_time (
    time_id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    month INT
);

-- Dimension: Airport
CREATE TABLE dim_airport (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    airport_code VARCHAR(10),
    airport_name VARCHAR(255)
);

-- Dimension: Carrier
CREATE TABLE dim_carrier (
    carrier_id INT AUTO_INCREMENT PRIMARY KEY,
    carrier_code VARCHAR(10),
    carrier_name VARCHAR(255)
);

-- Fact Table: Flight Delay Performance
CREATE TABLE fact_flight_delays (
    delay_id INT AUTO_INCREMENT PRIMARY KEY,
    time_id INT,
    airport_id INT,
    carrier_id INT,
    arr_flights INT,
    arr_del15 INT,
    arr_cancelled INT,
    arr_diverted INT,
    arr_delay INT,
    carrier_delay INT,
    weather_delay INT,
    nas_delay INT,
    security_delay INT,
    late_aircraft_delay INT,
    delay_ratio FLOAT,
    cancel_ratio FLOAT,
    divert_ratio FLOAT,
    total_delay_causes FLOAT,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (airport_id) REFERENCES dim_airport(airport_id),
    FOREIGN KEY (carrier_id) REFERENCES dim_carrier(carrier_id)
);

SELECT * FROM dim_time
SELECT * FROM dim_carrier
SELECT * FROM dim_airport
SELECT * FROM fact_flight_delays
