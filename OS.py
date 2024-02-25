import platform
print(platform.uname())

import os
print(os.name)
print(os.listdir())
print(os.getcwd())
print(os.system("ipconfig"))
os.mkdir("hello") # the relative path
os.rmdir("hello")
os.makedirs("hello/child")
os.removedirs("hello/child")
os.chdir("..")
print(os.getcwd())