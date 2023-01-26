# Wifi-Scanner
This code uses the subprocess.check_output() function to run the command netsh wlan show network which lists all available wifi networks. The output of this command is stored in the variable output.

Then, it uses the re.findall() function to extract all the wifi network names (SSID) from the output using regular expression. The regular expression r"(?:SSID[\s:]+)([\S]+)" looks for the string "SSID" followed by whitespace or colon and captures all non-whitespace characters that follow it. The extracted wifi names are stored in the list wifi_list.

Finally, the code uses a for loop to iterate through the wifi_list and print the name of each wifi network.

Please keep in mind that this code will only work on Windows operating system as it uses the netsh command. Also, the command might require administrator permission.
