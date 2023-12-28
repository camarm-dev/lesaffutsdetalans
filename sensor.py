import json
import logging
import sys
from datetime import datetime
from time import sleep
from gpiozero import MotionSensor
# from picamera import PiCamera


def record():
    """
    Increment records, update start_date and start recording a video
    :return:
    """
    global camera, start_date
    start_date = datetime.now()
    # camera.start_recording(f"{node}_{start_date.strftime('%Y-%m-%d_%H.%M.%S')}.h264")
    logging.info("[📸] Start recording, movement detected")


def post_record():
    """
    Stop recording a video, and save a report
    :return:
    """
    global records
    # camera.stop_recording()
    records += 1
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
    
    logging.info(f"[💾] Recorded {length} seconds video the {date.strftime('%Y/%m/%d')} at {date.strftime('%H:%M')}.")


def start_sensor():
    """
    Start the sensor while
    :return:
    """
    sensor = MotionSensor(27)
    was_motion = False
    sensor.wait_for_no_motion()
    logging.info(f"[📡] Sensor initialized, timeout is {int((datetime.now() - sensor_timeout).total_seconds())} seconds")
    while True:
        is_motion = sensor.value == 1

        if is_motion and not was_motion:
            record()
            was_motion = True
        elif not is_motion and was_motion:
            post_record()
            was_motion = False

        sleep(0.01)


if __name__ == '__main__':
    logging.basicConfig(level=logging.BASIC_FORMAT, filename="sensor.logs", filemode="a+",
                        format="%(message)s")

    stdout_logger = logging.StreamHandler()
    stdout_logger.setFormatter(logging.Formatter("%(message)s"))
    logging.getLogger().addHandler(stdout_logger)

    with open('config.json') as file:
        config = json.loads(file.read())

    node = config['node']
    version = config['version']
    records = 0
    # camera = PiCamera()
    start_date = datetime.now()

    sensor_timeout = start_date
    logging.info(f"[⚡] Starting {node}, version {version}")

    try:
        start_sensor()
    except KeyboardInterrupt:
        logging.info(f"[⚡] Sensor stopped, {records} videos recorded")
    except Exception as e:
        logging.error(f"[🚨] Sensor errored with {e}")
