import sqlite3

DATABASE_NAME = "cocoa.db"

def get_connection():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    """Create the farm_records table if it doesn't exist."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS farm_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            harvest_weight REAL NOT NULL,
            rejected_weight REAL NOT NULL,
            price_per_kg REAL NOT NULL,
            labour_cost REAL NOT NULL,
            transport_cost REAL NOT NULL,
            other_costs REAL NOT NULL,
            farm_size REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    
    connection.commit()
    connection.close()

def save_farm_record(harvest_weight, rejected_weight, price_per_kg, labour_cost, transport_cost, other_costs, farm_size):
         """Save a new farm record to the database."""
         connection = get_connection()
         cursor = connection.cursor()
         cursor.execute('''
           INSERT INTO farm_records (harvest_weight, rejected_weight, price_per_kg, labour_cost, transport_cost, other_costs, farm_size)
           VALUES (?, ?, ?, ?, ?, ?, ?);
           ''', (harvest_weight, rejected_weight, price_per_kg, labour_cost, transport_cost, other_costs, farm_size))
         connection.commit()
         connection.close()

def get_farm_records():
    """Retrieve all farm records from the database."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM farm_records')
    records = cursor.fetchall()
    connection.close()
    return records