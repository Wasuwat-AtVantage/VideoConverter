import os
import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", type=str, default='videos',help='Folders of Videos')
args = vars(parser.parse_args())

input_folder = args['folder']
output_folder = os.path.join(input_folder, 'mp4')
file_list = os.listdir(input_folder)
for file_name in file_list:
  file_path = os.path.join(input_folder, file_name)

  # Convert from .264 to .mp4 if needed
  # Strip garbage chunk of non-standard H264 format too.
  if file_path.endswith('.264'):
    print('Converting .264 file to .mp4')
    subprocess.call(['./convert', file_path])
    file_path = file_path.replace('.264', '.mp4')
    print('Use converted file: ' + file_path)
  elif file_path.endswith('.mp4'):
    print('Use file: ' + file_path)
  else :
    print('Unknown file type.')
delete_command = f"find {input_folder}/ -name '*.wav' -delete"
os.system(delete_command)
print('Finished.')
