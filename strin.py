name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
template = """Gravity facts about {name}
planet name: {planet}
gravity on {name}: {gravity} m/s2"""
print(template.format(name=name, planet=planet, gravity=gravity))