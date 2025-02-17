#  
# This App Created By Abdo
# Created Year: 2024
# Project Name: Files Crypter
# Supported Symbols: [A-Z] [a-z] [1-9] [!,.()"" ...]
# Can crypte images+videos and all programming languages files and more
# not support mp3 files and pdf or binary files
#

from genericpath import exists,isfile,isdir
import os
import numpy
from loading_animation import loading_an
from bin_crypting import des_binary,crp_binary
from chifres import crypt,alpha,bin_formats
import keyboard
import colorama as color



def status_msg(msg,stat=False):
    if stat:  
      print(color.Fore.GREEN+msg+color.Fore.WHITE)
    else:
      print(color.Fore.RED+msg+color.Fore.WHITE)
      
      
      
def save_path(file_n,saving):
    main_path=os.path.join(saving,file_n)
    return main_path
#
#   Crypte function
#
def crypte(filename='',password='',Save_path=''): 
         """Crypte File as .cpr file with password.
        >>> from crypting import crypte
        >>> crypte(filename='C:/txt.txt',password='123...',Save_path='C:/')
         """                                                                                             
         try:         
          if filename=="main_app.py" or filename=="crypting.py" or filename=="bin_crypting.py" or filename=="loading_animation.py" or filename=="chifres.py" or filename=="_cpr_chifres_.maincpr": 
            #self.labe.color=(1,0,0,1)
            status_msg("you cant crypte the program files");
            return
          
          if exists(filename)==False or exists(Save_path)==False: 
           if exists(filename)==False:
             #self.labe.color=(1,0,0,1)
             status_msg("this file not exist ");
           else:
             #self.labe.color=(1,0,0,1)
             status_msg("the saving path not exist");
           return
          elif isfile(filename)==False:
            status_msg("this not a file");
            return
          
          direction=filename.split(".")
    
    #      if numpy.size(direction)<2:
    #        status_msg('the file not valid !');
    #        return
          if numpy.size(direction)>=2:
              for img_form in bin_formats:
               if img_form==direction[-1]:
                 if exists(save_path(direction[0]+"_"+direction[-1]+".tvt",Save_path))==False:
                  crp_binary(save_path(filename,Save_path),Save_path,direction[0]+"_"+direction[-1]+".tvt")
                  filename=direction[0]+"_"+direction[-1]+".tvt"
                  direction=filename.split(".")  
                 else:
                      # self.labe.color=(1,0,0,1)
                       status_msg("there another tvt file with this name !")
                       return
          file=open(filename,"r+",encoding='utf-8')
          try:
           main=file.readlines()
          except:
            #self.labe.color=(1,0,0,1)
            status_msg("this file not support !")
            return;
          if open(filename,"r",encoding='utf-8').read()=='':
               # self.labe.color=(1,0,0,1)
                status_msg("this file is empty !")
                return;
          if exists(direction[0]+".cpr"): 
           # self.labe.color=(1,0,0,1)
            status_msg("this file already crypted !")
            return
          
          if len(password)<6: 
           # self.labe.color=(1,0,0,1)
            status_msg("min password length 6")
            return
          newfile=open(save_path(direction[0]+".cpr",Save_path),"x",encoding='utf-8')
          get_file_name=filename.split("\\")[-1]
          if exists(save_path(get_file_name,Save_path))==False: 
            #self.labe.color=(1,0,0,1)
            status_msg("the Saving path not valid")
            newfile.close()
            os.remove(save_path(direction[0]+".cpr",Save_path))
            return
          password+="/"+get_file_name
          for letter in password:
              
              searche=numpy.where(letter==alpha)
              if numpy.size(searche)>0:
                  crp=crypt[searche[0][0]]
                  newfile.write(crp)
          newfile.write("\n")
          canceled=False
          final_data=''
          status_msg("To Stop The operation press 'S'",True)
          alpha_counter=0  
          alpha_size=open(filename,'r+',encoding='utf-8').read()
          for line in main:
              A=line
              for alphabet in A:  
               if keyboard.is_pressed('S'):
                     canceled=True  
               if canceled==False: 
               # self.labe.color=(1,1,1,1)
                alpha_counter+=1
                prog=int(alpha_counter*100/len(alpha_size))
                loading_an('|',prog)
                if alphabet!=" " and alphabet!="": 
                  tolowe=str(alphabet)
                  search=numpy.where(alpha==tolowe)
                  if numpy.size(search)>0:
                    main_crp=crypt[search[0][0]]
                    final_data+=main_crp
                  else:  
                     final_data+=alphabet
                else:
                      final_data+=' '
               else:           
                    newfile.close()
                    os.remove(save_path(direction[0]+".cpr",Save_path))
                    if filename.split('.')[-1]=='tvt':
                          des_binary(save_path(get_file_name,Save_path),Save_path,get_file_name) 
                          file.close()
                          os.remove(filename)
                    else:
                      file.close() 
                    #self.labe.color=(0,1,0,1)
                    status_msg("\nthe operation canceled !") 
                    break 
          if canceled==False:
           newfile.write(final_data)
           newfile.close()
           file.close()
           final_data=''
           os.remove(filename)
           #self.labe.color=(0,1,0,1)
           status_msg("secussfuly crypte file \n file path is: "+Save_path,True)
      
         except NameError:
              #self.labe.color=(1,0,0,1)
              status_msg("cant crypte this file")
