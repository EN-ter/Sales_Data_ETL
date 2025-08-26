# Sales_Data_ETL
Syncs sales_data on Postgres DB with sales MySQL DB automating the extraction from the staging warheouse and loading data into the production warehouse.


# Scenario
Sync up of staging data warehouse and production data warehouse. Automating this sync up will save a lot of time and standardize the process. Load data from MySQL server which acts as a staging warehouse to the PostgreSQL which is a production data warehouse. This script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse. 

This program requires the python module mysql-connector-python to be installed.
Install it using the below command
pip3 install mysql-connector-python

This program requires the python module pg-db to be installed.
Install it using the below command
python3 -m pip install psycopg2

sales.sql is used in the staging warehouse (~13k rows), and the sales.csv in the production warehouse (~12k rows) for for initial data population. 
