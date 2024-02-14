class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_total_salary(self):
        # Menghitung total gaji berdasarkan gaji per jam dan jumlah jam kerja
        total_salary = self.hourly_rate * self.hours_worked
        return total_salary

# Membuat objek dari class "Employee"
employee_example = Employee("duta armi", hourly_rate=30, hours_worked=80)

# Menghitung total gaji
total_salary = employee_example.calculate_total_salary()

# Menampilkan total gaji
print(f"Total salary for {employee_example.name}: ${total_salary}")
