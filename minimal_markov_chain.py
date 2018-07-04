import random

# This list takes an initial state for the chain.
# we also update this list with all future states of the chain,
# resulting in an output that describes one complete possible
# realization of the markov chain
masterList = ["B"]

# keeps track of the number of times the "while-loop" has run
counter = 0

# max number of times the "while-loop" will run
upperLimit = 12

# This is a 2D list representing the relative wheightings of the
# movements between states in the chain. So “weightings[0] [0]”
# represents the chance of moving from an “A” state to another “A” state.
# “weightings[0] [1]” represents the chance of moving from an “A” state
# to a “B” state. weightings[1] [0] represents the chance of moving from
# an “B” state to an “A” state. Etc.

# --- Note that the wightings are values relative only to each other ---
# --- (not probabilities relative to 100 or something like that).    ---
weightings = [
             [20, 1, 1, 1],
             [1, 20, 1, 1],
             [1, 1, 20, 1],
             [1, 1, 1, 20]
             ]

# This function just prints the probability of movement between the various states.

def Probs():

    print(" ")
    print("A -> A: " + '{0:.2%}'.format(float(weightings[0][0])/float(sum(weightings[0]))))
    print("A -> B: " + '{0:.2%}'.format(float(weightings[0][1])/float(sum(weightings[0]))))
    print("A -> C: " + '{0:.2%}'.format(float(weightings[0][2])/float(sum(weightings[0]))))
    print("A -> D: " + '{0:.2%}'.format(float(weightings[0][3])/float(sum(weightings[0]))))

    print(" ")
    print("B -> A: " + '{0:.2%}'.format(float(weightings[1][0])/float(sum(weightings[1]))))
    print("B -> B: " + '{0:.2%}'.format(float(weightings[1][1])/float(sum(weightings[1]))))
    print("B -> C: " + '{0:.2%}'.format(float(weightings[1][2])/float(sum(weightings[1]))))
    print("B -> D: " + '{0:.2%}'.format(float(weightings[1][3])/float(sum(weightings[1]))))

    print(" ")
    print("C -> A: " + '{0:.2%}'.format(float(weightings[2][0])/float(sum(weightings[2]))))
    print("C -> B: " + '{0:.2%}'.format(float(weightings[2][1])/float(sum(weightings[2]))))
    print("C -> C: " + '{0:.2%}'.format(float(weightings[2][2])/float(sum(weightings[2]))))
    print("C -> D: " + '{0:.2%}'.format(float(weightings[2][3])/float(sum(weightings[2]))))

    print(" ")
    print("D -> A: " + '{0:.2%}'.format(float(weightings[3][0])/float(sum(weightings[3]))))
    print("D -> B: " + '{0:.2%}'.format(float(weightings[3][1])/float(sum(weightings[3]))))
    print("D -> C: " + '{0:.2%}'.format(float(weightings[3][2])/float(sum(weightings[3]))))
    print("D -> D: " + '{0:.2%}'.format(float(weightings[3][3])/float(sum(weightings[3]))))
    print(" ")

# This function performers a pseudo-random choice informed by the relatives weightings of the four states.

def WeightedRandom(weight1, weight2, weight3, weight4):
    totalWeight = weight1 + weight2 + weight3 + weight4
    randomInt = random.randint(1, totalWeight)

    if randomInt <= weight1:
        return 0
    elif randomInt > weight1 and randomInt <= (weight1 + weight2):
        return 1
    elif randomInt > (weight1 + weight2) and randomInt <= (weight1 + weight2 + weight3):
        return 2
    elif randomInt > (weight1 + weight2 + weight3):
        return 3
    else:
        return("error")

# This function routes the output of the WeightedRandom() function into the Choice() function
def GetNewState(row):
    return Choice(WeightedRandom(weightings[row][0], weightings[row][1], weightings[row][2], weightings[row][3]))

# Converts the output of WeightedRandom() into a letter (Markov state)
def Choice(argument):
    switcher = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
    }
    return switcher.get(argument, "nothing")

# Each time the "while-looped" is called, we get the last item in the list, evaluate it, and
# get a new Markov state based on the probabilities associated with that state
while (counter < upperLimit):

    if (masterList[-1] == "A"):
        masterList.append(GetNewState(0))
    elif (masterList[-1] == "B"):
        masterList.append(GetNewState(1))
    elif (masterList[-1] == "C"):
        masterList.append(GetNewState(2))
    elif (masterList[-1] == "D"):
        masterList.append(GetNewState(3))
    else:
        print("error")    
    counter += 1

Probs()
print(masterList)
