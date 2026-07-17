# კლასი Hotel
# აღწერა: სასტუმროს მართვის კლასი
# Attributes:
# • name: str – სასტუმროს სახელი
# • rooms: list – სასტუმროს ყველა ოთახი (Room ობიექტები)
# • bookings_log: list – დაჯავშნების ისტორია
# Methods:
# • show_available_rooms(self, room_type: str = None) -> list – თავისუფალი
# ოთახების სია

# • book_room_for_customer(self, customer: Customer, room_number: int, nights: int)
# -> bool – კონკრეტული ოთახის დაჯავშნა მომხმარებლისთვის
# • calculate_total_booking(self, room_number: int, nights: int) -> float – ჯამური
# ღირებულება
# • log_booking(self, customer: Customer, room: Room, total_price: float) – ლოგირება
# (შესაძლებელია logging მოდულით)
# • cancel_booking(self, customer: Customer, room_number: int) – დაჯავშნის
# გაუქმება
import logging

logging.basicConfig(
    filename="hotel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

class Hotel:
    def __init__(self, name, rooms: list, ):
        self._name = name
        self._rooms = rooms
        self._booking_log = []

    def show_available_rooms(self, room_type) -> list:
        rooms_list = [room for room in self._rooms if room._is_available and room._room_type == room_type ]

        return rooms_list
    
    def calculate_total_booking(self, room_number: int, nights: int) -> list:
        for room in self._rooms:
            if room._room_number == room_number:
                return room.calculate_price(nights)
    
    def log_booking(self, customer: Customer, room: Room, total_price: float):
        logger.info({
            "customer": customer,
            "room": room,
            "price": total_price
        })
    
    def cancel_booking(self, customer: Customer, room_number: int):
        for room in self._rooms:
            if room._room_number == room_number:
                room.release_room()
                customer.remove_room(room)

                logger.info(
                    f"{customer._name} cancelled booking for room {room._room_number}"
                )

                return True

        return False

    def book_room_for_customer(self, customer, room_number: int, nights: int):

        for room in self._rooms:

            if room._room_number == room_number:

                if not room._is_available:
                    print("ოთახი უკვე დაჯავშნილია")
                    return False

                total_price = room.calculate_price(nights)

                payment = customer.pay_for_booking(total_price)


                if payment == "sucessfully paid":

                    room.book_room()


                    customer.add_rooms(room)

                    customer._reward_points += int(total_price / 10)

                    self.log_booking(
                        customer,
                        room,
                        total_price
                    )


                    print("დაჯავშნა წარმატებით დასრულდა")

                    return True


                else:

                    print("ბიუჯეტი არ არის საკმარისი")

                    return False


        print("ასეთი ოთახი ვერ მოიძებნა")

        return False