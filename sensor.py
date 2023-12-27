import json
from datetime import datetime


def record():
    record_metadata = {
        "start_date": datetime.now()
    }
    record_metadata["end_date"] = datetime.now()
    post_record(record_metadata)


def post_record(record: dict):
    date = record['start_date']
    filename = f'{node}_{date.strftime()}'
    length = (record['end_date'] - date)

    report = {
        "software": version,
        "node": node,
        "record_duration": length
    }
    
    with open(f'records/{filename}.report') as file:
        file.write(json.dumps(report))
    
    print("[📸] Recorded")


def movement_detected():
    return True


def start_sensor():
    """
    Start the sensor while
    :return:
    """
    while True:
        if movement_detected():
            record()


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.loads(file.read())

    node = config['node']
    version = config['version']
    print(f"[⚡] Starting {node}, version {version}")

    try:
        start_sensor()
    except KeyError:
        print("[⚡] Sensor stopped")
    except Exception as e:
        print(f"[🚨] Sensor errored with {e}")
