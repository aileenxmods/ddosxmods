import os
os.system("clear")
print("""\33[0;32m[0] DdosV1\n[1] DdosV1.5\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("python3 .ddosv1.py")
elif c == "1":
    os.system("python3 .ddosv1.5.py")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("\33[0;32m[ √ ] S U C C E S S F U L L Y")
