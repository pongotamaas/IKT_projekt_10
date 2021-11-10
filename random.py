import random
import time
import os
def clear():
    os.system('CLS')
for ismetles in range(10):
    x = random.randint(1,6)
    print(x)
    time.sleep(1)
    clear()


    if x ==1:
        print (r"""
               
     _______ ))    
    /      /\
   /   O  /O \ 
((/_____ /    \
  \O    O\    / 
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)

    elif x ==2:
        print (r"""

     _______ ))    
    /o     /\
   /      /O \ 
((/_____o/    \
  \O    O\    / 
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)

    elif x ==3:
        print (r"""
               
     _______ ))    
    /o     /\
   /   o  /O \ 
((/_____o/    \
  \O    O\    /     
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)

    elif x ==4:
        print (r"""
               
     _______ ))    
    /o    o/\
   /      /O \ 
((/o____o/    \
  \O    O\    / 
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)

    elif x ==5:
        print (r"""
               
     _______ ))    
    /o    o/\
   /  o   /O \ 
((/o____o/    \
  \O    O\    / 
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)
    elif x ==6:
        print (r"""
               
     _______ ))    
    /o o o /\
   /      /O \ 
((/_o_o_o/    \
  \O    O\    / 
   \O    O\ O/  
    \O____O\/ ))          
  ((   
     """)