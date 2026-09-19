from database import create_table, save_farm_record, get_farm_records
print("Creating database and table...")

create_table()

print("saving test farm record...")

save_farm_record(
    500,      # harvest weight
    20,       # rejected weight
    2500,     # price per kg
    100000,   # labour cost
    30000,    # transport cost
    20000,    # other costs
    5         # farm size
)

print("Getting farm records...")

records = get_farm_records()
for record in records:
    print(record)