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
		The datastructure which i have used to solve the problem is a Graph because it would be helpful in keeping the record of the folders and files and also helpful in tranverse from parent Folder to childFolder.<br>
		 The  diagram  can be used to explain much better the structure :<br>
     <a>
        https://github.com/khatrpaw/Intel_interview_Assignment/blob/b5f6e042ca95af486103e99476e09268716c031e/file_structure_graph.png
     </a><br><br>
     
     Folder will be able to keep record of the subFolder and files as childeren < br>
     
     So we will have a root folder which will be initally empty subFolders .i.e No folder and files  
     
  2. Different Cmd :<br>
      <p>
      1. Add the folder : add /home <br>
               This will add home as a folder in root.subFolder array. <br>
               I am also trying to check whether if the path is correct or not by checking the if the subFolder of root contains the folders <br>
               for eg:  if give input is add /datasets/image <br>
               it will give print "No folder namd 'datasets' is found" becuase root has no subFolder as ss. So we need to create the first the folder datasets and then folder image <br>
        add /home <br>
        add /home/datasets <br>
        add /sys <br>
        add /home/datasets/annotations <br>
        .... <br>
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
  3. Filter the file in the folder : filter /home/datasets -type text <br>
  
      This will filter out the file on the type of the file.Such file has a attribute type.It will be used to filter. <br> 
  
  </p><p>
  4. delete the file/folder : delete /home/datasets/info.txt <br>
      this will be delete the file/folder .<br>
  
  </p>
  
  
  How to run the program
  
    python main.py
    
    If you want to run the test case :
      python unitTest.py
    
    
    
    
  
