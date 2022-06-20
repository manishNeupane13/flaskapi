from ipaddress import ip_address
import json
import re
from collections import Counter


def ipreader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

        return re.findall(regexp, log)


def osreader1():

    with open("access1.log", 'r') as logfile:
        log = logfile.read()
        regexp = r'\([\w\d\s\.]*;\s[\w]*;\s[\w\s\d]*[;\s]*[\w\d:\.]*\)'
        return re.findall(regexp, log)


def datereader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        regexp = r'\d{2}\/[A-z][a-z][a-z]\/\d{4}\:'
        return re.findall(regexp, log)


def hourreader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        return re.findall(':\d{2}\:', log)


def get_time_data():

    return json.dumps(Counter(datereader()))


def get_os_data():
    return json.dumps(Counter(osreader1()))


def get_hour_data():
    return json.dumps(Counter(hourreader()))


def get_ip_data():
    return json.dumps(Counter(ipreader()))


def ip_data():
    return Counter(ipreader())


if __name__ == "__main__":
    # if ("162.158.89.233" in Counter(ipreader()).keys()):
    #     print(Counter(ipreader())['162.158.89.233'])
    ip_data()
    get_ip_data()
    get_os_data()
    get_time_data()
    get_hour_data()
