# 1. მომხმარებელი სვამს მოთხოვნებს: ოთახის ტიპი, დღეების რაოდენობა
# 2. სისტემა აჩვენებს თავისუფალ ოთახებს
# 3. მომხმარებელი ირჩევს ოთახს
# 4. სისტემა ამოწმებს ბიუჯეტს და საშუალებას აძლევს გადახდას
# 5. დაჯავშნა ნებადართულია თუ ბიუჯეტი საკმარისია
# 6. სისტემა განახორციელებს ქულების დაგროვებას
# 7. დაჯავშნა ემატება bookings_log-ში (logging + ფაილში შენახვა)
# 8. შესაძლებელია დაჯავშნის გაუქმება

from hotel_view.customer import Customer
from hotel_view.room import Room
from hotel_view.hotel import Hotel

# ოთახების შექმნა (Room ობიექტების შექმნა)
rooms = [

    Room(1, "Single", 50, 1),
    Room(2, "Double", 100, 2),
    Room(3, "Suite", 200, 5)

]


# სასტუმროს შექმნა და ოთახების გადაცემა
hotel = Hotel(
    "Georgia Hotel",
    rooms
)


# მომხმარებლის შექმნა (სახელი და ბიუჯეტი)
customer = Customer(
    "Giorgi",
    500
)



# 1. მომხმარებელი სვამს მოთხოვნას: ოთახის ტიპი
room_type = input("Enter room type: ")



# 2. სისტემა აჩვენებს თავისუფალ ოთახებს
available_rooms = hotel.show_available_rooms(room_type)


for room in available_rooms:
    print(room)



# 3. მომხმარებელი ირჩევს ოთახს
room_number = int(
    input("Choose room number: ")
)



# მომხმარებელი უთითებს დღეების რაოდენობას
nights = int(
    input("Enter nights: ")
)



# 4. სისტემა ითვლის ფასს და ამოწმებს ბიუჯეტს
# 5. თუ ბიუჯეტი საკმარისია ხდება დაჯავშნა
hotel.book_room_for_customer(
    customer,
    room_number,
    nights
)



# 6. სისტემა აგროვებს ქულებს
print(
    "Reward points:",
    customer._reward_points
)



# მომხმარებლის მიმდინარე ბიუჯეტი
print(
    "Remaining budget:",
    customer._budget
)



# 7. დაჯავშნის ისტორიის ნახვა (bookings_log)
print(
    "Booking history:",
    hotel._booking_log
)



# 8. მომხმარებლის დაჯავშნების ნახვა
print(
    customer.show_booking_summary()
)



# 8. დაჯავშნის გაუქმება
hotel.cancel_booking(
    customer,
    room_number
)