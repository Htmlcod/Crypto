#  
# This App Created By Abdo
# Created Year: 2024
# Project Name: Files Crypter
# Supported Symbols: [A-Z] [a-z] [1-9] [!,.()"" ...]
# Support all types of files
#
import os
import colorama as color
from chifres import alpha

yellow=color.Fore.YELLOW
green=color.Fore.GREEN
blue=color.Fore.BLUE
red=color.Fore.RED
cyan=color.Fore.CYAN

def loading_an(symbol,value):
  terminal_width=int(os.get_terminal_size()[0])
  loader=''
  load=value
  value=int((terminal_width*value)/100)
  if value <= terminal_width:
      counter=str(int(load))+"% "
      loader=symbol*(value-len(counter))
      print("\r",end='') 
      print(cyan+counter+loader+color.Fore.WHITE,end='')
    


  