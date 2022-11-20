import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import time                

current_balance=100000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.shared_data={'Balance':tk.IntVar()}

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Cardpage, StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Cardpage")

    def show_frame(self, page_name):
        '''Shows a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Cardpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        
        selection_label = tk.Label(self,
                                   text='Card or Cardless?',
                                   font=('Century',32),
                                   foreground='white',
                                   bg='#3d3d5c')
        selection_label.pack(fill='x')
        
        spacing_label = tk.Label(self,height=4,bg='#3d3d5c')
        spacing_label.pack()
        
        button_frame = tk.Frame(self, background="#33334d")
        button_frame.pack(fill='both', expand=True)
        
        myFont = font.Font(size=13)
        
        def onClick():
            tkinter.messagebox.showinfo("Oops!","Sorry, this ATM does not support cash transactions via card.")
        
           
        card_button = tk.Button(button_frame, text='Using a Card', command = onClick, relief='raised', borderwidth=3, width=50, height=4, bg="#4dffc3")
        card_button.place(x=530,y=130)
        card_button['font']=myFont
        
        
        
        def cardless():
            controller.show_frame('StartPage')
            
        cardless_button = tk.Button(button_frame, text='Cardlesss', command = cardless, relief='raised', borderwidth=3, width=50, height=4, bg="#b3ffd9")
        cardless_button.place(x=530,y=230)
        cardless_button['font']=myFont
         
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#3d3d5c')
        self.controller = controller
        
        self.controller.title('ATM Management System')
        self.controller.state('zoomed')
        self.controller.iconphoto(False, tk.PhotoImage(file='C:/Users/ss21x/Desktop/Python/ATM project/atm.png'))
        
        headingLabel = tk.Label(self,
                                 text='ATM Management System',
                                 font=('orbitron',40,'bold'),
                                 foreground='white',
                                 background='#3d3d5c')
        headingLabel.pack(pady=25)
        
        spacing_label = tk.Label(self,height=4,bg='#3d3d5c')
        spacing_label.pack()
        
        password_Label = tk.Label(self,text='Enter 4 digit pin',
                                  font=('orbitron',13),
                                  bg='#3d3d5c',
                                  fg='white')
        password_Label.pack(pady=10)
        
        
        
        my_password=tk.StringVar()
        password_entry_space = tk.Entry(self,
                                        textvariable=my_password,
                                        font=('orbitron',12),
                                        width=22)
        password_entry_space.focus_set()
        password_entry_space.pack(ipady=7)
        
        def handle_focus_in(_):
            password_entry_space.configure(foreground='black', show='*')
            
        password_entry_space.bind('<FocusIn>', handle_focus_in)
        
        def check_password():
            if my_password.get() == '1234':
                my_password.set("")
                incorrect_password_label['text']=""
                controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text']='Invalid Password' 
        submit_button = tk.Button(self,
                                  text='Submit',
                                  command=check_password,
                                  relief='raised',
                                  borderwidth=3,
                                  width=40,
                                  height=2)
        
        submit_button.pack(pady=5)
        
        incorrect_password_label = tk.Label(self,
                                            text="",
                                            font=('orbitron',13),
                                            fg='white',
                                            bg='#33334d',
                                            anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()
        
        
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        
        headingLabel = tk.Label(self,
                                 text='ATM Management System',
                                 font=('orbitron',40,'bold'),
                                 foreground='white',
                                 background='#3d3d5c')
        headingLabel.pack(pady=25)
        
        option_label = tk.Label(self,
                                text='Options',
                                font=('orbitron',15),
                                foreground='white',
                                bg='#3d3d5c')
        option_label.pack()
        
        selection_label = tk.Label(self,
                                   text='Make a selection',
                                   font=('orbitron',14),
                                   foreground='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')
        
        button_frame = tk.Frame(self, background="#33334d")
        button_frame.pack(fill='both', expand=True)
        
        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = tk.Button(button_frame, text='Withdraw', command = withdraw, relief='raised', borderwidth=3, width=50, height=5)
        withdraw_button.grid(row=0, column=0, pady=5)
        
        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = tk.Button(button_frame, text='Deposit', command = deposit, relief='raised', borderwidth=3, width=50, height=5)
        deposit_button.grid(row=1, column=0, pady=5)
        
        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = tk.Button(button_frame, text='Check Balance', command = balance, relief='raised', borderwidth=3, width=50, height=5)
        balance_button.grid(row=2, column=0, pady=5)
        
        def exit():
            controller.show_frame('Cardpage')
        
  
        exit_button = tk.Button(button_frame, text='Exit', command = exit, relief='raised', borderwidth=3, width=50, height=5)
        exit_button.grid(row=3, column=0, pady=5)
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3d3d5c")
        self.controller = controller
        
        headingLabel = tk.Label(self,
                                 text='ATM Management System',
                                 font=('orbitron',40,'bold'),
                                 foreground='white',
                                 background='#3d3d5c')
        headingLabel.pack(pady=25)
        
        
        
       
        
        def withdraw(amount):
            global current_balance
            current_balance=current_balance-amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
        
        
        spacing_label = tk.Label(self,height=7,bg='#3d3d5c')
        spacing_label.pack()
        
       
        enter_amount_label = tk.Label(self,
                                text='Please Enter Amount',
                                font=('orbitron',15),
                                foreground='white',
                                bg='#3d3d5c')
        enter_amount_label.pack(pady=10)
        
       
        cash=tk.StringVar()
        amount_entry_space = tk.Entry(self,
                                        textvariable=cash,
                                        font=('orbitron',12),
                                        width=22)
        
        amount_entry_space.pack(ipady=7)
        
        
        
        def amt(_):
            global current_balance
            current_balance-=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set("")
            controller.show_frame("MenuPage")
            
        amount_entry_space.bind("<Return>",amt)
        
        
        
        button_frame = tk.Frame(self, bg="#33334d")
        button_frame.pack(fill='both', expand=True)
        
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()
        
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#3d3d5c")
        self.controller = controller
        
        headingLabel = tk.Label(self,
                                 text='ATM Management System',
                                 font=('orbitron',40,'bold'),
                                 foreground='white',
                                 background='#3d3d5c')
        headingLabel.pack(pady=25)
        
        spacing_label = tk.Label(self,height=4,bg='#3d3d5c')
        spacing_label.pack()
        
        deposit_money_Label = tk.Label(self,text='Enter amount',
                                  font=('orbitron',13),
                                  bg='#3d3d5c',
                                  fg='white')
        deposit_money_Label.pack(pady=10)
        
        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set("")
            
       
        cash=tk.StringVar()
        deposit_entry=tk.Entry(self, textvariable=cash, font=('orbitron',12), width=22)
        deposit_entry.pack(ipady=7)
        
        enter_button=tk.Button(self, text='Enter', command=deposit_cash, relief='raised', borderwidth=3, width=40, height=2)
        enter_button.pack(pady=10)
        
        two_tone_label=tk.Label(self, bg='#33334d')
        two_tone_label.pack(fill='both', expand=True)
        
        
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()

class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        
        headingLabel = tk.Label(self,
                                 text='ATM Management System',
                                 font=('orbitron',40,'bold'),
                                 foreground='white',
                                 background='#3d3d5c')
        headingLabel.pack(pady=25)
        
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self, textvariable=controller.shared_data['Balance'], font=('orbitron',13),fg='white',bg='#3d3d5c',anchor='w')
        balance_label.pack(fil='x')
        
        button_frame=tk.Frame(self,bg='#3d3d5c')
        button_frame.pack(fill='both',expand=True)
        
        def menu():
            controller.show_frame('MenuPage')
            
        
        menu_button = tk.Button(button_frame, command=menu, text='Menu', relief='raised', borderwidth=3, width=50, height=5)
        menu_button.grid(row=0, column=0, pady=5)
        
        def exit():
            controller.show_frame('Cardpage')
        exit_button = tk.Button(button_frame, text='Exit', command=exit, relief='raised', borderwidth=3, width=50, height=5)
        exit_button.grid(row=1, column=0, pady=5)
        
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        
        visa_pic = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image = visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic
        
        sbi_pic = tk.PhotoImage(file='sbi.png')
        sbi_label = tk.Label(bottom_frame, image = sbi_pic)
        sbi_label.pack(side='left')
        sbi_label.image = sbi_pic
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        
        tick()
        
        
    

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
