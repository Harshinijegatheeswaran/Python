
arr = map(int, raw_input("Enter student marks: ").split())

bubble = arr[:]
for i in range(len(bubble)):
    for j in range(len(bubble) - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

print "Bubble Sort:", bubble

insertion = arr[:]
for i in range(1, len(insertion)):
    key = insertion[i]
    j = i - 1
    while j >= 0 and insertion[j] > key:
        insertion[j + 1] = insertion[j]
        j -= 1
    insertion[j + 1] = key

print "Insertion Sort:", insertion

selection = arr[:]
for i in range(len(selection)):
    min_index = i
    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_index]:
            min_index = j
    selection[i], selection[min_index] = selection[min_index], selection[i]

print "Selection Sort:", selection
