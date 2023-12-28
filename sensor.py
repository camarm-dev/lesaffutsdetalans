import json
from datetime import datetime
from time import sleep
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
    # camera.start_recording(f"{node}_{start_date.strftime('%Y-%m-%d_%H.%M.%S')}.h264")
    print("[] Start recording")


def post_record():
    """
    Stop recording a video, and save a report
    :return:
    """
    # camera.stop_recording()
    date = start_date
    end_date = datetime.now()
    filename = f"{node}_{date.strftime('%Y-%m-%d_%H.%M.%S')}"
    length = int((end_date - date).total_seconds())

    report = {
        "software": version,
        "node": node,
        "record_duration": length,
        "start_date": date.timestamp(),
        "end_date": end_date.timestamp(),
        "position": config['position']
    }
    
    with open(f'records/{filename}.report', 'w+') as file:
        file.write(json.dumps(report))
    
    print(f"[📸] Recorded {length} seconds video the {date.strftime('%Y/%m/%d')} at {date.strftime('%H:%M')}.")


def start_sensor():
    """
    Start the sensor while
    :return:
    """
    sensor = MotionSensor(27)
    # sensor.when_motion = record
    # sensor.when_no_motion = post_record
    was_motion = False
    sensor.wait_for_no_motion()
    while True:
        is_motion = sensor.value == 1

        if is_motion and not was_motion:
            record()
            was_motion = True
        elif not is_motion and was_motion:
            post_record()
            was_motion = False

        print(sensor.is_active, sensor.pin, sensor.value)
        sleep(0.01)


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
