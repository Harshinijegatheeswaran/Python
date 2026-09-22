class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job, priority):
        self.heap.append((priority, job))
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def delete_max(self):
        if not self.heap:
            print("Heap is empty")
            return

        max_job = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.heapify_down(0)

        print("Processed Job:", max_job[1])
        print("Priority:", max_job[0])

    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def peek(self):
        if not self.heap:
            print("Heap is empty")
        else:
            print("Highest Priority Job:", self.heap[0][1])
            print("Priority:", self.heap[0][0])

    def display(self):
        if not self.heap:
            print("Heap is empty")
        else:
            print("Jobs in Heap Order:")
            for priority, job in self.heap:
                print(job, "-", priority)


heap = MaxHeap()

while True:
    print("\n1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display Jobs")
    print("5. Exit")

    choice = int(raw_input("Enter your choice: "))

    if choice == 1:
        job = raw_input("Enter job name: ")
        priority = int(raw_input("Enter priority: "))
        heap.insert(job, priority)

    elif choice == 2:
        heap.delete_max()

    elif choice == 3:
        heap.peek()

    elif choice == 4:
        heap.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
