k = 0

k = int(k)

from fnmatch import *

for x in range(11392,650000,32):

    if fnmatch(str(x), '12*12?'):

        k = (int(str(x)[0])+int(str(x)[1])) - (int(str(x)[-1])+int(str(x)[-2]))

        print(x,k)