import tkinter
import tkinter.messagebox
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def fcfs_visualization(arriv,pname,compl,wait,trnar):

    n = len(compl)

    temp=[]

    for i in range(n-1):
        arriv[i+1] = compl[i]
    for i in range(n):
        temp.append(compl[i]-arriv[i])

    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(pname, temp, left=arriv)
    

    new = customtkinter.CTk()
    new.title("VISUALIZATION")
    new.geometry("1200x750+60+60")

    base_frame = customtkinter.CTkScrollableFrame(master=new)
    base_frame.pack(pady=20, padx=20, fill="both", expand=True)

    top_frame = customtkinter.CTkFrame(master=base_frame)
    top_frame.pack(pady=5, padx=5, fill="both", expand=True)

    lab1 = customtkinter.CTkLabel(master=top_frame,
                                    text="PROCESS GANTT CHART",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab1.pack(pady=5, padx=5, fill="both", expand=True)

    fig.set_size_inches(9, 4)
    canvas = FigureCanvasTkAgg(fig, master=top_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10, padx=5, fill="both", expand=True)

    frame2 = customtkinter.CTkFrame(master=top_frame,
                                    height = 550)
    frame2.pack(pady=5, padx=5, fill="both", expand=True)

    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS WAITING TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.25, rely=0.1, anchor=customtkinter.CENTER)
    if sum(wait) > 0:
        temp = []
        for i in range(len(pname)):
            temp.append(pname[i]+" : "+str(wait[i]))
        fig, ax = plt.subplots()
        ax.pie(wait, labels = temp)
        fig.set_size_inches(5, 5)
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)
    else:
        lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="Can't Draw Pie Chart!\nAll Waiting Times are 0!",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
        lab2.place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)


    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS TURNAROUND TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.75, rely=0.1, anchor=customtkinter.CENTER)
    
    temp = []
    for i in range(len(pname)):
        temp.append(pname[i]+" : "+str(trnar[i]))
    fig, ax = plt.subplots()
    ax.pie(trnar, labels = temp)
    fig.set_size_inches(5, 5)
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.75, rely=0.64, anchor=customtkinter.CENTER)

    new.mainloop()


def sjf_visualization(arriv,pname,compl,wait,trnar,burst):

    n = len(compl)

    temp = []

    new = burst.copy()
    new.sort()
    for i in range(n):
        temp.append(burst.index(new[i]))

    compl.sort()

    tt = []
    for i in range(n):
        if i == 0:
            tt.append(arriv[i])
        else:
            tt.append(compl[i-1])
    arriv = tt

    dur = []

    for i in range(n):
        if i == 0:
            dur.append(burst[i])
        else:
            dur.append(compl[i]-compl[i-1])


    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(pname, dur, left=arriv)
    

    new = customtkinter.CTk()
    new.title("VISUALIZATION")
    new.geometry("1200x750+60+60")

    base_frame = customtkinter.CTkScrollableFrame(master=new)
    base_frame.pack(pady=20, padx=20, fill="both", expand=True)

    top_frame = customtkinter.CTkFrame(master=base_frame)
    top_frame.pack(pady=5, padx=5, fill="both", expand=True)

    lab1 = customtkinter.CTkLabel(master=top_frame,
                                    text="PROCESS GANTT CHART",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab1.pack(pady=5, padx=5, fill="both", expand=True)

    fig.set_size_inches(9, 4)
    canvas = FigureCanvasTkAgg(fig, master=top_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10, padx=5, fill="both", expand=True)

    frame2 = customtkinter.CTkFrame(master=top_frame,
                                    height = 550)
    frame2.pack(pady=5, padx=5, fill="both", expand=True)

    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS WAITING TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.25, rely=0.1, anchor=customtkinter.CENTER)
    if sum(wait) > 0:
        temp = []
        for i in range(len(pname)):
            temp.append(pname[i]+" : "+str(wait[i]))
        fig, ax = plt.subplots()
        ax.pie(wait, labels = temp)
        fig.set_size_inches(5, 5)
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)
    else:
        lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="Can't Draw Pie Chart!\nAll Waiting Times are 0!",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
        lab2.place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)


    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS TURNAROUND TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.75, rely=0.1, anchor=customtkinter.CENTER)
    
    temp = []
    for i in range(len(pname)):
        temp.append(pname[i]+" : "+str(trnar[i]))
    fig, ax = plt.subplots()
    ax.pie(trnar, labels = temp)
    fig.set_size_inches(5, 5)
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.75, rely=0.64, anchor=customtkinter.CENTER)

    new.mainloop()

