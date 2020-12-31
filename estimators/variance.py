#Complete the variance function to make it return the variance of a list of numbers

data1=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mean_data = mean(data)
    variance_numerator = []
    for i in data:
        variance_numerator.append((i - mean_data) ** 2)

    return mean(variance_numerator)

print(variance(data1))