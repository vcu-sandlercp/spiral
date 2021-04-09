def spiralize(number): #creating the function called spiralize
    n = (number - 1) / 2 #counting diagonals minus the center (1)

    return_value = 1 #initial return value is 1
    
    x=( 3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3 #used github to find this framework
    return_value = x #had trouble with this one at first, but assigned x before return_value and it worked
    return return_value

def SumDiagonals():
    diagonal = spiralize(501) #this is a 501x501 matrix

    print(diagonal)
SumDiagonals()