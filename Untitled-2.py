class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def display_info(self):
        # Menampilkan informasi lengkap mahasiswa
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Score: {self.score}")

# Membuat objek dari class "Student"
student_example = Student("duta armi", 21, 99)

# Menampilkan informasi lengkap mahasiswa
student_example.display_info()
