#!/usr/bin/env python3

import os
import shutil
import sys

from os import path

id_files = ['id_rsa', 'id_rsa.pub', '.gitconfig']
id_root = path.join(os.environ['USERPROFILE'], '.userprofiles')
status_file = path.join(id_root, 'current_id')

os.system("")

class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def print_help():
    fname = path.basename(path.realpath(sys.argv[0]))
    print('usage: {0} [command] [args]'.format(fname))
    print('commands:')
    print('  help, --help : print this message')
    print('  status, st   : show current and available ids')
    print('  checkout, co : checkout id')
    return

def file_exists(name):
    return path.exists(name) and path.isfile(name)

def get_status():
    if not file_exists(status_file):
        return None
    with open(status_file, 'r') as sf:
        return sf.read()[:64].strip();

def set_status(i):
    with open(status_file, 'w') as sf:
        sf.write(i)
    return

def print_status():
    current = get_status() or '<none>'
    ids = []
    if path.exists(id_root) and path.isdir(id_root):
        dir_items = os.listdir(id_root)
        ids += [p for p in dir_items if path.isdir(path.join(id_root, p))]
    if not current in ids:
        ids += [current]
    ids.sort()
    for p in ids:
        hl = p == current
        style = Style.GREEN if hl else Style.RESET
        star = '*' if hl else ' '
        print('{0} {1}{2}{3}'.format(star, style, p, Style.RESET))
    return

def checkout(new_id):
    # 0. check if new_id exists
    src = path.join(id_root, new_id, id_files[0])
    if not file_exists(src):
        print('checkout: no such id')
        sys.exit(1)
    # 1. save current id if exists
    current_id = get_status()
    if current_id:
        for f in id_files:
            src = path.join(id_root, f)
            if os.path.exists(src):
                dst = path.join(id_root, current_id, f)
                shutil.copyfile(src, dst)
                os.remove(src);
    # 2. checkout new id
    for f in id_files:
        src = path.join(id_root, new_id, f)
        if os.path.exists(src):
            dst = path.join(id_root, f)
            shutil.copyfile(src, dst)
    set_status(new_id)
    print('switched to id: ' + new_id)
    return

def main():
    if len(sys.argv) == 1:
        print_help()
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd in ('help', '--help'):
        print_help()
        sys.exit(0)
    if cmd in ('st', 'status'):
        print_status()
        sys.exit(0)
    if cmd in ('co', 'checkout'):
        if len(sys.argv) != 3:
            print('checkout: id expected')
            sys.exit(1)
        checkout(sys.argv[2])
        sys.exit(0)
    print('unrecognized command')
    sys.exit(1)

if __name__ == '__main__':
    main()
