#!/usr/bin/env python

"""
returns a random identifier
"""

import os
import sys

prefix = ""
suffix = ""

if len(sys.argv) > 1:
    prefix = sys.argv[1]
    if len(sys.argv) > 2:
        suffix = sys.argv[2]
    
# returns the provided name with a random hash added
print("%s%s%s" % (prefix, os.urandom(8).encode('hex'), suffix))
