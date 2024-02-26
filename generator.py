import random
import json
import psycopg2
from datetime import datetime
from time import sleep, time

def generate_random_bus_plate_number():
    return f"{random.randint(100, 999)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}"

def generate_random_json():
    template = {
        "angle": 79.84536743164062,
        "busDepotId": 272256687,
        "busDepotName": "ТОО УралТехСервис",
        "busId": 275814833,
        "busPlateNumber": generate_random_bus_plate_number(),
        "createDate": "2024-02-12T17:20:37",
        "distance": 0.03663880378007889,
        "lat": round(random.uniform(51.08, 51.16), 7),
        "lon": round(random.uniform(71.37, 71.46), 7),
        "localityCode": "ORAL",
        "recordId": 504332,
        "routeDirectionCode": "A_TO_B",
        "routeId": 300765962,
        "routeName": "Автовокзал (ул. Сырым Датова) - ТД Адал",
        "routeNumber": str(random.randint(43, 45)),
        "speed": 32.68107604980469,
        "terminalDate": datetime.utcnow().isoformat(),  # Use current timestamp in ISO format
        "terminalModel": "AV-S10",
        "terminalSerialNumber": "2106026b",
        "tripId": 7878355,
        "tripNumber": 68
    }

    return json.dumps(template, indent=4)

connection_params = {
    'host': 'bus_tracking_db_1',
    'database': 'bus',
    'user': 'postgres',
    'password': '1234567'
}

def create_connection():
    try:
        connection = psycopg2.connect(**connection_params)
        return connection

    except Exception as e:
        print(f"Error creating connection: {e}")
        return None

def insert_json_into_postgres(connection, json_data):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO bus_data (data) VALUES (%s);", (json_data,))
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()

db_connection = create_connection()
if db_connection:
    while True:
        for i in range(20):
            random_json_data = generate_random_json()
            insert_json_into_postgres(db_connection, random_json_data)
        print('UPDATED')
        sleep(1)
