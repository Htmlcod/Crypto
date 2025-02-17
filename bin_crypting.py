#  
# This App Created By Abdo
# Created Year: 2024
# Project Name: Files Crypter
# Supported Symbols: [A-Z] [a-z] [1-9] [!,.()"" ...]
# Support all types of files
#
import base64
import os
import numpy


bin_formats=["png","jpg","jpeg","gif","icon","bmp"];
###########Crypte image##################""
def crp_binary(bin_path,save_path,f):   
   bin_file_read=open(bin_path,'rb')
   data=bin_file_read.read()
   bin_crypte=base64.b64encode(data)
   bin_file_edit=open(os.path.join(save_path,f),'xb')
   bin_file_edit.write(bin_crypte)
   bin_file_edit.close()
   bin_file_read.close()
   os.remove(bin_path)
 
############Descrypte image#################
def des_binary(bin_path_des,save_path,img_n):
  bin_spl=img_n.split(".")[0].split("_")
  ipr_file_read=open(bin_path_des,'rb')
  bin_data=ipr_file_read.read()
  if numpy.size(bin_spl)>2:
        spls=''
        count=1
        for spl in bin_spl:
         if count<numpy.size(bin_spl):
          spls+=spl+"_"
          count+=1
        bin_spl[0]=spls
  bin_file=open(os.path.join(save_path,bin_spl[0]+"."+bin_spl[-1]),"xb")
  bin_file.write(base64.b64decode(bin_data))
  bin_file.close()
  ipr_file_read.close()
  
  
#crp_img()
#des_img()
