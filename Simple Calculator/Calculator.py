from tkinter import *
import random

list_warna = ["#f716f4","#f72a83","lightblue","#25f5e0","#075c1a"]
warna_random_tambah = random.choice(list_warna)
warna_random_kali = random.choice(list_warna)
warna_random_bagi = random.choice(list_warna)
warna_random_kurang = random.choice(list_warna)
warna_random_hasil = random.choice(list_warna)
warna_random_clear = random.choice(list_warna)
warna_random0 = random.choice(list_warna)
warna_random1 = random.choice(list_warna)
warna_random2 = random.choice(list_warna)
warna_random3 = random.choice(list_warna)
warna_random4 = random.choice(list_warna)
warna_random5 = random.choice(list_warna)
warna_random6 = random.choice(list_warna)
warna_random7 = random.choice(list_warna)
warna_random8 = random.choice(list_warna)
warna_random9 = random.choice(list_warna)

def label_tulis(tulis):
    global hasil_text, hasil
    
    hasil_text = hasil_text + str(tulis)
    
    hasil.set(hasil_text)

def delete(tulis):
    global hasil, hasil_text
    
    hasil_text = tulis
    
    hasil.set(hasil_text)
    
def operasi(tulis):
    global hasil, hasil_text
    
    hasil_text = hasil_text + str(tulis)
    
    hasil.set(hasil_text)
    
def hasil_operasi():
    global hasil_text
    
    try:
        total = str(eval(hasil_text))
        hasil.set(total)
        hasil_text = total
    except ZeroDivisionError:
        hasil.set("Error!")
    except SyntaxError:
        hasil.set("Masukan angka!")
        
def on_enter_hasil(event):
    button_hasil.config(bg=warna_random_hasil)
def on_enter_tambah(event):
    button_tambah.config(bg=warna_random_tambah)
def on_enter_kurang(event):
    button_kurang.config(bg=warna_random_kurang)
def on_enter_kali(event):
    button_kali.config(bg=warna_random_kali)
def on_enter_bagi(event):
    button_bagi.config(bg=warna_random_bagi)
def on_enter_0(event):
    button0.config(bg=warna_random0)
def on_enter_1(event):
    button1.config(bg=warna_random1)
def on_enter_2(event):
    button2.config(bg=warna_random2)
def on_enter_3(event):
    button3.config(bg=warna_random3)
def on_enter_4(event):
    button4.config(bg=warna_random4)
def on_enter_5(event):
    button5.config(bg=warna_random5)
def on_enter_6(event):
    button6.config(bg=warna_random6)
def on_enter_7(event):
    button7.config(bg=warna_random7)
def on_enter_8(event):
    button8.config(bg=warna_random8)
def on_enter_9(event):
    button9.config(bg=warna_random9)
def on_enter_clear(event):
    button_clear.config(bg=warna_random9)
    
    
def on_leave_hasil(event):
    button_hasil.config(bg="#252a2b")
def on_leave_tambah(event):
    button_tambah.config(bg="#252a2b")
def on_leave_kurang(event):
    button_kurang.config(bg="#252a2b")
def on_leave_kali(event):
    button_kali.config(bg="#252a2b")
def on_leave_bagi(event):
    button_bagi.config(bg="#252a2b")
def on_leave_0(event):
    button0.config(bg="#252a2b")
def on_leave_1(event):
    button1.config(bg="#252a2b")
def on_leave_2(event):
    button2.config(bg="#252a2b")
def on_leave_3(event):
    button3.config(bg="#252a2b")
def on_leave_4(event):
    button4.config(bg="#252a2b")
def on_leave_5(event):
    button5.config(bg="#252a2b")
def on_leave_6(event):
    button6.config(bg="#252a2b")
def on_leave_7(event):
    button7.config(bg="#252a2b")
def on_leave_8(event):
    button8.config(bg="#252a2b")
def on_leave_9(event):
    button9.config(bg="#252a2b")
def on_leave_clear(event):
    button_clear.config(bg="#252a2b")

root = Tk()
root.geometry("300x400")
root.configure(bg="#f5ce20")

hasil_text = ""
hasil = StringVar()

label_hasil = Label(root, bg="#252a2b",font=("Arial",20),fg="white",width=20,height=3, textvariable=hasil)
label_hasil.pack()

frame = Frame(root)
frame.pack()

