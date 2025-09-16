#File read
fileobject=open("sample.txt","r")
print(fileobject.read())

#Write File
fileobject=open("sample.txt","w")
fileobject.write("haii how are you?")
fileobject.close()

#append
fileobject=open("sample.txt","a")
fileobject.write(". so, no need to close the file.")

#with open
with open("sample.txt","w") as fileobject:
    fileobject.write("This is a line written using with open")

#using exception handling  
try:
    with open("sampleq.txt","r") as fileobject:
        fileobject.read()
except FileNotFoundError:
    print("Enter the valid file name")
      
      
      
print("Hello\tDevelopers ") #tabspace
print("Hello\"Developers\" ")

print("hekko world.\n welcome to coding")