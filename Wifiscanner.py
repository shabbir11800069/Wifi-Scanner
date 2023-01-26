import subprocess
import re

def scan_wifi():
    output = subprocess.check_output(["netsh", "wlan", "show", "network"]).decode()
    wifi_list = re.findall(r"(?:SSID[\s:]+)([\S]+)", output)
    for wifi in wifi_list:
        print(wifi)

scan_wifi()
