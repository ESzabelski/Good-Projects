#wGot the top, now need to get that formula transferred over to calculate the other numbers



from tkinter import *
from functools import partial





def call_result(Homeprice,Loanlength,Interestrate, Onetimebonus,Monthlyextra):
    #not sure how it knows what number to get>it gets it by the call using specific textname

    Home_Price_Local=(Homeprice.get())
    Home_Price_Local=int(Home_Price_Local)
    Loan_Length_Local=(Loanlength.get())
    Loan_Length_Local=int(Loan_Length_Local)
    Interest_Rate_Local=(Interestrate.get())
    Monthly_Rate_Local=float(Interest_Rate_Local)/12
    One_Time_Bonus_Local=(Onetimebonus.get())
    Monthly_Extra_Local=(Monthlyextra.get())
    #try:
    One_Time_Bonus_Local=int(One_Time_Bonus_Local)
    Monthly_Extra_Local=int(Monthly_Extra_Local)
    #except:
      #  pass

    #this formula is the base amounta bank calculates you have to pay each month
    Monthly_Pay_Result=((Monthly_Rate_Local*(int(Home_Price_Local)))/(1-((1+Monthly_Rate_Local)**-int(Loan_Length_Local))))
    Total_Payment=Monthly_Pay_Result*int(Loan_Length_Local)
    Total_Interest=Total_Payment-int(Home_Price_Local)


    New_Grand_Total=0
    New_Loan_Length=0
    Amount_Left=Home_Price_Local
    Total_Interest=0
    while Amount_Left>100:

        Monthly_Interest=Amount_Left*Monthly_Rate_Local
        Amount_Towards_Principal=(Monthly_Pay_Result-Monthly_Interest)+Monthly_Extra_Local
        Amount_Left=Amount_Left - Amount_Towards_Principal - One_Time_Bonus_Local
        New_Grand_Total=New_Grand_Total+Monthly_Pay_Result+Monthly_Extra_Local+One_Time_Bonus_Local   
        Total_Interest=Total_Interest+Monthly_Interest
        One_Time_Bonus_Local =0
        New_Loan_Length=New_Loan_Length+1

    Total_Difference_In_Money= Total_Payment-New_Grand_Total
    Time_Difference=Loan_Length_Local-New_Loan_Length 

    try:
        Monthly_Payment_Label.config(text = ("Your pre-set monthly payment is %d"  %(Monthly_Pay_Result)))
        Total_Payment_Label.config(text="Total cost of loan: %d" %Total_Payment)
        

        Total_Interest_Label.config(text=("Interest paid %d" %Total_Interest))

        New_Total_Payment_Label.config(text=("Modified grand total: %d" %New_Grand_Total))
        New_Total_Interest_Label.config(text=("Total interest paid: %d" %Total_Interest))
        New_Total_Difference_Label.config(text=("Difference between these loans %d" %Total_Difference_In_Money))
        New_Length_Difference_Label.config(text=("Loan is paid off %d months faster" %Time_Difference))
    except:
        pass
    return



#all this is just buttons/Labels
gui=Tk()
gui.geometry("500x500+700+150")
gui.title("Mortgage Calculator")
House_Price=StringVar(value="0")
Loan_Length=StringVar(value="360")
Interest_Rate=StringVar(value="0.00")
One_Time_Bonus=StringVar(value="0")
Monthly_Extra=StringVar(value="0")


LabelTitle=Label(gui,text="Mortage Calculator").grid(row=0, column=1)
House_Price_Label=Label(gui, text = "  Enter your total home/loan price   ").grid(row=1, column=0)
Loan_Length_Label=Label(gui, text = "  Length of loan in months (Eg 360)  ")
Loan_Length_Label.grid(row=2, column=0)
Interest_Rate_Label=Label(gui, text = "  Interest rate as decimal (Eg .04)   ").grid(row=3, column=0)
Blank_Label1=Label(gui, text = "    ").grid(row=4, column=0)
Blank_Label2=Label(gui, text = "    ").grid(row=6, column=0)
Blank_Label3=Label(gui, text = "    ").grid(row=7, column=0)



#result popup section of answers
Monthly_Payment_Label=Label(gui)
Monthly_Payment_Label.grid(row=8,column=0)
Total_Payment_Label=Label(gui)
Total_Payment_Label.grid(row=9,column=0)
Total_Interest_Label=Label(gui)
Total_Interest_Label.grid(row=10,column=0)

Blank_Label4=Label(gui, text = "    ").grid(row=11, column=0)
Blank_Label4=Label(gui, text = "    ").grid(row=12, column=0)
LowerTitle=Label(gui, text = "This Section Simulates Extra Payments").grid(row=13, column=1)
One_Time_Label=Label(gui, text = "One-time extra payment").grid(row=14, column=0)
Monthly_Time_Label=Label(gui, text = "Extra monthly payments").grid(row=15, column=0)
Blank_Label4=Label(gui, text = "    ").grid(row=16, column=0)

#result popups #2
New_Total_Payment_Label=Label(gui)
New_Total_Payment_Label.grid(row=17,column=0)
New_Total_Interest_Label=Label(gui)
New_Total_Interest_Label.grid(row=18,column=0)
New_Total_Difference_Label=Label(gui)
New_Total_Difference_Label.grid(row=19,column=0)
New_Length_Difference_Label=Label(gui)
New_Length_Difference_Label.grid(row=20,column=0)

#these are the enter sections
entryHome=Entry(gui,textvariable=House_Price, bd=4).grid(row=1,column=1)
entryLoan=Entry(gui,textvariable=Loan_Length, bd=4).grid(row=2,column=1)
entryRate=Entry(gui,textvariable=Interest_Rate,bd=4).grid(row=3,column=1)
entryOneTimeBonus=Entry(gui,textvariable=One_Time_Bonus, bd=4).grid(row=14,column=1)
entryMonthlyExtra=Entry(gui,textvariable=Monthly_Extra,bd=4).grid(row=15,column=1)





#ok so the way this appears to work is that this def is using this specifc name of the
#textvariable as well as the same name is stringvar, so 3 total: stringvar,entry, and def call
call_result=partial(call_result,House_Price,Loan_Length,Interest_Rate,One_Time_Bonus, Monthly_Extra)
buttCal=Button(gui, text="Calculate now!",command=call_result).grid(row=5, column=1)







#example of how to config this
#Total_Payment_Label.config(font=("Courier", 16))




#holy shit so this will COPY what is happening in the 2nd enter box notice some things
# has to be its own assignment, but some use another's assignment (eg. Loan_Length)
##Copy_Box_Example=StringVar()
##Copy_Box_Example=Entry(gui,textvariable=Loan_Length).grid(row=9,column=0)
##call_result=partial(call_result,House_Price,Loan_Length,number3, TESTX,Loan_Length)
##def call_result(n1,n2,n3,testx,copy):
##    num5=(copy.get()) 



## this is in the def, if i need to modify the box to something i want
##    square=int(Home_Price_Local)*int(Loan_Length_Local)
##    #this lower code overrides this, making it 20
##    while square<20:
##        square=square+1
##    Total_Payment_Label.config(text=("grand total is %d" %square))

