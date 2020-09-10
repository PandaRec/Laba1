count_of_blocks = int(input())
students_in_blocks = []
students_in_one_block = []

for i in range(count_of_blocks):
    count_in_block = int(input())
    for j in range(count_in_block):
        students_in_one_block.append(input())
    students_in_blocks.append(students_in_one_block)
    students_in_one_block = []
counter_to_true = 0

for i in range(len(students_in_blocks) + 1):
    for j in range(1, len(students_in_blocks)):
        if students_in_blocks[0][i] in students_in_blocks[j]:
            counter_to_true += 1
    if counter_to_true == len(students_in_blocks) - 1:
        print(students_in_blocks[0][i])
        counter_to_true = 0
    else:
        counter_to_true = 0
