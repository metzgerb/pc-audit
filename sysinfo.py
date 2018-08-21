"""Title: sysinfo.py
Description: Obtains and returns system information
Author: Brian Metzger
Last modified: 2018-08-21
"""

import platform

def get_system_info():
    sys_dict = {}
    sys_dict["OS"] = platform.platform()
    sys_dict["Architecture"] = platform.architecture()[0]
    sys_dict["Processor Type"] = platform.processor()
    sys_dict["Computer Name"] = platform.node()
    return sys_dict