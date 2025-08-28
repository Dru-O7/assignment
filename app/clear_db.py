import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import database, models

def reset_database():
    """
    Drops all tables and recreates them.
    """
    print("Dropping all tables...")
    models.Base.metadata.drop_all(bind=database.engine)
    print("Creating all tables...")
    models.Base.metadata.create_all(bind=database.engine)
    print("Database has been reset.")

if __name__ == "__main__":
    reset_database()
