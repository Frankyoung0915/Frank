import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0,width)
    b=random.randrange(0,height)
    window.title('祝愿')
    window.geometry("200x50"+"+"+str(a)+"+"+str(b))
    wordslist = ['万事如意', '新年快乐', '福星高照', '年年有余']
    text1 = wordslist[random.randint(0, len(wordslist)-1)]
    tk.Label(window,
        text= text1,  
        bg='Green',    
        font=('楷体', 17),     
        width=15, height=2  
        ).pack()   
    window.mainloop()
 
threads = []
for i in range(50):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
