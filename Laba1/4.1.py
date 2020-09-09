your_input = input()
counter = 0
while not your_input.__eq__("Спасибо"):
    your_input = input()
    counter += 1
print(counter+1)
