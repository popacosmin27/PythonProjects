import json
import os

# Sample menu items with realistic descriptions and prices
menu_items = [
    # Appetizers
    {
        "name": "Crispy Spring Rolls",
        "description": "Hand-rolled crispy spring rolls filled with vegetables, glass noodles, and mushrooms. Served with sweet chili sauce.",
        "price": 8.99,
        "category": "Appetizer"
    },
    {
        "name": "Bruschetta",
        "description": "Grilled artisan bread topped with fresh tomatoes, basil, garlic, and extra virgin olive oil.",
        "price": 7.99,
        "category": "Appetizer"
    },
    {
        "name": "Spinach Artichoke Dip",
        "description": "Creamy blend of spinach, artichokes, and melted cheeses, served with tortilla chips.",
        "price": 10.99,
        "category": "Appetizer"
    },

    # Main Courses
    {
        "name": "Grilled Salmon",
        "description": "Fresh Atlantic salmon fillet grilled to perfection, served with roasted vegetables and lemon herb sauce.",
        "price": 24.99,
        "category": "Main Course"
    },
    {
        "name": "Classic Beef Burger",
        "description": "1/2 pound Angus beef patty with lettuce, tomato, onion, and cheese on a brioche bun. Served with fries.",
        "price": 16.99,
        "category": "Main Course"
    },
    {
        "name": "Fettuccine Alfredo",
        "description": "Fresh fettuccine pasta in creamy Alfredo sauce with Parmesan cheese and fresh herbs.",
        "price": 18.99,
        "category": "Main Course"
    },
    {
        "name": "Chicken Marsala",
        "description": "Pan-seared chicken breast in Marsala wine sauce with mushrooms, served with mashed potatoes.",
        "price": 21.99,
        "category": "Main Course"
    },
    {
        "name": "Vegetable Stir-Fry",
        "description": "Fresh seasonal vegetables stir-fried in Asian sauce, served with steamed rice or noodles.",
        "price": 15.99,
        "category": "Main Course"
    },

    # Desserts
    {
        "name": "Chocolate Lava Cake",
        "description": "Warm chocolate cake with a molten center, served with vanilla ice cream and raspberry sauce.",
        "price": 8.99,
        "category": "Dessert"
    },
    {
        "name": "New York Cheesecake",
        "description": "Classic New York style cheesecake with graham cracker crust, topped with fresh berries.",
        "price": 7.99,
        "category": "Dessert"
    },
    {
        "name": "Tiramisu",
        "description": "Traditional Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cream.",
        "price": 8.99,
        "category": "Dessert"
    },

    # Beverages
    {
        "name": "Fresh Fruit Smoothie",
        "description": "Blend of seasonal fruits with yogurt and honey. Ask server for today's selections.",
        "price": 5.99,
        "category": "Beverage"
    },
    {
        "name": "Italian Soda",
        "description": "Sparkling water with your choice of flavored syrup and cream.",
        "price": 4.99,
        "category": "Beverage"
    },
    {
        "name": "Craft Beer",
        "description": "Selection of local and imported craft beers. Ask server for current options.",
        "price": 6.99,
        "category": "Beverage"
    },
    {
        "name": "House Wine",
        "description": "Selection of red or white house wines by the glass.",
        "price": 7.99,
        "category": "Beverage"
    }
]

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save menu items to JSON file
try:
    with open('data/menu.json', 'w', encoding='utf-8') as f:
        json.dump(menu_items, f, indent=2)
    print("Menu items have been successfully added to data/menu.json")
except IOError as e:
    print(f"Error saving menu items: {str(e)}")