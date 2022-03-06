import os
from humanize import naturalsize

def var_size():
    size = os.stat('/var/log/').st_size
    print(size)
    print(naturalsize(size))
    print(type(naturalsize(size)))
var_size()



