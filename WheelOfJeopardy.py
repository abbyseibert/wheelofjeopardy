from tkinter import *
import random,time
root = Tk()

class GameBoard:

    def __init__(self,cat_arr,round_two):
        self.canvas = Canvas(width=1000,height=750)
        self.cat_arr = cat_arr
        self.round_two = round_two
        self.player_one = [0, #score
                           1, #boolean, is it their turn?
                           0] #amount of free spins
        self.player_two = [0,0,0]
        self.player_three = [0,0,0]
        self.instructions = 'Player One, \nClick on the wheel to spin it.'
        self.spin_count = 0 #only fifty spins a round
        self.qs_left = 30 #start out with 30 questions on the board
        self.create_board()
        self.canvas.pack()
        self.spintime = 1
        self.cluetime = 0

    def create_board(self):
        # wheel 
        self.w_pos_one = [160,50,240,50,200,200]
        self.redone = self.canvas.create_polygon(self.w_pos_one,outline='red',fill='red',width=1)
        w_pos_two = [240,50,315,90,200,200]
        self.orangeone = self.canvas.create_polygon(w_pos_two,outline='orange',fill='orange',width=1)
        w_pos_three = [315,90,350,170,200,200]
        self.yellowone = self.canvas.create_polygon(w_pos_three,outline='yellow',fill='yellow',width=1)
        w_pos_four = [350,170,350,250,200,200]
        self.greenone = self.canvas.create_polygon(w_pos_four,outline='green',fill='green',width=1)
        w_pos_five = [350,250,315,310,200,200]
        self.blueone = self.canvas.create_polygon(w_pos_five,outline='blue',fill='blue',width=1)
        w_pos_six = [315,310,240,350,200,200]
        self.purpleone = self.canvas.create_polygon(w_pos_six,outline='purple',fill='purple',width=1)
        w_pos_seven = [240,350,160,350,200,200]
        self.blackone = self.canvas.create_polygon(w_pos_seven,outline='black',fill='black',width=1)
        w_pos_eight = [160,350,85,310,200,200]
        self.purpletwo = self.canvas.create_polygon(w_pos_eight,outline='purple',fill='purple',width=1)
        w_pos_nine = [85,310,50,250,200,200]                                         
        self.bluetwo = self.canvas.create_polygon(w_pos_nine,outline='blue',fill='blue',width=1)
        w_pos_ten = [50,250,50,170,200,200]
        self.greentwo = self.canvas.create_polygon(w_pos_ten,outline='green',fill='green',width=1)
        w_pos_eleven = [50,170,85,90,200,200]
        self.yellowtwo = self.canvas.create_polygon(w_pos_eleven,outline='yellow',fill='yellow',width=1)
        w_pos_twelve = [85,90,160,50,200,200]
        self.orangetwo = self.canvas.create_polygon(w_pos_twelve,outline='orange',fill='orange',width=1)
        # board
        self.canvas.create_rectangle(450,25,975,500,fill = 'blue')
        self.canvas.create_line(450,104,975,104,fill='black',width=3)
        self.canvas.create_line(450,183,975,183,fill='black',width=1)
        self.canvas.create_line(450,262,975,262,fill='black',width=1)
        self.canvas.create_line(450,341,975,341,fill='black',width=1)
        self.canvas.create_line(450,417,975,417,fill='black',width=1)
        self.canvas.create_line(537,25,537,500,fill='black',width=1)
        self.canvas.create_line(624,25,624,500,fill='black',width=1)
        self.canvas.create_line(712,25,712,500,fill='black',width=1)
        self.canvas.create_line(799,25,799,500,fill='black',width=1)
        self.canvas.create_line(886,25,886,500,fill='black',width=1)
        # board text 
        self.r1c1 = self.canvas.create_text(493,64,text=self.form_str(self.cat_arr[0]),fill='orange')
        self.r1c2 = self.canvas.create_text(580,64,text=self.form_str(self.cat_arr[1]),fill='orange')
        self.r1c3 = self.canvas.create_text(667,64,text=self.form_str(self.cat_arr[2]),fill='orange')
        self.r1c4 = self.canvas.create_text(754,64,text=self.form_str(self.cat_arr[3]),fill='orange')
        self.r1c5 = self.canvas.create_text(841,64,text=self.form_str(self.cat_arr[4]),fill='orange')
        self.r1c6 = self.canvas.create_text(928,64,text=self.form_str(self.cat_arr[5]),fill='orange')
        # board values - create an arr with round vals that way we can swap them at round two
        self.r2c1 = self.canvas.create_text(493,145,text='200',font=(24),fill='orange')
        self.r2c2 = self.canvas.create_text(580,145,text='200',font=(24),fill='orange')
        self.r2c3 = self.canvas.create_text(667,145,text='200',font=(24),fill='orange')
        self.r2c4 = self.canvas.create_text(754,145,text='200',font=(24),fill='orange')
        self.r2c5 = self.canvas.create_text(841,145,text='200',font=(24),fill='orange')
        self.r2c6 = self.canvas.create_text(928,145,text='200',font=(24),fill='orange')
        self.r3c1 = self.canvas.create_text(493,226,text='400',font=(24),fill='orange')
        self.r3c2 = self.canvas.create_text(580,226,text='400',font=(24),fill='orange')
        self.r3c3 = self.canvas.create_text(667,226,text='400',font=(24),fill='orange')
        self.r3c4 = self.canvas.create_text(754,226,text='400',font=(24),fill='orange')
        self.r3c5 = self.canvas.create_text(841,226,text='400',font=(24),fill='orange')
        self.r3c6 = self.canvas.create_text(928,226,text='400',font=(24),fill='orange')
        self.r4c1 = self.canvas.create_text(493,305,text='600',font=(24),fill='orange')
        self.r4c2 = self.canvas.create_text(580,305,text='600',font=(24),fill='orange')
        self.r4c3 = self.canvas.create_text(667,305,text='600',font=(24),fill='orange')
        self.r4c4 = self.canvas.create_text(754,305,text='600',font=(24),fill='orange')
        self.r4c5 = self.canvas.create_text(841,305,text='600',font=(24),fill='orange')
        self.r4c6 = self.canvas.create_text(928,305,text='600',font=(24),fill='orange')
        self.r5c1 = self.canvas.create_text(493,382,text='800',font=(24),fill='orange')
        self.r5c2 = self.canvas.create_text(580,382,text='800',font=(24),fill='orange')
        self.r5c3 = self.canvas.create_text(667,382,text='800',font=(24),fill='orange')
        self.r5c4 = self.canvas.create_text(754,382,text='800',font=(24),fill='orange')
        self.r5c5 = self.canvas.create_text(841,382,text='800',font=(24),fill='orange')
        self.r5c6 = self.canvas.create_text(928,382,text='800',font=(24),fill='orange')
        self.r6c1 = self.canvas.create_text(493,460,text='1000',font=(24),fill='orange')
        self.r6c2 = self.canvas.create_text(580,460,text='1000',font=(24),fill='orange')
        self.r6c3 = self.canvas.create_text(667,460,text='1000',font=(24),fill='orange')
        self.r6c4 = self.canvas.create_text(754,460,text='1000',font=(24),fill='orange')
        self.r6c5 = self.canvas.create_text(841,460,text='1000',font=(24),fill='orange')
        self.r6c6 = self.canvas.create_text(928,460,text='1000',font=(24),fill='orange')
        # wedge text // STORE STATE IN ARR
        text_pos_one = [200,115,270]
        self.spinagain_text = self.canvas.create_text(200,115,text='Spin Again',angle=270)
        text_pos_two = [240,130,240]
        self.catone_text = self.canvas.create_text(240,130,text=self.cat_arr[0],angle=240)
        text_pos_three = [270,165,210]
        self.loseturn_text = self.canvas.create_text(270,165,text='Lose Turn',angle=210)
        text_pos_four = [288,205,180]
        self.cattwo_text = self.canvas.create_text(288,205,text=self.cat_arr[1],angle=180)
        text_pos_five = [275,245,152]
        self.freeturn_text = self.canvas.create_text(275,245,text='Free Turn',angle=152)
        text_pos_six = [240,270,120]
        self.catthree_text = self.canvas.create_text(240,270,text=self.cat_arr[2],angle=120)
        text_pos_seven = [200,300,90]
        self.bankrupt_text = self.canvas.create_text(200,300,text='Bankrupt',angle=90,fill='white')
        text_pos_eight = [160,270,60]
        self.catfour_text = self.canvas.create_text(160,270,text=self.cat_arr[3],angle=60)
        text_pos_nine = [125,245,28]
        self.ochoice_text = self.canvas.create_text(125,245,text="Opponent's Choice",angle=28)
        text_pos_ten = [112,205,0]
        self.catfive_text = self.canvas.create_text(112,205,text=self.cat_arr[4],angle=0)
        text_pos_eleven = [130,165,-30]
        self.pchoice_text = self.canvas.create_text(130,165,text="Player's Choice",angle=-30)
        text_pos_twelve = [160,130,-60]
        self.catsix_text = self.canvas.create_text(160,130,text=self.cat_arr[5],angle=-60)
        # store where each wedge currently resides
        self.wheel_state = [[self.redone,self.w_pos_one],
                            [self.orangeone,w_pos_two],
                            [self.yellowone,w_pos_three],
                            [self.greenone,w_pos_four],
                            [self.blueone,w_pos_five],
                            [self.purpleone,w_pos_six],
                            [self.blackone,w_pos_seven],
                            [self.purpletwo,w_pos_eight],
                            [self.bluetwo,w_pos_nine],
                            [self.greentwo,w_pos_ten],
                            [self.yellowtwo,w_pos_eleven],
                            [self.orangetwo,w_pos_twelve]]
        self.text_state = [[self.spinagain_text,text_pos_one],
                           [self.catone_text,text_pos_two],
                           [self.loseturn_text,text_pos_three],
                           [self.cattwo_text,text_pos_four],
                           [self.freeturn_text,text_pos_five],
                           [self.catthree_text,text_pos_six],
                           [self.bankrupt_text,text_pos_seven],
                           [self.catfour_text,text_pos_eight],
                           [self.ochoice_text,text_pos_nine],
                           [self.catfive_text,text_pos_ten],
                           [self.pchoice_text,text_pos_eleven],
                           [self.catsix_text,text_pos_twelve]]
        
        # instructions box and text & player's score
        self.canvas.create_rectangle(25,525,975,725,outline='black',fill='white')
        self.canvas.create_text(85,540,text='Player One Score:  ')
        self.canvas.create_text(85,560,text='Player Two Score:  ')
        self.canvas.create_text(85,580,text='Player Three Score:')
        self.pone = self.canvas.create_text(180,540,text=self.player_one[0])
        self.ptwo = self.canvas.create_text(180,560,text=self.player_two[0])
        self.pthree = self.canvas.create_text(180,580,text=self.player_three[0])
        self.instr_box = self.canvas.create_text(500,600,text=self.instructions,font=(24))
        self.num_spins = self.canvas.create_text(500,700,text=self.spin_count)
        # clacker
        clacker_points = [190,30,210,30,200,60]
        self.canvas.create_polygon(clacker_points,
                                   outline='grey',
                                   fill='grey',
                                   width=1)
    

    def click(self,event): # listen for clicks
        # check if it's time for a spin click or time for a clue click
        if self.canvas.find_withtag(CURRENT):
            print(event.x)
            print(event.y)
            self.spin()
        
    def spin(self):
        # update spin count
        self.canvas.delete(self.num_spins)
        self.spin_count += 1
        self.num_spins = self.canvas.create_text(500,700,text=self.spin_count)
        spin_times = random.randint(1,20)
        for i in range(spin_times):
            self.canvas.after(100)
            self.rotate()
        self.what_now()

    def rotate(self):
        #rotate wedge
        wedge_hold = self.wheel_state[0][1]
        self.canvas.coords(self.redone,self.wheel_state[1][1])
        self.canvas.coords(self.orangeone,self.wheel_state[2][1])
        self.canvas.coords(self.yellowone,self.wheel_state[3][1])
        self.canvas.coords(self.greenone,self.wheel_state[4][1])
        self.canvas.coords(self.blueone,self.wheel_state[5][1])
        self.canvas.coords(self.purpleone,self.wheel_state[6][1])
        self.canvas.coords(self.blackone,self.wheel_state[7][1])
        self.canvas.coords(self.purpletwo,self.wheel_state[8][1])
        self.canvas.coords(self.bluetwo,self.wheel_state[9][1])
        self.canvas.coords(self.greentwo,self.wheel_state[10][1])
        self.canvas.coords(self.yellowtwo,self.wheel_state[11][1])
        self.canvas.coords(self.orangetwo,wedge_hold)

        #rotate text
        self.canvas.delete(self.spinagain_text)
        self.spinagain_text = self.canvas.create_text(self.text_state[1][1][0],self.text_state[1][1][1],text='Spin Again',angle=self.text_state[1][1][2])
        self.canvas.delete(self.catone_text)
        self.catone_text = self.canvas.create_text(self.text_state[2][1][0],self.text_state[2][1][1],text=self.cat_arr[0],angle=self.text_state[2][1][2])
        self.canvas.delete(self.loseturn_text)
        self.loseturn_text = self.canvas.create_text(self.text_state[3][1][0],self.text_state[3][1][1],text='Lose Turn',angle=self.text_state[3][1][2])
        self.canvas.delete(self.cattwo_text)
        self.cattwo_text = self.canvas.create_text(self.text_state[4][1][0],self.text_state[4][1][1],text=self.cat_arr[1],angle=self.text_state[4][1][2])
        self.canvas.delete(self.freeturn_text)
        self.freeturn_text = self.canvas.create_text(self.text_state[5][1][0],self.text_state[5][1][1],text='Free Turn',angle=self.text_state[5][1][2])
        self.canvas.delete(self.catthree_text)
        self.catthree_text = self.canvas.create_text(self.text_state[6][1][0],self.text_state[6][1][1],text=self.cat_arr[2],angle=self.text_state[6][1][2])
        self.canvas.delete(self.bankrupt_text)
        self.bankrupt_text = self.canvas.create_text(self.text_state[7][1][0],self.text_state[7][1][1],text='Bankrupt',angle=self.text_state[7][1][2],fill='white')
        self.canvas.delete(self.catfour_text)
        self.catfour_text = self.canvas.create_text(self.text_state[8][1][0],self.text_state[8][1][1],text=self.cat_arr[3],angle=self.text_state[8][1][2])
        self.canvas.delete(self.ochoice_text)
        self.ochoice_text = self.canvas.create_text(self.text_state[9][1][0],self.text_state[9][1][1],text="Opponent's Choice",angle=self.text_state[9][1][2])
        self.canvas.delete(self.catfive_text)
        self.catfive_text = self.canvas.create_text(self.text_state[10][1][0],self.text_state[10][1][1],text=self.cat_arr[4],angle=self.text_state[10][1][2])
        self.canvas.delete(self.pchoice_text)
        self.pchoice_text = self.canvas.create_text(self.text_state[11][1][0],self.text_state[11][1][1],text="Player's Choice",angle=self.text_state[11][1][2])
        self.canvas.delete(self.catsix_text)
        self.catsix_text = self.canvas.create_text(self.text_state[0][1][0],self.text_state[0][1][1],text=self.cat_arr[5],angle=self.text_state[0][1][2])


        # store where each wedge currently resides // BREAK THIS INTO SAVEWHEEL() & GETWHEEL()
        self.wheel_state = [[self.redone,self.wheel_state[1][1]],
                            [self.orangeone,self.wheel_state[2][1]],
                            [self.yellowone,self.wheel_state[3][1]],
                            [self.greenone,self.wheel_state[4][1]],
                            [self.blueone,self.wheel_state[5][1]],
                            [self.purpleone,self.wheel_state[6][1]],
                            [self.blackone,self.wheel_state[7][1]],
                            [self.purpletwo,self.wheel_state[8][1]],
                            [self.bluetwo,self.wheel_state[9][1]],
                            [self.greentwo,self.wheel_state[10][1]],
                            [self.yellowtwo,self.wheel_state[11][1]],
                            [self.orangetwo,wedge_hold]]
        self.text_state = [[self.spinagain_text,self.text_state[1][1]],
                           [self.catone_text,self.text_state[2][1]],
                           [self.loseturn_text,self.text_state[3][1]],
                           [self.cattwo_text,self.text_state[4][1]],
                           [self.freeturn_text,self.text_state[5][1]],
                           [self.catthree_text,self.text_state[6][1]],
                           [self.bankrupt_text,self.text_state[7][1]],
                           [self.catfour_text,self.text_state[8][1]],
                           [self.ochoice_text,self.text_state[9][1]],
                           [self.catfive_text,self.text_state[10][1]],
                           [self.pchoice_text,self.text_state[11][1]],
                           [self.catsix_text,self.text_state[0][1]]]
        self.canvas.update_idletasks()

    # look at the wedge in pos_one. move forward accordingly.
    def what_now(self):
        print("What did I land on?")
        for i in range(len(self.wheel_state)):
            if self.wheel_state[i][1] == self.w_pos_one:
                print(self.wheel_state[i][0]) # prints the color's position in wheel_state; use to map to cats
        if self.spin_count > 3: # this should probably exist in a separate function for time/spin monitoring
            self.spin_count = 0
            self.canvas.delete("all")
            self.round_one = self.cat_arr
            self.cat_arr = self.round_two
            self.create_board()
            self.canvas.pack()
        
    def clue_select(self):
        print("sup")

    def form_str(self,string):
        if len(string) > 10:
            middle = int(len(string)/2)
            str_arr = string.split()
            form_string = string[0:middle] + "\n" + string[middle:len(string)]
        else:
            form_string = string
        return form_string

