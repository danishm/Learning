def kph_to_mph(kph):
    mph = kph / 1.609344
    return mph


for kph in range(0,201,5):
    mph = kph_to_mph(kph)
    print(kph, "kph is", round(mph, 2), "mph")