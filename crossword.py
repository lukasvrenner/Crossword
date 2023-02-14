#!/usr/bin/env python3
import random
import numpy as np
from tkinter import *

squarex = 0  # x coordinate of squares
squarey = 0  # y coordinate of squares
sqrsize = 20  # size of squares
wordslist = []  # list of words and definitions/clues


fwrds = []  # final list of words
fdfntn = []
match = False  # to check whether or not there was a match


def compare (first_letter, second_letter):
    match = False
    acounter = 0  # checks location of matched "a" letters
    for ab in first_letter:
        bcounter = 0  # checks location of matched "b" letters

 
        for bb in second_letter:
            if ab == bb:
                # counter is added to matched letters, so that matched letters can be tracked
                first_letter[acounter].append (count)  # adds counter to matched letters
                second_letter[bcounter].append (count)  # adds counter to matched letters
                
                # sets verticle or horizontal
                try:
                    if globals()['vh' + str(swrds.index(first_letter))] == 0:
                        globals()['vh' + str(count)] = 1
                    else:
                        globals()['vh' + str(count)] = 0
                except:
                    pass
                # distance from begining of each word to the match
                globals()['dif' + str(count)] = [acounter - len(first_letter), bcounter]
                match = True  # shows that a match was found, allowing more computation to be ran
                break
            
            bcounter += 1
        acounter += 1
        if match == True:
            break

    return match

# open words file
my_file = open("words.txt", "r")    # opening the file in 'read' mode
data = my_file.read()   # reading the file

# removes all new lines, and splits strings on the '.'s into a list
data_into_list = data.replace("\n", "").split(".")
my_file.close()


# turns the previous list into a list of lists; word and then definition
for i in np.arange(0, len(data_into_list) + 1, 2):
    wordslist.append(data_into_list[i:i+2])
wordslist.remove(wordslist[-1])  # last item is [], so this is removed to avoid errors






# this part is done 10000 times to find the best solution of words   
for i in range (10000):
    vh0 = 0  # 0 for horizontal, 1 for verticle
    fmatch = True
    counter = []  # later used to count positions of words
    wrds = []  # list of words
    dfntn = []  # list of definitions/clues

    swrds = []  # list of words being compared in ordering
    words = random.sample(wordslist, k = 10)   # selects random words + definitions (still paired) and makes them into a new list
    for j in words:
        wrds.append(j[0])
        dfntn.append(j[1])
        
    for litter in wrds:
        sletters = []
        for bitter in litter:
            spbitter = bitter.split()
            sletters.append(spbitter)
        swrds.append(sletters)
    lister = [swrds[0]]
    
    # the following section compares the letters of the list
    for count in range(1, 10):
        counter.append(compare(random.choice(lister), swrds [count]))
        lister.append(swrds [count])
    
    
                

        
    
    
    # checks whether each found a match
    for check in counter:
        if check == False:
            fmatch = False
            
    if fmatch == True:     
        for adder in swrds:
            for addder in adder:
                if len(addder) == 1:
                    addder.append(0)
                    
                    
        
        xpos = 0
        ypos = 0
        for stuff in swrds:
            
            if globals()['vh' + str(swrds.index(stuff))] == 0:
                for things in stuff:
                    things.append(xpos)
                    things.append(ypos)
                    xpos += 1
            else:
                for things in stuff:
                    things.append(xpos)
                    things.append(ypos)
                    ypos += 1
            if swrds.index(stuff)!=9:
                xpos += globals()['dif' + str(swrds.index(stuff)+1)] [0]
                ypos -= globals()['dif' + str(swrds.index(stuff)+1)] [1]
                    
                    
                    
        fwrds.append(swrds)
        fdfntn.append(dfntn)



print(fwrds[-1])

for this in fwrds:
    for that in this:
        for no in that:
            for yes in that:
                if yes[-1] == no[-1] and yes[-2] == no[-2] and yes != no:
                    fwrds.remove[this]


# the following section is for creating the window
root = Tk()   # root is the window
root.title("Crossword Puzzle")   # sets the title of the window
root.geometry("1000x1000")   # sets size and shape of window

# canvas
w = Canvas(root, width=400, height=400)   # creates a canvas widget, allowing shapes to be drawn inside the window
w.create_rectangle(0, 0, 400, 400, fill="black", outline = 'white')   # black background for the puzzle

# text for clues
T = Text(root, height = 400, width = 400, wrap='word')   # creates a text widget for clues
l = Label(root, text = "Clues")   # sets title of widget 



for definition in fdfntn[-1]:
    T.insert('end', definition + "\n \n")   #displays clues
for wrd in wrds:
    # puts squares into place
    # WILL BE MODIFIED
    for f in fwrds[-1]:
        for lttr in f:
            w.create_rectangle(lttr[-2]*sqrsize, lttr[-1]*sqrsize, lttr[-2]*sqrsize+ sqrsize, lttr[-1]*sqrsize*sqrsize, fill="white", outline = 'black')


    # changes box positions -- DELETE!
    squarex = 0
    squarey += sqrsize * 2

# print(fwrd)
# puts items into window and closes words file
T.configure(state='disabled')   # disables the ability to edit the text widget after the program has been run
w.pack()
l.pack()
T.pack()
root.mainloop()