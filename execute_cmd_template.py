#!/usr/bin/python
import subprocess,sys,os

def exec_command():
    print("executing command : " + command)
    active_link = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = active_link.communicate()
    active_link.wait()
    if active_link.returncode != 0:
        print("Note return code id non zero for command:" + command)
    all_output = [x.strip for x in lines]
    all_output.append(active_link.returncode)
    return all_output

def usage():
    #test
    print(os.path.basename(sys.argv[0]) + " -h for help " )
    
def main():
    #test

if __name__ == "__main__":
    main()
