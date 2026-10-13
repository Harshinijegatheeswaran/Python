
size = 10
hash_table = [None] * size

def insert(roll, name):
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None or hash_table[pos] == "DELETED":
            hash_table[pos] = (roll, name)
            print "Student record inserted"
            return
    print "Hash table is full"

def search(roll):
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            break
        if hash_table[pos] != "DELETED" and hash_table[pos][0] == roll:
            print "Student found:", hash_table[pos]
            return
    print "Student not found"

def delete(roll):
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            break
        if hash_table[pos] != "DELETED" and hash_table[pos][0] == roll:
            hash_table[pos] = "DELETED"
            print "Student record deleted"
            return
    print "Student not found"

def display():
    print "\nHash Table:"
    for i, record in enumerate(hash_table):
        print i, ":", record

while True:
    print "\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit"
    choice = raw_input("Enter your choice: ")

    if choice == '1':
        roll = int(raw_input("Enter roll number: "))
        name = raw_input("Enter student name: ")
        insert(roll, name)
    elif choice == '2':
        roll = int(raw_input("Enter roll number: "))
        search(roll)
    elif choice == '3':
        roll = int(raw_input("Enter roll number: "))
        delete(roll)
    elif choice == '4':
        display()
    elif choice == '5':
        break
    else:
        print "Invalid choice"
