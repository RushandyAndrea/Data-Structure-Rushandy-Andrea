import itertools
import hashlib
import time

Davincs_quote = "Learning never exhausts the mind!"  # making the string accessible for all the functions
print(Davincs_quote)
print("===================================================")

# generate the hashed value of your quote - use absolute value for only positive numbers.
# Also, only use the first 6 digits.
int(hashlib.sha1(Davincs_quote.encode("utf-8")).hexdigest(), 16) % (10 ** 6)
abs(hash(Davincs_quote)) % (10 ** 6)
print("The hashed quote is: ", abs(hash(Davincs_quote)) % (10 ** 6))  # Testing hashed_quote

Davincs_quote_hashed = abs(hash(Davincs_quote))  # Hashed Quote

start_time = time.time()  # gives the starting time of the program
for i in range(10000000):
    j = 10 + i

end_time = time.time()
final_time = end_time - start_time
print("hashing time: ", final_time)


#  Create a list out of the string
def string_to_list(hash_string):
    list_string = []
    for character in hash_string:
        list_string.append(character)

    print(list_string)


# The individual hash values will open the lockbox but only if they are in the correct hashed sequence - thus the stack.
Davincs_passcode = str(abs(hash(Davincs_quote)) % (10 ** 6))  # hash with first 6 digits
string_to_list(Davincs_passcode)
digits = list(range(0, 10))

# creating a list for Davinc's passcode
key_list = [int(x) for x in str(Davincs_passcode)]
print(f"Secret 6 digits code is: {key_list}")


# Node class
class Node:
    def __init__(self, data=None, next=None, previous1=None):
        self.data = data  # instance variable
        self.next = next  # address of next node
        self.previous1 = previous1


class LinkedList:
    # Init a Linked List object.
    def __init__(self):
        self.head = None

    # Function to insert a new head node.
    def add_head(self, new_data):
        # Create new node with data.
        new_node = Node(new_data)
        # Point to new head.
        new_node.next = self.head
        new_node.previous1 = None
        if self.head is not None:
            self.head.previous1 = new_node
        # Move current head to new Node.
        self.head = new_node

    # Removes a node.
    def remove(self):
        og_head = self.head  # original head.
        new_head = og_head.next
        self.head = new_head
        #new_head.previous = None


DoubleLinkList = LinkedList()  # create object

# Use the linkedlist - reverse push into
print("Double linked list code format: ", end="")
for index in range(len(key_list)):
    # print("Printing index", index, end=" -->" )
    DoubleLinkList.add_head(key_list[len(key_list) - (index + 1)])  # reverse inserting

    print(DoubleLinkList.head.data, end=" ")
    if index < len(key_list) - 1:
        print(end=" --> ")

# Get the first 4 head
print("")
print("===================================================")
print("")
print("Cracking 4 digits......")
digits = list(range(0, 10))
length = 4

needed_toBe_cracked = ""

for number in range(length):
    needed_toBe_cracked += str(DoubleLinkList.head.data)
    DoubleLinkList.remove()

print()
print("Code that needs to be cracked =  ", needed_toBe_cracked)  # Test and shows us the empty string

start_ss = time.perf_counter_ns()  # Tracks the time
for permutation in itertools.product(digits, repeat=len(needed_toBe_cracked)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == Davincs_passcode:
        print(f"Code unlocked: {permutation}")
        break
# holly fuck, tf im doing
stop_ss = time.perf_counter_ns()  # this will stop the time counting.
total_time_ss = stop_ss - start_ss
print("This process time in seconds: ", total_time_ss * 10 ** -9)

# 6 digits
print("")
print("===================================================")
print("")
print("Cracking 6 digits......")
digits = list(range(0, 10))
length = 6

needed_toBe_cracked = ""

# Stay awake Rushandy...
for number in range(length):
    needed_toBe_cracked += str(DoubleLinkList.head.data)
    #DoubleLinkList.remove()
# Fuck this shit man. Who invented school? fuck a horse man.
print()
print("Code that needs to be cracked =  ", needed_toBe_cracked)  # Test and shows us the empty string

start_ss = time.perf_counter_ns()  # Tracks the time
for permutation in itertools.product(digits, repeat=len(needed_toBe_cracked)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == Davincs_passcode:
        print(f"Code unlocked: {permutation}")
        break

stop_ss = time.perf_counter_ns()  # this will stop the time counting.
total_time_ss = stop_ss - start_ss
print("This process time in seconds: ", total_time_ss * 10 ** -9)


# 8 digits
print("")
print("===================================================")
print("")
print("Cracking 8 digits......")
digits = list(range(0, 10))
length = 8

needed_toBe_cracked = ""

for number in range(length):
    needed_toBe_cracked += str(DoubleLinkList.head.data)
    #DoubleLinkList.remove()

print()
print("Code that needs to be cracked =  ", needed_toBe_cracked)  # Test and shows us the empty string

start_ss = time.perf_counter_ns()  # Tracks the time
for permutation in itertools.product(digits, repeat=len(needed_toBe_cracked)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == Davincs_passcode:
        print(f"Code unlocked: {permutation}")
        break

stop_ss = time.perf_counter_ns()  # this will stop the time counting.
total_time_ss = stop_ss - start_ss
print("This process time in seconds: ", total_time_ss * 10 ** -9)
