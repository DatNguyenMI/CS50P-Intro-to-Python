import sys
import requests
import json

def main():
    if len(sys.argv) !=2:
        sys.exit ("Missing command-line argument")
    try:
        n= float(sys.argv[1])
        value = n* get_price()
        print (f"${value:,.4f}")
    except ValueError:
        sys.exit ("Command-line argument is not a number")



def get_price():
    try:
        response =requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=501ab702db92f5835ac0149a4f210401a99950ddf0d4fd2caafb56965ef9c30c")
        content = response.json() #store file as json Dict
        data_dict = content["data"]  #return value in side {data} into a new Dict called data_dict
        value = float(data_dict["priceUsd"])
        return value
    except requests.RequestException:
        sys.exit


main()
