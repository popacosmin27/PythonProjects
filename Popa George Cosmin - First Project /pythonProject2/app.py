import streamlit as st
from datetime import datetime
import hashlib
import json
import os
from typing import Dict, List, Any, Union
from PIL import Image

home_image = Image.open('images/TOO_restaurant_Panoramique_vue_Paris_nuit_v2-scaled.png')
about_us_image = Image.open('images/26258537.jpg')


def load_data() -> None:
    """Initialize data directories and files if they don't exist"""
    if not os.path.exists('data'):
        os.makedirs('data')

    # Initialize data files with default values if they don't exist
    default_files = {
        'data/menu.json': [],
        'data/orders.json': [],
        'data/users.json': {}
    }

    for file_path, default_value in default_files.items():
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(default_value, f)
            except IOError as e:
                st.error(f"Error creating {file_path}: {str(e)}")


def save_menu(menu_items: List[Dict[str, Any]]) -> None:
    """Save menu items to JSON file"""
    try:
        with open('data/menu.json', 'w', encoding='utf-8') as f:
            json.dump(menu_items, f, indent=2)
    except IOError as e:
        st.error(f"Error saving menu: {str(e)}")


def load_menu() -> List[Dict[str, Any]]:
    """Load menu items from JSON file"""
    try:
        with open('data/menu.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except IOError as e:
        st.error(f"Error loading menu: {str(e)}")
        return []


def save_order(order: Dict[str, Any]) -> None:
    """Save order to JSON file"""
    try:
        orders = get_orders()
        orders.append(order)
        with open('data/orders.json', 'w', encoding='utf-8') as f:
            json.dump(orders, f, indent=2)
    except IOError as e:
        st.error(f"Error saving order: {str(e)}")


def get_orders() -> List[Dict[str, Any]]:
    """Get all orders from JSON file"""
    try:
        with open('data/orders.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except IOError as e:
        st.error(f"Error loading orders: {str(e)}")
        return []


def save_user(username: str, password: str) -> None:
    """Save user credentials to JSON file"""
    try:
        with open('data/users.json', 'r', encoding='utf-8') as f:
            users = json.load(f)

        users[username] = hashlib.sha256(password.encode()).hexdigest()

        with open('data/users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)
    except IOError as e:
        st.error(f"Error saving user: {str(e)}")


def verify_user(username: str, password: str) -> bool:
    """Verify user credentials"""
    try:
        with open('data/users.json', 'r', encoding='utf-8') as f:
            users = json.load(f)

        if username in users:
            return users[username] == hashlib.sha256(password.encode()).hexdigest()
        return False
    except IOError as e:
        st.error(f"Error verifying user: {str(e)}")
        return False


# --- Page Functions ---
def home_page() -> None:
    st.title("Welcome to Our Restaurant 🍽️")
    st.image(home_image, caption="Restaurant Ambiance")
    st.write("""
    Welcome to our restaurant! We offer a wide variety of delicious dishes 
    prepared by our expert chefs. Enjoy our comfortable ambiance and 
    excellent service.
    """)

    st.subheader("Today's Specials")
    menu = load_menu()
    if menu:
        for item in menu[:3]:  # Show only first 3 items
            st.write(f"**{item['name']}** - ${item['price']}")
            st.write(item['description'])


def delivery_page() -> None:
    st.title("Order Delivery 🚚")

    menu = load_menu()
    if not menu:
        st.warning("No items available in the menu")
        return

    order_items: List[Dict[str, Union[str, int, float]]] = []
    for item in menu:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"**{item['name']}** - ${item['price']}")
            st.write(item['description'])
        with col2:
            quantity = st.number_input(
                f"Quantity for {item['name']}",
                min_value=0,
                max_value=10,
                value=0,
                key=f"qty_{item['name']}"
            )
        st.text("")
        st.text("")
        if quantity > 0:
            order_items.append({
                'name': item['name'],
                'quantity': quantity,
                'price': item['price']
            })

    if order_items:
        st.subheader("Your Order")
        total = sum(item['quantity'] * item['price'] for item in order_items)
        st.write(f"Total: ${total:.2f}")

        with st.form("delivery_form"):
            name = st.text_input("Name")
            address = st.text_input("Delivery Address")
            phone = st.text_input("Phone Number")

            if st.form_submit_button("Place Order"):
                if name and address and phone:
                    order = {
                        'customer': name,
                        'address': address,
                        'phone': phone,
                        'items': order_items,
                        'total': total,
                        'timestamp': datetime.now().isoformat(),
                        'status': 'pending'
                    }
                    save_order(order)
                    st.success("Order placed successfully!")
                else:
                    st.error("Please fill in all fields")


def about_us_page() -> None:
    st.title("About Us 📖")
    st.image(about_us_image)
    st.write("""
    ### Our Story

    At our restaurant, we believe that food is more than just a meal—it’s a way to bring people together, to celebrate traditions, and to create lasting memories. Our journey began with a simple dream: to share our passion for good food and warm hospitality with our community. Inspired by [family recipes/traditional cuisine/local ingredients/culinary travels], we set out to create a space where everyone feels at home, whether they’re here for a casual bite or a special occasion.

    Our kitchen is guided by the values of quality, authenticity, and creativity. We work closely with local farmers, fishermen, and artisans to source the freshest ingredients, and our menu is a reflection of the changing seasons and the rich flavors of [your region/culture/country]. Every dish is crafted with care and attention to detail, blending traditional techniques with a modern touch.

    We opened our doors in 2020, and since then, we’ve been dedicated to offering more than just a dining experience. For us, it’s about creating a space where laughter, stories, and great food come together. Our team is like family, and we want our guests to feel the same—welcomed, valued, and always eager to return.

    Thank you for being a part of our journey. We look forward to serving you and sharing our passion for food with you, one delicious dish at a time.”

    

    ### Our Mission

    At our restaurant, our mission is to create a welcoming space where every guest feels at home, enjoying high-quality, delicious food that brings people together. We are dedicated to crafting dishes that honor tradition while embracing innovation, using the freshest ingredients sourced from trusted local farmers and suppliers.

    We believe in sustainability, supporting our community, and delivering exceptional service with a personal touch. Every meal is a celebration of the flavors, stories, and cultures that inspire us, and our goal is to provide an unforgettable dining experience that leaves a lasting impression. Whether it’s a casual meal or a special occasion, we are committed to making every visit a memorable one, guided by our passion for great food, hospitality, and a love for bringing people together.”
    

    ### Our Team

    At our restaurant, our team is the heart and soul of everything we do. We are a diverse group of passionate individuals who share a common love for great food, exceptional service, and creating unforgettable experiences for our guests. From the kitchen to the dining room, every member of our team plays a vital role in bringing our culinary vision to life.

    Our chefs are the creative minds behind our menu, crafting dishes that combine tradition with innovation, always using the freshest ingredients and techniques. Our kitchen staff works with dedication and precision to ensure that every plate that leaves our kitchen is a masterpiece.

    In the front of the house, our friendly and attentive service staff is dedicated to making every guest feel welcomed and valued. They bring warmth, energy, and a personal touch to every table, making sure that your dining experience is comfortable, enjoyable, and memorable.

    Behind the scenes, our management team ensures that every detail is perfect, from the moment you walk in the door to the time you leave. We work together like a family, each member bringing their unique talents, skills, and personality to the table, united by our commitment to hospitality and excellence.

    At our restaurant, we don’t just work together; we support each other, learn from each other, and grow together. We are proud to share our passion for food and service with you, and we can’t wait to welcome you to our restaurant.”

    """)


def contact_us_page() -> None:
    st.title("Contact Us ☎️")
    st.write("""
    ### Get in Touch

    We'd love to hear from you! Feel free to reach out with any questions, 
    feedback, or concerns.
    """)

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        if st.form_submit_button("Send Message"):
            if name and email and message:
                st.success("Message sent! We'll get back to you soon.")
            else:
                st.error("Please fill in all fields")

    st.write("""
    ### Location 📍

    27 Victoria Street  
    Bucharest, 117512

    ### Hours ⏰

    Monday - Friday: 11:00 AM - 10:00 PM  
    Saturday - Sunday: 10:00 AM - 11:00 PM

    ### Phone 📞

    +40752540596
    
    """)


def admin_login() -> None:
    st.title("Admin Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if verify_user(username, password):
                st.session_state['admin_logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid credentials")


def admin_page() -> None:
    st.title("Admin Dashboard 💻")

    # Logout button
    if st.button("Logout"):
        st.session_state['admin_logged_in'] = False
        st.rerun()

    tab1, tab2 = st.tabs(["Manage Menu", "View Orders"])

    with tab1:
        st.subheader("Add Menu Item")
        with st.form("add_menu_item"):
            name = st.text_input("Item Name")
            description = st.text_area("Description")
            price = st.number_input("Price", min_value=0.0, step=0.01)
            category = st.selectbox("Category", ["Appetizer", "Main Course", "Dessert", "Beverage"])

            if st.form_submit_button("Add Item"):
                if name and description and price > 0:
                    menu = load_menu()
                    menu.append({
                        'name': name,
                        'description': description,
                        'price': price,
                        'category': category
                    })
                    save_menu(menu)
                    st.success("Item added successfully!")
                else:
                    st.error("Please fill in all fields with valid values")

        st.subheader("Current Menu")
        menu = load_menu()
        for idx, item in enumerate(menu):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{item['name']}** - ${item['price']}")
                st.write(item['description'])
            with col2:
                if st.button("Delete", key=f"del_{idx}"):
                    menu.pop(idx)
                    save_menu(menu)
                    st.rerun()

    with tab2:
        st.subheader("Orders")
        orders = get_orders()
        for order in orders:
            with st.expander(f"Order from {order['customer']} - {order['timestamp']}"):
                st.write(f"**Customer:** {order['customer']}")
                st.write(f"**Address:** {order['address']}")
                st.write(f"**Phone:** {order['phone']}")
                st.write("**Items:**")
                for item in order['items']:
                    st.write(f"- {item['name']} x{item['quantity']}")
                st.write(f"**Total:** ${order['total']:.2f}")
                st.write(f"**Status:** {order['status']}")


def main() -> None:
    # Initialize session state
    if 'admin_logged_in' not in st.session_state:
        st.session_state['admin_logged_in'] = False

    # Initialize data
    load_data()

    # Navigation
    if not st.session_state['admin_logged_in']:
        page = st.sidebar.selectbox(
            "Navigate to",
            ["Home", "Delivery", "About Us", "Contact Us", "Admin Login"]
        )
    else:
        page = "Admin Dashboard"

    # Display selected page
    if page == "Home":
        home_page()
    elif page == "Delivery":
        delivery_page()
    elif page == "About Us":
        about_us_page()
    elif page == "Contact Us":
        contact_us_page()
    elif page == "Admin Login":
        admin_login()
    elif page == "Admin Dashboard":
        admin_page()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Restaurant App",
        page_icon="🍽️",
        layout="wide"
    )
    main()