planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
planets[3] = "Red planet"
print("Mars is also known as", planets[3])
planets.append("Pluto")
planets.pop()
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system")
planets_before_earth = planets[0:2]
print(planets_before_earth)