button_hasil = Button(frame, bg="#252a2b",width = 3,text="=",font=("Arial",20),fg="white",relief="flat",command=lambda: hasil_operasi())
button_hasil.grid(row=4,column=1)

button_bagi = Button(frame, bg="#252a2b",width = 3,text=":",font=("Arial",20),fg="white",relief="flat",command=lambda: operasi("/"))
button_bagi.grid(row=4,column=4)

button_kali = Button(frame, bg="#252a2b",width = 3,text="x",font=("Arial",20),fg="white",relief="flat",command=lambda: operasi("*"))
button_kali.grid(row=3,column=4)

button_kurang = Button(frame, bg="#252a2b",width = 3,text="-",font=("Arial",20),fg="white",relief="flat",command=lambda: operasi("-"))
button_kurang.grid(row=2,column=4)

button_tambah = Button(frame, bg="#252a2b",width = 3,text="+",font=("Arial",20),fg="white",relief="flat",command=lambda: operasi("+"))
button_tambah.grid(row=1,column=4)

button_clear = Button(frame, bg="#252a2b",width = 3,text="clear",font=("Arial",20),fg="white",relief="flat",command=lambda: delete(""))
button_clear.grid(row=4,column=2)

button0 = Button(frame, bg="#252a2b",width = 3,text="0",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("0"))
button0.grid(row=4,column=3)

button1 = Button(frame, bg="#252a2b",width = 3,text="1",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("1"))
button1.grid(row=3,column=3)

button2 = Button(frame, bg="#252a2b",width = 3,text="2",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("2"))
button2.grid(row=3,column=2)

button3 = Button(frame, bg="#252a2b",width = 3,text="3",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("3"))
button3.grid(row=3,column=1)

button4 = Button(frame, bg="#252a2b",width = 3,text="4",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("4"))
button4.grid(row=2,column=3)

button5 = Button(frame, bg="#252a2b",width = 3,text="5",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("5"))
button5.grid(row=2,column=2)

button6 = Button(frame, bg="#252a2b",width = 3,text="6",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("6"))
button6.grid(row=2,column=1)

button7 = Button(frame, bg="#252a2b",width = 3,text="7",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("7"))
button7.grid(row=1,column=3)

button8 = Button(frame, bg="#252a2b",width = 3,text="8",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("8"))
button8.grid(row=1,column=2)

button9 = Button(frame, bg="#252a2b",width = 3,text="9",font=("Arial",20),fg="white",relief="flat",command=lambda: label_tulis("9"))
button9.grid(row=1,column=1)


button_hasil.bind("<Enter>",on_enter_hasil)
button_hasil.bind("<Leave>",on_leave_hasil)

button_tambah.bind("<Enter>",on_enter_tambah)
button_tambah.bind("<Leave>",on_leave_tambah)

button_kurang.bind("<Enter>",on_enter_kurang)
button_kurang.bind("<Leave>",on_leave_kurang)

button_kali.bind("<Enter>",on_enter_kali)
button_kali.bind("<Leave>",on_leave_kali)

button_bagi.bind("<Enter>",on_enter_bagi)
button_bagi.bind("<Leave>",on_leave_bagi)

button0.bind("<Enter>",on_enter_0)
button0.bind("<Leave>",on_leave_0)

button1.bind("<Enter>",on_enter_1)
button1.bind("<Leave>",on_leave_1)

button2.bind("<Enter>",on_enter_2)
button2.bind("<Leave>",on_leave_2)

button3.bind("<Enter>",on_enter_3)
button3.bind("<Leave>",on_leave_3)

button4.bind("<Enter>",on_enter_4)
button4.bind("<Leave>",on_leave_4)

button5.bind("<Enter>",on_enter_5)
button5.bind("<Leave>",on_leave_5)

button6.bind("<Enter>",on_enter_6)
button6.bind("<Leave>",on_leave_6)

button7.bind("<Enter>",on_enter_7)
button7.bind("<Leave>",on_leave_7)

button8.bind("<Enter>",on_enter_8)
button8.bind("<Leave>",on_leave_8)

button9.bind("<Enter>",on_enter_9)
button9.bind("<Leave>",on_leave_9)

button_clear.bind("<Enter>",on_enter_clear)
button_clear.bind("<Leave>",on_leave_clear)
root.mainloop()