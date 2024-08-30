import tkinter as tk
class mean_Calculater:
  def __init__(self,master):
    self.master=master
    master.title("Calculater Avg")
    master.configure(bg='#363834')

    self.label=tk.Label(master,text="Enter your Numbers: ",font=("b nazanin",14,'bold'),bg='#363834',fg='#04bcf8')
    self.label.place(x=600,y=100)

    self.entry1=tk.Entry(master,font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',width=27)
    self.entry1.place(x=600,y=150)

    self.entry2=tk.Entry(master,font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',width=27)
    self.entry2.place(x=600,y=200)

    self.calculator_butten=tk.Button(master,text="Avg",width=14,height=1,font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',border=3,activebackground='#db5aba',activeforeground='#1f2421',command=self.calculate_gpa)
    self.calculator_butten.place(x=600,y=250)
    self.result_labl=tk.Label(master,text="",font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
    self.result_labl.place(x=600,y=400)

  def calculate_gpa(self):
    try:
      grade1=float(self.entry1.get())
      grade2=float(self.entry2.get())
      gpa=(grade1+ grade2)/2
      self.result_labl.config(text=f"your Avg= {gpa}",font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
    except ValueError:
      self.result_labl.config(text="enter namber",font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')



root=tk.Tk()
gpa_calculator=mean_Calculater(root)
root.mainloop()