# Menu class - do you want to use random categories? enter your own cs, qs and as?
class UserMenu:
    def __init__(self):
        print("\n\n--- THIS IS THE WHEEL OF JEOPARDY ---")
        print("... Thank you, Johnny.\n\n")
        print("1 - Play with a random selection of categories")
        print("2 - Define my own categories")
        print("Q - Quit")
        self.user_input()

    def user_input(self):
        selection = str(input("\nPlease select one of the options above: ")).upper()
        options = ['1','2','Q']
        while selection not in options:
            selection = str(input("\nPlease select one of the options above: "))
        if selection == '1':
            print("Okay")
            self.init_cats()
        elif selection == '2':
            print("2's a good option")
            self.create_cats()
        else:
            print("Exiting game...")
            exit()

    def create_cats(self):
        print("\nYou will choose 12 categories as well as 6 questions for each.\n")
        cat_one = str(input("What will be the first category? "))
        #c1_q1 = str(input("\nWhat will be the first question in " + cat_one + "? "))
        cat_two = str(input("What will be the second category? "))
        cat_three = str(input("What will be the third category? "))
        cat_four = str(input("What will be the fourth category? "))
        cat_five = str(input("What will be the fifth category? "))
        cat_six = str(input("What will be the sixth category? "))
        cat_arr = [cat_one,cat_two,cat_three,cat_four,cat_five,cat_six]
        test = GameBoard(cat_arr)
        test.canvas.bind("<Button-1>", test.click)
        
    def init_cats(self):
        dflt_cats = ["Supreme Court Justices",
                     "US Presidents",
                     "Computers",
                     "European Geography",
                     "Movies of the '80s",
                     "Quoth the Poet",
                     "Cheese",
                     "Famous Battles",
                     "Dystopian Novels",
                     "Anagrams",
                     "Say It Ain't Sew",
                     "The 'B'est in the Biz"]
        cat_one = dflt_cats[random.randint(0,11)]
        dflt_cats.remove(cat_one)
        cat_two = dflt_cats[random.randint(0,10)]
        dflt_cats.remove(cat_two)
        cat_three = dflt_cats[random.randint(0,9)]
        dflt_cats.remove(cat_three)
        cat_four = dflt_cats[random.randint(0,8)]
        dflt_cats.remove(cat_four)
        cat_five = dflt_cats[random.randint(0,7)]
        dflt_cats.remove(cat_five)
        cat_six = dflt_cats[random.randint(0,6)]
        dflt_cats.remove(cat_six)
        cat_arr = [cat_one,cat_two,cat_three,cat_four,cat_five,cat_six]
        # pass the dflt_cats for round two
        test = GameBoard(cat_arr,dflt_cats)
        test.canvas.bind("<Button-1>", test.click)
            
newgame = UserMenu()  
root.mainloop()
