#!/usr/bin/env python3
import random
import numpy as np
from tkinter import *

squarex = 0  # x coordinate of squares
squarey = 0  # y coordinate of squares
sqrsize = 20  # size of squares
wordslist = []  # list of words and definitions/clues

swrds = []  # list of words being compared in ordering
fwrds = []  # final list of words
match = False  # to check whether or not there was a match
fwrd = []

print("this may take a while...")  # to show that it is working, and that it may take a while

# open words file
my_file = open("Crossword/words.txt", "r")    # opening the file in 'read' mode
data = my_file.read()   # reading the file

# removes all new lines, and splits strings on the '.'s into a list
data_into_list = data.replace("\n", "").split(".")
my_file.close()
# turns the previous list into a list of lists; word and then definition
for i in np.arange(0, len(data_into_list) + 1, 2):
    wordslist.append(data_into_list[i:i+2])
words = random.sample(wordslist, k = 10)   # selects random words + definitions (still paired) and makes them into a new list



for litter in words [0]:
    sletters = []
    for bitter in litter:
        spbitter = bitter.split()
        sletters.append(spbitter)
    swrds.append(sletters)
    words[0] = swrds

def compare (first_letter, second_letter):
    match = False  # if false at end of comparison, skips order

    acounter = 0  # checks location of matched "a" letters
    for ab in first_letter:
        bcounter = 0  # checks location of matched "b" letters

 
        for bb in second_letter:
            if ab == bb:
                first_letter[acounter].append (counter)  # adds counter to matched letters
                second_letter[bcounter].append (counter)  # adds counter to matched letters
                match = True  # shows that a match was found, allowing more computation to be ran
                break
            
            bcounter += 1

        acounter += 1
        if match == True:
            break

    return match

