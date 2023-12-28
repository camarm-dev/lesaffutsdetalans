import json
from datetime import datetime
from gpiozero import MotionSensor
# from picamera import PiCamera


def record():
    """
    Increment records, update start_date and start recording a video
    :return:
    """
    global records, camera, start_date
    records += 1
    start_date = datetime.now()
    # camera.start_recording(f"'{node}_{start_date.strftime('%Y-%m-%d_%H.%M.%S')}'")
    print("Movement detected")


def post_record():
    """
    Stop recording a video, and save a report
    :return:
    """
    # camera.stop_recording()
    print("Movement stopped")
    date = start_date
    end_date = datetime.now()
    filename = f"'{node}_{date.strftime('%Y-%m-%d_%H.%M.%S')}'"
    length = (end_date - date)

    report = {
        "software": version,
        "node": node,
        "record_duration": length,
        "start_date": date,
        "end_date": end_date,
        "position": config['position']
    }
    
    with open(f'records/{filename}.report') as file:
        file.write(json.dumps(report))
    
    print(f"[📸] Recorded x seconds video the {date.strftime('%Y/%m/%d')} at {date.strftime('%H:%M')}.")


def start_sensor():
    """
    Start the sensor while
    :return:
    """
    sensor = MotionSensor(4)
    sensor.when_motion = record
    sensor.when_no_motion = post_record
    while True:
        sensor.wait_for_active()


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.loads(file.read())

    node = config['node']
    version = config['version']
    records = 0
    # camera = PiCamera()
    start_date = datetime.now()

    print(f"[⚡] Starting {node}, version {version}")

    try:
        start_sensor()
    except KeyboardInterrupt:
        print(f"[⚡] Sensor stopped, {records} videos recorded")
    except Exception as e:
        print(f"[🚨] Sensor errored with {e}")
