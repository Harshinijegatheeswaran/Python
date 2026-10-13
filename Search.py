
n = int(raw_input("Enter number of students: "))
roll_numbers = map(int, raw_input("Enter roll numbers: ").split())

key = int(raw_input("Enter roll number to search: "))

found = False
for i in range(n):
    if roll_numbers[i] == key:
        found = True
        break

if found:
    print "Linear Search: Roll number found"
else:
    print "Linear Search: Roll number not found"

arr = sorted(roll_numbers)
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print "Binary Search: Roll number found"
else:
    print "Binary Search: Roll number not found"
