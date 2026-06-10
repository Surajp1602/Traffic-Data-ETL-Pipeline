# Real-Time Traffic Data ETL Pipeline

## Project Overview

The Real-Time Traffic Data ETL Pipeline is a Data Engineering project designed to process, transform, and analyze traffic monitoring data. The pipeline extracts raw traffic records from CSV files, performs data cleaning and transformation operations, loads the processed data into a relational database, and generates analytical insights to support traffic management and decision-making.

This project demonstrates fundamental Data Engineering concepts including ETL workflows, data preprocessing, database integration, and analytical reporting using Python and SQL.

---

## Objectives

- Build a scalable ETL pipeline for traffic data processing.
- Automate data cleaning and validation.
- Store transformed data in a relational database.
- Generate meaningful traffic analytics using SQL queries.
- Demonstrate practical Data Engineering skills using Python and SQL.

---

## Technology Stack

### Programming Language
- Python 3.x

### Libraries
- Pandas
- NumPy
- SQLAlchemy
- SQLite3

### Database
- SQLite

### Development Tools
- VS Code
- Git
- GitHub

---

## Dataset Structure

The dataset contains traffic information collected at various locations.

| Column | Description |
|----------|-------------|
| timestamp | Date and time of observation |
| location | Traffic monitoring location |
| vehicle_count | Number of vehicles recorded |
| avg_speed | Average speed of vehicles (km/h) |

### Sample Data

| timestamp | location | vehicle_count | avg_speed |
|------------|------------|--------------|-----------|
| 2025-06-01 08:00:00 | Pune Station | 120 | 35 |
| 2025-06-01 09:00:00 | Pune Station | 150 | 28 |
| 2025-06-01 10:00:00 | Shivaji Nagar | 95 | 42 |

---

## Dashboard

<img width="1600" height="758" alt="Dashboard1" src="https://github.com/user-attachments/assets/d0999a80-8841-4bde-95c5-8f119dc6e92a" />
<img width="1110" height="820" alt="Dashboard2" src="https://github.com/user-attachments/assets/f26d1c01-0ec0-4680-bffb-ff9c1cfc170d" />
<img width="1016" height="787" alt="Dashboard3" src="https://github.com/user-attachments/assets/70123345-6fa3-4abb-b8ed-9fab90555559" />


---

## ETL Pipeline Architecture

```text
Raw Traffic CSV
       │
       ▼
Extract Data
       │
       ▼
Data Validation
       │
       ▼
Data Cleaning
(Missing Values, Duplicates)
       │
       ▼
Data Transformation
(Date-Time Features, Metrics)
       │
       ▼
Load to SQLite Database
       │
       ▼
SQL Analytics & Reports
       │
       ▼
Processed Outputs
