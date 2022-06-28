from tkinter import *
from tkinter import messagebox
import string

def error():
  messagebox.showerror('Error', 'Error')

def check():
    
    txt2= ent2.get("1.0",'end').replace("\n", "")
    txt2=txt2.replace(" ", "")
    for i in range(len(txt2)):
      if txt2[i] == '$':

        try:
          x=txt2[i+1]
        except:
          x=''

        if x =='$' or x in string.digits+'.':
              error()
              return False
              
   
    if any(i not in string.digits+'/*-+.$ ' for i in txt2):
     error()
     return False

    else:
      txt= ent.get()
      txt=txt.replace(" ", "")
      if not any(i not in string.digits+'. ' for i in txt):
          
          return txt2
      else:
        error()
        return False
    

                      
def cl():
  validate=check()
  if validate != False:

    txt=ent.get()
    if len(txt)==0:
            txt='1'
    txt2=validate.replace('$','*'+txt)
    result= round(float(eval(txt2)),2)
    ent3.delete(0,"end")
    ent3.insert(0,result)

    
       
   
def cf():
  validate=check()
  if validate != False:

    txt=ent.get()
    if len(txt)==0:
            txt='1'
    txt2=validate.replace('$','*'+txt)
    result= eval(txt2)
    result=round(result/float(txt),2)
    ent3.delete(0,"end")
    ent3.insert(0,result)
  
w=Tk()
f=Frame(w)
f.pack()

label=Label(f,text="Currency Calculator")
label.grid(column=0,row=0) 

label2=Label(f,text="result= ")
label2.grid(column=0,row=3)  

label3=Label(f,text="Exchange Rate:")
label3.grid(column=0,row=1)

label4=Label(f,text="calculate here: ")
label4.grid(column=0,row=2)

ent=Entry(f)
ent.grid(column=1,row=1)

ent2=Text(f,width=17,height=7)
ent2.grid(column=1,row=2)

ent3=Entry(f)
ent3.grid(column=1,row=3) 

btn=Button(f,text="Convert to local currency",command=cl)
btn.grid(column=0,row=4)

btn2=Button(f,text="Convert to foreign currency",command=cf)
btn2.grid(column=1,row=4)

w.mainloop()

