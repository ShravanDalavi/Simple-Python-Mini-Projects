import json
import datetime

class Plant:
    def __init__(self, name):
        self.name = name
        self.water_level = 5  # Water level from 0 to 10
        self.sunlight_level = 5  # Sunlight level from 0 to 10
        self.health = 5  # Health level from 0 to 10
        self.growth = 0  # Growth level
        self.last_care_date = datetime.datetime.now()

    def water(self):
        self.water_level = min(10, self.water_level + 3)
        self.update_health_and_growth()

    def provide_sunlight(self):
        self.sunlight_level = min(10, self.sunlight_level + 3)
        self.update_health_and_growth()

    def update_health_and_growth(self):
        current_date = datetime.datetime.now()
        days_since_last_care = (current_date - self.last_care_date).days
        self.last_care_date = current_date

        # Decrease levels due to time passing
        self.water_level = max(0, self.water_level - days_since_last_care)
        self.sunlight_level = max(0, self.sunlight_level - days_since_last_care)

        # Calculate health based on water and sunlight levels
        if self.water_level < 3 or self.sunlight_level < 3:
            self.health = max(0, self.health - 1)
        elif self.water_level > 7 and self.sunlight_level > 7:
            self.health = min(10, self.health + 1)
        else:
            self.health = max(0, min(10, self.health))

        # Increase growth if health is high
        if self.health > 7:
            self.growth += 1

    def __repr__(self):
        return (f"Plant: {self.name}\n"
                f"Water Level: {self.water_level}\n"
                f"Sunlight Level: {self.sunlight_level}\n"
                f"Health: {self.health}\n"
                f"Growth: {self.growth}\n"
                f"Last Care Date: {self.last_care_date.strftime('%Y-%m-%d %H:%M:%S')}")

class PlantCareSimulator:
    def __init__(self):
        self.plants = {}

    def create_plant(self, name):
        if name in self.plants:
            print("Plant already exists.")
        else:
            self.plants[name] = Plant(name)

    def care_for_plant(self, name, action):
        if name in self.plants:
            plant = self.plants[name]
            if action == 'water':
                plant.water()
            elif action == 'sunlight':
                plant.provide_sunlight()
            else:
                print("Invalid action.")
            plant.update_health_and_growth()
        else:
            print("Plant does not exist.")

    def view_plants(self):
        for plant in self.plants.values():
            print(plant)

    def save_to_file(self, filename='plants.json'):
        data = {name: plant.__dict__ for name, plant in self.plants.items()}
        with open(filename, 'w') as f:
            json.dump(data, f, default=str)
        print("Plants saved to file.")

    def load_from_file(self, filename='plants.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.plants = {name: Plant(**plant) for name, plant in data.items()}
                for plant in self.plants.values():
                    plant.last_care_date = datetime.datetime.strptime(plant.last_care_date, '%Y-%m-%d %H:%M:%S')
            print("Plants loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty plant simulator.")

def main():
    simulator = PlantCareSimulator()
    simulator.load_from_file()

    while True:
        print("\nVirtual Plant Care Simulator")
        print("1. Create Plant")
        print("2. Water Plant")
        print("3. Provide Sunlight to Plant")
        print("4. View All Plants")
        print("5. Save Plants to File")
        print("6. Load Plants from File")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter plant name: ")
            simulator.create_plant(name)
        elif choice == '2':
            name = input("Enter plant name to water: ")
            simulator.care_for_plant(name, 'water')
        elif choice == '3':
            name = input("Enter plant name to provide sunlight: ")
            simulator.care_for_plant(name, 'sunlight')
        elif choice == '4':
            simulator.view_plants()
        elif choice == '5':
            simulator.save_to_file()
        elif choice == '6':
            simulator.load_from_file()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
