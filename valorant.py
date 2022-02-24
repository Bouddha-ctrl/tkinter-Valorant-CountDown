import tkinter as tk
from PIL import ImageGrab , Image

import time
from threading import Thread

secs = 45 - 7 - 1


check = [1,1,0]  #if countdown dont check if planted,  activated, is planted 

def countdown():
    check[0] = 0
    t = hiden.cget("text")
    
    InT = int(t)
    
    mins, sec = divmod(InT, 60)
    timer = '{:02d}:{:02d}'.format(mins, sec)
    
    if InT==-1: 
        hiden.config(text=str(secs))
        check[0] = 1
        app.withdraw()
        return 0
    
    cool.config(text=timer)
    InT-=1
    hiden.config(text=str(InT))
    
    cool.after(1000,countdown)

def threaded_function(closed):
    image = ImageGrab.grab()
    y,x = image.size
    y//=2
    x = 25
    while(check[1] == 1):
        time.sleep(.25)
        image = ImageGrab.grab(bbox=(y, x, y+1, x+1))
        pix = image.getpixel((0,0))
        #print(pix,end='\n')
        if pix == (155,0,0) or pix == (113,0,0) :
            if check[0]==1 and check[2]==0 :
        #if pix[0] > 200 and check[0]==1:
                check[2]==1
                app.deiconify()
                countdown()
                
                #time.sleep(10 + 15 + 10 + 6) #5 min defuse after plant, 15 round lobby, 10 min push to plant, 6 plant(8)
        else:
            
            check[2] = 0
    return False

thread = Thread(target = threaded_function, args =(10, )) 

def btn_action():
    stat = btn.cget("text")

    if stat=='Enable':
        stat = 'Disable'
        btn.config(text=stat)
        thread.start()
        
    elif stat=='Disable':
        stat = 'Done'
        btn.config(text=stat,state='disabled')
        check[1]=0
    else:
        print("ERROR STAT")

def on_closing():
    check[1]=0
    
    app2.destroy()


app2 = tk.Tk()

# App Geometry and components
app2.geometry("300x100+300+200")
app2.title("Valorant GUI")
app2.resizable(False, False)

app2.protocol("WM_DELETE_WINDOW", on_closing)


active = tk.Label(app2,text="Stat :", fg="#FF0000",font = 'Verdana 12 bold')
active.place(x=20, y=0)

btn = tk.Button(app2, text="Enable", bg= 'grey', command=btn_action , height=2, width=8)
btn.place(x = 200,y = 0)





app = tk.Toplevel(app2)

# App Geometry and components
app.geometry("100x30+1270+700")
app.title("Valorant")
app.resizable(False, True)

app.configure(bg='')
app.overrideredirect(True)
app.lift()
app.wm_attributes("-topmost", True)
app.wm_attributes("-disabled", True)
app.wm_attributes("-transparentcolor", "white")


cool = tk.Label(app,text=str(secs),bg='grey', fg="#FF0000",font = 'Verdana 12 bold')
app.wm_attributes("-transparentcolor", 'grey')

cool.place(x=20, y=0)

hiden = tk.Label(app,text=secs, font = 'Verdana 12')
hiden.place_forget()


app2.mainloop()
