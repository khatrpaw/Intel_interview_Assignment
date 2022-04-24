
from datetime import datetime
import random

from File import NewFile
from Folder import NewFolder
from FolderStructure import FolderStructure



def option_menu():
    print("\n--------**- Sample Cmd -**-------------------------------------------------")
    print(" 1. Add Sub Folder -  'add /path/foldername' \n ")
    print(" 2. Add File -  'add /path/fileName.ext' ext  means (.txt,.png,avi)\n ")
    print(" 3. Filter By Type -  'filter path -type ext'  ext  means (.txt,.png,avi) \n ")
    print(" 4. Display All Files under Folder -   'view /path/folderName'  \n ") 
    print(" 5. Display all the Folder under Root Folder - 'view'               \n ")
    print(" 6. Exit  - Press q or type exit")

##Get user Input and Run the application
def run():
    folderObj = FolderStructure()
    while 1 :
    
        get_user_input = input(">>  ")
    
        ##To Close the application
    
        if get_user_input == "q" or get_user_input == 'exit':
            print("Application is closed")
            break
        
        ##Other commands from the users

        split_user_input = get_user_input.split(" ")

        if split_user_input[0] == 'add' :
            if len(split_user_input) > 1 and split_user_input[1][0] == "/" :

                folderObj.add_item(split_user_input[1])
            else :

                print("Wrong Path ! Re-enter the path ")

        
        elif split_user_input[0] == 'view' :

            if len(split_user_input) == 1 :
                folderObj.view_All_Item()
            else :
                if split_user_input[1][0] == "/" :
                    folderObj.view_item(split_user_input[1])  
                else :
                    print("Wrong Path ! Re-enter the path of the folder")
                  
        elif split_user_input[0] == 'filter' :
            folderObj.filter_item(" ".join(split_user_input[1:]))
        
        elif split_user_input[0] == 'delete' :
            if split_user_input[1][0] == "/" :
                folderObj.delete_item(split_user_input[1])
            else :
                print("Wrong Path ! Re-enter the path of the folder")
        
        else :
            print("Wrong Command . Please re-enter")


if __name__=="__main__":
    print(" \n Welcome to Folder Struction Application \n")
    print("----------------------------------------------------\n")
    option_menu()
    run()