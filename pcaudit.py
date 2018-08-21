"""Title: pcaudit.py
Description: Controls the general flow of execution for the program.
Author: Brian Metzger
Last modified: 2018-08-20
"""

import sysinfo

#TODO: Check arguments for commandline usage

#TODO: Determine Operating system


#TODO: Get system info
platform_info = sysinfo.get_system_info()
for x in platform_info:
    print(x + ":\t" + platform_info[x])
    
cpu_info = sysinfo.get_cpu_info()
for x in cpu_info:
    print(x + ":\t" + str(cpu_info[x]))
    
    
#TODO: Get installed program info

#TODO: Write data to file