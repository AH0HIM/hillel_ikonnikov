import argparse
import time
import ipdb
import sys
print(sys.argv)
#
#
parser = argparse.ArgumentParser()
#
parser.add_argument('command', help="Command to execute. Required!")
parser.add_argument('-i', dest="install", action="store_true", help="Install app")
parser.add_argument('-s', action="store_true", help="Silent install output")
parser.add_argument('--verbose', action="store_false", help="Silent install output")
parser.add_argument('-a', '--action', type=str, default='run', help="Install option")
parser.add_argument('-ia', '--iaction', type=int, default=0, help="Install option")


arguments = parser.parse_args()

def func(*args):
    ipdb.set_trace()
    summ = 0 + arguments.iaction
    return sum

func()
pass
#
# args.ip
# args.port
# args.id
#
# time.sleep(12500)