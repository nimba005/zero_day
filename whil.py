from time import sleep
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)
print("Blast off!! 🚀")
planet = {
    'name': 'mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moons(s)')
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
 print(f'{key}: {rainfall[key]}cm')
 total_rainfall = 0
 for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter.')