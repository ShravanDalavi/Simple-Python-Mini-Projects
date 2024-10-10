import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}\n"

class RecipeRecommendationSystem:
    def __init__(self):
        self.recipes = [
            Recipe("Pancakes", ["flour", "milk", "egg", "sugar", "baking powder"], "Mix all ingredients and cook on a griddle."),
            Recipe("Omelette", ["egg", "milk", "salt", "pepper"], "Beat eggs and milk, then cook in a pan with salt and pepper."),
            Recipe("Salad", ["lettuce", "tomato", "cucumber", "olive oil", "salt"], "Chop vegetables and mix with olive oil and salt.")
        ]
        self.available_ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient not in self.available_ingredients:
            self.available_ingredients.append(ingredient)
        else:
            print("Ingredient already added.")

    def recommend_recipes(self):
        recommended = []
        for recipe in self.recipes:
            if all(item in self.available_ingredients for item in recipe.ingredients):
                recommended.append(recipe)
        if recommended:
            for recipe in recommended:
                print(recipe)
        else:
            print("No recipes found with the available ingredients.")

    def save_ingredients(self, filename='ingredients.json'):
        with open(filename, 'w') as f:
            json.dump(self.available_ingredients, f)
        print("Ingredients saved to file.")

    def load_ingredients(self, filename='ingredients.json'):
        try:
            with open(filename, 'r') as f:
                self.available_ingredients = json.load(f)
            print("Ingredients loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty ingredient list.")

def main():
    system = RecipeRecommendationSystem()
    system.load_ingredients()

    while True:
        print("\nRecipe Recommendation System")
        print("1. Add Ingredient")
        print("2. Recommend Recipes")
        print("3. Save Ingredients to File")
        print("4. Load Ingredients from File")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ingredient = input("Enter ingredient name: ").strip()
            system.add_ingredient(ingredient)
        elif choice == '2':
            system.recommend_recipes()
        elif choice == '3':
            system.save_ingredients()
        elif choice == '4':
            system.load_ingredients()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
