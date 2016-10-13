import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
from func import *

built_in_cmds = {}

def register_command(name,func):
    """
    注册命令
    """
    built_in_cmds[name] = func

def init():
    """
    注册
    """
    register_command("cd",cd)
    register_command("exit",exit)
    register_command("getenv",getenv)
    register_command("history",history)


def shell_loop():
    status = SHELL_STATUS_RUN
    while status == SHELL_STATUS_RUN:
        display_cmd_prompt()
        ignore_signals()
        try:
            cmd = sys.stdin.readline()
