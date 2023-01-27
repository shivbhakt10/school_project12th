from tkinter import *
from tkinter import messagebox
import os
import shutil

mainroot=Tk()
          
mainroot.geometry('870x582')
mainroot.configure(bg='black')
mainroot.minsize(width=870,height=582)
mainroot.maxsize(width=870,height=582)
mainroot.title('Practical Manager') 

def mainscreen():
          l=Label(text="Practical \n \tManager",font="cursive 30 bold italic",fg='orange',bg='black')
          l.place(x=240,y=20)
          b11=Button(text="Class - 11",font="cursive 20 bold italic",fg='orange',bg='black',command=lambda:[secondscreen11(),forgetmc()])
          b12=Button(text="Class - 12",font="cursive 20 bold italic",fg='orange',bg='black',command=lambda:[secondscreen12(),forgetmc()])
          b11.place(x=340,y=300)
          b12.place(x=340,y=400)
          def forgetmc():
                    l.place_forget()
                    b11.place_forget()
                    b12.place_forget()

def secondscreen11():
          bq=Button(text="Questions",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),questionscreen11()])
          ba=Button(text='Practical\'s',font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),practicalscreen11()])
          bq.place(x=370,y=200)
          ba.place(x=370,y=300)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),mainscreen()])
          bb.place(x=755,y=0)
          def forgetspc():
                    bq.place_forget()
                    ba.place_forget()
                    bb.place_forget()

def secondscreen12():
          bq=Button(text="Questions",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),questionscreen12()])
          ba=Button(text='Practical\'s',font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),practicalscreen12()])
          bq.place(x=370,y=200)
          ba.place(x=370,y=300)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgetspc(),mainscreen()])
          bb.place(x=755,y=0)
          def forgetspc():
                    bq.place_forget()
                    ba.place_forget()
                    bb.place_forget()

def questionscreen11():
          l=Label(text='Question\'s',font="cursive 30 bold italic",fg='orange',bg='black')
          l.place(x=300,y=20)
          ba=Button(text="Add",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),addq11()])
          bu=Button(text="Update",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),uq11()])
          bc=Button(text="See",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),seeq11()])
          bd=Button(text="Delete",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),dq11()])
          ba.place(x=180,y=150)
          bu.place(x=280,y=250)
          bc.place(x=430,y=350)
          bd.place(x=520,y=450)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),secondscreen11()])
          bb.place(x=755,y=0)
          
          def forgotques():
                    l.place_forget()
                    ba.place_forget()
                    bu.place_forget()
                    bc.place_forget()
                    bd.place_forget()
                    bb.place_forget()
def questionscreen12():
          l=Label(text='Question\'s',font="cursive 30 bold italic",fg='orange',bg='black')
          l.place(x=300,y=20)
          ba=Button(text="Add",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),addq12()])
          bu=Button(text="Update",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),uq12()])
          bc=Button(text="See",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),seeq12()])
          bd=Button(text="Delete",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),dq12()])
          ba.place(x=180,y=150)
          bu.place(x=280,y=250)
          bc.place(x=430,y=350)
          bd.place(x=520,y=450)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),secondscreen12()])
          bb.place(x=755,y=0)
          
          def forgotques():
                    l.place_forget()
                    ba.place_forget()
                    bu.place_forget()
                    bc.place_forget()
                    bd.place_forget()
                    bb.place_forget()
                    
def practicalscreen11():
          l=Label(text='Practical\'s',font="cursive 30 bold italic",fg='orange',bg='black')
          l.place(x=300,y=20)
          bu=Button(text="Update",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),up11()])          
          ba=Button(text="Add",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),addp11()])
          bc=Button(text="See",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),sp11()])
          bd=Button(text="Delete",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),dp11()])
          ba.place(x=180,y=150)
          bu.place(x=280,y=250)
          bc.place(x=430,y=350)
          bd.place(x=520,y=450)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),secondscreen11()])
          bb.place(x=755,y=0)
          def forgotques():
                    l.place_forget()
                    ba.place_forget()
                    bu.place_forget()
                    bc.place_forget()
                    bd.place_forget()
                    bb.place_forget()
                    
