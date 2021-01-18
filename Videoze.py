# IMPORTING LIBRARYS
from moviepy.editor import VideoFileClip
import os
import sys
import tkinter as Tk
from tkinter import messagebox
import threading

# GLOBAL VARIABLE DEC
totalseconds = 0
loc = ""
tk = Tk.Tk()
counter = 0
inputvar = Tk.StringVar()
noofvideos = Tk.StringVar()
resulthour = Tk.StringVar()


# FUNCTION DEFINATION
def threadfunc():
    threading.Thread(target=onclick()).start()


# buttonclick
def onclick():
    print(inputvar.get())
    import time
    time.sleep(4)
    try:
        os.chdir(inputvar.get())
    except:
        messagebox.showerror("Invalid Path")
    else:
        threading.Thread(target=searching(inputvar.get())).start()

        convert(totalseconds)


# Convertion of seconds
def convert(seconds):
    try:
        global counter
        global totalseconds
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        seconds = int(seconds)
        resulthour.set(
            f"\n\n**Watch TIME ==" + str(hours) + "Hours:" + str(minutes) + "minuates:" + str(seconds) + "seconds=**")
        print(f"\n\n**Watch TIME ==" + str(hours) + "Hours:" + str(minutes) + "minuates:" + str(seconds))
        totalseconds = 0
        noofvideos.set("" + str(counter + 1))
        counter = 0
    except Exception as e:
        print("ERROR CODE :CON ", e)


# finding mp4 duration
def clipduration(cwd, filemp4):
    try:
        global counter
        global totalseconds
        os.chdir(cwd)
        clip = VideoFileClip(filemp4)
        thisfilesec = clip.duration
        print("***", filemp4, thisfilesec, "***")
        totalseconds = totalseconds + thisfilesec
        if (thisfilesec != totalseconds):
            counter = counter + 1
        clip.close()
    except Exception as e:
        print("---", e, "---")


# walking through all dir
def searching(loc1):
    try:

        for subfolders in os.listdir():
            print(subfolders)
            os.chdir(loc1)
            if os.path.isdir(subfolders):
                os.chdir(f"{loc1}\\{subfolders}")
                for file in os.listdir():
                    if os.path.isfile(file):
                        print(file)
                        threading.Thread(target=clipduration(os.getcwd(), file)).start()

            if os.path.isfile(subfolders):
                threading.Thread(target=clipduration(os.getcwd(), subfolders)).start()
    except Exception as e:
        print("ERROR CODE :SEA", e)


# Main Frame Layout
def layout():
    tk.minsize(900, 550)
    tk.maxsize(900, 550)
    tk.title("WMK v1.0")
    # header Part
    header = Tk.Label(text="Videoze", font="Calibri 30 bold", anchor="nw", background="white", padx=9)
    header.pack(fill=Tk.X, side=Tk.TOP, anchor="n")
    subtitle = Tk.Label(text="Developed by Jaspreet Singh", font="Calibri 10 bold", anchor="nw", padx=9)
    subtitle.pack(fill=Tk.X, side=Tk.TOP, anchor="n")
    # Section 1 INPUT
    inputsection = Tk.Frame(tk, relief=Tk.SUNKEN, borderwidth="1")
    inputtext = Tk.Label(inputsection, font="Calibri 9", text="Input", padx=9)
    entryinput = Tk.Entry(inputsection, width="30", font="Calibri 9", textvariable=inputvar)
    inputtext.pack(side=Tk.LEFT, anchor="n", pady=40)
    entryinput.pack(pady=40)
    submit = Tk.Button(inputsection, text="Go", command=threadfunc)
    submit.pack(pady=6, ipadx=12)
    inputsection.pack(side=Tk.LEFT, fill=Tk.Y)

    # Section2
    Resultsection = Tk.Frame(tk, relief=Tk.SUNKEN, borderwidth="1")
    resulttext = Tk.Label(Resultsection, text="Result:", font="Calibri 9", padx=9)
    resulttext.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=39)
    novfile = Tk.Label(Resultsection, text="NO OF Videos =", font="Calibri 10")
    novfile.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=69)
    rnovfile = Tk.Label(Resultsection, text="0Videos", font="Calibri 10", textvariable=noofvideos)
    rnovfile.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=69)
    result = Tk.Label(Resultsection, font="Calibri 14", textvariable=resulthour)
    result.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=69)
    Resultsection.pack(side=Tk.LEFT, anchor="n", fill=Tk.BOTH, padx=5, ipadx=30)

    # Section 3 About
    aboutsection = Tk.Frame(tk, relief=Tk.SUNKEN, borderwidth="1")
    about = Tk.Label(aboutsection, text="About:", font="Calibri 9", padx=9)
    about.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=39)
    aboutc = Tk.Label(aboutsection,
                      text="How to use?\n Just Simply add the folder location of your \n Videos inside Input block \n Then Press Enter \n \n \nBasic Idea behind software!\n A simple which will leads you\n to count watching hours for \n serials or webseries \n \n \n \n \n \n Designed by Jaspreet Singh \n \n Bug report at \n Gmail\nJaspreetsidhu3may@gmail.com\n Github:\n https://github.com/jaspreetsidhu3 \n \n!Enjoy!",
                      font="Calibri 9", padx=9)
    aboutc.pack(side=Tk.LEFT, fill=Tk.X, anchor="n", pady=69)
    aboutsection.pack(side=Tk.LEFT, anchor="n", fill=Tk.BOTH, padx=5, ipadx=60)
    tk.mainloop()


try:
    threading.Thread(target=layout()).start()
    sys.setrecursionlimit(5000)
    print("Done")
except Exception as e:
    print("Main function Error")
