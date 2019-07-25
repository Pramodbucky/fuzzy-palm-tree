#!/usr/bin/env python
# coding: utf-8

# For important files to move from source to destination.
# And this files move from defined source i.e Downloads to defined destination

# In[9]:


import shutil
import os
import glob

def filemove(source_dir,dest_dir):
    userchoice = int(input("1. Partial Move\n2. Complete Move\n "))
    if userchoice == 1:
        sw = input("Startswithfile: ")
        ew = input("Endswith: ")
        for file in os.listdir(source_dir):
            if file.startswith('{}'.format(sw)) and file.endswith('{}'.format(ew)):
                fullpath = os.path.join(source_dir,file)
                shutil.move(fullpath,dest_dir)
                print("{} is moved!!".format(file))
            else:
                print("Files doesnot exit!!!!")
    elif userchoice == 2:
        for file in os.listdir(source_dir):
            fullpath = os.path.join(source_dir,file)
            shutil.move(fullpath,dest_dir)
            print("{} is moved!!".format(file))
            
    else:
        print("Wrong Choices!!!")
            
def filedel(source_dir):
        userchoice = int(input("1. Partial delete\n2. Complete delete\n "))
        count = 1
        if userchoice ==1:
            sw = input("Startswithfile: ")
            ew = input("Endswith: ")
            final_source_dir = source_dir + '/' + sw + '*' + ew
            file_list = glob.glob(final_source_dir)
            for file in file_list:
                os.remove(file)
                count = count + 1
            print("{} files deleted!!!".format(count))
                
            
        elif userchoice ==2:
            source_dir = source_dir + '/*'
            file_list = glob.glob(source_dir)
            for file in file_list:
                os.remove(file)
                print("All Files deleted!!!")

        else:
            print("Wrong choice!!!")

userchoice = input("Do you want your own location??...[y/n] ")
if userchoice =='y':
    source_dir = input("Enter source location after os and location should seperate by '/': ")
    dest_dir = input("Enter destination location after os and location should seperate by '/': ")
    
else:
    print("We are doing this for download source and destination is Torrentfile")
    source_dir = "/Users/pkc/Downloads"
    dest_dir = "/Users/pkc/Desktop/Torrentfile"
    
print(source_dir)
print(dest_dir)
userchoice = int(input("1.Move\n2.Delete\n3.Both\n"))
if userchoice == 1:
    filemove(source_dir,dest_dir)
    
elif userchoice == 2:
    filedel(source_dir)
    
elif userchoice == 3:
    filemove(source_dir,dest_dir)
    filedel(source_dir)
    
else:
    print("Wrong Choices!!!")


# import glob
# import os
# fin = 'Bulk'
# tin = 'csv'
# gin = fin + '*' + tin
# print(gin)
# inn = 'Unit*pdf'
# source_dir = "/Users/pkc/Downloads/*"
# file_list = glob.glob(source_dir)
# print(file_list)

# In[ ]:





# In[ ]:




