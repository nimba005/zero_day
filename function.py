def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""fuel report:
    main_tank: {main_tank}
    external_tank: {external_tank}
    hydrogen_tank: {hydrogen_tank}
    """
    print(output)
main_tank: 80
external_tank: 70
hydrogen_tank: 75
generate_report(80, 70, 75)

from datetime import timedelta, datetime
def arrival_time(hours=0):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
print(arrival_time())

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
print(sequence_time(4, 14, 18))

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")