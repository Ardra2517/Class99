import os
import shutil

source=input("Enter source..")
destination=input("Enter destination..")

source=source+'/'
destination=destination+'/'

a=os.listdir(source)
for i in a:
    shutil.move((source+i),destination)
