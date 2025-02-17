from genericpath import exists
import numpy
import os

#   
#            alphabet
alpha=numpy.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","3","5","6","4","8","9","7","2","/","<",">",".","©","-","*","%","&","$","^",",","?","!",":",")","0","(",";","=","+","~","[","]","_","'","{","}","@","#",'"',"é","à","è","£","µ","|","`","§","°","¿","¥","¡","ض","ص","ث","ق","ف","غ","ع","ه","خ","ح","ج","د","ش","س","ي","ب","ل","ا","ت","ن","م","ك","ط","ذ","ئ","ء","ؤ","ر","ى","ة","و","ز","ظ","أ"])
#           Keys
crypt=numpy.array(["η","ί","⨝","ϣ","ϗ","έ","Ϸ","ϼ","⨕","Ω","ϋ","ϧ","ϛ","ϝ","Δ","ϟ","⨖","ϡ","ϻ","ς","Ξ","↛","↯","ͱ","Ϗ","⫝","ϖ","ϙ","Ͼ","ͽ","Ͽ","⇕","ᾪ","ᾣ","⫻","ὥ","Ὥ","ἱ","ἆ","⫭","Γ","δ","ὰ","£","µ","π","ζ","§","°","¿","¥","¡","∎","∇","∯","∻","∺","∴","≎","≞","≛","≘","≓","≟","≣","⊎","⊍","⊋","⊊","⊄","⊌","⊑","⊐","⊗","⊖","⊕","⊘","⊛","⊜","⊞","⊟","⊠","⊢","⊣","⊧","⊨","⊦","⊶","⊷","⊪","⋔","⋚","⋛","⋄","⋇","①","④","⑦","②","⑤","⑧","③","⑥","⑨","½","¾","¼","⅓","⅔","⅕","⅘","⅗","⅖","⅙","⅚","⅐","⅝","⅜","⅛","⅞","⅑","⅒","⅟","⋳","⋨","⋧","∦","⊰","∢","√","⋢","∠","∝","∥","∤","∔","∑","∛"])  
#          imgs formats
bin_formats=["png","jpg","jpeg","gif","icon","bmp","pdf","mp3","wav","exe","zip","fbx","obj","blend","tar","apk","mp4","7z","mtl","mb","xapk","opus","3gpp","iso","m2v"]
# Main cpr file
cpr_file="_cpr_chifres_.maincpr"       
def file_config(alpha=alpha,crypt=crypt):
    if exists(cpr_file)==False:
        main_cpr=open(cpr_file,"x",encoding='utf-8')
        cpr_count=0
        for cpr in alpha:
            main_cpr.writelines(cpr+" \ "+str(crypt[cpr_count])+"\n")
            cpr_count+=1
    else:
        main_cpr=open(cpr_file,"r",encoding='utf-8')
        alpha=numpy.array([])
        crypt=numpy.array([])
        line_count=0
        for lines in main_cpr.readlines():
            get_cpr=lines.split(" \ ")
            line_count+=1
            if numpy.size(get_cpr)==2:
                if get_cpr[0]!='\n' and get_cpr[1]!='\n':
                    
                    alpha=numpy.append(alpha,get_cpr[0])
                    crypt=numpy.append(crypt,get_cpr[1].split('\n')[0])
                else:
                    print(cpr_file+": error in line "+str(line_count)+" null value")
                    break 
            else:
                
                print(cpr_file+": error in line "+str(line_count)+" missing format example('e \ v')")
                break   
    if numpy.size(alpha)==numpy.size(crypt):        
        for one in alpha:  
            sr=numpy.copy(alpha==one)
            get_copy=numpy.where(sr==True)
            if numpy.size(get_copy)>1:
                print(cpr_file+": Error Duplicated symbole in index "+str(get_copy[0])+":"+str(alpha[get_copy]))
                exit()
        for one in crypt:
            sr=numpy.copy(crypt==one)
            get_copy=numpy.where(sr==True)
            if numpy.size(get_copy)>1:
                print(cpr_file+": Error Duplicated symbole in index "+str(get_copy[0])+":"+str(alpha[get_copy]))
                exit()
                
    else:
     if numpy.size(alpha)>numpy.size(crypt):
        print(cpr_file+": crypt array length short than alpha array")
     else:
        print(cpr_file+": alpha array length short than crypt array")
    
     exit()

def reset_to_default():
    if exists(cpr_file):
        os.remove(cpr_file)
        file_config()
        

file_config()
    
    
    
            
        