import unittest

from FolderStructure import FolderStructure

class Testing(unittest.TestCase) :


    def testCase(self):
        folderObj = FolderStructure()
        path = "add /home"
        print(path)
        folderObj.add_item(path)

        path = "add /home/datasets"
        print(path)
        folderObj.add_item(path)

        path = "add /home/datasets/annotations"
        print(path)
        folderObj.add_item(path)

        path = "add /home/datasets/images"
        print(path)
        
        folderObj.add_item(path)

        path = "add /home/datasets/info.txt"
        print(path)
        
        folderObj.add_item(path)

        path = "add /home/datasets/annotations/img-001.txt"
        print(path)
        
        folderObj.add_item(path)
        path = "add /home/datasets/annotations/img-002.txt"
        print(path)
        
        folderObj.add_item(path)
        
    
        path = "add /home/datasets/images/img-001.png"
        print(path)
        
        folderObj.add_item(path)
        
    
        path = "add /home/datasets/images/img-002.png"
        print(path)
        
        folderObj.add_item(path)
        
    
        path = "add /home/datasets/images/video-001.avi"
        print(path)
        
        folderObj.add_item(path)
        
    
        path = "add /home/intel/images/video-001.avi"
        print(path)
        
        folderObj.add_item(path)
        
    
        path = "view"
        print(path)
        
        folderObj.view_All_Item()
    
    
        path = "view /home"
        print(path)
        
        folderObj.view_item(path)

    
        path = "view /home/datasets"
        print(path)
        
        folderObj.view_item(path)

    
        path = "view /home/intel"
        print(path)
        
        folderObj.view_item(path)
    
    
        path = "filter /home/datasets -type text"
        print(path)
        
        folderObj.filter_item(path)


    
        path = "filter /home/datasets -type image"
        print(path)
        
        folderObj.filter_item(path)
        
    

    
        path = "filter /home/intel -type video"
        print(path)
        
        folderObj.filter_item(path)

        path = "view /home/datasets"
        print(path)
        folderObj.view_item(path)
   
        path = "delete /home/datasets/info.txt"
        print(path)
        folderObj.delete_item(path)

        path = "view /home/datasets"
        print(path)
        folderObj.view_item(path)

if __name__=="__main__":
    unittest.main()