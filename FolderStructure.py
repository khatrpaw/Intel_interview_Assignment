from datetime import datetime
import random
from NewFile import NewFile
from NewFolder import NewFolder


class FolderStructure() :
    root_dict = NewFolder()

    root_dict.name = "root"
    root_dict.subFolder = []

    file_type = {'txt'  : 'text',
                 'png'  : 'image',
                 'avi'  : 'video'}

    def __int__(self) :
        super().__init__()
#########################################################################################
#  Steps followed to add the folder                                                     #          
#     1. currentDic point to the root Folder                                            #
#     2. Divide the path into array for "/home/Datasets" as ['home','datasets']         #
#     3. Traverse into folder by checking whether the subfolder conatins that dic       #
#     4. If no folder/File is found in the subFolder                                    #
#            - check whether its a new folder/file to be created                        #
#        else                                                                           #
#           -found append  file/folder in the subFolder                                 #
#                                                                                       #
# for example :                                                                         #
#  root.subFolder[home.subFolder[dataset.subFolder[info.txt,image.subFolder[]]',        #
#               folder1.subFolder[folder11.subFolder[]]]']                              #
#  add /home/folder1/folder11                                                           #
#########################################################################################




    def add_item(self,path):  
        path = path.split('/')[1:] ##Get the path
        currentDic = self.root_dict.subFolder #Pointed to
        while path :
            dicpath = path.pop(0)
            foundStatus = False
            for idx,dic in enumerate(currentDic) :
                if dic.name == dicpath and len(path) == 0 :
                    if isinstance(dic,NewFolder) :
                        print("Folder with same name already exits")
                    elif isinstance(dic,NewFile) :
                        print("File with same name already exits")
                    foundStatus = True
                    break
                elif dic.name == dicpath and len(path) > 0 :
                    currentDic = currentDic[idx].subFolder
                    foundStatus = True
                    break
            if not foundStatus and len(path) > 0 :
                print("\nNo Folder exits as '"+ dicpath +"'! First create folder '"+ dicpath +"'")
                break
            elif not foundStatus and len(path) == 0 :
                if "." in dicpath:                      #check for whether is file or folder
                    newFile = self.getFileInfo(dicpath)
                    currentDic.append(newFile)    
                else :
                    newFolder = self.getFolderInfo(dicpath)
                    currentDic.append(newFolder)
                    currentDic = currentDic[-1].subFolder

##############################
# Create New File or Folder  #
##############################

    def getFileInfo(self,item):
        
        file = NewFile()
        
        file.name = item
        
        item_info = item.split('.')[1]
        
        if item_info in self.file_type :
            file.type = self.file_type[item_info]
        if file.type == 'text' :
            file.size = str(round(random.uniform(0.3, 5.0), 2)) + " kb"
        elif file.type == 'image' :
            file.size = str(round(random.uniform(1.0, 10.0), 2)) + " mb"
        elif file.type == 'video' :
            file.size = str(round(random.uniform(10.0, 50.0), 2)) + " mb"
        
        file.upload_time = datetime.now().strftime("%H:%M:%S %B %d, %Y")

        return file
    
    def getFolderInfo(self,item):
        folder = NewFolder()
        folder.name = item
        folder.subFolder = []
        folder.upload_time = datetime.now().strftime("%H:%M:%S %B %d, %Y")
        return folder




#########################################################################################
#  Steps followed to View the folder                                                    #          
#     1. currentDic point to the root Folder                                            #
#     2. Divide the path into array for "/home/Datasets" as ['home','datasets']         #
#     3. Traverse into folder by checking whether the subfolder contains that folder    #
#     4. If no folder/File is found in the subFolder                                    #
#            - print "No folder/file was found"                                         #
#        else                                                                           #
#           - if found the it show all the items in the folder and and subFolder        #
#########################################################################################


    def view_item(self,folderPath):
        path = folderPath.split("/")[1:]
        currentDic = self.root_dict.subFolder
        while path :
            dicPath = path.pop(0)
            foundStatus = False
            for idx,dic in enumerate(currentDic) :
                if dic.name == dicPath and len(path) == 0 :
                    print("\n\t"+ dic.name)
                    print("-----------------------------------------------")
                    if len(dic.subFolder) == 0:
                        print("\n \t No File/Folder Found under folder ' " + dic.name + " '")
                        foundStatus = True
                        break
                    else :
                        for item in dic.subFolder:
                            if isinstance(item, NewFolder):
                                print("\n\t |- " + item.name)
                                self.getAllFolderItems(item.subFolder)
                            else :
                                print("\n\t |- " + item.name  +"\t ("+ item.size + ", " + item.type +")")
                        foundStatus = True
                        break
                elif dic.name == dicPath and len(path) > 0 :                                            
                    currentDic = currentDic[idx].subFolder
                    foundStatus = True
                    break
            
            if not foundStatus and len(path) >= 0 :
                print(" No File/Folder name '"+ dicPath +"' Found \n")
                break

    def getAllFolderItems(self,currentDic) :

        for item in currentDic:
            if isinstance(item, NewFolder):
                print("\t \t|-- " + item.name)
            else :
                print("\t \t|-- " + item.name  +"\t ("+ item.size + ", " + item.type +")")
                
