import subprocess

def system_call_return(str = ""):
    if subprocess.call(str, shell=True):
        print "Warning: %s fail" % str
        return False
    else:
        return True