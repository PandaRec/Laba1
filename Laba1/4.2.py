inputs = list()
temp_input = float(input())
inputs.append(temp_input)

while temp_input > -300:
    temp_input = float(input())
    inputs.append(temp_input)
del inputs[len(inputs)-1]
print(sum(inputs) / len(inputs))
