import tkinter as tk
import os
from tkinter import messagebox
import pdb

creds = 'admin.txt'
proj = 'projects.txt'
global key
global key2
global key3

LARGE_FONT = ("Verdana",22)

def Details(p):
	with open(key3, 'a') as f:
		f.write(p)
		f.write('|')
		f.close()
	return

def Assign(pop):
	global key3
	key3 = pop+'.txt'
	return

def CheckLogin():
	global key
	with open(creds) as f:
		for line in f:
			if nameEL.get() in line:
				matchedLine = line
				l = matchedLine.split('|')
				uname=l[0]
				pword=l[1].rstrip()
				if nameEL.get() == uname and pwordEL.get() == pword:
					key=uname
					logged()
				elif pwordEL.get() != pword:
					messagebox.showinfo("Oops!", "Invalid Name or Password")

def logged():
	done.destroy()
	log1 = SQA2()

def FSSignup():
	with open(creds, 'a') as f:
		f.write(nameE.get())
		f.write('|')
		f.write(pwordE.get())
		f.write('\n')
		f.close()
		messagebox.showinfo("Success", "Profile Created")
		return

def Creation():
	with open(proj, 'a') as f:
		f.write(nameP.get())
		f.write('|')
		f.write(key)
		f.write('|')
		f.write(numbP.get())
		f.write('\n')
		f.close()
		w=nameP.get()+'.txt'
		with open(w,'w+') as a:
			a.close
		messagebox.showinfo("Success", "Project Test Created")

class SQA2(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "SQA")
		tk.Tk.wm_geometry(self, "700x550")

		box = tk.Frame(self)
		box.pack(expand=True)
		box.grid_rowconfigure(0, weight=1)
		box.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Testlog, Adlog, Testchos, Adchos, Quest, Adops, Results, Create, Testing):
			frame = F(box, self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(Adops)

	def show_frame(self, boxes):
		frame = self.frames[boxes]
		frame.tkraise()

class SQA(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "SQA")
		tk.Tk.wm_geometry(self, "700x550")

		box = tk.Frame(self)
		box.pack(expand=True)
		box.grid_rowconfigure(0, weight=1)
		box.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Adlog, Testchos, Adchos, Quest, Adops,Testing, Create,  Testlog, Results):
			frame = F(box, self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self, boxes):
		frame = self.frames[boxes]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Login As\n", font=LARGE_FONT)
		label.grid(row=5, column=1, sticky="w")
		button1 = tk.Button(self, text="Admin", command=lambda:controller.show_frame(Adlog))
		button1.grid(row=10, column=0, sticky="w")
		button2 = tk.Button(self, text="Tester", command=lambda:controller.show_frame(Testchos))
		button2.grid(row=10, column=2, sticky="w")

