from tkinter import *
import csv
import random 

def home():
	r= Tk()

	def new_entry():
		
		Tk.destroy(r)

		root_n =Tk()

		def home_code_n():
			root_n.destroy()
			home()

		def get_string(entry):
			x=entry.get()
			return str(x).upper()

		def get_int(entry):
			x=entry.get()
			return int(x)

		## "" LAYOUT OF THE WINDOW FOR NEW ENTRY ""	
		H_LABEL = Label(text="NEW RECORD'S ENTRY",width=30,height=2,pady=10,font=20)
		H_LABEL.grid(row=0,column=0)
		
		ln=Label(text='Name:',width=15,height=2,pady=5,font=15)
		ln.grid(row=1,column=0)
		
		Name=Entry(root_n)
		Name.grid(row=1,column=1)
		Name.focus()
		Name.bind('<Return>',lambda funct1:Contact.focus())


		lc=Label(text='Contact:',width=15,height=2,pady=5,font=15)
		lc.grid(row=2,column=0)

		Contact=Entry(root_n)
		Contact.grid(row=2,column=1)
		Contact.focus()
		Contact.bind('<Return>',lambda funct1:Address.focus())


		la=Label(text='Address:',width=15,height=2,pady=5,font=15)
		la.grid(row=3,column=0)
		
		Address=Entry(root_n)
		Address.grid(row=3,column=1)
		Address.focus()
		Address.bind('<Return>',lambda funct1:Pin.focus())

		lp=Label(text='Pin:',width=15,height=2,pady=5,font=15)
		lp.grid(row=4,column=0)
		
		Pin	=Entry(root_n)
		Pin.grid(row=4,column=1)


		def submit():
			file=open('Database.csv','a',newline='')
			wrtr = csv.writer(file)
			data=[get_string(Name),get_int(Contact),get_string(Address),get_int(Pin)]
			wrtr.writerow(data)
			file.close()

			Name.delete(first=0,last=30)
			Contact.delete(first=0,last=30)
			Address.delete(first=0,last=30)
			Pin.delete(first=0,last=30)

		submit=Button(text='Submit:',width=20,height=1,pady=5,font=10,command=submit)
		submit.grid(row=5,column=0)

		HOME=Button(text='Home',width=20,height=1,pady=5,font=10,command=home_code_n)
		HOME.grid(row=5,column=1)

		root_n.mainloop()

	def search():

		Tk.destroy(r)

		root_s=Tk()

		def home_code_s():
			root_s.destroy()
			home()


		Head = Label(text='SEARCH MEMO !!',width=40,height=1,pady=3,font=10)
		Head.grid(row=0,column=0)

		Title= Label(text='Name Of The recepient',width=40,height=1,pady=3,font=8)
		Title.grid(row=1,column=0)

		Input=Entry(root_s)
		Input.grid(row=2,column=0)

		def di():
			user_search = (Input.get()).upper()

			st=["Not Found"]
			with open('Database.csv','r',newline='') as file:
					read=csv.reader(file)
					for i in read:
						if i[0]==user_search:
							st=i
			file.close()

			d1=Label(text=['Name','Contact','Address','Pin'],width=50,height=1,pady=2,font=8)
			d1.grid(row=4,column=0)

			d2=Label(text=st,width=50,height=1,pady=2,font=8)
			d2.grid(row=5,column=0)


		s=Button(text='SEARCH',width=15,height=1,pady=3,font=10,command=di)
		s.grid(row=6,column=0)

		HOME=Button(text='Home',width=20,height=1,pady=5,font=10,command=home_code_s)
		HOME.grid(row=6,column=1)

		root_s.mainloop()



	def display():
		Tk.destroy(r)

		root_d = Tk()

		def home_code_d():
			root_d.destroy()
			home()
		
		main_title = Label(text="DISPLAY MEMO !!!!",width=20,height=1,pady=3,font=15)
		main_title.grid(row=0,column=0)

		HOME=Button(text='Home',width=20,height=1,pady=5,font=10,command=home_code_d)
		HOME.grid(row=0,column=1)
		
		head_n=Label(text='Name',width=15,height=1,pady=3,font=10)
		head_n.grid(row=1,column=0)

		head_c=Label(text='Contact',width=15,height=1,pady=3,font=10)
		head_c.grid(row=1,column=1)

		head_a=Label(text='Address',width=15,height=1,pady=3,font=10)
		head_a.grid(row=1,column=2)

		head_p=Label(text='Pin',width=15,height=1,pady=3,font=10)
		head_p.grid(row=1,column=3)


		with open('Database.csv','r',newline='') as file:
			obj=csv.reader(file)
			n=2
			for rows in obj:
					d1=Label(text=rows[0],width=15,height=1,pady=3,font=8)
					d1.grid(row=n,column=0)

					d2=Label(text=rows[1],width=15,height=1,pady=3,font=8)
					d2.grid(row=n,column=1)

					d3=Label(text=rows[2],width=15,height=1,pady=3,font=8)
					d3.grid(row=n,column=2)

					d4=Label(text=rows[3],width=15,height=1,pady=3,font=8)
					d4.grid(row=n,column=3)
					n+=1
			file.close()

		root_d.mainloop()


	def delete():
		r.destroy()
		root_del =Tk()

		def home_code_del():
			root_del.destroy()
			home()
		
		main_head =Label(text="DELETING MEMO !!!!",width=20,height=1,pady=10,font=15)
		main_head.grid(row=0,column=0)

		Instr =Label(text='Name of the recepient to be deleted',width=30,height=1,pady=5,font=10)
		Instr.grid(row=1,column=0)

		new_rec=[]

		Choice=Entry(root_del)
		Choice.grid(row=1,column=1)

		def onclick():
			target=(Choice.get()).upper()

			check="Record not found"
			with open('Database.csv','r') as file:
					entries=csv.reader(file)
					for row in entries:
						if row[0]!=target:
							new_rec.append(row)
							check="Deletion Done !"
						
			file.close()
			with open('Database.csv','w',newline='') as nf_obj:

					write = csv.writer(nf_obj)
					write.writerows(new_rec)
					print(new_rec)

					nf_obj.close()

			done = Label(root_del,text=check,width=15,height=1,pady=10,font=10)
			done.grid(row=3,column=0)




		Delete=Button(text='Delete',width=10,height=1,pady=5,font=10,command=onclick)
		Delete.grid(row=2,column=0)

		HOME=Button(text='Home',width=20,height=1,pady=5,font=10,command=home_code_del)
		HOME.grid(row=2,column=1) #adi

		root_del.mainloop()


	b1 = Button(r,text='New Records Entry',width=15,height=1,pady=5,font=10,command=new_entry)
	b2 = Button(text='Delete Records',width=15,height=1,pady=5,font=10,command=delete)
	b3 = Button(text='Display All',width=15,height=1,pady=5,font=10,command=display)
	b4 = Button(text='Search Records',width=15,height=1,pady=5,font=10,command=search)
	b5 = Button(text='Exit Program',width=15,height=1,pady=5,font=10,command=r.quit)

	HEAD_LABEL = Label(text='DATABASE MANAGEMENT',width=30,height=2,pady=10,font=20)
	HEAD_LABEL.grid(row=0,column=0)

	b1.grid(row=1,column=0)
	b2.grid(row=2,column=0)
	b3.grid(row=3,column=0)
	b4.grid(row=4,column=0)
	b5.grid(row=5,column=0)


	general_instru=Label(text='General Instruction:: \nYou can enter the details in any case \nthe entry will always be \nsaved in uppercase')
	general_instru.grid(row=6,column=0,pady=5)

	r.mainloop()

home()
