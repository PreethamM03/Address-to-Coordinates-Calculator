from pprint import pprint
import googlemaps as gm
API_KEY = 'PASTE YOUR GOOGLE API'

map_client = gm.Client(API_KEY)

address = input("what is your address? ")
response = map_client.geocode(address)

#pprint(response)
print("The Coordinates are", response[0]['geometry']["location"]['lat'], "latitude and",response[0]['geometry']["location"]['lng'],"longitude")