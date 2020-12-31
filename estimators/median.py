#Complete the median function to make it return the median of a list of numbers

data1=[1,2,5,10,-20]

def median(data):
    sorted_data = sorted(data)
    return sorted_data[int(round((len(data) / 2), 1))]

print(median(data1))