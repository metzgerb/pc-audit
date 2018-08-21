"""Title: pcaudit.py
Description: Controls the general flow of execution for the program.
Author: Brian Metzger
Last modified: 2018-08-20
"""

import sysinfo

#TODO: Check arguments for commandline usage

#TODO: Determine Operating system
sys_platform = sysinfo.get_system_info()
for x in sys_platform:
    print(x + ":\t" + sys_platform[x])


#TODO: Get system info

#TODO: Get installed program info

#TODO: Write data to file