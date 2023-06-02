import customtkinter
from CTkMessagebox import CTkMessagebox
import algorithm

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def home():

    def exit():
        app.destroy()

    def start():

        def get_pro():

            def getval():
                
                pname = []
                burst = []
                arriv = []
                prior = []

                for i in range(len(row)):
                    if i%4 == 1:
                        arriv.append(int(row[i].get()))
                    elif i%4 == 2:
                        burst.append(int(row[i].get()))
                    elif i%4 == 3:
                        prior.append(int(row[i].get()))
                    else:
                        pname.append(row[i].get())


                
                app.destroy()

                if ptype == 'First Come First Serve(FCFS)':
                    algorithm.fcfs(pname,burst,arriv,prior)
                elif ptype == 'Shortest Job First(SJF)':
                    algorithm.sjf(pname,burst,arriv,prior)
                elif ptype == 'Priority Scheduling':
                    algorithm.priority(pname,burst,arriv,prior)



            global num, ptype
            num_lbl.pack_forget()
            num_ent.pack_forget()
            ty_lbl.pack_forget()
            ty_menu.pack_forget()
            next_btn.place_forget()
            frame_1.pack_forget()

            app.geometry("700x500")
            app.title("INPUT VALUES")

            tframe = customtkinter.CTkFrame(master=app)
            tframe.pack(pady=10, padx=10, fill="both", expand=True)

            lab1 = customtkinter.CTkLabel(master=tframe,
                                    text="Process ID",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
            lab1.place(relx=0.15, rely=0.03,anchor=customtkinter.CENTER)

            lab2 = customtkinter.CTkLabel(master=tframe,
                                    text="Arrival Time",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
            lab2.place(relx=0.38, rely=0.03, anchor=customtkinter.CENTER)

            lab3 = customtkinter.CTkLabel(master=tframe,
                                    text="Burst Time",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
            lab3.place(relx=0.62, rely=0.03, anchor=customtkinter.CENTER)

            lab4 = customtkinter.CTkLabel(master=tframe,
                                    text="Priority",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
            lab4.place(relx=0.85, rely=0.03, anchor=customtkinter.CENTER)

            sframe = customtkinter.CTkScrollableFrame(master=tframe)
            sframe.pack(pady=40, padx=10, fill="both", expand=True)
            row=[]
            for i in range(num):
                for j in range(4):
                    e = customtkinter.CTkEntry(master=sframe,width=140)
                    if j == 0:
                        val = "P"+str(i+1)
                        e.insert(0,val)
                    elif j == 3 and (ptype == 'First Come First Serve(FCFS)' or ptype == 'Shortest Job First(SJF)'):
                        e.insert(0,i+1)
                    e.grid(row=i, column=j, padx=10, pady=10)
                    row.append(e)


            sub_btn = customtkinter.CTkButton(master=tframe,
                                        text="Submit",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=getval)
            sub_btn.place(relx=0.5, rely=0.95, anchor=customtkinter.CENTER)

        def validate():

            global num, ptype
            get = num_ent.get()
            ptype = ty_menu.get()
            if get.isdigit() == False:
                CTkMessagebox(title="Error", message="Input Integer Values Only!!!", icon="cancel")
            else:
                num = int(get)
                if num <= 0:
                    CTkMessagebox(title="Error", message="Can't Schedule 0 or less Process!!!", icon="cancel")
                else:
                    if ptype == "Select":
                        CTkMessagebox(title="Error", message="Please Select a Scheduling Type!!!", icon="cancel")
                    else:
                        get_pro()

        
        head_lbl.pack_forget()
        desc_lbl.pack_forget()
        start_btn.place_forget()
        exit_btn.place_forget()

        app.geometry("600x450")
        frame_1.pack(pady=10, padx=10, fill="both", expand=True)

        num_lbl = customtkinter.CTkLabel(master=frame_1,
                                    text="Enter Number of Process",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=60)
        num_lbl.pack(pady=10, padx=10)

        num_ent = customtkinter.CTkEntry(master=frame_1,placeholder_text="Eg-1,2,3,..")
        num_ent.pack(pady=10, padx=10)

        ty_lbl = customtkinter.CTkLabel(master=frame_1,
                                    text="Select Scheduling Type",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=60)
        ty_lbl.pack(pady=10, padx=10)

        ty_menu= customtkinter.CTkOptionMenu(master=frame_1,
                                            dynamic_resizing=True,
                                            values=['Select','First Come First Serve(FCFS)','Shortest Job First(SJF)','Priority Scheduling','Round Robin'])
        ty_menu.pack(pady=10, padx=10)

        next_btn = customtkinter.CTkButton(master=frame_1,
                                        text="Next",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=validate)
        next_btn.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


    app = customtkinter.CTk()
    app.geometry("600x450")
    app.title("PROCESS SCHEDULING AND ANALYZING TOOL")


    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=20, fill="both", expand=True)

    head_lbl = customtkinter.CTkLabel(master=frame_1,
                                    text="PROCESS SCHEDULING AND ANALYZING TOOL",
                                    font=("Consolas", 25),
                                    width=120,
                                    height=100)
    head_lbl.pack(pady=10, padx=10)

    desc_lbl = customtkinter.CTkLabel(master=frame_1,
                                    text="A Software Tool for Scheduling and Visualizing various Process \nScheduling Methods. This Tool is Developed using \nTkinter Library of Python.",
                                    font=("Consolas", 15),
                                    width=120,
                                    height=10)
    desc_lbl.pack(pady=20, padx=10)

    start_btn = customtkinter.CTkButton(master=frame_1,
                                        text="Start",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=start)
    start_btn.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
    exit_btn = customtkinter.CTkButton(master=frame_1,
                                        text="Exit",
                                        width=80,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=exit)
    exit_btn.place(relx=0.5, rely=0.94, anchor=customtkinter.CENTER)


    app.mainloop()

home()