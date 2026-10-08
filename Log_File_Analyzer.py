print("\nLog File Analyzer")
file=open("log.txt", "r")
successful_logins=0
failed_logins=0
failed_attempts={}
suspicious_users=0
most_targeted_user=""
highest_failed_attempts=0
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
    if attempts > highest_failed_attempts:
           highest_failed_attempts=attempts
           most_targeted_user=username
           
print("Suspicious Users:", suspicious_users)
print("Most Targeted Username:",most_targeted_user)
print("Failed  Attempts:",highest_failed_attempts)
