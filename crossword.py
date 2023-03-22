#!/usr/bin/env python3
import random
import numpy as np
from tkinter import *

sqrsize = 30  # size of squares
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
                        globals()['dif' + str(count)] = [acounter, bcounter]

                    else:
                        globals()['vh' + str(count)] = 0
                        globals()['dif' + str(count)] = [-bcounter, -acounter]
                except:
                    pass
                globals()['match' + str(count)] = swrds.index(first_letter)
                match = True  # shows that a match was found, allowing more computation to be ran
                break

            bcounter += 1
        acounter += 1
        if match == True:
            break

    return match


# calculate the positon of each letter in a word
def pos (word, init_x, init_y, vh):
    x = int(init_x)
    y = int(init_y)
    for lttr in word:
        lttr.append(x)
        lttr.append(y)
        if vh == 0:
            x += 1
        else:
            y += 1
    return word

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
    match_counter = []  # later used to count positions of words
    wrds = []  # list of words
    dfntn = []  # list of definitions/clues
    swrds = []  # list of words being compared in ordering
    words = random.sample(wordslist, k = 10)   # selects random words + definitions (still paired) and makes them into a new list
    works = True
    


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
        match_counter.append(compare(random.choice(lister), swrds [count]))
        lister.append(swrds [count])








    # checks whether each found a match
    for check in match_counter:
        if check == False:
            fmatch = False

    if fmatch == True:
        for adder in swrds:
            for addder in adder:
                if len(addder) == 1:
                    addder.append(0)





        xpos0 = 0
        ypos0 = 0
        swrds[0] = pos(swrds[0], xpos0, ypos0, vh0)
        xpos1 = globals()['xpos' + str(match1)] + dif1[0]
        ypos1 = globals()['ypos' + str(match1)] - dif1[1]
        swrds[1] = pos(swrds[1], xpos1, ypos1, vh1)
        xpos2 = globals()['xpos' + str(match2)] + dif2[0]
        ypos2 = globals()['ypos' + str(match2)] - dif2[1]
        swrds[2] = pos(swrds[2], xpos2, ypos2, vh2)
        xpos3 = globals()['xpos' + str(match3)] + dif3[0]
        ypos3 = globals()['ypos' + str(match3)] - dif3[1]
        swrds[3] = pos(swrds[3], xpos3, ypos3, vh3)
        xpos4 = globals()['xpos' + str(match4)] + dif4[0]
        ypos4 = globals()['ypos' + str(match4)] - dif4[1]
        swrds[4] = pos(swrds[4], xpos4, ypos4, vh4)
        xpos5 = globals()['xpos' + str(match5)] + dif5[0]
        ypos5 = globals()['ypos' + str(match5)] - dif5[1]
        swrds[5] = pos(swrds[5], xpos5, ypos5, vh5)
        xpos6 = globals()['xpos' + str(match6)] + dif6[0]
        ypos6 = globals()['ypos' + str(match6)] - dif6[1]
        swrds[6] = pos(swrds[6], xpos6, ypos6, vh6)
        xpos7 = globals()['xpos' + str(match7)] + dif7[0]
        ypos7 = globals()['ypos' + str(match7)] - dif7[1]
        swrds[7] = pos(swrds[7], xpos7, ypos7, vh7)
        xpos8 = globals()['xpos' + str(match8)] + dif8[0]
        ypos8 = globals()['ypos' + str(match8)] - dif8[1]
        swrds[8] = pos(swrds[8], xpos8, ypos8, vh8)
        xpos9 = globals()['xpos' + str(match9)] + dif9[0]
        ypos9 = globals()['ypos' + str(match9)] - dif9[1]
        swrds[9] = pos(swrds[9], xpos9, ypos9, vh9)
        
        all_letters = [word for sublist in swrds for word in sublist]
        for that in all_letters:
            for other in all_letters:
                if that[-1] == other [-1] and that[-2] == other [-2] and that != other:
                    works = False
        if works == True:
            fwrds.append(swrds)
            fdfntn.append(dfntn)


for each in fwrds:
    max_left = 0
    max_up = 0
    max_right = 0
    max_down = 0
    for every in each:
        for one in every:
            if one[-2] < max_left:
                max_left = one[-2]
            if one[-1] < max_up:
                max_up = one[-1]
            if one[-2] > max_right:
                max_right = one[-2]
            if one[-1] > max_down:
                max_down = one[-1]
    for a_word in each:
        for a_letter in a_word:
            a_letter[-2] -= max_left
            a_letter[-1] -= max_up


# the following section is for creating the window
root = Tk()   # root is the window
root.title("Crossword Puzzle")   # sets the title of the window
root.geometry("1000x1000")   # sets size and shape of window

# canvas
w = Canvas(root, width=(max_right-max_left+1)*sqrsize, height=(max_down-max_up+1)*sqrsize)   # creates a canvas widget, allowing shapes to be drawn inside the window
w.create_rectangle(0, 0, (max_right-max_left+1)*sqrsize, (max_down-max_up+1)*sqrsize, fill="black", outline = 'white')   # black background for the puzzle

# text for clues
T = Text(root, height = 400, width = 400, wrap='word')   # creates a text widget for clues
l = Label(root, text = "\nClues")   # sets title of widget


# Verticle clues
T.insert('end', "Verticle: \n")
for defindex, definition in enumerate(fdfntn[-1]):
    if fwrds[-1] [defindex] [0] [-2] == fwrds[-1] [defindex] [1] [-2]:
        T.insert('end', str(defindex+1)+"." + definition + "\n")   #displays clues

# Horizontal Clues
T.insert('end', "\n\nHorizontal:\n")
for defindex, definition in enumerate(fdfntn[-1]):
    if fwrds[-1] [defindex] [0] [-2] != fwrds[-1] [defindex] [1] [-2]:
        T.insert('end', str(defindex+1)+"." + definition + "\n")   #displays clues

# puts squares into place
index_counter = 1
for wrd_index, f in enumerate(fwrds[-1]):
    for lttr in f:
        w.create_rectangle(lttr[-2]*sqrsize, lttr[-1]*sqrsize, lttr[-2]*sqrsize+ sqrsize, lttr[-1]*sqrsize+sqrsize, fill="white", outline = 'black')
    w.create_text(f[0][-2]*sqrsize + 7, f[0] [-1]*sqrsize+6, text=wrd_index+1)



"""displays the correct words in the canvas"""
# Add a button to toggle this
# for wrd_answer in fwrds[-1]:
    # for lttr_answer in wrd_answer:
        # w.create_text(lttr_answer[-2]*sqrsize+10, lttr_answer[-1]*sqrsize+10, text=lttr_answer[0])


# puts items into window and closes words file
T.configure(state='disabled')   # disables the ability to edit the text widget after the program has been run
w.pack()
l.pack()
T.pack()
root.mainloop()
