class CarQueue:
    def __init__(self, capacity=None):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        if self.capacity is None:
            return False
        return len(self.queue) >= self.capacity

    def enqueue(self, car_plate):
        if self.is_full():
            print("\nError: Parking lot is full! Cannot park '%s'." % car_plate)
            return False

        self.queue.append(car_plate)
        print("\nSuccess: Car '%s' has entered the parking lot." % car_plate)
        return True

    def dequeue(self):
        if self.is_empty():
            print("\nError: Parking lot is empty! No cars to remove.")
            return None

        removed_car = self.queue.pop(0)
        print("\nSuccess: Car '%s' has left the parking lot." % removed_car)
        return removed_car

    def peek(self):
        if self.is_empty():
            print("\nThe parking lot is empty.")
            return None
        print("\nNext car to exit: '%s'" % self.queue[0])
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("\nThe parking lot is currently empty.")
            return

        print("\n--- Current Parked Cars (Exit -> Entrance) ---")
        for index, car in enumerate(self.queue, start=1):
            print(" Slot %d: %s" % (index, car))
        print("----------------------------------------------\n")


def main():
    
    try:
        get_input = raw_input
    except NameError:
        get_input = input

   
    capacity_input = get_input("Enter max parking capacity (press Enter for unlimited): ").strip()
    capacity = int(capacity_input) if capacity_input.isdigit() else None

    parking_lot = CarQueue(capacity=capacity)

    while True:
        print("\n====================================")
        print("   CAR PARKING MANAGEMENT SYSTEM    ")
        print("====================================")
        print("1. Enqueue (Park a Car)")
        print("2. Dequeue (Retrieve Front Car)")
        print("3. Peek (View Next Car to Exit)")
        print("4. Display All Parked Cars")
        print("5. Exit")

        choice = get_input("Enter your choice (1-5): ").strip()

        if choice == '1':
            plate = get_input("Enter license plate number: ").strip()
            if plate:
                parking_lot.enqueue(plate)
            else:
                print("\nError: License plate cannot be empty.")

        elif choice == '2':
            parking_lot.dequeue()

        elif choice == '3':
            parking_lot.peek()

        elif choice == '4':
            parking_lot.display()

        elif choice == '5':
            print("\nExiting Parking Management System. Goodbye!")
            break

        else:
            print("\nError: Invalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()
