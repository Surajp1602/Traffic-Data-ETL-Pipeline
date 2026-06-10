import pandas as pd
from sqlalchemy import create_engine

# ----------------------------------
# STEP 1: READ DATA
# ----------------------------------

print("Reading CSV...")

df = pd.read_csv("data/raw/traffic.csv")

print(df.head())

# ----------------------------------
# STEP 2: CLEAN DATA
# ----------------------------------

print("\nCleaning data...")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# ----------------------------------
# STEP 3: TRANSFORM DATA
# ----------------------------------

print("\nTransforming data...")

df["hour"] = df["timestamp"].dt.hour

df["traffic_level"] = df["vehicle_count"].apply(
    lambda x: "High" if x > 150 else "Low"
)

print(df.head())

# ----------------------------------
# STEP 4: SAVE CLEANED DATA
# ----------------------------------

print("\nSaving processed CSV...")

df.to_csv(
    "data/processed/cleaned_traffic.csv",
    index=False
)

# ----------------------------------
# STEP 5: LOAD INTO DATABASE
# ----------------------------------

print("\nLoading into SQLite database...")

engine = create_engine(
    "sqlite:///traffic.db"
)

df.to_sql(
    "traffic_data",
    engine,
    if_exists="replace",
    index=False
)

# ----------------------------------
# STEP 6: RUN ANALYTICS
# ----------------------------------

print("\nRunning analytics...")

query = """
SELECT
location,
AVG(vehicle_count) AS avg_vehicles
FROM traffic_data
GROUP BY location
"""

result = pd.read_sql(query, engine)

print("\nAverage Vehicles By Location:")
print(result)

print("\nPipeline completed successfully.")