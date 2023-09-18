# -*- coding: utf-8 -*-
"""
@author: mdiechannel
"""
# 
# For PYTHON 3+ with pySerial module installed
# GW INSTEK GSP-827 Spectrum Analyzer
# Hello Word! Only queries to the instrument.
#
'''
Query List

CON:SYS:CLOCK?      # Query the system date and clock
CON:SYS:FW?         # Query the Firmware version
CON:SYS:VER?        # Query the Software version and built date
MEAS:FREQ:CEN?      # Query the center frequency
MEAS:FREQ:ST?       # Query the start frequency
MEAS:FREQ:STP?      # Query the stop frequency
MEAS:FREQ:SS?       # Query the step size of the frequency settings
MEAS:SPAN?          # Query Span
MEAS:REFL?          # Query Reference
MEAS:REFL:SCAL?     # Query amplitude scale
MEAS:REFL:UNIT?     # Query the amplitude unit
MEAS:PEAK:TRACK?    # Query the track status
MEAS:TRA:SAVE:FROM? # Query the source for trace saving
MEAS:TRA:SWITCH?    # Query the trace for data dump
MEAS:TRA:READ?      # Query Dump the assigned trace data
#                     It is 501 points of 10 bit DAC (digital to analogconverter) data.
#                     The DAC value is from 0 to 1,023.
MEAS:TRA:ATRA?      # Query the status (on/off) of trace A
MEAS:TRA:BTRA?      # Query the status (on/off) of trace B
MEAS:TRA:AVG:COUNT? # Query the number of trace averaging
MEAS:TRA:AVG?       # Query the status (on/off)
MEAS:TRA:FRE?       # Query the status (on/off) of trace freeze function
MEAS:TRA:DET:M?     # Query the trace detection mode
CON:RBW:MODE?       # Query the RBW mode.
CON:RBW?            # Query the RBW
CON:VBW:MODE?       # Query the VBW mode.
CON:VBW?            # Query the VBW
CON:SWEEP?          # Query the sweep time mode
CON:TG:NORM?        # Query TG status (on/off) of TG.
CON:TRIG:MODE?      # Query trigger mode
CAL:INPUTZ?         # Query the offset of 75 Ohm input impedance.
and more. See ´GSP827 Command List´ 2004 rev.1.5
'''

command_list=['CON:SYS:CLOCK?',
'CON:SYS:FW?', 
'CON:SYS:VER?',
'MEAS:FREQ:CEN?',
'MEAS:FREQ:ST?',
'MEAS:FREQ:STP?',
'MEAS:FREQ:SS?',
'MEAS:SPAN?',
'MEAS:REFL?',
'MEAS:REFL:SCAL?',
'MEAS:REFL:UNIT?',
'MEAS:PEAK:TRACK?',
'MEAS:TRA:SAVE:FROM?',
'MEAS:TRACE:SWITCH?',
'MEAS:TRA:READ?',
'MEAS:TRA:ATRA?',
'MEAS:TRA:BTRA?',
'MEAS:TRA:AVG:COUNT?',
'MEAS:TRA:AVG?',
'MEAS:TRA:FRE?',
'MEAS:TRA:DET:M?',
'CON:RBW:MODE?',
'CON:RBW?',
'CON:VBW:MODE?',
'CON:VBW?',
'CON:SWEEP?',
'CON:TG:NORM?',
'CON:TRIG:MODE?',
'CAL:INPUTZ?'
]

import serial     

ser = serial.Serial("COM6", 57600, timeout=1) #COM PORT NUMBER GSP-827 57600 - 8 - N - 1
if ser.isOpen():    # make sure port is open
    print(ser.name + ' is open')    # starting
    for command in command_list:
        cmd=command+'\r'
        cmd=cmd.encode()
        ser.write(cmd)
        print('SEND: ', cmd)
        print(ser.readline())    
    ser.close()        