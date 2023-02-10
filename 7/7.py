class Employee:
    def __init__(self, last_name, position, work_experience, portfolio, efficiency_coefficient, technology_stack, salary):
        self.last_name = last_name
        self.position = position
        self.work_experience = work_experience
        self.portfolio = portfolio
        self.efficiency_coefficient = efficiency_coefficient
        self.technology_stack = technology_stack
        self.salary = salary
        
    def __str__(self):
        return f"{self.last_name}, {self.position}, {self.work_experience}, {self.portfolio}, {self.efficiency_coefficient}, {self.technology_stack}, {self.salary}"

class EmployeeRecords:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def sort_by_last_name(self):
        self.employees.sort(key=lambda x: x.last_name)
        
    def sort_by_efficiency(self):
        self.employees.sort(key=lambda x: x.efficiency_coefficient, reverse=True)
        
    def print_employees(self):
        for employee in self.employees:
            print(employee)

# Example usage
employee_records = EmployeeRecords()
employee_records.add_employee(Employee("Smith", "Developer", 5, "www.portfolio.com", 0.8, ["Python", "JavaScript"], 100000))
employee_records.add_employee(Employee("Jones", "Manager", 10, "www.portfolio.com", 0.9, ["Python", "JavaScript", "C++"], 120000))
employee_records.add_employee(Employee("Brown", "Developer", 2, "www.portfolio.com", 0.7, ["Java", "C#"], 80000))

employee_records.sort_by_last_name()
print("Employees sorted by last name:")
employee_records.print_employees()

employee_records.sort_by_efficiency()
print("Employees sorted by efficiency:")
employee_records.print_employees()
