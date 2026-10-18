import hashlib
import os
file_path=input("Enter the file path:")
with open(file_path,"rb") as file:
    file_content=file.read()
file_hash=hashlib.sha256(file_content).hexdigest()
print("File SHA-256 Hash:",file_hash)
if os.path.exists("hash_record.txt"):
    with open("hash_record.txt", "r") as file:
        original_hash = file.read()

    if file_hash == original_hash:
        print("File is unchanged.")
    else:
        print("WARNING: File has been modified!")

else:
    with open("hash_record.txt", "w") as file:
        file.write(file_hash)

    print("Original hash saved successfully.")