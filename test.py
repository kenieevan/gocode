import os
import datetime

a1="hello,world    "
a1 = a1 * 8000

cmd = "./echo " + a1
#cmd = "./echojoin " + a1

output = os.popen(cmd);
result = output.read()

print len(result)