def practicalscreen12():
          l=Label(text='Practical\'s',font="cursive 30 bold italic",fg='orange',bg='black')
          l.place(x=300,y=20)
          bu=Button(text="Update",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),up12()])          
          ba=Button(text="Add",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),addp12()])
          bc=Button(text="See",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),sp12()])
          bd=Button(text="Delete",font="cursive 25 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),dp12()])
          ba.place(x=180,y=150)
          bu.place(x=280,y=250)
          bc.place(x=430,y=350)
          bd.place(x=520,y=450)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[forgotques(),secondscreen12()])
          bb.place(x=755,y=0)
          def forgotques():
                    l.place_forget()
                    ba.place_forget()
                    bu.place_forget()
                    bc.place_forget()
                    bd.place_forget()
                    bb.place_forget()                 


def addq11():
          l=Label(text='Question :',font="cursive 20 bold italic",fg='orange',bg='black')
          l.place(x=10,y=65)
          t=Text(width=50,height=10,font="cursive 17 bold")
          t.place(x=160,y=80)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[faddq11(),questionscreen11()])
          bb.place(x=755,y=0)
          bo=Button(text=" Submit ",font='cursive 20 bold italic',bg='black',fg='light blue',command=lambda:[addingq()])
          bo.place(x=350,y=420)
          
          def addingq():
                    try:
                              ques=t.get(1.0, "end-1c")
                              os.mkdir(f'logs//11//practicals//{ques}')
                              with open(f'logs//11//practicals//{ques}//students.txt','w'):
                                        pass
                              with open('logs//11//0u357i0ns//0u357i0n.txt','a') as f:
                                                            f.write(ques+'\n')
                              t.delete(1.0,"end")
                              
                              messagebox.showinfo('Submittion👍',"Question added successfully ..!!!")
                                        
                              
                    except:
                              messagebox.showerror('Error 101☠','Someting went wrong !   \n[OR]\n Question already exist..!')
          def faddq11():
                    l.place_forget()
                    t.place_forget()
                    bb.place_forget()
                    bo.place_forget()
          
def addq12():
          l=Label(text='Question :',font="cursive 20 bold italic",fg='orange',bg='black')
          l.place(x=10,y=65)
          t=Text(width=50,height=10,font="cursive 17 bold")
          t.place(x=160,y=80)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[faddq12(),questionscreen12()])
          bb.place(x=755,y=0)
          bo=Button(text=" Submit ",font='cursive 20 bold italic',bg='black',fg='light blue',command=lambda:[addingq()])
          bo.place(x=350,y=420)
          
          def addingq():
                    try:
                              ques=t.get(1.0, "end-1c")
                              os.mkdir(f'logs//12//practicals//{ques}')
                              with open(f'logs//12//practicals//{ques}//students.txt','w'):
                                        pass
                              with open('logs//12//0u357i0ns//0u357i0n.txt','a') as f:
                                        f.write(ques+'\n')
                              
                              t.delete(1.0,"end")
                              messagebox.showinfo('Submittion👍',"Question added successfully ..!!!")
                    except:
                              messagebox.showerror('Error 101☠','Someting went wrong !  \n[OR]\n Question already exist..!')
          def faddq12():
                    l.place_forget()
                    t.place_forget()
                    bb.place_forget()
                    bo.place_forget()
          
          
