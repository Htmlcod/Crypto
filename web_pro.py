from cmath import e
from genericpath import exists, isfile
from multiprocessing.connection import wait
import shutil
from asyncore import write
import os
from time import sleep
from tkinter import E
import colorama as color
import numpy as np

html_block='<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<link rel="stylesheet" href="css/style.css">\n<title>Document</title>\n</head>\n<body>\n</body>\n</html>'
css_tags='*{\nmargin: 0px;\npadding: 0px;\n}'
color.init(autoreset=True)
play=True
yellow=color.Fore.YELLOW
green=color.Fore.GREEN
blue=color.Fore.BLUE
red=color.Fore.RED
cyan=color.Fore.CYAN

def error(msg):
    print(red+msg)

def loading(max_blocks=100,longe=0.01,load='|',coloring=color.Fore.LIGHTMAGENTA_EX,txt="_______WEB-PRO_______"):
  i=0
  org_ic=load
  while i<max_blocks:
      i+=1
      if i==max_blocks/2:
          load+=txt
      load+=org_ic
      print(color.Style.BRIGHT)
      print(coloring+load)
      sleep(longe)
      if i<max_blocks:
       os.system('cls')
loading()
#main
def create_proj(def_loc='C:/xampp/htdocs/server/',pro_name='',openit=False):
    def_location=def_loc+pro_name
    css_loc=def_location+'/css'
    jav_loc=def_location+'/javascript'
    if openit:
      os.system('code '+def_location)
      os.system('start C:/xampp/xampp_start.exe')
      os.system("start chrome.exe http://localhost/server/"+pro_name)
    else:
      os.mkdir(def_location)
      os.mkdir(css_loc)
      os.mkdir(jav_loc)
      main_file=open('index.php','x')
      main_file.write(html_block)
      main_file.close()
      css_file=open('style.css','x')
      css_file.write(css_tags)
      css_file.close()
      js_file=open('main.js','x')
      js_file.close()
      shutil.move('index.php',def_location)
      shutil.move('style.css',css_loc)
      shutil.move('main.js',jav_loc)

def web_pro_start():
  while True: 
    inp_val=input('> ')
    splits=inp_val.split(' ')
    if splits[0]=='-n':
        if splits[1]=="-xampp":
            if splits[2]!='':
                create_proj(pro_name=splits[2])
                if len(splits)>=4:
                 if splits[3]=='-open':
                      create_proj(pro_name=splits[2],openit=True)
                print(green+'project created.')
            else:
                error('undefind project name !')
        elif splits[1]=="-c":
            if splits[2]!='' and splits[3]!='':
               create_proj(splits[2],splits[3])
               if len(splits)>=5:
                if splits[4]=='-open':
                    create_proj(pro_name=splits[3],openit=True)
            else:
                error('undefind project name or directory !')
        else:
            error('wrong command')
    elif splits[0]=='--help':
        print(color.Fore.LIGHTYELLOW_EX+'-n == New Project \n then save directory (-xampp [xampp server path] or -c [costume path])\n then type project name \n -open to open project')
    elif splits[0]=='-close':
             os.system('start xampp_stop.exe')
             os.system('TASKKILL /F /IM code.exe')
             os.system("TASKKILL /F /IM chrome.exe")
    elif splits[0]=='-open':
        proj_name=''
        if len(splits)>=2:
           proj_name=splits[1]     
        else:
          projects_list=os.listdir('C:/xampp/htdocs/server/')
          count=0
          all_projects=[]
          for project in projects_list:
           if isfile('C:/xampp/htdocs/server/'+project)==False:
            print(yellow+'['+str(count)+'] '+green+project)
            all_projects.append(project)
            count+=1
          select=input(blue+'select num: ') 
          if int(select)<=count:
            proj_name=all_projects[int(select)]
          else:
              error('out of range !')
        if proj_name!='':
         if exists('C:/xampp/htdocs/server/'+proj_name):
          os.system('cls')
          print(green+"ready to open "+proj_name+'...')
          create_proj(pro_name=proj_name,openit=True)
          print(green+proj_name+' opened !')
         else:
            error('undefind "'+proj_name+'" project')
    elif splits[0]=='-shut':
         loading(50,txt='GODE-BYE',coloring=cyan)
         break
          
    else:
        error('wrong command \n try --help')
        
########################
try:
   web_pro_start()
except e:
    error('somthing wrong !')
    print(red+e)
####################

    
