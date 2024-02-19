import random
import json
import psycopg2

def generate_random_bus_plate_number():
    # Generates a random bus plate number in the format XXXXX where X can be a digit or an uppercase letter
    return f"{random.randint(100,999)}{chr(random.randint(65,90))}{chr(random.randint(65,90))}"

def generate_random_json():
    template = {
        "angle": 79.84536743164062,
        "busDepotId": 272256687,
        "busDepotName": "ТОО УралТехСервис",
        "busId": 275814833,
        "busPlateNumber": "412AQ07",  # to be randomized
        "createDate": "2024-02-12T17:20:37",
        "distance": 0.03663880378007889,
        "lat": 51.2088128,  # to be randomized
        "lon": 51.3769565,  # to be randomized
        "localityCode": "ORAL",
        "recordId": 504332,
        "routeDirectionCode": "A_TO_B",
        "routeId": 300765962,
        "routeName": "Автовокзал (ул. Сырым Датова) - ТД Адал",
        "routeNumber": "20",  # to be randomized
        "speed": 32.68107604980469,
        "terminalDate": "2024-02-12T17:20:37",
        "terminalModel": "AV-S10",
        "terminalSerialNumber": "2106026b",
        "tripId": 7878355,
        "tripNumber": 68
    }

    # Randomizing specific fields
    template['busPlateNumber'] = generate_random_bus_plate_number()
    template['lat'] = round(random.uniform(51.08, 51.16), 7)  # Latitude ranges from -90 to 90
    template['lon'] = round(random.uniform(71.37, 71.46), 7)  # Longitude ranges from -180 to 180
    template['routeNumber'] = str(random.randint(43, 45))  # Assuming route numbers range from 1 to 100

    return json.dumps(template, indent=4)

connection_params = {
    'host': '127.0.0.1',
    'database': 'bus',
    'user': 'postgres',
    'password': '123'
}
def create_connection():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**connection_params)
        return connection

    except Exception as e:
        print(f"Error creating connection: {e}")
        return None

def insert_json_into_postgres(connection, json_data):
    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert the JSON data into the 'bus_data' table
        cursor.execute("INSERT INTO bus_data (data) VALUES (%s);", (json_data,))

        # Commit the transaction
        connection.commit()

        print("JSON data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor (do not close the connection here)
        cursor.close()
db_connection = create_connection()
if db_connection:
# Generate and print the random JSON entity
    for i in range(40):
        random_json_data = generate_random_json()
        insert_json_into_postgres(db_connection,random_json_data)