def seeq11():
          scrollbar = Scrollbar(mainroot)
          scrollbar.pack(side=RIGHT, fill=Y)
          text = Text(mainroot, yscrollcommand = scrollbar.set,width=54,height=20,font="cursive 17 bold")
          text.place(x=20,y=20)
          scrollbar.config(command=text.yview)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fseeq11(),questionscreen11()])
          bb.place(x=735,y=0)
          def seeingq():
                    try:
                              with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                                        a=f.readlines()
                                        for i in range(1,len(a)+1):
                                                  text.insert(END,f'Q-{i}. {a[i-1]}')
                                                  
                    except:
                              messagebox.showerror('Eroor 102','Something went wrong ..!!')
          seeingq()
          def fseeq11():
                    text.place_forget()
                    bb.place_forget()
                    scrollbar.pack_forget()
          
def seeq12():
          scrollbar = Scrollbar(mainroot)
          scrollbar.pack(side=RIGHT, fill=Y)
          text = Text(mainroot, yscrollcommand = scrollbar.set,width=54,height=20,font="cursive 17 bold")
          text.place(x=20,y=20)
          scrollbar.config(command=text.yview)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fseeq12(),questionscreen12()])
          bb.place(x=735,y=0)
          def seeingq():
                    try:
                              with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                                        a=f.readlines()
                                        for i in range(1,len(a)+1):
                                                  text.insert(END,f'Q-{i}. {a[i-1]}')
                    except:
                              messagebox.showerror('Eroor 102','Something went wrong ..!!')
          seeingq()
          def fseeq12():
                    text.place_forget()
                    bb.place_forget()
                    scrollbar.pack_forget()

def uq11():
          l=Label(text='New Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          l.place(x=5,y=205)
          tt=Text(width=45,height=10,font="cursive 17 bold")
          tt.place(x=190,y=210)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fuq11(),questionscreen11()])
          bb.place(x=755,y=0)
          bo=Button(text=" UPDATE ",font='cursive 20 bold italic',bg='black',fg='light blue',command=lambda:[updating()])
          bo.place(x=350,y=500)
          tl=Label(text='Select Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          tl.place(x=5,y=20)
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')                 
                              
          def p(*args):
                    global question
                    question=t.get()
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=50)
          ot.place(x=210,y=20)
          
          def updating():
                    try:
                              newq=tt.get(1.0, "end-1c")
                              global question
                              oqi=questions.index(question)
                              questions[oqi] = newq+'\n'
                              
                              question=question.replace('\n','')
                              os.rename(f'logs//11//practicals//{question}',f'logs//11//practicals//{newq}')
                              with open('logs//11//0u357i0ns//0u357i0n.txt','w') as f:
                                        for i in questions:
                                                  f.write(i)
                              
                              messagebox.showinfo('update','Updated successfully ...!!')
                              
                              
                              
                    except:
                              messagebox.showerror('Eroor 101','Something went wrong ..!!')
                    
          def fuq11():
                    l.place_forget()
                    tt.place_forget()
                    bb.place_forget()
                    bo.place_forget()
                    tl.place_forget()
                    ot.place_forget()
          
          
def uq12():
          l=Label(text='New Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          l.place(x=5,y=205)
          tt=Text(width=45,height=10,font="cursive 17 bold")
          tt.place(x=190,y=210)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fuq12(),questionscreen12()])
          bb.place(x=755,y=0)
          bo=Button(text=" UPDATE ",font='cursive 20 bold italic',bg='black',fg='light blue',command=lambda:[updating()])
          bo.place(x=350,y=500)
          tl=Label(text='Select Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          tl.place(x=5,y=20)
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                    questions=f.readlines()
                    if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
                              
          def p(*args):
                    global question
                    question=t.get()
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=50)
          ot.place(x=210,y=20)
          
          def updating():
                    try:
                              newq=tt.get(1.0, "end-1c")
                              global question
                              oqi=questions.index(question)
                              questions[oqi] = newq+'\n'
                              question=question.replace('\n','')
                              os.rename(f'logs//12//practicals//{question}',f'logs//12//practicals//{newq}')
                              with open('logs//12//0u357i0ns//0u357i0n.txt','w') as f:
                                        for i in questions:
                                                  f.write(i)
                              
                              messagebox.showinfo('update','Updated successfully ...!!')
                    except:
                              messagebox.showerror('Eroor 102','Something went wrong ..!!')
                    
          def fuq12():
                    l.place_forget()
                    tt.place_forget()
                    bb.place_forget()
                    bo.place_forget()
                    tl.place_forget()
                    ot.place_forget()
      
