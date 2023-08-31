# nested

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "hamburg", "Stu"]
}

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "hamburg", "Stu"]
}

travel_log3 = [
    {
        "countries": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12,
    },
    {
        "countries": "Germany", "cities_visited": ["Berlin", "hamburg", "Stu"], "total_visits": 5,
    }

]

# print(capitals)
# print(travel_log)
# print(travel_log2)
print(travel_log3)


# Travel log
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, numb, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = numb
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
