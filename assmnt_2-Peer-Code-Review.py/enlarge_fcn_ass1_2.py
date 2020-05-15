# enlarge_fcn_ass1_2.py

def enlarge(num):
    return num * 1000


if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW IF EXECUTING THIS SCRIPT FROM THE COMMAND LINE, 
    # OTHERWISE, DON'T RUN IT (EX IF TRYING TO IMPORT SOMETHING)

    x = 8
    print(enlarge(x))

    y = int(input("Please input a number: "))

    print ("Your number * 1000 = ", enlarge(y))