def dq11():
          l=Label(text='Delete :',font="cursive 20 bold italic",fg='orange',bg='black')
          l.place(x=20,y=120)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fdq11(),questionscreen11()])
          bb.place(x=755,y=0)
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                    questions=f.readlines()
                    if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          def p(*args):
                    question=t.get()
                    questions.remove(question)
                    with open('logs//11//0u357i0ns//0u357i0n.txt','w') as f:
                          for i in questions:
                              f.write(i)
                    question=question.replace('\n','')
                    shutil.rmtree(f'logs//11//practicals//{question}')
                    messagebox.showinfo('Info','Question Deleted')
                    
          
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=100)
          ot.place(x=170,y=120)
          
          def fdq11():
                    l.place_forget()
                    bb.place_forget()
                    ot.place_forget()
                    
def dq12():
          l=Label(text='Delete :',font="cursive 20 bold italic",fg='orange',bg='black')
          l.place(x=20,y=120)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fdq12(),questionscreen12()])
          bb.place(x=755,y=0)
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                    questions=f.readlines()
                    if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          def p(*args):
                    question=t.get()
                    questions.remove(question)
                    with open('logs//12//0u357i0ns//0u357i0n.txt','w') as f:
                          for i in questions:
                              f.write(i)
                    question=question.replace('\n','')
                    shutil.rmtree(f'logs//12//practicals//{question}')
                    
                    messagebox.showinfo('Info','Question Deleted')
                    
                  
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=100)
          ot.place(x=170,y=120)
          
          def fdq12():
                    l.place_forget()
                    bb.place_forget()
                    ot.place_forget()

def addp11():
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          def p(*args):
                    global question
                    question=t.get()
          def addp():
                    try:
                              name=tn.get(1.0, "end-1c")
                              code=tc.get(1.0, "end-1c")
                              global question
                              question=question.replace('\n','')
                              with open(f'logs//11//practicals//{question}//students.txt','r') as f:
                                        a=f.readlines()
                                        if name not in a:
                                                  with open(f'logs//11//practicals//{question}//students.txt','a') as f:
                                                            f.write(name+'\n')
                                                  with open(f'logs//11//practicals//{question}//{name}.txt','w') as f:
                                                            f.write(code)
                                                  messagebox.showinfo('Info','Code added successfully ...!!')
                                        else:
                                              messagebox.showerror('error','File already exits')     
                    except:
                              messagebox.showerror('error','something went wrong') 
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=5)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[faddp11(),practicalscreen11()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=80)
          tn=Text(width=20,height=1,font="cursive 17 bold")
          tn.place(x=250,y=80)
          cl=Label(text='Code : :',font="cursive 18 bold italic",fg='orange',bg='black')
          cl.place(x=20,y=150)
          tc=Text(width=57,height=13,font="cursive 17 bold")
          tc.place(x=100,y=150)
          ao=Button(text=' Submit ',font="cursive 18 bold italic",fg='light blue',bg='black',command=addp)
          ao.place(x=300,y=520)
          
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=50)
          ot.place(x=170,y=10)
          
          def faddp11():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    tn.place_forget()
                    cl.place_forget()
                    tc.place_forget()
                    ot.place_forget()
                    ao.place_forget()


