from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


def flight_deals(home_city):
    data_manager = DataManager()
    sheet_data = data_manager.retrieve_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    home_iata_code = flight_search.get_iata_code(home_city)

    # Update google sheet and sheet_data with IATA codes
    for i, row in enumerate(sheet_data):
        city = row['city']
        row_id = row['id']
        lowest_price = row['lowestPrice']
        iata_code = flight_search.get_iata_code(city)
        flight_data = flight_search.get_flight_data(home_iata_code, iata_code).flight_dict
        if row['iataCode'] != iata_code:
            data_manager.edit_row(iata_code, row_id)
            sheet_data[i]['iataCode'] = iata_code

        if flight_data and flight_data['price'] < lowest_price:
            notification_manager.send_text(flight_data)


if __name__ == "__main__":
    home_city = input("Enter the departure city: ")
    flight_deals(home_city)
