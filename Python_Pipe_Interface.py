# pipes — Interface to shell pipelines.
# The pipes module defines a class to abstract the concept of a pipeline — a sequence of converters from one
# file to another.
# Because the module uses /bin/sh command lines, a POSIX or compatible shell for os.system() and os.popen()
# is required.
# The pipes module defines the following class:
# class pipes.Template 
# An abstraction of a pipeline.
# 
# Example:
# 

import pipes

t = pipes.Template()
t.append('tr a-z A-Z', '--')

f = t.open('pipefile', 'w')
f.write('hello world')

f.close()

open('pipefile').read()

#
# OUTPUT:
#
# 'HELLO WORLD'
#
#