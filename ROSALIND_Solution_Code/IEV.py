##  Calculating Expected Offspring

data = "1 0 0 1 0 1"
dataset = data.split(" ")

potential = [2, 2, 2, 1.5, 1, 0]

sum = 0

for i in range(len(dataset)):
    sum += int(dataset[i])*potential[i]

print(sum)