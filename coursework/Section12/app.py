import time
from datetime import datetime

def hours_to_seconds(hours):
    return (hours * 60) * 60


hosts_path = "data/hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com"]
written = False

while True:
    if 8 <= datetime.now().hour <= 16:
        if not written:
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
                        written = True

    else:
        if written:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
                written = False
    time.sleep(20)
