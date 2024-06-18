import re
import smtplib

def main():
    user = ['Dhal items', 'vegetables', 'fruits', 'dry fruits', 'cosmetics', 'vessels','juice','chocolate','chips']
    print("Press 1 for dhal")
    print("Press 2 for vegetables")
    print("Press 3 for fruits")
    print("Press 4 for dry fruits")
    print("Press 5 for cosmetics")
    print("Press 6 for vessels")
    print("press 7 for juice")
    print("press 8 for chocolate")
    print("press 9 for chips")

    num = int(input('Press number to select: '))

    if num == 1:
        dhal()
    elif num == 2:
        vegetables()
    elif num == 3:
        fruits()
    elif num == 4:
        dry_fruits()
    elif num == 5:
        cosmetics()
    elif num == 6:
        vessels()
    elif num == 7:
        juice()
    elif num == 8:
        chocolate()
    elif num == 9:
        chips()
    else:
        print("Invalid choice. Please select a number from 1 to 6.")
        main()

def dhal():
    print('Please select your dhal:')
    process_item("dhal", 30)

def vegetables():
    print('Please select your vegetables:')
    process_item("vegetables", 30)

def fruits():
    print('Please select your fruits:')
    process_item("fruits", 80)

def dry_fruits():
    print('Please select your dry fruits:')
    process_item("dry fruits", 80)

def cosmetics():
    print('Please select your cosmetics:')
    process_item("cosmetics", 100)

def vessels():
    print('Please select your vessels:')
    process_item("vessels", 150)

def juice():
    print('Please select your juice:')
    process_item("juice", 50)

def chocolate():
    print('Please select your chocolate:')
    process_item("chocolate", 40)

def chips():
    print('Please select your chips:')
    process_item("chips", 50)

def process_item(item_name, unit_price):
    try:
            f= open("ex10.txt", "r") 
            txt = f.read()
            your_item = input("Enter item name: ")
            x = re.search(your_item, txt)

            if x:
                print("Your item is available.")
                how_many = int(input("How many items do you want?: "))
                cost = how_many * unit_price

                # Add item cost to the global cost variable
                global total_cost
                total_cost += cost

                another_item()
            else:
                print("Sorry, the item is not available.")
                main()

    except FileNotFoundError:
        print("Error: File 'ex10.txt' not found.")
        main()

def another_item():
    another = input("Do you want to purchase another item? (yes/no): ")
    if another.lower() == "yes":
        main()
    else:
        cost_all()

def cost_all():
    try:
        gst_rate = 18
        gst_price = total_cost * gst_rate / 100
        net_price = total_cost + gst_price

        print(f"Total cost of the products: ${total_cost}")
        print(f"GST applied at {gst_rate}%: ${gst_price}")
        print(f"Total cost of the products after GST: ${net_price}")

        # Sending email
        receiver_email = ["20t126@kce.ac.in"]
        sender_email = "harish3000000@gmail.com"
        password = "qdlg ybtw dagf kqyo"

        subject = "Purchase Confirmation"
        body = f"**Thanks for purchasing in our supermarket!**\n\nYour total cost of purchase: ${net_price}"

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP authentication failed. Email not sent.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Initialize total cost
total_cost = 0

# to restart the program
main()