#!/usr/bin/env python
"""
report on git repos not on the expected branch e.g. 'master'
"""
from argparse import ArgumentParser
from gitutils import findbranch
import asyncio


def main():
    p = ArgumentParser()
    p.add_argument('codepath', help='path to code root', nargs='?', default='~/code')
    p.add_argument('mainbranch', nargs='?',
                   default='master', help='name of your main branch')
    P = p.parse_args()

    loop = asyncio.new_event_loop()

    # necessary since we're returning from subprocess
    # for other types of applications, asyncio.run() does this implicitly.
    asyncio.get_child_watcher().attach_loop(loop)

    branch = loop.run_until_complete(findbranch(P.mainbranch, P.codepath))

    for b in branch:
        print(b[0], ' => ', b[1])


if __name__ == '__main__':
    main()
