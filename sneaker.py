#DCIT Assignment: Class 
#Concept - Shoe/sneaker/ type/  
#Method - color/model 
#properties - use 

#from msilib import type_binary


# ---------------------------------------------

class Shoe:  
    def __init__(self,inputted_style, inputted_use): 
        self.style = inputted_style
        self.use = inputted_use


Robbys_shoe = Shoe("flats","walking")
Chicas_shoe = Shoe("sneaker","running")
Yesenias_shoe = Shoe("heel","dancing")

print(Robbys_shoe.style)
print(Chicas_shoe.use) 



