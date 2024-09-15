def restaurant_chatbot():
 while True:
    print("Welcome to Paragon! What would you like to know?")
    print("1. Menu\n2. Reservations\n3. Pricing & Payment\n4. Feedback & Complaints\n5.Exit")
    
    user_input = input("Enter option (1-4): ").strip()

    if user_input == "1":
        menu()
    elif user_input == "2":
        reservation()
    elif user_input == "3":
        pricing_payment()
    elif user_input == "4":
        feedback_complaints()
    elif user_input == "5":
        break
    else:
        print("Sorry, I didn't understand your choice.")

def menu():
    while True:
        print("What would you like to know about the menu?")
        user_input = input("You: ").lower()
        
        if "price" in user_input or "dish" in user_input:
            print("Here is the menu: [link to menu]")
        elif "vegan" in user_input or "veg" in user_input:
            print("We offer vegan and vegetarian options like the Vegan Buddha Bowl and Plant-Based Burgers.")
        elif "special" in user_input:
            print("Today's specials: Grilled Salmon, Spicy Chicken Tacos, and Vegan Buddha Bowl.")
        else:
            print("Sorry, I didn't understand your question.")
        
        if input("Do you have any more questions? (yes/no): ").lower() != "yes":
            break

def reservation():
    while True:
        user_input = input("Would you like to reserve a table? (yes/no): ").lower()
        
        if "yes" in user_input:
            print("Table reserved for you.")
        else:
            print("No reservation made.")
        
        if input("Do you have any more questions? (yes/no): ").lower() != "yes":
            break

def pricing_payment():
    while True:
        user_input = input("What would you like to know about pricing or payment?: ").lower()
        
        if "price" in user_input:
            print("You can view the price list on the menu here: [link to the menu]")
        elif "payment" in user_input or "methods" in user_input:
            print("We accept cash, credit cards, and mobile payments like Google Pay.")
        else:
            print("Sorry, I didn't understand your question.")
        
        if input("Do you have any more questions? (yes/no): ").lower() != "yes":
            break

def feedback_complaints():
    while True:
        user_input = input("Do you want to provide feedback or register a complaint?: ").lower()
        
        if "feedback" in user_input or "yes" in user_input:
            print("Thank you for your feedback! You can also leave a review on our website.")
        elif "complain" in user_input:
            print("We're sorry to hear that. Please provide your order number, and we'll address your issue.")
        else:
            print("Sorry, I didn't understand your question.")
        
        if input("Do you have any more questions? (yes/no): ").lower() != "yes":
            break

restaurant_chatbot()
