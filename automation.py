# Import libraries required for connecting to mysql
# pip3 install mysql-connector-python
import mysql.connector

# Import libraries required for connecting to DB2 or PostgreSql
# python3 -m pip install psycopg2
import psycopg2

# Connect to MySQL
# connectction details
php_user = 'root'
php_pw = '<PASSWORD>'
php_hostname = '<HOST NAME>'
php_db='sales'
connection_php = mysql.connector.connect(user=php_user, password=php_pw,host=php_hostname,database=php_db)
cursor_php = connection_php.cursor()

# Connect to PostgreSql
# connectction details
dsn_database ="postgres" 
dsn_user='postgres'  
dsn_pwd ='<PASSWORD>' 
dsn_hostname = '<HOST NAME'
dsn_port ="5432"             
    

conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   password=dsn_pwd,
   host=dsn_hostname, 
   port= dsn_port
)

cursor_pg = conn.cursor()

# Find out the last rowid from PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on PostgreSql.

def get_last_rowid():
	SQL =  'SELECT MAX(rowid) FROM sales_data'
	cursor_pg.execute(SQL)
	last_row = cursor_pg.fetchone()
	if last_row is None:
		print("No rows found in sales_data.")
		return 0  # or None, depending on how you want to handle it
	return(last_row[0])


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	SQL =  'SELECT * FROM sales_data WHERE rowid > %s'
	cursor_php.execute(SQL, (rowid,))
	latest_records = cursor_php.fetchall()
	return(latest_records)		

new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
	SQL = 'INSERT INTO sales_data (rowid, product_id, customer_id, quantity) VALUES (%s, %s, %s, %s)'
	cursor_pg.executemany(SQL, records)
	conn.commit()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
cursor_php.close()

# disconnect from PostgreSql data warehouse 
cursor_pg.close()
conn.close()

# End of program