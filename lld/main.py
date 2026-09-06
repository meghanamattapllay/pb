class Vehicle:
    def __init__(self,number,type,owner):
        self.number=number
        self.type=type
        self.owner=owner

    def entry(self):
        print("Vehicle entered")

    def exit(self):
        print("Vehicle exited")


class Ticket:
    def __init__(self,id,vehicle):
        self.id=id
        self.vehicle=vehicle
        self.entry_time="10:00"
        self.exit_time=None
        self.fee=0

    def generate_ticket(self):
        print("Ticket generated")
        print("Ticket ID:",self.id)

    def calculate_fee(self):
        self.fee=50
        return self.fee

    def show(self):
        print("Ticket ID:",self.id)
        print("Vehicle:",self.vehicle.number)
        print("Entry:",self.entry_time)
        print("Exit:",self.exit_time)
        print("Fee:",self.fee)


class Booking:
    def __init__(self,id):
        self.id=id
        self.status="Pending"

    def confirm(self):
        self.status="Confirmed"
        print("Booking confirmed")

    def cancel(self):
        self.status="Cancelled"
        print("Booking cancelled")


class Payment:
    def __init__(self,id,amount):
        self.id=id
        self.amount=amount
        self.status="Pending"

    def pay(self):
        self.status="Paid"
        print("Payment successful")

    def receipt(self):
        print("Payment ID:",self.id)
        print("Amount:",self.amount)
        print("Status:",self.status)


class ParkingSlot:
    def __init__(self,id,type):
        self.id=id
        self.type=type
        self.vehicle=None

    def park(self,vehicle):
        if self.vehicle is None and self.type==vehicle.type:
            self.vehicle=vehicle
            return True
        return False

    def remove(self):
        vehicle=self.vehicle
        self.vehicle=None
        return vehicle

    def show(self):
        if self.vehicle:
            print(self.id,self.type,"Occupied")
        else:
            print(self.id,self.type,"Free")


class ParkingLot:
    def __init__(self,name):
        self.name=name
        self.slots=[]
        self.tickets=[]

    def add_slot(self,slot):
        self.slots.append(slot)

    def remove_slot(self,id):
        for slot in self.slots:
            if slot.id==id and slot.vehicle is None:
                self.slots.remove(slot)
                print("Slot removed")
                return
        print("Slot cannot be removed")

    def available_slots(self):
        count=0
        for slot in self.slots:
            if slot.vehicle is None:
                count+=1
        print("Available slots:",count)

    def park_vehicle(self,vehicle):
        for slot in self.slots:
            if slot.park(vehicle):
                ticket=Ticket(len(self.tickets)+1,vehicle)
                self.tickets.append(ticket)
                print("Vehicle parked at slot",slot.id)
                ticket.generate_ticket()
                return ticket
        print("No slot available")
        return None

    def remove_vehicle(self,number):
        for slot in self.slots:
            if slot.vehicle and slot.vehicle.number==number:
                slot.remove()
                print("Vehicle removed")
                return True
        print("Vehicle not found")
        return False

    def find_vehicle(self,number):
        for slot in self.slots:
            if slot.vehicle and slot.vehicle.number==number:
                print("Vehicle found at slot",slot.id)
                return
        print("Vehicle not found")

    def show_slots(self):
        print("\nParking Slots")
        for slot in self.slots:
            slot.show()


class User:
    def __init__(self,name):
        self.name=name

    def login(self):
        print("Login successful")


class Admin(User):
    def add_slot(self,lot,id,type):
        lot.add_slot(ParkingSlot(id,type))
        print("Slot added")

    def remove_slot(self,lot,id):
        lot.remove_slot(id)


class Customer(User):
    def __init__(self,name):
        super().__init__(name)
        self.vehicle=None
        self.ticket=None
        self.booking=None

    def add_vehicle(self,vehicle):
        self.vehicle=vehicle

    def book(self,lot):
        if self.vehicle:
            self.booking=Booking(1)
            self.booking.confirm()
            self.ticket=lot.park_vehicle(self.vehicle)

    def cancel(self,lot):
        if self.vehicle:
            lot.remove_vehicle(self.vehicle.number)

    def view_ticket(self):
        if self.ticket:
            self.ticket.show()


lot=ParkingLot("City Parking")

admin=Admin("Admin")
customer=Customer("Meghana")

admin.login()
customer.login()

admin.add_slot(lot,1,"Car")
admin.add_slot(lot,2,"Car")
admin.add_slot(lot,3,"Bike")
admin.add_slot(lot,4,"Bike")
admin.add_slot(lot,5,"Car")


while True:
    print("\n--- PARKING LOT ---")
    print("1.Add Vehicle")
    print("2.Park Vehicle")
    print("3.Remove Vehicle")
    print("4.Find Vehicle")
    print("5.Show Slots")
    print("6.Available Slots")
    print("7.View Ticket")
    print("8.Make Payment")
    print("9.Add Slot")
    print("10.Remove Slot")
    print("11.Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        number=input("Enter vehicle number: ")
        type=input("Enter vehicle type: ")
        owner=input("Enter owner name: ")
        customer.add_vehicle(Vehicle(number,type,owner))
        print("Vehicle added")

    elif choice==2:
        if customer.vehicle:
            customer.vehicle.entry()
            customer.book(lot)
        else:
            print("Add vehicle first")

    elif choice==3:
        number=input("Enter vehicle number: ")
        lot.remove_vehicle(number)

    elif choice==4:
        number=input("Enter vehicle number: ")
        lot.find_vehicle(number)

    elif choice==5:
        lot.show_slots()

    elif choice==6:
        lot.available_slots()

    elif choice==7:
        customer.view_ticket()

    elif choice==8:
        if customer.ticket:
            amount=customer.ticket.calculate_fee()
            payment=Payment(1,amount)
            payment.pay()
            payment.receipt()
        else:
            print("No ticket")

    elif choice==9:
        id=int(input("Enter slot id: "))
        type=input("Enter slot type: ")
        admin.add_slot(lot,id,type)

    elif choice==10:
        id=int(input("Enter slot id: "))
        admin.remove_slot(lot,id)

    elif choice==11:
        print("Thank you")
        break

    else:
        print("Invalid choice")