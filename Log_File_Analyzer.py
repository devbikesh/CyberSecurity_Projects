# Log File Analyzer
print("\nLog File Analyzer")

# Open the log file in read mode
file = open("log.txt", "r")

# Initialize login counters
successful_logins = 0
failed_logins = 0

# Store the number of failed attempts for each username
failed_attempts = {}

# Initialize suspicious user counter
suspicious_users = 0

# Track the username with the highest number of failed attempts
most_targeted_user = ""
highest_failed_attempts = 0

# Read and analyze each line in the log file
for line in file:

    # Count successful logins
    if "LOGIN_SUCCESS" in line:
        successful_logins += 1

    # Process failed login attempts
    if "LOGIN_FAILED" in line:
        parts = line.split()

        # Extract the username from the log entry
        username = parts[4]

        # Count failed attempts for each username
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

        # Increase the total failed login counter
        failed_logins += 1

# Close the log file
file.close()

# Display total login counts
print("\nTotal Successful Logins:", successful_logins)
print("Total Failed Logins:", failed_logins)

# Display failed login attempts for each username
print("\nFailed Login Attempts by Username:")

for username, attempts in failed_attempts.items():

    # Flag users with three or more failed attempts
    if attempts >= 3:
        suspicious_users += 1
        print("Suspicious Activity:", username, "Failed Attempts:", attempts)

    else:
        print("Normal Activity:", username, "Failed Attempts:", attempts)

    # Identify the username with the highest number of failed attempts
    if attempts > highest_failed_attempts:
        highest_failed_attempts = attempts
        most_targeted_user = username

# Display the final security summary
print("\n===== SECURITY SUMMARY =====")

print("Total Successful Logins:", successful_logins)
print("Total Failed Logins:", failed_logins)
print("Suspicious Users:", suspicious_users)

# Handle the case where no failed login attempts were recorded
if highest_failed_attempts > 0:
    print("Most Targeted Username:", most_targeted_user)
    print("Failed Attempts:", highest_failed_attempts)
else:
    print("No failed login attempts recorded.")