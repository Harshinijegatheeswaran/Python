class CarNode:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None


class CarParkingQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, car_number):
        new_car = CarNode(car_number)
        if self.rear is None:
            self.front = self.rear = new_car
        else:
            self.rear.next = new_car
            self.rear = new_car
        print("Car entered the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty. No cars waiting.")
            return None
        leaving_car = self.front.car_number
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Car moved into the parking lot.")
        return leaving_car

    def display(self):
        if self.front is None:
            print("Queue Status: Empty")
            return
        current = self.front
        cars = []
        while current:
            cars.append(current.car_number)
            current = current.next

        print("Current Queue: " + ", ".join(cars))
if __name__ == "__main__":
    parking = CarParkingQueue()

    while True:
        print("\nCAR PARKING MANAGEMENT SYSTEM")
        print("1. Enqueue Car")
        print("2. Dequeue Car")
        print("3. Display Queue")
        print("4. Exit")
        choice = str(input("Enter choice (1-4): ")).strip()

        if choice == "1":
            car_num = str(input("Enter Car Number: ")).strip()
            if car_num:
                parking.enqueue(car_num)
            else:
                print("Car number cannot be empty.")
        elif choice == "2":
            parking.dequeue()
        elif choice == "3":
            parking.display()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
