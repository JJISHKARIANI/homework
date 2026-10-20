class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        MovieTicket.total_tickets_sold += 1

ticket_1 = MovieTicket(movie_title="Odyssey", seat_number="8", price="20")
ticket_2 = MovieTicket(movie_title="Odyssey", seat_number="9", price="20")
ticket_3 = MovieTicket(movie_title="Odyssey", seat_number="10", price="20")        

print("=" * 40)
print(f"ticket 1: movie: {ticket_1.movie_title}, seat: {ticket_1.seat_number}, price: {ticket_1.price}")
print("=" * 40)
print(f"ticket 2: movie: {ticket_2.movie_title}, seat: {ticket_2.seat_number}, price: {ticket_2.price}")
print("=" * 40)
print(f"ticket 3: movie: {ticket_3.movie_title}, seat: {ticket_3.seat_number}, price: {ticket_3.price}")
print("=" * 40)
print(f"total tickets sold: {MovieTicket.total_tickets_sold}")