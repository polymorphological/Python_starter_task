#1
string1 = "Hello, world!"
string2 = "Goodbye, world!"
common_chars = [char for char in string1 if char in string2]
print(common_chars)
#2
short_links = {}

def shorten_link(long_link, short_name):
    short_links[short_name] = long_link
    print(f"Link {long_link} has been shortened to {short_name}")

def get_long_link(short_name):
    if short_name in short_links:
        print(f"The long link for {short_name} is {short_links[short_name]}")
    else:
        print(f"{short_name} not found.")

long_link = input("Enter the long link: ")
short_name = input("Enter the short name: ")
shorten_link(long_link, short_name)

short_name = input("Enter the short name to get long link: ")
get_long_link(short_name)
#3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))

print("Unique values in list1:", unique_list1)
print("Unique values in list2:", unique_list2)
#4
collections - це стандартний модуль Python, який забезпечує кілька спеціалізованих структур даних такі як:

OrderedDict - словник, який зберігає елементи в порядку їх додавання. 
Він містить ті ж функції, що і звичайний словник, але додатково має метод move_to_end(),
який дозволяє перемістити елемент на кінець.

defaultdict - словник, який містить значення за замовчуванням для нового елементу. 
Це дозволяє зберігати дані без перевірки чи існує ключ в словнику перед додаванням значення.

ChainMap - клас, який дозволяє зєднати кілька словників або мапінги у одну структуру даних.
Він дозволяє запитувати дані з кількох словників одночасно та переважає дані з першого словнику над даними з наступного.
#5
string = "..." # рядок з 1000 слів
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
#6
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, author, title):
        new_book = Book(author, title)
        self.books.append(new_book)
    
    def view_books(self):
        for book in self.books:
            print(book.author + ": " + book.title)
    
    def sort_by_author(self):
        self.books.sort(key=lambda x: x.author)
        self.view_books()
    
    def sort_by_title(self):
        self.books.sort(key=lambda x: x.title)
        self.view_books()

library = Library()
library.add_book("Author 1", "Title 1")
library.add_book("Author 2", "Title 2")
library.add_book("Author 3", "Title 3")
library.view_books()
print("Sorted by author:")
library.sort_by_author()
print("Sorted by title:")
library.sort_by_title()
#7
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