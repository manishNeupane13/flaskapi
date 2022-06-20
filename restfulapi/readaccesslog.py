import re


def ipreader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        return (re.findall(regexp, log))
        # return (ips_list)


def osreader1():
    # global ubuntu_list
    with open("access1.log", 'r') as logfile:
        log = logfile.read()
        regexp = r'\([\w\d\s\.]*;\s[\w]*;\s[\w\s\d]*[;\s]*[\w\d:\.]*\)'
        return (re.findall(regexp, log))
        # return ubuntu_list


def datatimereader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        regexp = r'\d{2}\/[A-z][a-z][a-z]\/\d{4}\:'
        return re.findall(regexp, log)


def hourreader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        return re.findall(':\d{2}\:', log)


def access_log_data():
    ip_address_list = ipreader()
    os_list = osreader1()
    date_list = datatimereader()
    hour_list = hourreader()
    access_log_dict = {}
    for i in range(1, 1001):
        access_log_dict[i] = {"Ip_Address": ip_address_list[i],
                              "Operating_System": os_list[i], "Date": date_list[i], "Hour": hour_list[i]}
    return (access_log_dict)


# print(len(ipreader()))
# print(len(osreader1()))
# print(len(datatimereader()))
# print(len(hourreader()))

if __name__=="__main__":
    log_data=access_log_data().values()
# print(access_log_data()[1])    
