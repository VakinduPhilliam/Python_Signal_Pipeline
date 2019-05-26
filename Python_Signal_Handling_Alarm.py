# Python Signal Handling
# Python Custom signal handler
# 'signal' - Set handlers for asynchronous events.
# This module provides mechanisms to use signal handlers in Python.
# The signal.signal() function allows defining custom handlers to be executed when a signal is received. 
# A small number of default handlers are installed: SIGPIPE is ignored (so write errors on pipes and sockets
# can be reported as ordinary Python exceptions) and SIGINT is translated into a KeyboardInterrupt exception.
# A handler for a particular signal, once set, remains installed until it is explicitly reset (Python emulates
# the BSD style interface regardless of the underlying implementation), with the exception of the handler for
# SIGCHLD, which follows the underlying implementation.
#
# The example below uses the alarm() function to limit the time spent waiting to open a file; this is useful if
# the file is for a serial device that may not be turned on, which would normally cause the os.open() to hang indefinitely.
# The solution is to set a 5-second alarm before opening the file; if the operation takes too long, the alarm signal will
# be sent, and the handler raises an exception.
 
import signal, os

def handler(signum, frame):
    print('Signal handler called with signal', signum)

    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely

fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
