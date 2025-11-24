ip_list=["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.0.1"]
import subprocess
import os
for ip in ip_list:
    import platform
    system = platform.system().lower()
    if "windows" in system:
        ping_flag="-n"
    else:
        ping_flag="-c"
    result = subprocess.run(["ping", ping_flag, "1", ip],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is unreachable")            