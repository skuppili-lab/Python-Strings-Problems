#Log Parser — You have a server log line: "[ERROR] 2024-01-15 : Disk full on /dev/sda1". 
# How do you extract just the date and error message?

log="[ERROR] 2024-01-15 : Disk full on /dev/sda1"
date,error_msg=log.split(":")
print(date.split("] ")[-1],error_msg.strip())