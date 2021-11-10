class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data, stop_overs):
      self.flight_dict = {
          "price": data['price'],
          "departure_city": data['cityFrom'],
          "dc_code": data['cityCodeFrom'],
          "arrival_city": data['cityTo'],
          "ac_code": data['cityCodeTo'],
          "outbound_date": data['route'][0]['local_departure'].split("T")[0],
          "inbound_date": data['route'][-1]['local_arrival'].split("T")[0],
          "stop_overs": stop_overs,
          "link": data['deep_link']
      }
      if stop_overs:
        self.flight_dict['via_city'] = data['route'][0]['cityTo']
