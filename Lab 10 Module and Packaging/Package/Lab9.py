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


# ----------------------------------------------------------------------------------------------------------------

# Temporay Secretary

class TemporarySecretary(Secretary_role, Hourly_employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        Hourly_employee.__init__(self, id, name, hours_worked, hourly_rate)
    def calculate_payroll(self):
        return Hourly_employee.calculate_payroll(self)

