import random, openpyxl

#this program simulates WRITING a massive excel sheet, it writes all these random
#values as if it is a vet's office or something.  Can be used to
#show how to modify cells


wb=openpyxl.load_workbook('try.xlsx')
sheet=wb.get_sheet_by_name("Sheet1")

for rowNum in range (2,1000):
    animal=random.choice( ['Bird', 'Dog', 'Cat'] )
    dog_weight=random.randint(10,100) #re-assigns a new weight every time here
    cat_weight=random.randint(5,25)
    bird_weight=random.randint(1,3)
    age=random.randint(1,15)
    adict={"Dog":dog_weight, "Cat":cat_weight,"Bird":bird_weight} #note a changing dictionary here for each loop

    sheet.cell(row=1,column=1).value= "Animal"
    sheet.cell(row=1,column=2).value= "Weight"
    sheet.cell(row=1,column=3).value= "Age"
    
    if animal in adict:
        sheet.cell(row=rowNum,column=1).value= animal
        sheet.cell(row=rowNum,column=2).value= adict[animal]
        sheet.cell(row=rowNum,column=3).value= age        


wb.save("exampleCreation.xlsx")
