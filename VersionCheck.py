import subprocess

print("Full screen or Small screen")
Answer = input("Choose your preference: ")

# SmallScreen Choice
if Answer == "Smallscreen" or Answer == "smallscreen" or Answer == "Small Screen" or Answer == "small screen":
    subprocess.call([r'C:\Users\elija\Documents\Snake.py123456789\SmallScreen.bat'])

else:
    print("")

# FullScreenChoice

if Answer == "Fullscreen" or Answer == "fullscreen" or Answer == "Full Screen" or Answer == "full screen":
    subprocess.call([r'C:\Users\elija\Documents\Snake.py123456789\FullScreen.bat'])

else:
    print("")