#
#      Descrypte Function
#
def descrypte(filename='',password='',Save_path=''):
        """Descrypte File as original file with password.
        >>> from crypting import descrypte
        >>> descrypte(filename='C:/txt.txt',password='123...',Save_path='C:/')
         """  
        try:
         if exists(filename) and exists(Save_path):
          direction=filename.split(".")
          if  numpy.size(direction)<2:
                status_msg('the file name not valid !');
                return
          if direction[-1]!="cpr" and direction[-1]!="ipr":
           
            #self.labe.color=(1,0,0,1)
            status_msg("this not .cpr file")
            return
          if exists(filename)==False : 
            
            #self.labe.color=(1,0,0,1)
            status_msg("this file not exist")
            return                        
          file=open(filename,"+r",encoding='utf-8')
          main=file.readlines()
          if open(filename,"r",encoding='utf-8').read()=='':
                #self.labe.color=(1,0,0,1)
                status_msg("this file is empty or not valid!")
                return;
          pssbe=main[0]
          pss=""
          for letter in pssbe:
                searche=numpy.where(letter==crypt)
                if numpy.size(searche)>0:
                  psswo=alpha[searche[0][0]]
                  pss+=str(psswo)
          main_pass=pss.split("/")
          if main_pass[0]!=password: 
            #self.labe.color=(1,0,0,1)
            status_msg("wrong password !")
            return
          if exists(save_path(main_pass[1],Save_path))==False:
               newfile=open(save_path(main_pass[1],Save_path),"x",encoding='utf-8')
          else:
              #self.labe.color=(1,0,0,1)
              status_msg("error there another tvt file\n in this path: "+save_path(main_pass[1],Save_path))
              return

          final_data=''
          canceled=False
          status_msg("To Stop The operation press 'S'",True)
          alpha_counter=0  
          alpha_size=open(filename,'r+',encoding='utf-8').read()
          for line in main:
            A=line
            for alphabet in A:
             if keyboard.is_pressed('S'):
                     canceled=True  
             if canceled==False: 
              alpha_counter+=1
               # self.labe.color=(1,1,1,1)
              prog=int(int(alpha_counter)*100)/int(len(alpha_size))
              loading_an('|',prog)
              #self.alpha_counter=self.alpha_counter+1 
              #self.labe.color=(1,1,1,1)
              #self.labe.text=str(int((int(self.alpha_counter)*100)/int(len(self.alpha_size))))+"%"
              #self.prog.value=int(int(self.alpha_counter)*100)/int(len(self.alpha_size))
             
              if alphabet!=" " and alphabet!="": 
                tolowe=str(alphabet)
                search=numpy.where(crypt==tolowe)
                if numpy.size(search)>0:
                  main_crp=alpha[search[0][0]]
                  final_data+=main_crp
                else:
                  final_data+=alphabet
              else:
                    final_data+=' '
             else:
                newfile.close()
                file.close()
                os.remove(save_path(main_pass[1],Save_path))
                #self.labe.color=(0,1,0,1)
                status_msg("\nthe operation canceled !")
                break

          if canceled==False: 
           newfile.write(final_data)
           newfile.close()
           file.close()
           final_data=''
           filename=filename
           os.remove(filename)
           read_file=open(save_path(main_pass[1],Save_path),'r+',encoding='utf-8')
           first_line=read_file.readline()
           orginal_data=read_file.read()
           splited_data=orginal_data.split(first_line)
           original_file=open(save_path(main_pass[1],Save_path),"w",encoding='utf-8')
           original_file.write(splited_data[0])
           original_file.close()
           read_file.close()
           filename=main_pass[1]
           format_check=filename.split('.')
           if numpy.size(format_check)>=2:
               if format_check[-1]=="tvt":
                  des_binary(save_path(filename,Save_path),Save_path,filename)
                  os.remove(save_path(main_pass[1],Save_path)) 
         
           #self.labe.color=(0,1,0,1)
           status_msg("secussfuly descrypte file \n file path is: "+Save_path,True) 
             
                

        
            

         else:
             if exists(filename)==False:
              # self.labe.color=(1,0,0,1)
               status_msg("This file not exist !")
             else:
               #self.labe.color=(1,0,0,1)
               status_msg("The Saving path not exist !")                    
             return 
        except NameError:
          #self.labe.color=(1,0,0,1)
          status_msg("i cant descrypte this file")
          return
 #
 #              New crypted file Function
 #
