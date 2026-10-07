print("\nLog File Analyzer")
file=open("log.txt", "r")
successful_logins=0
failed_logins=0
failed_attempts={}
suspicious_users=0
for line in file:
    if "LOGIN_SUCCESS"in line:
     successful_logins+=1
    if "LOGIN_FAILED" in line:
     parts=line.split()
     print("username:",parts[4])
     if parts[4] in failed_attempts:
         failed_attempts[parts[4]]+=1
     else:
        failed_attempts[parts[4]]=1
     failed_logins+=1

file.close()
print("\nTotal Successful Logins:", successful_logins)
print("Total Failed Logins:", failed_logins)
print("\n Failed Login Attempts by Username:")
for username, attempts in failed_attempts.items():
    if attempts >= 3:
       suspicious_users+=1
       print("Suspicious Activity :",username, "Failed Attempts:", attempts)
    else:
       print("Normal Activity :",username, "Failed Attempts:", attempts)
print("Suspicious Users:", suspicious_users)
