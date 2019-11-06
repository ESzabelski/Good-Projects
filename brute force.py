#a brute force password breaker demo.  This is for demo purposes of using a password 8 letters long composed
#with a defined range of letters




#key lessons, when adding the 3rd letter, i realized i had to have a blank string in the 2 letter section to cycle correctly




letters=["a","b","c","d","e","f","g","h","",]# "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",""]

pw=""
guess=""
print("this program is to simulate a large-scale brute force password breaker")
print("This program can hack longer passwords, this is for quick demo purposes only")
print("")
print("")
print("pick a password up to EIGHT letters long using A-H")
pw=input()

#third,second,first letter
first_letter_index  =0
second_letter_index =-1
third_letter_index  =-1
fourth_letter_index  =-1
fifth_letter_index =-1
sixth_letter_index =-1
seventh_letter_index =-1
eighth_letter_index =-1

while guess != pw:

#I realize now that this isn't need, because of the blank string
#but its good to keep if not blank string in other programs
    
##    if len(guess)<=1:
##        guess=letters[first_letter_index]
##    elif len(guess)==2:
##        guess=letters[second_letter_index]+letters[first_letter_index]
##    elif len(guess)==3:
##        guess=letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]
##    elif len(guess)==4:
##        guess=letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]
##    elif len(guess)==5:
##        guess=letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]         
##    elif len(guess)==6:
##        guess=letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
##    elif len(guess)==7:
##        guess=letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
##    elif len(guess)==8:
##        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  

    guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  

    #2 letter pws
    if first_letter_index==len(letters)-1:
        first_letter_index=0
        second_letter_index+=1 #this is set to zero first time, and adds 1 each after
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
        #print("  *Second Letter change*:",guess)


     #3 letter pws   
    if second_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
       # print("    *Third Letter Change*",guess)

    #4letter pws
    if third_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  =0
        fourth_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]          
        print("        *FOURTH Letter Change*",guess)


    #5letter pws
    if fourth_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  =0
        fourth_letter_index  =0
        fifth_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
        print("        *FIFTH Letter Change*",guess)



    #6
    if fifth_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  =0
        fourth_letter_index  =0
        fifth_letter_index  =0
        sixth_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
        print("            *SIXTH Letter Change*",guess)

        #7
    if sixth_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  =0
        fourth_letter_index  =0
        fifth_letter_index  =0
        sixth_letter_index  =0
        seventh_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
        print("         *SEVENTH Letter Change*",guess)

        #8
    if seventh_letter_index==len(letters)-1:
        first_letter_index  =0
        second_letter_index =0
        third_letter_index  =0
        fourth_letter_index  =0
        fifth_letter_index  =0
        sixth_letter_index  =0
        seventh_letter_index  =0
        eighth_letter_index  +=1
        guess=letters[eighth_letter_index]+letters[seventh_letter_index]+letters[sixth_letter_index]+letters[fifth_letter_index]+letters[fourth_letter_index]+letters[third_letter_index]+letters[second_letter_index]+letters[first_letter_index]  
        print("    *EIGHTH Letter Change*",guess)

        
    #print("AFTER IF:",guess)    
    first_letter_index+=1    

    
print("")
print("")
print("password is",guess, " :) " )
