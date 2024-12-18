import customtkinter

from interface.main_page import MainPage
from interface.information import Information
from interface.location import Location
from interface.flight_type_page import FlightTypePage
from interface.login import Login
from interface.sign_up import Signup
from interface.trips import One_Way
from interface.trips import Round_Trip
from interface.seats import Seats
from interface.ticket import Ticket
from interface.checkout import Checkout
from interface.invoice import Invoice

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1000x600")
        self.title('SAFR — Airline Reservation System')
        self.iconbitmap("images/Logo.ico")
        self.resizable(0, 0)
        
        mainpage = MainPage(self)
        login = Login(self)
        signup = Signup(self)
        information = Information(self)
        location = Location(self)
        flight_type = FlightTypePage(self)
        oneway = One_Way(self)
        roundtrip = Round_Trip(self)
        seats = Seats(self)
        checkout = Checkout(self)
        invoice = Invoice(self)
        ticket = Ticket(self)
        
        self.current_window = 0
        self.windows = [mainpage, information, location, flight_type,
                        oneway, roundtrip, seats, checkout, invoice,
                        ticket, login, signup]
        
        self.MAIN_PAGE = self.windows.index(mainpage)
        self.INFORMATION_PAGE = self.windows.index(information)
        self.LOCATION_PAGE = self.windows.index(location)
        self.FLIGHT_TYPE_PAGE = self.windows.index(flight_type)
        self.ONEWAY_PAGE = self.windows.index(oneway)
        self.ROUNDTRIP_PAGE = self.windows.index(roundtrip)
        self.SEATS_PAGE = self.windows.index(seats)
        self.CHECKOUT_PAGE = self.windows.index(checkout)
        self.INVOICE_PAGE = self.windows.index(invoice)
        self.TICKET_PAGE = self.windows.index(ticket)
        self.LOGIN_PAGE = self.windows.index(login)
        self.SIGNUP_PAGE = self.windows.index(signup)
        
        self.configure_layout()
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')

    def configure_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def show_next_frame(self):
        self.windows[self.current_window].grid_remove()
        
        self.current_window += 1
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_previous_frame(self):
        self.windows[self.current_window].grid_remove()
        
        self.current_window -= 1
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_home_frame(self):
        pass
        
app = App()
app.mainloop()