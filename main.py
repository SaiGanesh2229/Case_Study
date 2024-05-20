from dao.CarLeaseRepository import ICarLeaseRepositoryImpl
from pyodbc import Error
from tabulate import tabulate
from datetime import datetime


class CarRentalSystem:
    def __init__(self):
        self.car_lease_repository = ICarLeaseRepositoryImpl()

    def start(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if not self.main_menu_handler(choice):
                break

    def display_main_menu(self):
        print("Welcome to Car Rental System")
        print("1. Customer Management")
        print("2. Vehicle Management")
        print("3. Lease Management")
        print("4. Payment Handling")
        print("5. Exit")

    def main_menu_handler(self, choice):
        if choice == "1":
            self.customer_management()
        elif choice == "2":
            self.vehicle_management()
        elif choice == "3":
            self.lease_management()
        elif choice == "4":
            self.payment_handling()
        elif choice == "5":
            self.exit_system()
            return False
        else:
            self.invalid_choice()
        return True

    def customer_management(self):
        while True:
            self.display_customer_menu()
            choice = input("Enter your choice: ")
            if not self.customer_menu_handler(choice):
                break

    def display_customer_menu(self):
        print("Operations for Customer table. Please select from the following")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. List Customers")
        print("4. Find Customer by ID")
        print("5. Back to Main Menu")

    def customer_menu_handler(self, choice):
        if choice == "1":
            self.add_customer()
        elif choice == "2":
            self.remove_customer()
        elif choice == "3":
            self.list_customers()
        elif choice == "4":
            self.find_customer_by_id()
        elif choice == "5":
            return False
        else:
            self.invalid_choice()
        return True

    def add_customer(self):
        try:
            customer_details = {
                "customer_id": input("Enter new customer ID: "),
                "first_name": input("Enter first name: "),
                "last_name": input("Enter last name: "),
                "email": input("Enter email: "),
                "phone_number": input("Enter phone number: "),
            }
            self.car_lease_repository.add_customer(**customer_details)
            print("Customer added successfully.")
        except Exception as e:
            print(f"Error adding customer: {e}")

    def remove_customer(self):
        try:
            customer_id = input("Enter customer ID to remove: ")
            self.car_lease_repository.remove_customer(customer_id)
            print("Customer removed successfully.")
        except Exception as e:
            print(f"Error removing customer: {e}")

    def list_customers(self):
        try:
            customers = self.car_lease_repository.list_customers()
            if customers:
                print(tabulate(customers, headers="keys", tablefmt="grid"))
            else:
                print("No customers found.")
        except Exception as e:
            print(f"Error listing customers: {e}")

    def find_customer_by_id(self):
        try:
            customer_id = input("Enter customer ID to find: ")
            customer = self.car_lease_repository.find_customer_by_id(customer_id)
            if customer:
                print(tabulate([customer], headers="keys", tablefmt="grid"))
            else:
                print("Customer not found.")
        except Exception as e:
            print(f"Error: {e}")

    def vehicle_management(self):
        while True:
            self.display_vehicle_menu()
            choice = input("Enter your choice: ")
            if not self.vehicle_menu_handler(choice):
                break

    def display_vehicle_menu(self):
        print("Operations for Vehicle table. Please select from the following")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("6. Back to Main Menu")

    def vehicle_menu_handler(self, choice):
        if choice == "1":
            self.add_car()
        elif choice == "2":
            self.remove_car()
        elif choice == "3":
            self.list_available_cars()
        elif choice == "4":
            self.list_of_rented_cars()
        elif choice == "5":
            self.find_car_by_id()
        elif choice == "6":
            return False
        else:
            self.invalid_choice()
        return True

    def add_car(self):
        try:
            vehicle_details = {
                "vehicle_id": input("Enter vehicle ID: "),
                "make": input("Enter make: "),
                "model": input("Enter model: "),
                "year": int(input("Enter year: ")),
                "daily_rate": float(input("Enter daily rate: ")),
                "status": input("Enter status (available/notAvailable): "),
                "passenger_capacity": int(input("Enter passenger capacity: ")),
                "engine_capacity": float(input("Enter engine capacity: ")),
            }
            self.car_lease_repository.add_car(**vehicle_details)
            print("Vehicle added successfully.")
        except Exception as e:
            print(f"Error adding vehicle: {e}")

    def remove_car(self):
        try:
            vehicle_id = input("Enter vehicle ID to remove: ")
            self.car_lease_repository.remove_car(vehicle_id)
            print("Vehicle removed successfully.")
        except Exception as e:
            print(f"Error removing vehicle: {e}")

    def list_available_cars(self):
        try:
            cars = self.car_lease_repository.list_available_cars()
            if cars:
                print(tabulate(cars, headers="keys", tablefmt="grid"))
            else:
                print("No available cars found.")
        except Exception as e:
            print(f"Error listing available cars: {e}")

    def list_of_rented_cars(self):
        try:
            cars = self.car_lease_repository.list_of_rented_cars()
            if cars:
                print(tabulate(cars, headers="keys", tablefmt="grid"))
            else:
                print("No rented cars found.")
        except Exception as e:
            print(f"Error listing rented cars: {e}")

    def find_car_by_id(self):
        try:
            car_id = input("Enter car ID to find: ")
            car = self.car_lease_repository.find_car_by_id(car_id)
            if car:
                print(tabulate([car], headers="keys", tablefmt="grid"))
            else:
                print("Car not found.")
        except Exception as e:
            print(f"Error: {e}")

    def lease_management(self):
        while True:
            self.display_lease_menu()
            choice = input("Enter your choice: ")
            if not self.lease_menu_handler(choice):
                break

    def display_lease_menu(self):
        print("Operations for Lease table. Please select from the following")
        print("1. Create Lease")
        print("2. Return Car")
        print("3. List Active Leases")
        print("4. List Lease History")
        print("5. Back to Main Menu")

    def lease_menu_handler(self, choice):
        if choice == "1":
            self.create_lease()
        elif choice == "2":
            self.return_car()
        elif choice == "3":
            self.list_active_leases()
        elif choice == "4":
            self.list_lease_history()
        elif choice == "5":
            return False
        else:
            self.invalid_choice()
        return True

    def create_lease(self):
        try:
            lease_details = {
                "lease_id": input("Enter new lease ID: "),
                "customer_id": input("Enter customer ID: "),
                "car_id": input("Enter car ID: "),
                "start_date": input("Enter start date (YYYY-MM-DD): "),
                "end_date": input("Enter end date (YYYY-MM-DD): "),
                "lease_type": input("Enter lease type (DailyLease/MonthlyLease): "),
            }
            self.car_lease_repository.create_lease(**lease_details)
            print("Lease created successfully.")
        except Exception as e:
            print(f"Error creating lease: {e}")

    def return_car(self):
        try:
            lease_id = input("Enter lease ID to return the car: ")
            self.car_lease_repository.return_car(lease_id)
            print("Car returned successfully.")
        except Exception as e:
            print(f"Error returning car: {e}")

    def list_active_leases(self):
        try:
            leases = self.car_lease_repository.list_active_leases()
            if leases:
                print(tabulate(leases, headers="keys", tablefmt="grid"))
            else:
                print("No active leases found.")
        except Exception as e:
            print(f"Error listing active leases: {e}")

    def list_lease_history(self):
        try:
            leases = self.car_lease_repository.list_lease_history()
            if leases:
                print(tabulate(leases, headers="keys", tablefmt="grid"))
            else:
                print("No lease history found.")
        except Exception as e:
            print(f"Error listing lease history: {e}")

    def payment_handling(self):
        while True:
            self.display_payment_menu()
            choice = input("Enter your choice: ")
            if not self.payment_menu_handler(choice):
                break

    def display_payment_menu(self):
        print("Operations for Payments table. Please select from the following")
        print("1. Record Payment")
        print("2. Retrieve Payment History")
        print("3. Calculate Total Revenue")
        print("4. List All Payments")
        print("5. Back to Main Menu")

    def payment_menu_handler(self, choice):
        if choice == "1":
            self.record_payment()
        elif choice == "2":
            self.retrieve_payment_history()
        elif choice == "3":
            self.calculate_total_revenue()
        elif choice == "4":
            self.list_all_payments()
        elif choice == "5":
            return False
        else:
            self.invalid_choice()
        return True

    def record_payment(self):
        try:
            payment_details = {
                "payment_id": int(input("Enter new payment ID: ")),
                "lease_id": int(input("Enter lease ID: ")),
                "payment_date": datetime.strptime(
                    input("Enter payment date (YYYY-MM-DD): "), "%Y-%m-%d"
                ),
                "amount": float(input("Enter payment amount: ")),
            }
            self.car_lease_repository.record_payment(**payment_details)
            print("Payment recorded successfully.")
        except ValueError:
            print(
                "Invalid input. Please enter valid lease ID, payment date, and payment amount."
            )
        except Exception as e:
            print(f"Error recording payment: {e}")

    def retrieve_payment_history(self):
        try:
            lease_id = int(input("Enter lease ID: "))
            payments = self.car_lease_repository.retrieve_payment_history(lease_id)
            if payments:
                print(tabulate(payments, headers="keys", tablefmt="grid"))
            else:
                print("No payment history found for the given lease ID.")
        except ValueError:
            print("Invalid input. Please enter a valid lease ID.")
        except Exception as e:
            print(f"Error retrieving payment history: {e}")

    def calculate_total_revenue(self):
        try:
            total_revenue = self.car_lease_repository.calculate_total_revenue()
            print(tabulate([[f"Total Revenue: {total_revenue}"]], tablefmt="grid"))
        except Exception as e:
            print(f"Error calculating total revenue: {e}")

    def list_all_payments(self):
        try:
            payments = self.car_lease_repository.list_all_payments()
            if payments:
                print(tabulate(payments, headers="keys", tablefmt="grid"))
            else:
                print("No payments found.")
        except Exception as e:
            print(f"Error listing all payments: {e}")

    def exit_system(self):
        print("Exit")
        exit()

    def invalid_choice(self):
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    CarRentalSystem().start()
