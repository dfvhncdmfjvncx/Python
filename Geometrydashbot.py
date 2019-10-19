# The import statments allow the program to use code made by other people for specific tasks.
#Code that is made by others and released for anyone to use are called modules.
import PIL.ImageGrab
import pyautogui
import time
import pytesseract
import random
''' for import pytesseract we have to use this statement to allow the module to use a special file on my computer'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\js2t\AppData\Local\Tesseract-OCR\tesseract.exe'


''' This code holds coordinates on the screen, so the computer can click on them'''
class Coordinates:
    replaybtn = (648, 845)
    nums = (750, 550)


'''This function clicks the geometry dash restart button.
 functions are pieces of code that are stored, and you can run them anywhere by typing the functions name.'''
def click_restart():
    pyautogui.click(Coordinates.replaybtn)


''' this function takes in a list, ex. [0,1,2,5,6,8,4,] and returns the the second item in it.'''
def sort_second(val):
    return val[1]


''' This function creates a population of lists by taking in the amount of lists and the length of the lists.'''
def initialize(length_of_list, population):
    motherlist = []
    for person in range(population):
        motherlist.append([])
        for binary in range(length_of_list):
            motherlist[person].append(random.randint(0, 1))
    return motherlist


''' This function takes in a list and makes it 'play' the game. It gives out the score of the list.'''
def fitness_scorer(inp):
    click_restart()
    time.sleep(0.1)
    t0 = time.time()
    time.sleep(0.1)
    for num in inp:
        if num == 1:
            pyautogui.keyDown('space')
            time.sleep(0.05)
            pyautogui.keyUp('space')
            time.sleep(0.2)
        img = PIL.ImageGrab.grab(
            bbox=(Coordinates.nums[0], Coordinates.nums[1], Coordinates.nums[0] + 300, Coordinates.nums[1] + 300))
        value = pytesseract.image_to_string(img)
        if len(value) > 10:
            t1 = time.time()
            break
    time.sleep(2)
    tim = (t1-t0)
    if tim < 0:
        tim = 0
    return round(tim)


''' This function takes in the tested lists, their scores and how many need to breed.
 It gives out the lists that should breed. '''
def breeding_selection(score_list, no_of_selections):
    # rank first list second
    selected = []
    counter = 0
    scores = []
    sorted_score_list = sorted(score_list)[::-1]
    for x in sorted_score_list:
        scores.append(x[1])
    for y in sorted_score_list:
        y[1] = scores[counter]
        counter += 1
    for item in range(no_of_selections):
        selected.append(sorted_score_list[item])
    for v in selected:
        v = v[0]
    return selected


''' This function takes in two lists as parents and 'breeds' them. It gives out a 'kid' list.
 The kid list is a combination of the parent lists.'''
def crossover(p1, p2):
    counter = 0
    holder = 0
    point1 = random.randint(5, 18)
    point2 = random.randint(5, 18)
    p1_re = p1[::-1]
    for bit in p1:
        if bit == p1[point1]:
            break
        holder = p2[counter]
        p2[counter] = bit
        p1[counter] = holder
        holder = 0
        counter += 1
    for newbit in p1_re:
        counter2 = 0
        holder2 = 0
        if newbit == p1[point2]:
            break
        holder = p2[counter2]
        p2[counter] = newbit
        p1[counter] = holder2
        holder = 0
        counter += 1
    picker = random.randint(1, 2)
    if picker == 1:
        return p1
    if picker == 2:
        return p2


''' This function takes a list and 'mutates' it. This just changes some items in the list at random.'''
def mutation(list_input):
    for h in list_input:
        random_num = random.randint(0, 100)
        if random_num < 98:
            if h == 0:
                h = 1
            if h == 1:
                h = 0
    return list_input


''' This code holdsthe randomly generated population of lists '''
class Motherlist:
    motherlist = initialize(145, 1000)


'''This function uses all the other functions to make one cycle of
 playing the game, being ranked, breeding, and mutation.'''
def compute(max_fitness):
    scorelist = []
    for sequence in Motherlist.motherlist:
        scorelist.append([fitness_scorer(sequence), sequence])
    for ry in scorelist:
        if ry[0] > max_fitness:
            return '{} is optimal'.format(ry)
    selection = breeding_selection(scorelist, 200)
    motherlist = []
    for thing in selection:
        for U in selection:
            if random.randint(0, 100) <= 2:
                motherlist.append(crossover(thing, U))
            else:
                pass
    for yu in motherlist:
        yu = mutation(yu)
    return '{} are the top 20 lists for this generation'.format(selection)


''' this code repeats the cycle of playing the game, being ranked, breeding, and mutation 100 times, to get the list that
can beat the level'''
if __name__ == '__main__':
    for qe in range(100):
        print(compute(122))
        if qe == 99:
            break