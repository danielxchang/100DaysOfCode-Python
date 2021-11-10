class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        try:
            self.flight_info = data['data'][0]
        except IndexError:
            self.flight_dict = None
        else:
            self.flight_dict = {
                "price": self.flight_info['price'],
                "departure_city": self.flight_info['cityFrom'],
                "dc_code": self.flight_info['cityCodeFrom'],
                "arrival_city": self.flight_info['cityTo'],
                "ac_code": self.flight_info['cityCodeTo'],
                "outbound_date": self.flight_info['route'][0]['local_departure'].split("T")[0],
                "inbound_date": self.flight_info['route'][-1]['local_arrival'].split("T")[0]
            }
