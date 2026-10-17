import subprocess
output=subprocess.check_output(
    "netsh wlan show profile", 
    shell=True
).decode()
print(output)