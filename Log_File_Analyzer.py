print("\nLog File Analyzer")
file=open("log.txt", "r")
successful_logins=0
failed_logins=0
for line in file:
    if "LOGIN_SUCCESS"in line:
     successful_logins+=1
    if "LOGIN_FAILED" in line:
     failed_logins+=1
file.close()
print("\nTotal Successful Logins:", successful_logins)
print("Total Failed Logins:", failed_logins)