def addp12():
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!') 
                                        
          def p(*args):
                    global question
                    question=t.get()
          
          def addp():
                    try:
                              name=tn.get(1.0, "end-1c")
                              code=tc.get(1.0, "end-1c")
                              global question
                              question=question.replace('\n','')
                              with open(f'logs//12//practicals//{question}//students.txt','r') as f:
                                        a=f.readlines()
                                        if name not in a:
                                                  with open(f'logs//12//practicals//{question}//students.txt','a') as f:
                                                            f.write(name+'\n')
                                                  with open(f'logs//12//practicals//{question}//{name}.txt','w') as f:
                                                            f.write(code)
                                                  messagebox.showinfo('Info','Code added successfully ...!!')
                                        else:
                                              messagebox.showerror('error','File already exits')     
                    except:
                              messagebox.showerror('error','something went wrong') 
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=5)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[faddp12(),practicalscreen12()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=80)
          tn=Text(width=20,height=1,font="cursive 17 bold")
          tn.place(x=250,y=80)
          cl=Label(text='Code : :',font="cursive 18 bold italic",fg='orange',bg='black')
          cl.place(x=20,y=150)
          tc=Text(width=57,height=13,font="cursive 17 bold")
          tc.place(x=100,y=150)
          ao=Button(text=' Submit ',font="cursive 18 bold italic",fg='light blue',bg='black',command=addp)
          ao.place(x=300,y=520)
          
          t=StringVar()
          t.set(questions[0])
          ot=OptionMenu(mainroot,t,*questions,command=p)
          ot.config(width=50)
          ot.place(x=170,y=10)
             
          def faddp12():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    tn.place_forget()
                    cl.place_forget()
                    tc.place_forget()
                    ot.place_forget()
                    ao.place_forget()

def up11():
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          def updateingp11():
                    try:
                              code=tc.get(1.0,'end-1c')
                              global sname
                              sname=sname.replace('\n','')
                              with open(f'logs//11//practicals//{question}//{sname}.txt','w') as f:
                                        f.write(code)
                              messagebox.showinfo('info','Code updated successfully ..!!')
                                
                    except:
                               messagebox.showerror('error','something went wrong')
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=5)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fup11(),practicalscreen11()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=80)
          cl=Label(text='New Code :',font="cursive 14 bold italic",fg='orange',bg='black')
          cl.place(x=3,y=150)
          tc=Text(width=55,height=13,font="cursive 17 bold")
          tc.place(x=115,y=150)
          ao=Button(text=' Submit ',font="cursive 18 bold italic",fg='light blue',bg='black',command=updateingp11)
          ao.place(x=300,y=520)
          def pq(*args):
                    global question
                    question=tq.get()
                    
                    question=question.replace('\n','')
                    with open(f'logs//11//practicals//{question}//students.txt','r') as f:
                              global names
                              names=f.readlines()
                              if names == []:
                                        messagebox.showerror('Error','Empty file. NO stident found..!!')
                                        
                    stname()
                    
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=10)
          
          def stname():
          
                  def pn(*args):
                        global sname
                        sname=tn.get()
          
                  tn=StringVar()
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=80)
                                        
          
          def fup11():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    cl.place_forget()
                    tc.place_forget()
                    ao.place_forget()
                    otq.place_forget()
                    otn.place_forget()


def up12():
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
                        
          def updateingp12():
                    try:
                              code=tc.get(1.0,'end-1c')
                              global sname
                              sname = sname.replace('\n','')
                              with open(f'logs//12//practicals//{question}//{sname}.txt','w') as f:
                                        f.write(code)
                              messagebox.showinfo('info','Code updated successfully ..!!')    
                    except:
                              messagebox.showerror('error','something went wrong')
                              
            
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=5)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fup12(),practicalscreen12()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=80)
          cl=Label(text='New Code :',font="cursive 14 bold italic",fg='orange',bg='black')
          cl.place(x=3,y=150)
          tc=Text(width=55,height=13,font="cursive 17 bold")
          tc.place(x=115,y=150)
          ao=Button(text=' Submit ',font="cursive 18 bold italic",fg='light blue',bg='black',command=updateingp12)
          ao.place(x=300,y=520)
          def pq(*args):
                    global question
                    question=tq.get()
                    
                    question=question.replace('\n','')
                    with open(f'logs//12//practicals//{question}//students.txt','r') as f:
                              global names
                              names=f.readlines()
                              if names == []:
                                        messagebox.showerror('Error','Empty file. NO stident found..!!')
                                        
                    stname()
          
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=10)

          def stname():
          
                  def pn(*args):
                        global sname
                        sname=tn.get()
          
                  tn=StringVar()
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=80)
          def fup12():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    cl.place_forget()
                    tc.place_forget()
                    ao.place_forget()
                    otq.place_forget()
                    otn.place_forget()

