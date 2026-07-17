import unittest

from functional import Room, Hotel, Customer



class TestHotelSystem(unittest.TestCase):


    # Customer.pay_for_booking() – ბიუჯეტის სწორად შემცირება
    def test_customer_payment(self):

        customer = Customer(
            "Giorgi",
            500
        )


        result = customer.pay_for_booking(200)


        # ამოწმებს გადახდა წარმატებულია თუ არა
        self.assertEqual(
            result,
            "sucessfully paid"
        )


        # ამოწმებს ბიუჯეტი სწორად შემცირდა თუ არა
        self.assertEqual(
            customer._budget,
            300
        )



    # Hotel.book_room_for_customer() – დაჯავშნა მხოლოდ თავისუფალ ოთახებზე
    def test_book_available_room(self):


        room = Room(
            1,
            "Single",
            100,
            1
        )


        hotel = Hotel(
            "Georgia Hotel",
            [room]
        )


        customer = Customer(
            "Giorgi",
            500
        )



        # პირველი დაჯავშნა უნდა შესრულდეს
        result = hotel.book_room_for_customer(
            customer,
            1,
            2
        )


        self.assertTrue(result)


        # ვამოწმებთ რომ ოთახი აღარ არის თავისუფალი
        self.assertFalse(
            room._is_available
        )



        # მეორე მცდელობა იგივე ოთახზე უნდა ჩავარდეს
        result2 = hotel.book_room_for_customer(
            customer,
            1,
            1
        )


        self.assertFalse(result2)



if __name__ == "__main__":
    unittest.main()