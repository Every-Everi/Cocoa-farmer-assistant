from UI import dashboard
from database import create_table

from UI.dashboard import start_dashboard

def main():
    start_dashboard()

    create_table()  # Ensure the database and table are created before saving records

#----- import the farmers data on the screen

if __name__ == "__main__":
    main()