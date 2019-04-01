#!/usr/bin/env python
# encoding: utf-8
# email: ringzero@0x557.org
# http://github.com/ring04h/weakfilescan

"""
    weakfilescan
    userage: python wyspider.py http://wuyun.org
"""

import sys
import random
import libs.requests as requests
from controller import *

if __name__ == "__main__":
    if len(sys.argv) == 3:
        output_file = 'output_' + str(random.randint(1000, 9999)) + '.json'
        with open(sys.argv[1], 'r') as f:
            for line in f:
            	try:
            		line = line.strip()
	                result = json.dumps(start_wyspider(line), indent=2)
	                with open(output_file, 'a') as fw:
	                    fw.write(result)
	                    fw.write('\n')
	            except Exception as e:
	            	print(repr(e))
        sys.exit(0)
    elif len(sys.argv) == 2:
        print json.dumps(start_wyspider(sys.argv[1]), indent=2)
        sys.exit(0)
    else:
        print("usage: %s http://wuyun.org php" % sys.argv[0])
        sys.exit(-1)
