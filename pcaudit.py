#!/usr/bin/awk BEGIN{a=ARGV[1];b="";for(i=1;i<ARGC;i++){b=b"\t"ARGV[i];}sub(/[a-z_.\-]+$/,"venv/bin/python3",a);system(a""b)}

#shebang source: https://stackoverflow.com/questions/33225082/relative-shebang-how-to-write-an-executable-script-running-portable-interpreter/33225083#33225083

"""Title: pcaudit.py
Description: Controls the general flow of execution for the program.
Author: Brian Metzger
Last modified: 2020-02-09
"""


from sysinfo import sysinfo

def main():
    #TODO: Determine Operating system


    #Collect platform information
    platform_info = sysinfo.get_system_info()
    
    #Collect processor information
    cpu_info = sysinfo.get_cpu_info()
    
    #TODO: Collect hardware informatino
    
    #TODO: Collect user account information
    
    #TODO: Collect installed program info
    

    #TODO: Output results
    for x in platform_info:
        print(x + ":\t" + platform_info[x])
        
    for x in cpu_info:
        print(x + ":\t" + str(cpu_info[x]))
    
    
if __name__ == "__main__":
    main()