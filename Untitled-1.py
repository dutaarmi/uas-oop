class Car:
    def __init__(self, brand, year, speed=0):
        self.brand = brand
        self.year = year
        self.speed = speed

    def calculate_time(self, distance):
        # Menghitung waktu yang dibutuhkan untuk menempuh jarak tertentu berdasarkan kecepatan
        if self.speed <= 0:
            return "Cannot calculate time. The car is not moving."

        time_required = distance / self.speed
        return f"Time required to travel {distance} km at {self.speed} km/h: {time_required:.2f} hours"

# Membuat objek dari class "Car"
car_example = Car("becakkotong", 2025, speed=5000)

# Menghitung waktu yang dibutuhkan untuk menempuh jarak 100 km dengan kecepatan 60 km/jam
result = car_example.calculate_time(100)

# Menampilkan hasil perhitungan waktu
print(result)
