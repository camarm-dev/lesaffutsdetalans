import json
import os
import requests


def upload(video: str):
    """
    Upload a video and his metadata
    :param video: video path without extension
    :return:
    """
    with open(f'{video}.report') as file:
        report = json.loads(file.read())

    with open(f'{video}.mp4', 'fb') as video:
        requests.post('https://lesaffutsdetalans.fr/api/upload', data=report, files={'video': video})


def upload_records(paths: list):
    """
    Upload each video
    :param paths: All
    :return:
    """
    for video in paths:
        upload(video)
        print(f'[⬆️] Uploaded {video}.mp4')


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.loads(file.read())

    node = config['node']
    version = config['version']
    key = config['key']

    videos = [path.replace('.mp4', '') for path in os.listdir('records') if path.endswith('.mp4')]

    print(f'[🎬] Uploading {len(videos)} records as {node}, V {version}...')
    upload_records(videos)

