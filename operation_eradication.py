# operation_eradication
# Make sure to copy and paste the results of `rclone ls "Eradication:"` inside a text file names locations.txt.
# i will update the script to do all that by itself.
import os

f = open('locations.txt', 'r')
for i in f:
    fine_name = i.split()[1].split('/')[-1]
    file_location = i.split()[1][:-len(file_name)]
    os.system(f'touch {file_name}')
    os.system(f'rclone copy {file_name} "Eradication:/{file_location}"')
    os.system(f'rm {file_name}')
