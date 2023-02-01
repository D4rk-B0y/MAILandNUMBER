import os, platform, time 
 print('\n\x1b[1;92m[●] Checking Update.....');time.sleep(0.5) 
 os.system('git pull') 
 def Update(): 
     exit('\033[1;91m[●] Commands On Update Please Wait For Update ❤ ') 
 def Run(): 
         bit = platform.architecture()[0] 
         if bit == '64bit': 
             print("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools") 
             print('[●] Follow My Github First') 
             os.system('xdg-open https://github.com/D4rk-B0y') 
             import gmx64  
         elif bit == '32bit': 
             print("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools") 
             print('[●] Follow My Github First') 
             os.system('xdg-open https://github.com/D4rk-B0y') 
             import gmx32 
         else: 
             exit('\033[1;31m[●] Connection & Network Error') 
 Run()
 
     
 
     
 
  
 
 
     
 
    





    
    






    
    