def new_file(file_name,Save_path,file_data,password):
    """create new Crypted File as .cpr file with password.
        >>> from crypting import new_file
        >>> new_file(filename='txt.txt',Save_path='C:/examp/','file_data='examp...',password='123...'')
    """  
    new_file=file_name
    if numpy.size(new_file.split("."))>2:
          #self.labe.color=(1,0,0,1)
          status_msg("the file name not valid !");
          return
    if exists(Save_path):
       if exists(save_path(new_file,Save_path)):
           #self.labe.color=(1,0,0,1)
           status_msg("this file already exist");
           return   
       xfile=open(save_path(new_file,Save_path),"x",encoding='utf-8')
       xfile.write(file_data)
       xfile.close()
       crypte(save_path(new_file,Save_path),password,save_path(new_file,Save_path))
    else:
         #self.labe.color=(1,0,0,1)
         status_msg("the saving path not valid");
         return 


def multi_cpr(path,password,cryp=True):
 """Crypte multi Files as .cpr files with password.
 >>> from crypting import multi_cpr
 >>> multi_cpr(path='C:/folder/',password='123...',cryp=True(crypte)/False(descrypte))
  """  
 if exists(path):
   if isdir(path):
     sel_dir=os.listdir(path)
     exec_folders=[]
     for file in sel_dir:
        file_path=os.path.join(path,file)
        if isfile(file_path):
            spl_len=file_path.split('.')
            if numpy.size(spl_len)>=2:
              spl_len=file_path.split('.')[-1]
              if cryp==True:
                if spl_len!="cpr":
                      crypte(file_path,password,path)
              else:
                if spl_len=="cpr":
                  descrypte(file_path,password,path)
        elif isdir(file_path):
            exec_folders.append(file_path)
     for folder in exec_folders:
         multi_cpr(folder,password,cryp)

   else:
         status_msg('this is not a folder')
 else:
       status_msg('this path not exist')
        
