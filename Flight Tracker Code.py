from tkinter import *

class FlightTracker:
    def __init__(self, window):
        # This will Initialize the main window allowing it to have an infinite
        self.GUI_window = window
        self.GUI_window.geometry("800x500")
        self.GUI_window.resizable(False, False)
        self.GUI_window.title("Flight Arrival Tracker")

        # Create labels, entry, and buttons
        self.create_labels_entry_buttons()

        # Create a list to store flight data
        self.flight_data = []

    def create_labels_entry_buttons(self):
        # Label
        label = Label(self.GUI_window,
                      text="Flight Arrival Tracker",
                      font=("Arial", 20, "bold"),
                      fg="#00FF00",
                      bg="black",
                      relief=RAISED,
                      bd=10,
                      padx=40,
                      pady=15)
        label.pack()

        # Shows the Label for: (Enter Flight Number: (Entry widget box) )
        label_EFN = Label(self.GUI_window,
                          text="Enter Flight Number:",
                          font=("Arial", 10, "bold"),
                          fg="#00FF00",
                          bg="black", )
        label_EFN.pack()
        label_EFN.place(x=215, y=170)

        # Entry widget for the user to enter the flight number
        self.entry = Entry(self.GUI_window, font=("Arial", 11))
        self.entry.pack()
        self.entry.place(x=355.45, y=170)

        # Text widget to display the flight information
        self.result_text = Text(self.GUI_window, width=52, height=10, font=("Arial", 10, "bold"))
        self.result_text.pack()
        self.result_text.place(x=214, y=250)

        # User click the Enter button to Search for Data in .csv.
        button_enter = Button(self.GUI_window,
                              text="Enter",
                              command=self.click_Enter,
                              font=("Arial", 8, "bold"),
                              fg="#00FF00",
                              bg="black",
                              padx=10,
                              pady=0)
        button_enter.pack()
        button_enter.place(x=525, y=170)

        # Creates the Write label button for user to press data in the FlightData-W.csv file.
        button_Write = Button(self.GUI_window,
                              text="Write",
                              command=self.click_Write,
                              font=("Arial", 8, "bold"),
                              fg="#00FF00",
                              bg="black",
                              padx=10,
                              pady=0)
        button_Write.pack()
        button_Write.place(x=595.73, y=170.27)

        # Delete button basically clears the information presented in the box.
        button_Delete = Button(self.GUI_window,
                               text="Delete",
                               command=self.click_Delete,
                               font=("Arial", 10, "bold"),
                               fg="#00FF00",
                               bg="black",
                               padx=5,
                               pady=0)
        button_Delete.pack()
        button_Delete.place(x=366, y=420)

    def click_Enter(self):
        # Gets the flight number entered by the user
        flight_number = self.entry.get()

        # Opens the text file (FlightData-R.csv) and searches for the flight number then outputs all information on flight.
        with open("FlightData-R.csv", "r") as file:
            for line in file:
                if flight_number in line:
                    # Split the line into individual pieces of data
                    data = line.split(',')

                    # Formats the different  outputs
                    formatted_output = f"Flight Number: {data[0]}\n" \
                                       f"Flight Origin: {data[1]}\n" \
                                       f"Aircraft Number: {data[2]}\n" \
                                       f"Airline Name: {data[3]}\n" \
                                       f"Airline Code: {data[4]}\n" \
                                       f"Plane Model: {data[5]}\n" \
                                       f"Distance: {data[6]}" " km\n" \
                                       f"Speed: {data[7]}" " km/h\n" \
                                       f"Time tabled Arrival: {data[8]}"

                    # Displays the information in the Text widget
                    self.result_text.delete(1.0, "end")
                    self.result_text.insert("end", formatted_output)
                    return

        # This is for when the flight number is not found
        self.result_text.delete(1.0, "end")
        self.result_text.insert("end", "Flight not found.")

    def click_Write(self):
        # Gets the detail/info of the flight number entered by the user
        flight_number = self.entry.get()

        # Which would open the text file (FlightData-W.csv) and write the flight number in the column.
        with open("FlightData-W.csv", "a") as write_file:
            write_file.write(flight_number + "\n")

    def click_Delete(self):
        #Completely clears the entry and result_text widgets when Delete is clicked
        self.entry.delete(0, "end")
        self.result_text.delete(1.0, "end")


# Create the main window
root = Tk()

# Creates an instance of the FlightTracker class
app = FlightTracker(root)

# Sets the background color and starts the main loop
root.config(background="black")
root.mainloop()
# Allows the application to have an infinite loop to stay open.
