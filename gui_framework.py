from tkinter import *
from tkinter.filedialog import *
import PyPDF2

def load_pdf(filename):
    f = open(filename,'rb')
    return PyPDF2.PdfFileReader(f)

def load1():
    f1 = askopenfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))
    filename1.set(f1.split('/')[-1])

    pdf = load_pdf(f1)
    pages1.set(pdf.getNumPages())
    start1.set('1')
    end1.set(pdf.getNumPages())


def save_pdf():
    pass

root = Tk()
root.title('PDF Merger')

filename1 = StringVar()
pages1 = StringVar()
start1 = StringVar()
end1 = StringVar()

Label(root,text='PDF Manipulator').grid(row=0,column=2,sticky=E)

Button(root,text='Add PDF',command=load1).grid(row=1,column=0)
Label(root,textvariable=filename1,width=20).grid(row=1,column=1,sticky=(N, S, E, W))

Label(root,text='Pages: ').grid(row=1,column=2)
Label(root,textvariable=pages1,width=3).grid(row=1,column=3,sticky=(N, S, E, W))

Label(root,text='Start: ').grid(row=1,column=4)
s1 = Entry(root,textvariable=start1,width=3)
s1.grid(row=1,column=5)

Label(root,text='End: ').grid(row=1,column=6)
e1 = Entry(root,textvariable=end1,width=3)
e1.grid(row=1,column=7)

Button(root,text='Save PDF As: ', command=save_pdf,width=10).grid(row=3,column=2,sticky=E)

for child in root.winfo_children():
    child.grid_configure(padx=10,pady=10)

root.mainloop()
