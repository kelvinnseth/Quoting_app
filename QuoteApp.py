import tkinter as tk
from tkinter import messagebox


class QuotingApp:
    def __init__(self):
        self.rate_sqm = 20            # Rate per square meter
        self.total = 0                 # Total cost before discount
        self.discount_amount = 0       # Amount of discount applied

    def get_cost(self, customer):
        # Calculate the cost based on the customer's dimensions
        if customer.length < 1 or customer.width < 1:
            raise ValueError("Length and Width must be greater than zero")  # Validate input dimensions
        area = customer.length * customer.width  # Calculate area (length * width)
        cost = self.rate_sqm * area              # Calculate total cost (area * rate)
        self.total = float(cost)                  # Store total cost as a float
        return self.total                          # Return the calculated total cost

    def apply_discount(self, percentage):
        # Apply a discount to the total cost
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")  # Validate discount percentage
        calculated_discount = percentage / 100                          # Convert percentage to a decimal
        self.discount_amount = self.total * calculated_discount         # Calculate the discount amount
        return self.discount_amount                                      # Return the discount amount

    def show_quote(self, customer):
        # Generate a formatted quote string with details
        discounted = self.total - self.discount_amount                  # Calculate final cost after discount
        return (f"Your Quote is £{self.total:.2f}\n"                    # Total cost
                f"We've applied a discount of £{self.discount_amount:.2f}\n"  # Discount amount
                f"Dimensions are {customer.length}M by {customer.width}M\n"  # Dimensions
                f"Final quote is £{discounted:.2f}\n")                  # Final quoted price

    def generate_quote(self, customer, discount):
        # Generate a full quote for a customer with an optional discount
        self.get_cost(customer)           # Get the cost based on customer dimensions
        self.apply_discount(discount)     # Apply the given discount percentage
        return self.show_quote(customer)  # Show the complete quote


class Customer:
    def __init__(self, length, width):
        # Initialize the customer with given dimensions
        self.length = length      # Length of the area
        self.width = width        # Width of the area


class QuoteAppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Quoting Application")

        self.quote_app = QuotingApp()  # Create an instance of QuotingApp

        # Create labels and entry fields for length and width
        self.length_label = tk.Label(master, text="Length (M):")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.width_label = tk.Label(master, text="Width (M):")
        self.width_label.pack()

        self.width_entry = tk.Entry(master)
        self.width_entry.pack()

        self.discount_label = tk.Label(master, text="Discount Percentage:")
        self.discount_label.pack()

        self.discount_entry = tk.Entry(master)
        self.discount_entry.pack()

        # Create a button to generate the quote
        self.quote_button = tk.Button(master, text="Generate Quote", command=self.generate_quote)
        self.quote_button.pack()

        # Text widget to display the quote result
        self.result_text = tk.Text(master, width=50, height=15)
        self.result_text.pack()

    def generate_quote(self):
        try:
            # Check for empty fields
            if not self.length_entry.get() or not self.width_entry.get() or not self.discount_entry.get():
                raise ValueError("All fields must be filled out.")

            # Get values from the input fields
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            discount = float(self.discount_entry.get())

            # Create a customer instance
            customer = Customer(length, width)

            # Generate the quote
            quote = self.quote_app.generate_quote(customer, discount)

            # Clear previous results
            self.result_text.delete(1.0, tk.END)

            # Display the quote
            self.result_text.insert(tk.END, quote)

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))  # Show error message for invalid input


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()                   # Create the main window
    gui = QuoteAppGUI(root)          # Create the GUI
    root.mainloop()                  # Start the Tkinter main loop
