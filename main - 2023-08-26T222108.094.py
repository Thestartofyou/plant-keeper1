import time
import random

class VirtualPlant:
    def __init__(self, species):
        self.species = species
        self.water_level = 50
        self.sunlight_level = 50
        self.health = 100
        self.age = 0

    def care(self, water_amount, sunlight_amount):
        self.water_level += water_amount
        self.sunlight_level += sunlight_amount
        self.age += 1

    def simulate_growth(self):
        self.health = max(0, self.health - 5)
        self.water_level -= random.randint(3, 7)
        self.sunlight_level -= random.randint(2, 5)

    def is_alive(self):
        return self.health > 0

def main():
    print("Welcome to Virtual Plant Caretaker!")

    species = input("Choose a plant species: ")
    plant = VirtualPlant(species)

    while plant.is_alive():
        print("\nPlant Status:")
        print(f"Species: {plant.species}")
        print(f"Age: {plant.age} days")
        print(f"Health: {plant.health}%")
        print(f"Water Level: {plant.water_level}%")
        print(f"Sunlight Level: {plant.sunlight_level}%")

        action = input("\nSelect an action (water/sunlight/quit): ").lower()

        if action == "quit":
            break
        elif action == "water":
            plant.care(water_amount=20, sunlight_amount=-10)
        elif action == "sunlight":
            plant.care(water_amount=-10, sunlight_amount=20)

        plant.simulate_growth()
        time.sleep(1)  # Simulate one day

    if not plant.is_alive():
        print("\nUnfortunately, your plant didn't survive. Better luck next time!")

if __name__ == "__main__":
    main()