def dp11():
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          l=Label(text="* Delete *",font="cursive 25 bold italic underline",fg='orange',bg='black')
          l.place(x=250,y=20)
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=150)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fdp11(),practicalscreen11()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=250)
          def pq(*args):
                    global question
                    question=tq.get()
                    question=question.replace('\n','')
                    with open(f'logs//11//practicals//{question}//students.txt','r') as f:
                              global names
                              names=f.readlines()
                              
                              if names == []:
                                        messagebox.showerror('Error','Empty file. NO stident found..!!')
                                        
                    deleting()
          
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=150)
          def deleting():
                  def pn(*args):
                            try:
                                    sname=tn.get()

                                    if sname in names:
                                          names.remove(sname)
                                          with open(f'logs//11//practicals//{question}//students.txt','w') as f:
                                                for i in names:
                                                      f.write(i)
                                          sname=sname.replace('\n','')
                                          os.remove(f'logs//11/practicals//{question}//{sname}.txt')
                                          messagebox.showinfo('done','succesfully deleted ..!!')
                                          
                            except:
                                  messagebox.showerror('error','something went wrong ..!!')

                  tn=StringVar()
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=250)
                  
          def fdp11():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    otq.place_forget()
                    otn.place_forget()
                    l.place_forget()     

def dp12():
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          l=Label(text="* Delete *",font="cursive 25 bold italic underline",fg='orange',bg='black')
          l.place(x=250,y=20)
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=150)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fdp12(),practicalscreen12()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=250)
          def pq(*args):
                    
                    global question
                    question=tq.get()
                    question=question.replace('\n','')
                    with open(f'logs//12//practicals//{question}//students.txt','r') as f:
                              global names
                              names=f.readlines()
                              
                              if names == []:
                                        messagebox.showerror('Error','Empty file. NO stident found..!!')
                                        
                    deleting()
          
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=150)
          def deleting():
                  def pn(*args):
                            try:
                                    sname=tn.get()

                                    if sname in names:
                                          names.remove(sname)
                                          with open(f'logs//12//practicals//{question}//students.txt','w') as f:
                                                for i in names:
                                                      f.write(i)
                                          sname=sname.replace('\n','')
                                          os.remove(f'logs//12/practicals//{question}//{sname}.txt')
                                          messagebox.showinfo('done','succesfully deleted ..!!')
                                          
                            except:
                                  messagebox.showerror('error','something went wrong ..!!')

                  tn=StringVar()
                  
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=250)
          
          def fdp12():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    otq.place_forget()
                    otn.place_forget()
                    l.place_forget()
          
def sp11():
          with open('logs//11//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
          
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=150)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fsp11(),practicalscreen11()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=250)
                 
          def pq(*args):
                        global question
                        question=tq.get()
                        question=question.replace('\n','')
                        with open(f'logs//11//practicals//{question}//students.txt','r') as f:
                                  global names
                                  names=f.readlines()

                                  if names == []:
                                            messagebox.showerror('Error','Empty file. NO stident found..!!')

                        seeing()
          
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=150)
          def seeing():
                  def pn(*args):
                            try:
                                    sname=tn.get()

                                    if sname in names:
                                          sname=sname.replace('\n','')
                                          with open(f'logs//11/practicals//{question}//{sname}.txt','r') as f:
                                                sps11(f.read())
                                          
                                          
                            except:
                                  messagebox.showerror('error','something went wrong ..!!')

                  tn=StringVar()
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=250)
          
          def fsp11():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    otq.place_forget()
                    otn.place_forget()  
                    
          def sps11(texts):
                    fsp11()
                    scrollbar = Scrollbar(mainroot)
                    scrollbar.pack(side=RIGHT, fill=Y)
                    text = Text(mainroot, yscrollcommand = scrollbar.set,width=54,height=20,font="cursive 17 bold")
                    text.place(x=20,y=20)
                    scrollbar.config(command=text.yview)
                    bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fseeq11(),sp11()])
                    bb.place(x=735,y=0)
                    text.insert(END,texts)
                    def fseeq11():
                              text.place_forget()
                              bb.place_forget()
                              scrollbar.pack_forget()
                              

