# Problem No 01

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle [Width: {self.width}, Height: {self.height}, Area: {self.area()}]"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square [Side: {self.width}, Area: {self.area()}]"

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def surface_area(self):
        return 6 * super().area()

    def volume(self):
        return self.width ** 3

    def __str__(self):
        return (f"Cube [Side: {self.width}, Surface Area: {self.surface_area()}, "
                f"Volume: {self.volume()}]")

# -------------------------------------------------------------------------------------------------------

# Problem No 02


class Payroll_system:
    def calculate_payroll(self, employees):
        print("Calculate Payroll")
        print("===========================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print()

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Salary_employee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class Hourly_employee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class Commission_employee(Salary_employee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager_role(Salary_employee):
    def work(self, hours):
        print(f"{self.name} oversees and delegates tasks for {hours} hours.")

class Secretary_role(Salary_employee):
    def work(self, hours):
        print(f"{self.name} efficiently organizes and manages documents for {hours} hours.")

class SalesPerson_role(Commission_employee):
    def work(self, hours):
        print(f"{self.name} engages with clients and closes deals for {hours} hours.")

class FactoryWorker_role(Hourly_employee):
    def work(self, hours):
        print(f"{self.name} diligently assembles products for {hours} hours.")



class Productivity_system:
    def Track(self, employees, hours):
        print("Productivity System Tracking")
        print('-----------------------------')
        for employee in employees:
            employee.work(hours)
            print()