class Adlog(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		global pwordE 
		global nameE
		intruction = tk.Label(self, text='Please Enter new Credidentials\n')
		intruction.grid(row=0, column=0, sticky="E")
		nameL = tk.Label(self, text='New Username: ')
		pwordL = tk.Label(self, text='New Password: ')
		nameL.grid(row=1, column=0, sticky="W")
		pwordL.grid(row=2, column=0, sticky="W")
		nameE = tk.Entry(self)
		pwordE = tk.Entry(self, show='*')
		nameE.grid(row=1, column=1)
		pwordE.grid(row=2, column=1)
		signupButton = tk.Button(self, text='Signup', command=FSSignup)
		signupButton.grid(columnspan=2, sticky="W")

		global nameEL
		global pwordEL
		intruction = tk.Label(self, text='Please Login\n')
		intruction.grid(sticky="E")
		nameL = tk.Label(self, text='Username: ')
		pwordL = tk.Label(self, text='Password: ')
		nameL.grid(row=5, column=0, sticky="W")
		pwordL.grid(row=6, column=0, sticky="W")
		nameEL = tk.Entry(self)
		pwordEL = tk.Entry(self, show='*')
		nameEL.grid(row=5, column=1)
		pwordEL.grid(row=6, column=1)
		loginB = tk.Button(self, text='Login', command=CheckLogin)
		loginB.grid(columnspan=2, sticky="W")
		
class Create(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		global nameP
		global numbP
		intruction = tk.Label(self, text='Please Enter the Project Details\n')
		intruction.grid(row=0, column=0, sticky="E")
		nameL = tk.Label(self, text='New Project Name: ')
		projn = tk.Label(self, text='New Project Number: ')
		nameL.grid(row=1, column=0, sticky="W")
		projn.grid(row=2, column=0, sticky="W")
		nameP = tk.Entry(self)
		numbP = tk.Entry(self)
		nameP.grid(row=1, column=1)
		numbP.grid(row=2, column=1)
		signupButton = tk.Button(self, text='Create', command=Creation)
		signupButton.grid(columnspan=2, sticky="W")
		backButton = tk.Button(self, text='Back', command=lambda:controller.show_frame(Adops))
		backButton.grid(columnspan=2, sticky="W")

class Testchos(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		i=0
		with open(proj) as f:
			for line in f:
				txt=line.split('|')
				i+=1
				tk.Label(self,text=txt[0],bg='blue',fg='white').grid(row=i, column=1)
				tk.Button(self,text="Accept",command=Assign(txt[0])).grid(row=i, column =3)
		submit=tk.Button(self, text='Go', command=lambda:controller.show_frame(Testlog))
		submit.grid(row=15,column=1)
		backButton = tk.Button(self, text='Back', command=lambda:controller.show_frame(StartPage))
		backButton.grid(row=15,column=3)

class Adchos(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		i=0
		with open(proj) as f:
			for line in f:
				txt=line.split('|')
				i+=1
				tk.Label(self,text=txt[0],bg='blue',fg='white').grid(row=i, column=1)
				tk.Button(self,text="Accept",command=Assign(txt[0])).grid(row=i, column =3)
		submit=tk.Button(self, text='View Results', command=lambda:controller.show_frame(Results))
		submit.grid(row=15,column=1)
		backButton = tk.Button(self, text='Back', command=lambda:controller.show_frame(Adops))
		backButton.grid(row=15,column=3)

class Testlog(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		global nameT
		intruction = tk.Label(self, text='Please Enter your Details\n')
		intruction.grid(row=0, column=0, sticky="E")
		nameL = tk.Label(self, text='Name: ')
		nameL.grid(row=1, column=0, sticky="W")
		nameT = tk.Entry(self)
		nameT.grid(row=1, column=1)
		signupButton1 = tk.Button(self, text='Test', command=lambda:[Details(nameT.get()),controller.show_frame(Testing)])
		signupButton1.grid(columnspan=2, sticky="W")

class Quest(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		tk.Label(self, text="Answer the following queries with a rating from 1 to 5").grid(row=0,columnspan=2)
		i=1
		self.hen=[]
		global h
		with open('questionnaire.txt','r') as f:
			for line in f:
				tk.Label(self,text=line.rstrip()).grid(row=(i*2))
				h=tk.Entry(self)
				h.grid(row=(i*2)+1, column=0)
				self.hen.append(h)
				i+=1
			f.close
		tk.Button(self,text='Finish',command=lambda:[self.writer(i-1),self.seperator(),controller.show_frame(StartPage)]).grid()

	def writer(self,l):
		i=0
		with open(key3,'a') as f:
			for i in range(l):
				f.write(self.hen[i].get())
				f.write('#')
			f.close()

	def seperator(self):
		with open(key3,'a') as f:
			f.write('\n')
			f.close()
	
class Testing(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		tk.Label(self, text="Follow the appropriate description of test parameter and enter the final no. of TC's performed, TC's passes and TC's failed").grid(row=0,columnspan=4)
		i=1
		self.nen=[]
		self.pen=[]
		self.den=[]
		global n
		global p
		global d
		with open('tests.txt','r') as f:
			for line in f:
				txt=line.rstrip().split('|')
				tk.Label(self,text=txt[0]+'\n'+txt[1]).grid(row=(i*3))
				tk.Label(self,text="No of test cases: ").grid(row=(i*3)+1,column=0)
				n=tk.Entry(self)
				n.grid(row=(i*3)+2,column=0)
				self.nen.append(n)
				tk.Label(self,text="No of passed cases: ").grid(row=(i*3)+1,column=1)
				p=tk.Entry(self)
				p.grid(row=(i*3)+2,column=1)
				self.pen.append(p)
				tk.Label(self, text="No of failed cases: ").grid(row=(i*3)+1,column=2)
				d=tk.Entry(self)
				d.grid(row=(i*3)+2,column=2)
				self.den.append(d)
				i+=1
			f.close()
		tk.Button(self,text='Next',command=lambda:[self.writer(i-1),self.seperator(),controller.show_frame(Quest)]).grid()
	
	def writer(self,l):
		with open(key3,'a') as f:
			i=0
			for i in range(l):
				f.write(self.nen[i].get())
				f.write('-')
				f.write(self.pen[i].get())
				f.write('-')
				f.write(self.den[i].get())
				f.write('#')
			f.close()

	def seperator(self):
		with open(key3,'a') as f:
			f.write('|')
			f.close()

class Adops(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		button1 = tk.Button(self, text='Check response to Project Tests', command=lambda:controller.show_frame(Adchos))
		button2 = tk.Button(self, text='Create a new Project Test', command=lambda:controller.show_frame(Create))
		button3 = tk.Button(self, text='Logout', command=lambda:controller.show_frame(StartPage))
		button1.grid(columnspan=5, sticky="nsew")
		button2.grid(columnspan=5, sticky="nsew")
		button3.grid(columnspan=5, sticky="nsew")

class Results(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		tk.Label(self,text='The Results of the testing phase are as follows:').grid(row=0,columnspan=3,sticky='w')
		with open(key3,'r') as f:
			a=b=c=a1=b1=c1=d1=d2=d3=d4=i=0		#MAKE THIS BETTER!!!!!
			for line in f:
				i+=1
				txt=line.split('|')
				tes=txt[1].rstrip().split('#')
				a+=int(tes[0].split('-')[0])
				b+=int(tes[1].split('-')[0])
				c+=int(tes[2].split('-')[0])
				a1+=int(tes[0].split('-')[1])
				b1+=int(tes[1].split('-')[1])
				c1+=int(tes[2].split('-')[1])
				que=txt[2].rstrip().split('#')
				d1+=int(que[0])
				d2+=int(que[1])
				d3+=int(que[2])
				d4+=int(que[3])
			if(i!=0):
				tk.Label(self, text='Test 1:\nTotal Tests:'+str(a)+'\nTC Passed:'+str(a1)+'\nTC Fail:'+str(a-a1)).grid(row=1,column=0,sticky='w')
				tk.Label(self, text='Test 2:\nTotal Tests:'+str(b)+'\nTC Passed:'+str(b1)+'\nTC Fail:'+str(b-b1)).grid(row=1,column=1,sticky='w')
				tk.Label(self, text='Test 3:\nTotal Tests:'+str(c)+'\nTC Passed:'+str(c1)+'\nTC Fail:'+str(c-c1)).grid(row=1,column=2,sticky='w')
				tk.Label(self, text='Reviews Averages:\nQ1:'+str(d1/i)+'\nQ2:'+str(d2/i)+'\nQ3:'+str(d3/i)+'\nQ4:'+str(d4/i)).grid(row=6,column=1,sticky='w')
		f.close()
		button3 = tk.Button(self, text='Back', command=lambda:controller.show_frame(Adops))
		button3.grid(columnspan=5, sticky="nsew")

done = SQA()
done.mainloop()