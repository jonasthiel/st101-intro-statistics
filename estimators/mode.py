#Complete the mode function to make it return the mode of a list of numbers

data1=[1,2,5,10,-20,5,5]

def mode(data):
    mode = 0
    counter = 0
    for i in range(len(data)):
        if data.count(data[i]) > counter:
            mode = data[i]
            counter = data.count(data[i])

    return mode

print(mode(data1))