def sp12():
          
          with open('logs//12//0u357i0ns//0u357i0n.txt','r') as f:
                              questions=f.readlines()
                              if questions == []:
                                        messagebox.showerror('Error','Empty file. NO questions found..!!')
                                        
          ql=Label(text='Question :',font="cursive 18 bold italic",fg='orange',bg='black')
          ql.place(x=20,y=150)
          bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fsp12(),practicalscreen12()])
          bb.place(x=755,y=0)
          nl=Label(text='Name of student :',font="cursive 18 bold italic",fg='orange',bg='black')
          nl.place(x=10,y=250)
          def pq(*args):
                        global question
                        question=tq.get()
                        question=question.replace('\n','')
                        with open(f'logs//12//practicals//{question}//students.txt','r') as f:
                                  global names
                                  names=f.readlines()

                                  if names == []:
                                            messagebox.showerror('Error','Empty file. NO stident found..!!')

                        seeing()
                   
          tq=StringVar()
          tq.set(questions[0])
          otq=OptionMenu(mainroot,tq,*questions,command=pq)
          otq.config(width=50)
          otq.place(x=170,y=150)
          
          def seeing():
                  def pn(*args):
                            try:
                                    sname=tn.get()

                                    if sname in names:
                                          sname=sname.replace('\n','')
                                          with open(f'logs//12/practicals//{question}//{sname}.txt','r') as f:
                                                sps12(f.read())
                                          
                                          
                            except:
                                  messagebox.showerror('error','something went wrong ..!!')

                  tn=StringVar()
                  tn.set(names[0])
                  global otn
                  otn=OptionMenu(mainroot,tn,*names,command=pn)
                  otn.config(width=50)
                  otn.place(x=240,y=250)
            
          def fsp12():
                    ql.place_forget()
                    bb.place_forget()
                    nl.place_forget()
                    otq.place_forget()
                    otn.place_forget()       
          def sps12(texts):
                    scrollbar = Scrollbar(mainroot)
                    scrollbar.pack(side=RIGHT, fill=Y)
                    text = Text(mainroot, yscrollcommand = scrollbar.set,width=54,height=20,font="cursive 17 bold")
                    text.place(x=20,y=20)
                    scrollbar.config(command=text.yview)
                    bb=Button(text='<-- Back',font="cursive 18 bold italic",fg='orange',bg='black',command=lambda:[fseeq12(),sp12()])
                    bb.place(x=735,y=0)
                    text.insert(END,texts)
                    def fseeq12():
                              text.place_forget()
                              bb.place_forget()
                              scrollbar.pack_forget()
                    
if __name__=='__main__':
      if os.path.exists('logs') == False:
                os.mkdir('logs')
                os.path.join('logs')
                os.mkdir('logs//11')
                os.mkdir('logs//12')
                os.mkdir('logs//11//0u357i0ns')
                os.mkdir('logs//12//0u357i0ns')
                os.mkdir('logs//11//practicals')
                os.mkdir('logs//12//practicals')
                with open('logs//11//0u357i0ns//0u357i0n.txt','w'):
                          pass
                with open('logs//12//0u357i0ns//0u357i0n.txt','w'):
                          pass
                mainscreen()
      else:
                mainscreen()
          

mainroot.mainloop()

