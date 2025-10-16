class DatabaseConnection:
    _instance = None # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            print("Creating new database connection instance...")
        return cls._instance

    def connect(self):
        print("Connecting to the database...")

# Usage example
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()

    print(f"db1 is db2: {db1 is db2}")  # Should print True, confirming both are the same instance