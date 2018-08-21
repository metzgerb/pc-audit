"""Title: sysinfo.py
Description: Obtains and returns system information
Author: Brian Metzger
Last modified: 2018-08-21
"""

import platform
import psutil

def get_system_info():
    sys_dict = {}
    sys_dict["PC Name"] = platform.node()
    sys_dict["OS"] = platform.platform()
    sys_dict["Arch"] = platform.architecture()[0]
    return sys_dict
    
def get_cpu_info():
    cpu_dict = {}
    cpu_dict["CPU Type"] = platform.processor()
    cpu_dict["Freq. (Mhz)"] = psutil.cpu_freq()[2]
    cpu_dict["Physical Cores"] = psutil.cpu_count(logical=False)
    cpu_dict["Logical Cores"] = psutil.cpu_count()
    return cpu_dict