###################################################################################
# View ALL Item will show all the folders and files present in the root folder    #
###################################################################################
    def view_All_Item(self) :
        
        print("\n\t Folder Name \t \t  | \t \t Upload Time")
        print("------------------------------------------------------------------------------\n")
        current = self.root_dict
        for item in current.subFolder:
            if item is not None :
                print("\t"+ item.name +"\t \t \t \t \t " +item.upload_time + "\n")


#########################################################################################
#  Steps followed to filter the file based on type                                      #          
#     1. currentDic point to the root Folder                                            #
#     2. Divide the path into array for "/home/Datasets" as ['home','datasets']         #
#     3. Traverse into folder by checking whether the subfolder conatins that dic       #
#     4. If no folder/File is found in the subFolder                                    #
#            - check whether its a new folder to be created or it folder need to exists #
#      else                                                                             #
#           - if found the it will filter based on the type of the file                 #
#########################################################################################


    def filter_item(self,filterCommand):
        filterType = filterCommand.split(" -type ")[1]
        filterPath = filterCommand.split(" -type ")[0].split("/")[1:]
        currentDic = self.root_dict.subFolder
        while filterPath :
            dicPath = filterPath.pop(0)
            foundStatus = False
            for idx,dic in enumerate(currentDic) :
                if dic.name == dicPath and len(filterPath) == 0 :
                    print("\n\t"+ dic.name)
                    print("-----------------------------------------------")
                    if len(dic.subFolder) == 0:
                        print("\n \t No File/Folder Found under folder ' " + dic.name + " '")
                        foundStatus = True
                        break
                    else :
                        for item in dic.subFolder:
                            if isinstance(item, NewFolder):
                                print("\n\t |- " + item.name)
                                self.getAllFolderItemsWithFilter(item.subFolder,filterType)
                            elif isinstance(item,NewFile) and item.type == filterType :
                                print("\n\t |- " + item.name  +"\t ("+ item.size + ", " + item.type +")")

                        foundStatus = True
                        break
                elif dic.name == dicPath and len(filterPath) > 0 :                                            
                    currentDic = currentDic[idx].subFolder
                    foundStatus = True
                    break
            
            if not foundStatus and len(filterPath) >= 0 :
                print(" No File/Folder name '"+ dicPath +"' Found")
                break

    def getAllFolderItemsWithFilter(self,currentDic,filterType) :
        for item in currentDic:
            if isinstance(item,NewFile) and item.type == filterType :
                print("\t \t|-- " + item.name  +"\t ("+ item.size + ", " + item.type +")")


#########################################################################################
#  Steps followed to delete the folder/file                                             #          
#     1. currentDic point to the root Folder                                            #
#     2. Divide the path into array for "/home/Datasets" as ['home','datasets']         #
#     3. Traverse into folder by checking whether the subfolder conatins that dic       #
#     4. If no folder/File is found in the subFolder                                    #
#            - check whether its a new folder to be created or it folder need to exists #
#        else                                                                           #
#           - if found delete the file/folder from the SubFolder                        #
#########################################################################################


    def delete_item(self,folderPath):
        path = folderPath.split("/")[1:]
        current = self.root_dict.subFolder
       
        while path :
            dicPath = path.pop(0)
            foundStatus = False
            for idx,dic in enumerate(current) :
                if dic.name == dicPath and len(path) == 0 :
                    del current[idx]
                    foundStatus = True
                    break
                
                elif dic.name == dicPath and len(path) > 0 :
                    current = current[idx].subFolder
                    foundStatus = True
                    break
            
            if not foundStatus and len(path) >= 0 :
                print(" No File/Folder name '"+ dicPath +"' Found")
                break
