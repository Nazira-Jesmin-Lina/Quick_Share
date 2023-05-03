from tkinter import *
import socket
import threading
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Quick Share!")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)


def screen_share():
    root.withdraw()
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg='#f4fdfe')
    window.resizable(False, False)

    def back_btn():
        window.withdraw()
        root.deiconify()

    def connect_btn():
        print("connect button pressed")

    def share_scrn_btn():
        print("share your screen button pressed")

    # icon
    image_icon1 = PhotoImage(file="image/send_fin.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="image/bg_send_450x560.png")
    Label(window, image=Sbackground).place(x=-2, y=-2)

    Mbackground = PhotoImage(file="image/sss_ui.png")
    Label(window, image=Mbackground).place(x=130, y=20)

    host = socket.gethostname()
    ip_address = socket.gethostbyname(host)
    Label(window, text=f'IP: {ip_address}', bg='#87CEEB', fg='#000').place(x=190, y=190)

    Button(window, text="connect", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=connect_btn).place(x=110, y=250)

    SenderID = Entry(window, width=22, fg="black", border=4, bg='white', font=('arial', 15))
    SenderID.place(x=110, y=320)
    SenderID.focus()
    SenderID.insert(0, "IP Address")
    Button(window, text="Share your Screen", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=share_scrn_btn).place(x=110, y=380)

    Button(window, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=back_btn).place(x=110, y=450)

    def on_closing():
        print("User clicked close button")
        window.destroy()
        root.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()


def file_transfer():
    label1.destroy()
    label2.destroy()
    label3.destroy()

    # file_trans.destroy()
    # scrn_share.destroy()

    def back_press():
        label11.destroy()
        label22.destroy()
        label33.destroy()
        bck.destroy()

        global label1
        label1 = Label(root, text="Welcome!!", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
        label1.place(x=20, y=30)

        # Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

        global scrn_image
        scrn_image = PhotoImage(file="image/scrn_share.png")
        global scrn_share
        scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=screen_share)
        scrn_share.place(x=50, y=100)

        global file_image
        file_image = PhotoImage(file="image/file_transfer.png")
        global file_trans
        file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
        file_trans.place(x=300, y=100)
        global label2
        label2 = Label(root, text="Screen Share", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        label2.place(x=40, y=200)
        global label3
        label3 = Label(root, text="File Transfer", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        label3.place(x=280, y=200)

    # def catch_minimize(event):
    #     root.wm_state()
    #     print("window minimzed")

    def Send():
        root.withdraw()
        window = Toplevel(root)
        window.title("Send")
        window.geometry('450x560+500+200')
        window.configure(bg='#f4fdfe')
        window.resizable(False, False)

        def select_file():
            global filename
            global basename
            file = filedialog.askopenfile(initialdir=os.getcwd(), title='Select image File',
                                          filetypes=(('file type', '*.txt'), ('all files', '*.*')))
            if file:
                filename = file.name
                basename = os.path.basename(filename)
                print("Exact file name:", basename)
                Label(window, text=f' {basename}', font=('Acumin Variable Concept', 13,), bg='#7FFFD4',
                      fg="#000").place(x=114, y=305)

        def sender():
            s = socket.socket()
            host = socket.gethostname()
            port = 8085
            s.bind((host, port))
            s.listen(1)
            print(host)
            print('waiting for any incoming connection.........')
            conn, addr = s.accept()
            conn.send(basename.encode())
            print(basename)
            ack = conn.recv(1024).decode()
            print(ack)
            if ack == 'OK':
                with open(filename, 'rb') as file:
                    while True:
                        file_data = file.read(1024)
                        if not file_data:
                            break
                        conn.send(file_data)
                print("Data has been transmitted successfully...")
                send_btn.destroy()
                Label(window, text=f'Data has been transmitted successfully...', font=('Acumin Variable Concept', 13,),
                      bg='#7FFFD4', fg="#000").place(
                    x=90, y=350)

        def back_btn():
            window.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="image/send_fin.png")
        window.iconphoto(False, image_icon1)

        Sbackground = PhotoImage(file="image/bg_send_450x560.png")
        Label(window, image=Sbackground).place(x=-2, y=-2)

        Mbackground = PhotoImage(file="image/file_UI.png")
        Label(window, image=Mbackground, bg='#f4fdfe').place(x=130, y=20)

        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
        Label(window, text=f'IP: {ip_address}', bg='#7FFFD4', fg="#000", ).place(x=190, y=200)

        Button(window, text="+Select File", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=select_file).place(x=110, y=250)

        global send_btn
        send_btn = Button(window, text="Send", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
                          command=sender)
        send_btn.place(x=110, y=350)
        sel_file = Entry(window, width=22, fg="black", border=4, bg='#7FFFD4', font=('arial', 15))
        sel_file.place(x=110, y=300)
        sel_file.focus()
        sel_file.insert(0, "....")

        Button(window, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=back_btn).place(x=110, y=400)

        def on_closing():
            print("User clicked close button")
            window.destroy()
            root.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)

        window.mainloop()

    def Receive():
        root.withdraw()
        main = Toplevel(root)
        main.title("Receive")
        main.geometry('450x560+500+200')
        main.configure(bg='#f4fdfe')
        main.resizable(False, False)

        def receiver():
            ID = str(SenderID.get())

            s = socket.socket()
            port = 8085
            s.connect((ID, port))
            filename1 = s.recv(1024).decode()
            print(filename1)
            rcv = "RECEIVE\\" + filename1
            with open(rcv, 'wb') as file:
                while True:
                    file_data = s.recv(1024)
                    if not file_data:
                        break
                    file.write(file_data)
            print("file has been received successfully..")
            rr.destroy()
            Label(main, text=f'File has been received successfully.....', font=('Acumin Variable Concept', 13,),
                  bg='#7FFFD4', fg="#000").place(
                x=90, y=360)

        def back_btn():
            main.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="image/rcv_fin.png")
        main.iconphoto(False, image_icon1)
        Hbackground = PhotoImage(file="image/bg_send_450x560.png")
        Label(main, image=Hbackground).place(x=-2, y=-2)

        Mbackground = PhotoImage(file="image/file_UI.png")
        Label(main, image=Mbackground, bg='#f4fdfe').place(x=130, y=40)

        # Label(main, text="Input Sender IP", font=('arial', 10, 'bold'), bg='#7FFFD4', fg="#000",).place(x=110, y=250)
        SenderID = Entry(main, width=22, fg="black", border=2, bg='white', font=('arial', 15))
        SenderID.place(x=110, y=300)
        SenderID.focus()
        SenderID.insert(0, "Sender IP..")

        Button(main, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=back_btn).place(x=110, y=420)

        imageicon = PhotoImage(file="image/arrow-removebg-preview_30x30.png")
        rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=240, bg='#7FFFD4', fg="#000",
                    font='arial 14 bold',
                    command=receiver)
        rr.place(x=110, y=350)

        def on_closing():
            print("User clicked close button")
            main.destroy()
            root.destroy()

        main.protocol("WM_DELETE_WINDOW", on_closing)

        main.mainloop()

    global label11
    label11 = Label(root, text="File transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
    label11.place(x=20,
                  y=30)

    Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

    send_image = PhotoImage(file="image/send_fin.png")
    send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
    send.place(x=50, y=100)

    rcv_image = PhotoImage(file="image/rcv_fin.png")
    rcv = Button(root, image=rcv_image, bg="#f4fdfe", bd=0, command=Receive)
    rcv.place(x=300, y=100)

    global label22
    label22 = Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
    label22.place(x=60, y=200)

    global label33
    label33 = Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
    label33.place(x=300, y=200)

    bck = Button(root, text="Back", width=10, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
                 command=back_press)
    bck.place(x=150, y=500)
    root.mainloop()


# icon
image_icon = PhotoImage(file="image/icon.PNG")
root.iconphoto(False, image_icon)
global label1
label1 = Label(root, text="Welcome!!", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
label1.place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

global scrn_image
scrn_image = PhotoImage(file="image/scrn_share.png")
global scrn_share
scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=screen_share)
scrn_share.place(x=50, y=100)

global file_image
file_image = PhotoImage(file="image/file_transfer.png")
global file_trans
file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
file_trans.place(x=300, y=100)
global label2
label2 = Label(root, text="Screen Share", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
label2.place(x=40, y=200)
global label3
label3 = Label(root, text="File Transfer", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
label3.place(x=280, y=200)

background = PhotoImage(file="image/background.png")
Label(root, image=background).place(x=-2, y=280)


def on_closing():
    print("User clicked close button")
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

# root.bind("<Unmap>", catch_minimize)

root.mainloop()
