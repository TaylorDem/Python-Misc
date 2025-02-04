# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:45:39 2024

This implements 3 different page replacement algorithms:
    First in First out, Least Recently Used, and Second Chance
    
Commented out section to randomize the reference string for further testing.
Classes created for LRU and Second Chance to ensure extra info is attached to 
the frame/page.

@author: demar
"""

"""
#check with extra random values to ensure algorithms are correct
import random
refstring = [random.randint(1,9) for _ in range(20)]
"""

refstring = [1,4,6,8,2,3,5,6,2,1]


#FIFO
def FIFO(frames):
    print("FIFO:")
    pages = [0] * frames    #dynamically allocated number of frames
    faultcount = 0          #keeps track of faults
    recentchange = 0        #keeps track of frame that was changed
    for x in refstring:     #cycle through the refstring
        Found = False       #flag for if the page was found
        for f in range(frames):     #cycle through frames
            #found page
            if x == pages[f]:
                Found = True
                break
            #empty frames
            if not pages[f]:
                pages[f] = x
                faultcount+= 1
                recentchange+= 1
                Found = True
                break
        #replacement needed
        if not Found:
            #recent change mod frames will give us the oldest frame unchanged
            pages[recentchange%frames] = x
            faultcount += 1
            recentchange+=1
        #print current data each loop
        print(x, ": ")
        print(pages,"\n")
    return faultcount


#keep counter with the page
class LRU_page():
    def __init__(self):
        self.page = 0
        self.counter = 0

def LRU(frames):
    print("LRU:")
    pages = [LRU_page() for l in range(frames)] #generate frames list
    faultcount = 0
    #instead of recent change we put a counter in the page dat
    changecounter = 0
    for x in refstring:
        print(x, ": ")
        Found = False
        for f in range(frames):
            #found page
            if x == pages[f].page:
                #update counter when found
                pages[f].counter = changecounter
                changecounter+=1
                Found = True
                break
            #empty frames
            if pages[f].page == 0:
                pages[f].page = x
                pages[f].counter = changecounter
                faultcount+= 1
                changecounter += 1
                Found = True
                break
        if not Found:
            #lambda function to grab the counters for the min function
            lru = min(pages, key=lambda i: i.counter)
            #lru is a LRU_page so we can index for position in the list
            lru_index = pages.index(lru)
            pages[lru_index].page = x
            pages[lru_index].counter = changecounter
            faultcount+= 1
            changecounter += 1
            
        #print out the current data:
        print("Pages:", end=" ")
        for p in range(frames):
            print(pages[p].page, end=" ")
        print("\nCount:", end=" ")
        for p in range(frames):
            print(pages[p].counter, end=" ")
        print("\n")
    return faultcount



#keep a bool "bit" for second chances
class SC_page():
    def __init__(self):
        self.page = 0
        self.sc = False
        
        
def SC(frames):
    print("Second Chance:")
    pages = [SC_page() for q in range(frames)]
    faultcount = 0
    recentchange = 0
    for x in refstring:
        print(x, ": ")
        Found = False
        for f in range(frames):
            #found page
            if x == pages[f].page:
                pages[f].sc = True
                Found = True
                break
            #empty frames
            if not pages[f].page:
                pages[f].page = x
                faultcount+= 1
                recentchange+= 1
                Found = True
                break
        #using FIFO algorithm with a check for second chance
        if not Found:
            for c in range(frames):  #loop through them all if we need to
                #if we have a second chance flip the bit to false and move on
                if pages[recentchange%frames].sc: 
                    pages[recentchange%frames].sc = False
                    recentchange+=1
                #when we find the one thats good to replace break the loop
                if not pages[recentchange%frames].sc: 
                    break
            pages[recentchange%frames].page = x
            faultcount+=1
            recentchange+=1
            
        #print current data:
        print("Pages:",end="\t")
        for p in range(frames):
            print(pages[p].page, end=" ")
        print("\nBits: ",end="\t")
        for p in range(frames):
            if pages[p].sc:
                print("t", end=" ")
            else:
                print("f", end=" ")
        print("\n")
    return faultcount



#run all algorithms and compare:
num_frames = 3
fifo_fault = FIFO(num_frames)
lru_fault = LRU(num_frames)
sc_fault = SC(num_frames)
print("Faults of FIFO v LRU v SC with", num_frames, "frames: ", \
      fifo_fault, "v", lru_fault, "v", \
          sc_fault, " respectively.")
        