import smtplib
import random

random.seed()

attendees = ({'name':'John','email':'john@email.com'},\
	{'name':'Mary','email':'mary@email.com'},\
	{'name':'Ethel','email':'ethel@email.com'},\
	{'name':'Fred','email':'fred@email.com'})


# Create an ordered list
order=[None]*len(attendees)
for i in range(0,len(attendees)):
	order[i]=i
 
# Randomize the order 
for i in range (0,len(attendees)-1):
	sorter = random.randint(0,len(attendees)-1)
	temp = order[i]
	order[i]= order[sorter]
	order[sorter] = temp 


user = 'someaccount@gmail.com' # Gmail account from which to send emails to the attendees 
login = 'yourPassword' # Password of said account

smtpObj=smtplib.SMTP('smtp.gmail.com', 587) 
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user,login)

for i in range(0,len(attendees)):
	giver = attendees[order[i]]['name']
	try:
		receiver = attendees[order[i+1]]['name']
	except IndexError:
		receiver = attendees[order[i+1-len(attendees)]]['name']
	string = 'Subject: Christmas exchange\nHey '+giver+',\nFor this Christmas, you will give a gift to:\n\n\n\n\n'+receiver+'\n\n\n\n\nMerry Christmas!'
	string = string.encode('utf-8')
	smtpObj.sendmail(user,attendees[order[i]]['email'], string )

print('All done. Enjoy your presents!')

smtpObj.quit()