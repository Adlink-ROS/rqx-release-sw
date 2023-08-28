#!/usr/bin/env python3

# To use gpioget, you have to install gpiod
# sudo apt install gpiod

import apt
import sys
import subprocess

APP_NAME="Check RQX IO Board"
APP_VERSION="0.9.0"

if __name__ == '__main__':

    print("")
    print("%s %s" % (APP_NAME, APP_VERSION))
    print("")

    cache = apt.Cache()
    if not cache['gpiod'].is_installed:
        print("")
        print("Error! gpiod is not installed.")
        print("Please use apt to install: sudo apt install gpiod")
        print("")
        sys.exit(1)

    LEOPARD_GMSL_ID = [0,0,0,0]
    ADLINK_GMSL_ID = [0,1,0,1]
    ADLINK_FPDL_ID = [0,1,1,1]

    board_id = [0, 0, 0, 0]
    
    # ID0
    p = subprocess.Popen("gpioget gpiochip0 4", shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = p.communicate()
    board_id[0] = stdoutput[0]-ord('0')
    
    # ID1
    p = subprocess.Popen("gpioget gpiochip0 7", shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = p.communicate()
    board_id[1] = stdoutput[0]-ord('0')
    
    # ID2
    p = subprocess.Popen("gpioget gpiochip0 5", shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = p.communicate()
    board_id[2] = stdoutput[0]-ord('0')
    
    # ID3
    p = subprocess.Popen("gpioget gpiochip0 6", shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = p.communicate()
    board_id[3] = stdoutput[0]-ord('0')
        
    if board_id == LEOPARD_GMSL_ID:
        print("LEOPARD")
    elif board_id == ADLINK_GMSL_ID:
        print("ADLINK GMSL")
    elif board_id == ADLINK_FPDL_ID:
        print("ADLINK FPDL")
    else:
        print("UNKNOWN")
    
    
    # Below code use python3-libgpiod which is not available in Ubuntu 18.04 (Python 3.6)
    
    # with gpiod.Chip('gpiochip0') as chip:
    #     lines = chip.get_lines([4,7,5,6])
    #     lines.request(consumer='gpioget', type=gpiod.LINE_REQ_DIR_IN)
    #     ID = lines.get_values()

    #     LEOPARD_GMSL_ID = [0,0,0,0]
    #     ADLINK_GMSL_ID = [0,1,0,1]
    #     ADLINK_FPDL_ID = [0,1,1,1]
    #     if ID == LEOPARD_GMSL_ID:
    #         print("LEOPARD")
    #     elif ID == ADLINK_GMSL_ID:
    #         print("ADLINK GMSL")
    #     elif ID == ADLINK_FPDL_ID:
    #         print("ADLINK FPDL")
    #     else:
    #         print("UNKNOWN")
