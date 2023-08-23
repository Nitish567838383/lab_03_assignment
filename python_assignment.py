flight_data = {
    "AI161E90": ("BLR", "BOM", 5600),
    "BR161F91": ("BOM", "BBI", 6750),
    "AI161F99": ("BBI", "BLR", 8210),
    "VS171E20": ("JLR", "BBI", 5500),
    "AS171G30": ("HYD", "JLR", 4400),
    "AI131F49": ("HYD", "BOM", 3499)
}

city_names = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def fetch_flight_information(flight_code=None, source=None, destination=None):
    if flight_code:
        if flight_code in flight_data:
            src, dest, price = flight_data[flight_code]
            print(f"Flight Code: {flight_code}")
            print(f"Source: {city_names[src]}")
            print(f"Destination: {city_names[dest]}")
            print(f"Price: {price}")
        else:
            print("Flight not found.")
    elif source:
        matching_flights = [(code, src, dest, price) for code, (src, dest, price) in flight_data.items() if src == source]
        if matching_flights:
            print("Flights from", city_names[source])
            for code, src, dest, price in matching_flights:
                print(f"Flight Code: {code}")
                print(f"Destination: {city_names[dest]}")
                print(f"Price: {price}")
        else:
            print("No flights found from", city_names[source])
    elif destination:
        matching_flights = [(code, src, dest, price) for code, (src, dest, price) in flight_data.items() if dest == destination]
        if matching_flights:
            print("Flights to", city_names[destination])
            for code, src, dest, price in matching_flights:
                print(f"Flight Code: {code}")
                print(f"Source: {city_names[src]}")
                print(f"Price: {price}")
        else:
            print("No flights found to", city_names[destination])
    else:
        print("Please provide valid input.")

user_input_type = int(input("Enter 1 for Flight Code, 2 for source city, or 3 for destination city: "))
if user_input_type == 1:
    flight_code = input("Enter Flight Code: ")
    fetch_flight_information(flight_code=flight_code)
elif user_input_type == 2:
    source = input("Enter source city: ")
    fetch_flight_information(source=source)
elif user_input_type == 3:
    destination = input("Enter destination city: ")
    fetch_flight_information(destination=destination)
else:
    print("Invalid input type.")
