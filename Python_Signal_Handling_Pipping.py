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
# Piping output of your program to tools like head(1) will cause a SIGPIPE signal to be sent to your process when
# the receiver of its standard output closes early. This results in an exception like BrokenPipeError: [Errno 32] Broken pipe.
# To handle this case, wrap your entry point to catch this exception as follows:
 
import os
import sys

def main():

    try:

        # simulate large output (your code replaces this loop)

        for x in range(10000):
            print("y")

        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.

        sys.stdout.flush()

    except BrokenPipeError:

        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown

        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())

        sys.exit(1)  # Python exits with error code 1 on EPIPE

if __name__ == '__main__':
    main()
