import hashlib
file_path=input("Enter the file path:")
with open(file_path,"rb") as file:
    file_content=file.read()
file_hash=hashlib.sha256(file_content).hexdigest()
print("File SHA-256 Hash:",file_hash)
with open("important.txt","w") as file:
    file.write(file_hash)
print("original hash saved sucessfully.")