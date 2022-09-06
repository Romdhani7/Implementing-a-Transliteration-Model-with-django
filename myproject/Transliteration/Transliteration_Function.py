from .Dictionaries import *
import langid
lang_dectetor={
    'hi':Indian_Dict,
    'mr':Indian_Dict,
    'ru':Russian_Dict ,
    'bg':Russian_Dict ,
    'ky':Russian_Dict ,
    'sr':Russian_Dict ,
    'uk':Russian_Dict,
    'en':Russian_Dict ,
    'mn':Russian_Dict ,
    'zh':Chine_Dict ,
    'ar':Arabic_Dict, 
    'ps':Arabic_Dict, 
    'en':English_Dict ,
    
}
#detection language 
def Detection_Lang(Name):
    txt=str(Name)
    detect=langid.classify(txt) 
    language =detect[0]
    return language
#transliteration_function
def Transliteration (word):
    language=Detection_Lang(word)
    get_Asci=lang_dectetor[language]
    word= word.upper()
    char=''
    
    for i in word :
      if " " in i :
          char+=" "
      if i in get_Asci.keys():
        char +=get_Asci[i]
        
        char=char.lower() 
      
           
    return char