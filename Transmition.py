import tkinter as tk
from tkinter import messagebox,Canvas
import subprocess

shellfolder="/rpitx/"

def File(name):
    if name.endswith(".sh"):
       return shellfolder+name
    return shellfolder+name+".sh"

# ------------------------------------------excuting powershell code------------------------------------------------------

# THE PATH OF THE .sh FILE NEED TO BE CHANGED IN EVERY SUPROCESS.RUN

def chirp(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testchirp'),          args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))
    else:
        pro = subprocess.run(['cat', File('testchirp'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))




def spectrum(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testspectrum'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))
    else:
        pro = subprocess.run(['cat', File('testfsq'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))
def rf(root,args):
    if(args == ""):
         args=str(434000000 )
         pro = subprocess.run(['cat', File('testfsq'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
         print(pro.stdout)
         print(pro.returncode)
         if pro.returncode == 1:
          d1 = tk.Tk()

          # Positions the window in the center of the page.
          d1.geometry("+{}+{}".format(500, 250))

          d1.configure(bg="#11055b")
          mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
          mycanvas1.pack(fill="both", expand="true")
          mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
          d1.title("STATUS")
          d1.after(5000, lambda: d1.destroy())
          root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                     "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testfsq'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

def fmrds(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testfmrds'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testfmrds'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))


def nfm(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testnfm'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testnfm'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

def ssb(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testssb'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testssb'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))


def am(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testam'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testam'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))


def freedv(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testfreedv'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testfreedv'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

def sstv(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testsstv'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testsstv'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

def pocsag(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testpocsag'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testpocsag'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))


def opera(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testopera'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testopera'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))


def rtty(root,args):
    if (args == ""):
        args = str(434000000)
        pro = subprocess.run(['cat', File('testrtty'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))

    else:
        pro = subprocess.run(['cat', File('testrtty'), args], capture_output=True, shell=True)
        # subprocess.run(['cat','"./scratch.sh ",args],shell=True)
        print(pro.stdout)
        print(pro.returncode)
        if pro.returncode == 1:
            d1 = tk.Tk()

            # Positions the window in the center of the page.
            d1.geometry("+{}+{}".format(500, 250))

            d1.configure(bg="#11055b")
            mycanvas1 = Canvas(d1, width=500, height=200, bg="#11055b")
            mycanvas1.pack(fill="both", expand="true")
            mycanvas1.create_text(250, 100, text="Transmitting Data...", font=("Times new Roman", 40), fill="white")
            d1.title("STATUS")
            d1.after(5000, lambda: d1.destroy())
            root.after(5000, lambda: messagebox.showinfo("STATUS",
                                                         "DATA TRANSMITTED SUCCESSFULLY!!!"))



# ------------------------------------------------------------------------------------------------------------------------
