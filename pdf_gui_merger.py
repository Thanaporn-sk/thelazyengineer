from tkinter import *
from tkinter.filedialog import *
from PDF_Merger import *

def load():
    f = askopenfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))

    pdf = PDF_Doc(f)

    pdf_list.append(pdf)
    listbox.insert(END, pdf.display)


def save_pdf():
    writer = PyPDF2.PdfFileWriter()

    output_filename = asksaveasfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))
    output_file = open(output_filename,'wb')

    for doc in pdf_list:
        doc.add_to_writer(writer)

    writer.write(output_file)
    output_file.close()
    root.quit()

def remove():
    index = int(listbox.curselection()[0])
    pdf_list.pop(index)
    listbox.delete(ANCHOR)
    print(pdf_list)

def display():
    index = int(listbox.curselection()[0])
    value = w.get(index)
    filename.set(value)
    pages.set(pdf_list[index].pages)
    start.set(pdf_list[index].start)
    end.set(pdf_list[index].end)

def set_start(*args):
    index = int(listbox.curselection()[0])
    pdf_list[index].start = int(start.get())

def set_end(*args):
    index = int(listbox.curselection()[0])
    pdf_list[index].end = int(end.get())

pdf_list = []

root = Tk()
root.title('PDF Merger')

filename = StringVar()
pages = StringVar()
start = StringVar()
end = StringVar()


Label(root,text='PDF Manipulator').grid(row=0,column=0,columnspan=4)

Button(root,text='Add PDF',command=load).grid(row=2,column=0)
Button(root,text='Remove PDF',command=remove).grid(row=3,column=0)

listbox = Listbox(root)
listbox.bind('<<ListboxSelect>>',display)
listbox.grid(row=1,rowspan=4,column=1)


Label(root,text='File: ').grid(row=1,column=2)
Label(root,textvariable=filename,width=20).grid(row=1,column=3,sticky=(N, S, E, W))

Label(root,text='Pages: ').grid(row=2,column=2)
Label(root,textvariable=pages).grid(row=2,column=3)

Label(root,text='Start: ').grid(row=3,column=2)
s1 = Entry(root,textvariable=start,width=3)
s1.grid(row=3,column=3)

Label(root,text='End: ').grid(row=4,column=2)
e1 = Entry(root,textvariable=end,width=3)
e1.grid(row=4,column=3)


Button(root,text='Save PDF As: ', command=save_pdf,width=10).grid(row=5,column=0,columnspan=4)

for child in root.winfo_children():
    child.grid_configure(padx=10,pady=10)

start.trace('w', set_start)
end.trace('w', set_end)

root.mainloop()
