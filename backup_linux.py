#!/usr/bin/python3
import subprocess,sys,os,getopt,re,datetime,pprint,csv

backupdir=("/var/tmp/" + os.uname()[1] + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "/")

def exec_cmd(command):
    print("executing command: " + command)
    active_link = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = active_link.communicate()
    active_link.wait()
    if active_link.returncode != 0:
        print("Note return code is non zero for command:" + command)
    all_output = [x.strip for x in lines]
    all_output.append(active_link.returncode)
    return all_output

cmd_list_backup = [
        'mkdir -p ' + backupdir,
        'cp -pr /etc ' + backupdir,
        'uname -a > ' + backupdir + 'uname-a.txt'
        ]

def backuphost():
    for cmd in cmd_list_backup:
        exec_cmd(cmd)

def main():
    backuphost()

if __name__ == "__main__":
    main()

