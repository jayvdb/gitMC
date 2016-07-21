#!/usr/bin/env python
"""
for a root directory $rdir, assumes all subdirectories are Git repos
and pulls to the current branch
"""
from time import sleep
import subprocess as S
from random import randrange
#
from pygitutils.common import codepath

rdir = codepath()

dlist = [x for x in rdir.iterdir() if x.is_dir()]

failed=[]
for d in dlist:
    print(' --> {}'.format(d))
    try:
        S.check_call(['git','pull'], cwd=str(d))
    except S.CalledProcessError:
        failed.append(d)

    sleep(randrange(10)*.1) # don't hammer the remote server, delay of 0-1 second

if failed:
    print('paths with git pull ERROR: \n{}'.format('\n'.join([str(f) for f in failed])))
