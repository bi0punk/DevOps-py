import os
from humanize import naturalsize

size = os.stat('/var/log/').st_size

print(size)
print(type(naturalsize(size)))