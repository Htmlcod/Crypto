#  
# This App Created By Abdo
# Created Year: 2024
# Project Name: Files Crypter
# Supported Symbols: [A-Z] [a-z] [1-9] [!,.()"" ...]
# Support all types of files
#
from genericpath import exists
from crypting import crypte,descrypte,new_file,status_msg,multi_cpr
import colorama as color
import os
from chifres import reset_to_default
class Main():
    def operations_manager():

        
        selection=input(color.Fore.YELLOW+'past order:> '+color.Fore.WHITE) 
        if selection.isnumeric():
            selection=int(selection)
            if selection > 0 and selection<7:
               if selection!=3 and selection!=4 and selection!=5 and selection!=6:
                 file_path=input(color.Fore.YELLOW+'entre file path :> '+color.Fore.WHITE)
                 if exists(file_path)==False:
                     status_msg('this file not exist')
                     return
               elif selection==5 or selection==6:
                   file_path=input(color.Fore.YELLOW+'entre folder path :>'+color.Fore.WHITE)
               elif selection==4:
                   reset_to_default()
                   status_msg('the chifres reseted',True)
                   return
               else:
                 file_path=input(color.Fore.YELLOW+'entre file name :>'+color.Fore.WHITE)
                 file_data=input(color.Fore.YELLOW+'entre youre file data :> '+color.Fore.WHITE)
                 if file_data=='':
                     status_msg('data is null !')
                     return
               if selection!=5 and selection!=6:
                   save_path=input(color.Fore.YELLOW+'entre saving path :> '+color.Fore.WHITE)
                   if exists(save_path)==False:
                         status_msg('the saving path not valid !')
                         return
               file_password=input(color.Fore.YELLOW+'entre password (min length 6) :> '+color.Fore.WHITE)
               if len(file_password)<6:
                   status_msg('password to short !')
                   return
               if selection==1:
                   crypte(file_path,file_password,save_path)
               elif selection==2:
                   descrypte(file_path,file_password,save_path)
               elif selection==5:
                    multi_cpr(file_path,file_password)
                    os.system('cls')
                    status_msg('the folder crypted ',True)
               elif selection==6:
                   multi_cpr(file_path,file_password,False)
                   os.system('cls')
                   status_msg('the folder descrypted ',True)
               else:
                   new_file(file_path,save_path,file_data,file_password)
                   
            else:
                status_msg("out of order !")  
                
        else:
            status_msg('please check your inputs !')
              


if __name__=='__main__':
    ter_wid=os.get_terminal_size()[0]
    str=''
    str2=''
    title='FILES CRYPTER'
    for pos in range(0,ter_wid):
       str2+='*'
       if pos<int((ter_wid-len(title))):
           
           str+='_'
           if pos==int((ter_wid-len(title)-2)/2):
              str+=title
    os.system("cls")
    print(color.Fore.LIGHTMAGENTA_EX+str2+str+str2+color.Fore.WHITE)
    print(color.Fore.YELLOW+' Select youre operation :'+color.Fore.WHITE) 
    op1='  1-__Crypte file__'
    op2='  2-__Descrypte file__'
    op3='  3-__Crypte new file__'  
    op4='  4-__Reset chifres to default__' 
    op5='  5-__Crypte multi files in folder__' 
    op6='  6-__Descrypte multi files in folder__'  
    print(color.Fore.BLUE+op1+'\n'+op2+'\n'+op3+'\n'+op4+'\n'+op5+'\n'+op6+'\n'+color.Fore.WHITE)
    while True:
        Main.operations_manager()




