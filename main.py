#!/usr/bin/env python

from ctypes import *

# From alsa-lib Git 3fd4ab9be0db7c7430ebd258f2717a976381715d
# $ grep -rn snd_lib_error_handler_t
# include/error.h:59:typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...) /* __attribute__ ((format (printf, 5, 6))) */;

# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    #print 'messages are yummy'
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so')

# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)

from recognize import recognize
from sound_recorder import record
from speak import speak
from distance import get_distance
from led import led
from execute_cmd import execute_cmd
import time


run = True
while run:
    #run = False
    #dist = get_distance()
    led(True)
    record()
    led(False)
    #time.sleep(10)
    cmd  =  recognize()
    if(cmd != -1):
        #speak(cmd)
        execute_cmd(cmd)
        print(cmd)
    if cmd == "stop":
        break
