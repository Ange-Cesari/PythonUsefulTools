acceptable=["0","1","2","3","4","5","6","7","8","9"]

nb_start=input("Enter a number where the 3 digits are different\n>")
flag=0
for i in nb_start:
    if i not in acceptable:
        print("character", i,"is not valid")
        flag+=1
    
    
    
if flag>0:
    print("Enter again")    
else:
    print("reversing number", nb_start)
    nb_start_reverse  = nb_start[::-1]
    print(nb_start_reverse)
    nb_step3=0

    if int(nb_start) > int(nb_start_reverse):
        
        nb_step3 = int(nb_start) - int(nb_start_reverse)
        print(nb_start, "-", nb_start_reverse, "=", nb_step3 )

    elif int(nb_start_reverse) > int(nb_start):
        nb_step3 = int(nb_start_reverse) - int(nb_start)
        print(nb_start_reverse, "-",nb_start , "=", nb_step3 )

    else:
        print("Entered number is not valid")
        
    if nb_step3 > 0:
            
        nb_step3_reverse=str(nb_step3)[::-1]
        print("Reverse the number: ", nb_step3_reverse)
        nb_final = int(nb_step3)+int(nb_step3_reverse)
        print(nb_step3, "+",nb_step3_reverse , "=", nb_final )
        print("Final number is", nb_final)
        if nb_final == 1089:
            print("You find the right number !")
        else:
            print("Not correct. It might be order problem !")

