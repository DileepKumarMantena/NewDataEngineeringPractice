countries_capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}


def get_capital(country):


    if country in countries_capitals:
        return f"The capital of {country} is {countries_capitals[country]}."
    else:
        return f"Country '{country}' not found in the records."



country_name = input("Enter the name of the country: ")


print(get_capital(country_name))