#seasons

m=input("Month : ")
d=int(input("Date : "))
if(d > 1 and d <= 31):
    if (m == 'Apr' or m=='May'):
        print("Summer")
    elif (m=='Jun' and d<=20):
        print("Summer")
    elif (m=='Mar' and d>=20):
        print("Summer")
    elif (m == 'Jul' or m=='Aug'):
        print("Spring")
    elif (m=='Jun' and d>=21):
        print("Spring")
    elif (m=='Sep' and d<=21):
        print("Spring")    
    elif (m == 'Oct' or m=='Nov'):
        print("Fall") 
    elif (m=='sep' and d>=22):
        print("Fall")
    elif (m=='Dec' and d<=21):
        print("Fall")      
    elif (m == 'Feb' or m=='Jan'):
        print("Winter")
    elif (m=='Mar' and d<=19):
        print("Winter")
    elif (m=='Dec' and d>=20):
        print("Winter")
else :
    print("Wrong Input")
            
            
      
