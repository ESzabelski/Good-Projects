
import pyperclip, re



phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})             #next 3
    (\s|-|\.)
    (\d{4})             #last four
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)



emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+   
    @
    [a-zA-Z0-9.-]+ 
    (\. [a-zA-Z] {2,4})
    )''', re.VERBOSE)


website_Regex=re.compile(r'''(
    (http:// | https://)
    (www\.)?
    ([a-zA-Z0-9])+
    (\.[a-zA-Z0-9])?    #second website like smile.amazon
    (\.[A-Za-z]{2,4})
    
    )''', re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum= '-'.join([groups[1],groups[3],groups[5]]) #group 1 is first group for area, 3 and 5 are AFTER dash
    if groups[8] != '':  #8 is after and nested after the .ext part
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in website_Regex.findall(text):
    matches.append(groups[0])

#copy results to clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard")
    print('\n'.join(matches))

else:
    print("no phone or email addresses found.")

    
