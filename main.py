MouseTrap = "Mouse Trap"

# Step 1:
print("Step 1.")
print("")
Step1 = "What is the meaning of life?"
x = Step1.split()
print(x)

charCount = len(x[2])
print(charCount)

subtractChar = len(x[3]) - len(x[4])
print(subtractChar)

# Step 2:
Step1 = ()
result = 0
print("Step 2")
print("")
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print(result)

# Step 3
result_List = []
for i in str(result):
    result_List.append(int(i))
print("Step 3.")
print("")
result_List.pop()
result_List.pop()
print(result_List)

sum_Values = result_List.pop()
sum_Values = result_List.pop() + sum_Values
print("The sum of the 2 values: ", sum_Values)  # The last 2 values in the list ( 3 and 1)

mult_Values = result_List.pop()
mult_Values = result_List.pop() * mult_Values
print("The multiplication of the 2 values: ", mult_Values)  # The remaining values of 2 and 3

average_Value = round((sum_Values + mult_Values) / 2)
print("The average is: ", average_Value)
# Step 4
# h(k) = k1 % m
dict = {}
m = average_Value
k_list = [3, 2, 9, 11, 7, 8, 13, 17]

collision = 0
for k1 in k_list:
    if k1 % m in dict.keys():  # The parameter k is the value that we want to calculate the key for
        collision += 1
    dict.update({k1 % m: k1})
print("Step 4.")
print("")
print(collision)  # the number of collision that occur after executing the above hash function
print(dict)

# Step 5
d = {}
for x in range(1, collision + 1):
    d[x] = x ** 2
print("Step 5.")
print("")
print("D is: ", d)

# access the index of the d dictionary here
v2 = d[2]  # value of dictionary
v3 = d[3]  # value of dictionary
sumOfValue = v2 * v3
end_value = sumOfValue + d[4]
print("Step 5 output is: ", end_value)

# Step 6
# cabbage, remove all adjacent letters
cabbage = 'e'
stringCabbage = cabbage


def Step6String(stringCabbage):
    # Store the string without
    # duplicate elements

    stringOne = stringCabbage
    strEmpty = []

    # Store the index of str
    i = 0
    while i < len(stringOne):
        # This should check for empty string
        if len(strEmpty) == 0 or stringOne[i] != strEmpty[-1]:
            strEmpty.append(stringOne[i])
            i += 1
        else:
            strEmpty.pop()
            i += 1

        # This is if stack is empty
        if len(strEmpty) == 0:
            return "String is empty!"

        # This is for if stack is not empty
        else:
            stringTwo = ""
            for i in strEmpty:
                stringTwo += str(i)
            return stringTwo

    final = Step6String(stringCabbage)
    numberSt = 0
    for char in final:
        numOrd = ord(char)
        numberSt += numOrd
    print("Step 6")
    print("")
    print(numberSt)

    # Step 7
    print("Step 7")
    print("")
    sum_of_6 = [int(x) for x in str(numberSt)]
    num_of_7 = 0
    for z in sum_of_6:
        num_of_7 += z
    print("Number of sum 7 is: ", num_of_7)

    # calculation here
    final_of_7 = end_value - (numberSt + 4)
    print("Output of the final equation: ", final_of_7)
