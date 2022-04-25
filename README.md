# Intel_interview_Assignment
Intel_interview_Assignment - File Structure Application


Goal :<br>
  <p>
	The goal of the project of the project was to create file structure application where user will be able to create foler,subFolder,file. <br>
	It should also provide the funcationality where the user is able to view the root file structure or also with specific folder structure. <br>
	The user can also filter the view of the folder based on the type of file. the type can be text,image and video. <br> 
	The user can also travserse the folder and also delete all the items inside the folder. <br>
  </p>

Gerenal Approach : <br>
	1. Selection of the datastructure : <br>
		The datastructure which i have used to solve the problem is a tree because in this case the files/folders will be children stored in subFolders which will be helpful in traverse from parent Folder to childFolder.<br>
		 The diagram has been used to explain much better the structure :<br>
     <a>
        https://github.com/khatrpaw/Intel_interview_Assignment/blob/c414f11d81ffb4457aa3f5e8eeb7724d11f53fb6/file_structure_tree.png
     </a><br><br>
     
     
     class NewFolder : 
    		def __int__(self,name) : 
        		self.subFolder = []  
        		self.name = name  
        		self.upload_time = datetime.now.strftime("%H:%M:%S %B %d, %Y")
    
     So the folder will store all the children folders and files in subFolders
     
     		class NewFile:
    			def __int__(self,name,type,size, upload_time= datetime.now()):
        			self.name = name
        			self.type = type
        			self.size = size
        			self.upload_time = upload_time.strftime("%H:%M:%S %B %d, %Y")
     
     
     Folder will be able to keep record of the subFolder and files as childeren 
     
     So we have a root folder which will be initally empty subFolders .i.e No folder and files  
     
     So structure of the data is          root.subFolder['home.subFolders['datasets.subFolders['image','annotations']','Folder1.subFolders[]']','sys.subFolders[]']
     this structure of the data means :
     				     root  
     					- datasets 
						--image 
						--Folder1
					- sys
     
  2. Different Cmd :<br>
      <p>
      1. Add the folder : add /home <br><br>
         
	This will add home as a folder in root.subFolder array. <br>
        I am also trying to check whether if the path is correct or not by checking the if the subFolder of root contains the folders <br>
        
	for eg:  if give input is add /datasets/image <br>
               it will give print "No folder namd 'datasets' is found" becuase root has no subFolder as datasets. So we need to create the first the folder datasets and then folder image <br>
	
        	add /home 
        	add /home/datasets 
        	add /sys 
        	add /home/datasets/annotations 
		add/home/add/home/info.txt 
		.... 
  </p>  
  <p>
	
  2.View the root folder :  <B>view </B>
        
        It will show all the subFolders of the root <br>
        	In this case : <br>
          		-home  <br>
          		-sys  <br>
          		-usr  <br>
          		-text.txt <br>
	
  <B> view the specific Folder :</B> view /home/datasets <br>
  
 </p>
 
 <p>
  3. Filter the file baed on the type parameters in the folder : filter /home/datasets -type text <br>
  
      This will filter out the file on the type of the file. Every file has a attribute type. It will be used to filter. <br> 
  
  </p> 
  <p>
  4. delete the file/folder : 
		delete /path/filename <br>
		delete /path/folderName <br>
		
		delete /home/datasets/info.txt 
      		this will be delete the info.txt inside the dataset folder
	
  
  </p>
  
  
How to run the program
  
    python main.py
    
 If you want to run the test case :
      
    python unitTest.py
    
    
    
    
  
