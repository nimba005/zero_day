try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")

def main():
    try:
        configuration = open('error.txt')
    except Exception:
        print("couldn't find the error.txt file!")
if __name__ == '__main__':
    main()

loaded_config = """# Rocket ship configuration file!
fuel_tanks=4
oxygen_tanks=3
initial_production_level=84
$ End of file"""
parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'unable to parse {line}')
print(parsed_config)

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
print(water_left(5, 100, 2))