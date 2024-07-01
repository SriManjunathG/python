import re
import smtplib
import mysql.connector
 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="01234",
    database="movie_ticket_booking"
   
)
#****
mycursor=mydb.cursor()
#***

def Welcome():
    print("Welcome to Parvathi Cinimas")
    user = ['Maharaja','Garudan','Kalki 2D','Kalki 3D']
    print("Press 'Screen 1' for 'Maharaja'")
    print("Press 'Screen 2' for 'Garudan'")
    print("Press 'Screen 3' for 'Kalki 2D'")
    print("Press 'Screen 4' for dry 'Kalki 3D'")

    screen_no = int(input('Select the Movie:'))

    if screen_no == 1:
        movie_name = 'Maharaja'
        Maharaja()
    elif screen_no == 2:
        movie_name = 'Garudan'
        Garudan()
    elif screen_no == 3:
        movie_name = 'Kalki 2D'
        Kalki_2D()
    elif screen_no == 4:
        movie_name = 'Kalki 3D'
        Kalki_3D()
    else:
        print("Invalid choice. Please select Screen from 1 to 4.")
        Welcome()

def Maharaja():
    print('You selected Maharaja Movie:')
    process_item("Maharaja", 120)

def Garudan():
    print('You selected Garudan Movie:')
    process_item("Garudan",120)

def Kalki_2D():
    print('You Selected Kalki 2D Movie:')
    process_item("Kalki 2D",120)

def Kalki_3D():
    print('You Selected Kalki 3D Movie:')
    process_item("Kalki 3D",150)

def process_item(item_name, unit_price):
    try:
            f= open("seats_available.txt", "r") 
            txt = f.read()
            #print(txt)
            seats_No = eval(input("Select your seat: "))
            x = re.search(seats_No, txt)
            #txt=remove(your_seat)
            #print(txt)
            if x:
                print("Your seat is availble.")
                no_of_tickets = int(input("How many seats have you booked: "))
                cost = no_of_tickets * unit_price

                # Add item cost to the global cost variable
                global total_cost
                total_cost += cost

                again_book()
            else:
                print("Sorry, the item is not available.")
                Welcome()

    except FileNotFoundError:
        print("Error: File 'seats_available.txt' not found.")
        Welcome()

def again_book():
    again = input("Do you want to book again press 'yes' else 'no' ? (yes/no): ")
    if again.lower() == "yes":
        Welcome()
    else:
        cost_all()

def cost_all():
    try:
        gst_rate = 18
        gst_price = total_cost * gst_rate / 100
        net_price = total_cost + gst_price

        print(f"Total cost of the tickets: {total_cost}RS")
        print(f"GST applied at {gst_rate}%: {gst_price}RS")
        print(f"Total cost of the tickets after GST: {net_price}RS")

        # Sending email
        receiver_email = input('Enter your Mail Id:')
        sender_email = "harish3000000@gmail.com"
        password = "acra zktl ljfz bzwn"

        subject = "Purchase Confirmation"
        body = f"*Thanks for Booking Tickets*\n\nYour total cost of Ticket is:{net_price}RS"

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully!")
        database()

    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP authentication failed. Email not sent.")
    except Exception as e:
        print(f"Error: {str(e)}")

def database(): 
    sql="insert into movie_show(screen_no,movie_name,seats_No,no_of_tickets) values (%s,%s,%s,%s)"
    screen_no=int(input("enter screen_no:"))
    movie_name=input("enter movie_name:")
    seats_No=input("enter seats_No:")
    no_of_tickets=int(input("enter No,no_of_tickets:"))
    val=(screen_no,movie_name,seats_No,no_of_tickets)
    #***
    mycursor.execute(sql,val)
    #****
    mydb.commit()#to save the data into database
    
    print("data saved successfully")

# Initialize total cost
total_cost = 0

# to restart the program
Welcome()