# goes through different combinations of words
# eliminates some that don't work
# this part will take a while
for a in words:
    for b in words:
        if a != b:  # to avoid duplicates
            counter = 0  # number added to the matches to differentiate between them
            an = list(a)  # this had to be done so it doesn't modify the original list
            bn = list(b)
            match = compare(an[0], bn[0])
            if match == True:  # it only will keep comparing if there is a match
                for c in words:
                    if a != c and b != c:  # to avoid duplicates
                        cn = list(c)
                        counter = 1  # number added to the matches to differentiate between them
                        match = compare(bn[0], cn[0])  # first compares c to b
                        if match == False:
                            match = compare(an[0], cn[0])
                        
                        if match == True:
                            for d in words:
                                if a != d and b != d and c != d:  # to avoid duplicates
                                    counter = 2  # number added to the matches to differentiate between them
                                    dn = list(d)
                                    match = compare(cn[0], dn[0])
                                    if match == False:
                                        match = compare(bn[0], dn[0])
                                    if match == False:
                                        match = compare(an[0], dn[0])
                                    
                                    if match == True:
                                        for e in words:
                                            if a != e and b != e and c != e and d != e:  # to avoid duplicates
                                                counter = 3  # number added to the matches to differentiate between them
                                                en = list(e)
                                                match = compare(dn[0], en[0])
                                                if match == False:
                                                    match = compare(cn[0], en[0])
                                                if match == False:
                                                    match = compare(bn[0], en[0])
                                                if match == False:
                                                    match == compare(an[0], en[0])
                                                
                                                if match == True:
                                                    for f in words:
                                                        if a != f and b != f and c != f and d != f and e != f:  # to avoid duplicates
                                                            counter = 4  # number added to the matches to differentiate between them
                                                            fn = list(f)
                                                            match = compare(en[0], fn[0])
                                                            if match == False:
                                                                match == compare(dn[0], fn[0])
                                                            if match == False:
                                                                match == compare(cn[0], fn[0])
                                                            if match == False:
                                                                match = compare(bn[0], fn[0])
                                                            if match == False:
                                                                compare(an[0], fn[0])
                                                            
                                                            if match == True:
                                                                for g in words:
                                                                    if a != g and b != g and c != g and d != g and e != g and f != g:  # to avoid duplicates
                                                                        counter = 5  # number added to the matches to differentiate between them
                                                                        gn = list(g)
                                                                        match = compare(fn[0], gn[0])
                                                                        if match == False:
                                                                            match == compare(en[0], gn[0])
                                                                        if match == False:
                                                                            match = compare(dn[0], gn[0])
                                                                        if match == False:
                                                                            match == compare(cn[0], gn[0])
                                                                        if match == False:
                                                                            match = compare(bn[0], gn[0])
                                                                        if match == False:
                                                                            match = compare(an[0], gn[0])
                                                                        
                                                                        if match == True:    
                                                                            for h in words:
                                                                                if a != h and b!= h and c != h and d != h and e != h and f != h and g != h:  # to avoid duplicates
                                                                                    counter = 6  # number added to the matches to differentiate between them
                                                                                    hn = list(h)
                                                                                    match = compare(gn[0], hn[0])
                                                                                    if match == False:
                                                                                        match = compare(fn[0], hn[0])
                                                                                    if match == False:
                                                                                        match == compare(en[0], hn[0])
                                                                                    if match == False:
                                                                                        match = compare(dn[0], hn[0])
                                                                                    if match == False:
                                                                                        match == compare(cn[0], hn[0])
                                                                                    if match == False:
                                                                                        match = compare(bn[0], hn[0])
                                                                                    if match == False:
                                                                                        match = compare(an[0], hn[0])
                                                                                    
                                                                                    if match == True:
                                                                                        for i in words:
                                                                                            if a != i and b != i and c != i and d != i and e != i and f != i and g != i and h != i:  # to avoid duplicates
                                                                                                iN = list(i)
                                                                                                match = compare(hn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(gn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(fn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(en[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(dn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(cn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(bn[0], iN[0])
                                                                                                if match == False:
                                                                                                    match = compare(an[0], iN[0])
                                                                                                
                                                                                                if match == True:

                                                                                                    for j in words:
                                                                                                        if a != j and b != j and c != j and d != j and e != j and f != j and g != j and h != j and i != j:  # to avoid duplicates
                                                                                                            # need to continue pattern here but haven't gotten around to it yet
                                                                                                            jn = list(j)
                                                                                                            match = compare(iN[0], jn)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                            
                                                                                                            if match == True:
                                                                                                                cwrd = []
                                                                                                                cwrd.append(a)
                                                                                                                
                                                                                                                cwrd.append(b)
                                                                                                                cwrd.append(c)
                                                                                                                cwrd.append(d)
                                                                                                                cwrd.append(e)
                                                                                                                cwrd.append(f)
                                                                                                                cwrd.append(g)
                                                                                                                cwrd.append(h)
                                                                                                                cwrd.append(i)
                                                                                                                cwrd.append(j)
                                                                                                                fwrd.append(cwrd)


# this section creates the window
root = Tk()
root.title("Crossword Puzzle")  # sets the title of the window
root.geometry("1000x1000")   # sets size and shape of window

# canvas
w = Canvas(root, width=400, height=400)  # creates a canvas widget, allowing shapes to be drawn inside the window
w.create_rectangle(0, 0, 400, 400, fill="black", outline = 'white')   # black background for the puzzle

# text for clues
T = Text(root, height = 400, width = 400, wrap='word')   # creates a text widget for clues
l = Label(root, text = "Clues")  # sets title of widget 




# WILL BE MODIFIED
for definition in words [1]:
    T.insert('end', definition + "\n \n")  # displays clues
for wrd in words [0]:
    # puts squares into place

    for f in wrd:
        w.create_rectangle(squarex, squarey, squarex + sqrsize, squarey + sqrsize, fill="white", outline = 'black')
        squarex += sqrsize

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