def ps_visualization(arriv,pname,compl,wait,trnar,burst,prior):

    n = len(compl)

    temp = []

    new = prior.copy()
    new.sort()
    for i in range(n):
        temp.append(prior.index(new[i]))

    compl.sort()

    tt = []
    for i in range(n):
        if i == 0:
            tt.append(arriv[i])
        else:
            tt.append(compl[i-1])
    arriv = tt

    dur = []

    for i in range(n):
        if i == 0:
            dur.append(burst[i])
        else:
            dur.append(compl[i]-compl[i-1])


    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(pname, dur, left=arriv)
    

    new = customtkinter.CTk()
    new.title("VISUALIZATION")
    new.geometry("1200x750+60+60")

    base_frame = customtkinter.CTkScrollableFrame(master=new)
    base_frame.pack(pady=20, padx=20, fill="both", expand=True)

    top_frame = customtkinter.CTkFrame(master=base_frame)
    top_frame.pack(pady=5, padx=5, fill="both", expand=True)

    lab1 = customtkinter.CTkLabel(master=top_frame,
                                    text="PROCESS GANTT CHART",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab1.pack(pady=5, padx=5, fill="both", expand=True)

    fig.set_size_inches(9, 4)
    canvas = FigureCanvasTkAgg(fig, master=top_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10, padx=5, fill="both", expand=True)

    frame2 = customtkinter.CTkFrame(master=top_frame,
                                    height = 550)
    frame2.pack(pady=5, padx=5, fill="both", expand=True)

    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS WAITING TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.25, rely=0.1, anchor=customtkinter.CENTER)
    if sum(wait) > 0:
        temp = []
        for i in range(len(pname)):
            temp.append(pname[i]+" : "+str(wait[i]))
        fig, ax = plt.subplots()
        ax.pie(wait, labels = temp)
        fig.set_size_inches(5, 5)
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)
    else:
        lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="Can't Draw Pie Chart!\nAll Waiting Times are 0!",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
        lab2.place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)


    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS TURNAROUND TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.75, rely=0.1, anchor=customtkinter.CENTER)
    
    temp = []
    for i in range(len(pname)):
        temp.append(pname[i]+" : "+str(trnar[i]))
    fig, ax = plt.subplots()
    ax.pie(trnar, labels = temp)
    fig.set_size_inches(5, 5)
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.75, rely=0.64, anchor=customtkinter.CENTER)

    new.mainloop()

def ps_visualization(arriv,pname,compl,wait,trnar,burst,quant):

    n = len(compl)

    temp = []

    new = prior.copy()
    new.sort()
    for i in range(n):
        temp.append(prior.index(new[i]))

    compl.sort()

    tt = []
    for i in range(n):
        if i == 0:
            tt.append(arriv[i])
        else:
            tt.append(compl[i-1])
    arriv = tt

    dur = []

    for i in range(n):
        if i == 0:
            dur.append(burst[i])
        else:
            dur.append(compl[i]-compl[i-1])


    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(pname, dur, left=arriv)
    

    new = customtkinter.CTk()
    new.title("VISUALIZATION")
    new.geometry("1200x750+60+60")

    base_frame = customtkinter.CTkScrollableFrame(master=new)
    base_frame.pack(pady=20, padx=20, fill="both", expand=True)

    top_frame = customtkinter.CTkFrame(master=base_frame)
    top_frame.pack(pady=5, padx=5, fill="both", expand=True)

    lab1 = customtkinter.CTkLabel(master=top_frame,
                                    text="PROCESS GANTT CHART",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab1.pack(pady=5, padx=5, fill="both", expand=True)

    fig.set_size_inches(9, 4)
    canvas = FigureCanvasTkAgg(fig, master=top_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10, padx=5, fill="both", expand=True)

    frame2 = customtkinter.CTkFrame(master=top_frame,
                                    height = 550)
    frame2.pack(pady=5, padx=5, fill="both", expand=True)

    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS WAITING TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.25, rely=0.1, anchor=customtkinter.CENTER)
    if sum(wait) > 0:
        temp = []
        for i in range(len(pname)):
            temp.append(pname[i]+" : "+str(wait[i]))
        fig, ax = plt.subplots()
        ax.pie(wait, labels = temp)
        fig.set_size_inches(5, 5)
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)
    else:
        lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="Can't Draw Pie Chart!\nAll Waiting Times are 0!",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
        lab2.place(relx=0.25, rely=0.64, anchor=customtkinter.CENTER)


    lab2 = customtkinter.CTkLabel(master=frame2,
                                    text="PROCESS TURNAROUND TIME",
                                    font=("Consolas", 20),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.75, rely=0.1, anchor=customtkinter.CENTER)
    
    temp = []
    for i in range(len(pname)):
        temp.append(pname[i]+" : "+str(trnar[i]))
    fig, ax = plt.subplots()
    ax.pie(trnar, labels = temp)
    fig.set_size_inches(5, 5)
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.75, rely=0.64, anchor=customtkinter.CENTER)

    new.mainloop()
'''
pname = ["P1","P2","P3","P4","P5"]
arriv = [0,2,4,6,8]
burst = [5,4,3,2,1]
compl = [5,15,8,11,9]
trnar = [3,4,5,6,7]
wait = [0,1,2,3,4]


sjf_visualization(arriv,pname,compl,wait,trnar,burst)
'''