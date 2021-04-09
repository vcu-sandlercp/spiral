def spiralize(number): #creating the function called spiralize
    n = (number - 1) / 2 #counting diagonals minus the center (1)
    
    x=( 3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3 #used github to find this framework
    return x

def SumDiagonals():
    diagonal = spiralize(501) #this is a 501x501 matrix

    print(diagonal)

SumDiagonals() #using function created above to sum the diagonals in the spiralize() function
#This makes n=250 because (501-1)/2 = 250