#!/usr/bin/python
import subprocess,sys,os,argparse,getopt,time

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

def check_pid(pid):
    try:
        os.kill(int(pid), 0)
    except OSError:
        return 1
    else:
        return 0

def email_fun(pid,email_id):
    email_sub = "pid {} exited".format(pid)
    email_body = "pid {} exited".format(pid)
    email_cmd = '''echo "{}" |mailx -s "{}" -c {} {}'''.format(email_body,email_id,email)
    exec_command(email_cmd)

def usage():
    #test
    print(os.path.basename(sys.argv[0]) + " -h for help " )
    print(os.path.basename(sys.argv[0]) + " <pid to monitor>" )
    
def main():
    try:
        global pid
        global email
        pid = sys.argv[1]
        email = sys.argv[2]
    except:
        usage()
        sys.exit()
    while check_pid(pid) == 0:
        print("{} is running, waiting for 10 seconds before trying again".format(pid))
        print(time.ctime())
        time.sleep(10)
    else:
        print("{} exited, sending email now".format(pid))
        print(time.ctime())
        email_fun(pid)
    
   

if __name__ == "__main__":
    main()
