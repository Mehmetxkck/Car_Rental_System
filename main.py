class Car:
    def __init__(self, brand, model, year, daily_rate):
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.availability = True

    def rent(self, days):
        if self.availability:
            total_cost = self.daily_rate * days
            self.availability = False
            print(f"{self.brand} {self.model} {days} günlüğüne kiralandı. Toplam ücret: {total_cost} TL.")
            return total_cost
        else:
            print(f"{self.brand} {self.model} şu an kirada.")
            return None

    def return_car(self):
        if not self.availability:
            self.availability = True
            print(f"{self.brand} {self.model} geri getirildi.")
        else:
            print(f"{self.brand} {self.model} zaten mevcut.")


class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} sisteme eklendi.")

    def display_available_cars(self):
        print("Mevcut araçlar:")
        for index, car in enumerate(self.cars):
            if car.availability:
                print(f"{index}: {car.brand} {car.model} ({car.year}) - Günlük: {car.daily_rate} TL")

    def rent_car(self, car_index, days):
        if 0 <= car_index < len(self.cars):
            car = self.cars[car_index]
            car.rent(days)
        else:
            print("Geçersiz araç indeksi.")

    def return_car(self, car_index):
        if 0 <= car_index < len(self.cars):
            car = self.cars[car_index]
            car.return_car()
        else:
            print("Geçersiz araç indeksi.")


# Örnek kullanım:

# Sistemi oluştur
rental_system = CarRentalSystem()

# Araçlar oluştur ve sisteme ekle
car1 = Car("Toyota", "Corolla", 2020, 200)
car2 = Car("Honda", "Civic", 2021, 250)
car3 = Car("BMW", "X5", 2022, 500)

rental_system.add_car(car1)
rental_system.add_car(car2)
rental_system.add_car(car3)

# Mevcut araçları göster
rental_system.display_available_cars()

# Bir aracı 3 günlüğüne kirala
rental_system.rent_car(1, 3)

# Aynı aracı tekrar kiralamaya çalış
rental_system.rent_car(1, 2)

# Kiralanan aracı geri getir
rental_system.return_car(1)

# Araçları tekrar göster
rental_system.display_available_cars()
