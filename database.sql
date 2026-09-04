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