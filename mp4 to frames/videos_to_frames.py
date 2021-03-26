import cv2
from os import listdir
from os.path import isdir, isfile, join
from pathlib import Path

ROOT_FILES_PATH = 'videos'
RESULT_PATH = 'videos/res'
FOLDER_NUM = 1

video_path = ROOT_FILES_PATH 
video_files = [f for f in listdir(video_path) if isfile(join(video_path, f))]
for file in video_files:
    video_captures = cv2.VideoCapture(join(video_path, file))
    success, image = video_captures.read()
    frame_number = 0
    video_name = file.split('.mp4')[0]
    out_path = join(RESULT_PATH, video_name)
    while success:
        Path(out_path).mkdir(parents=True, exist_ok=True)
        for i in range(FOLDER_NUM):
            Path(join(out_path, str(i))).mkdir(parents=True, exist_ok=True)
        # save frame as JPEG file
        cv2.imwrite(f'{out_path}/{(frame_number % FOLDER_NUM)}/frame_{frame_number}.jpg', image)
        success, image = video_captures.read()
        frame_number += 1
    print(f'Finished processing file {file}')


