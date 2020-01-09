#!/usr/bin/env python

"""

Inspired by the routine that builds command documentation.  This executes each command
to try and get the docs.  Any errors will cause a crash.

Execute each command with the --dumpdoc flag to get the documentation.

"""

import os
import sys
import subprocess


def eval_commands(listcmd):
    # B) build a dict of every command (using our existing commands that do this!)
    cmdlst = subprocess.check_output(listcmd, shell=True).split("\n")
    
    # execute each command with the --dumpdoc flag
    for c in cmdlst:
        if c:
            print("... testing [%s]" % (c))
            subprocess.check_output("%s --dumpdoc" % (c), shell=True)
            

print("Testing commands...")
eval_commands("ctm-list-commands")
print("SUCCESS")
