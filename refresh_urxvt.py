from subprocess import check_output
import os
import signal

def get_pid(name):
    return list(map(int, check_output(["pidof", name]).split()))

def refresh_urxvt():
    for i in get_pid("urxvt"):
        os.kill(i, signal.SIGHUP)
