def badge_maker(name):
    return "Hello, my name is {}.".format(name) 

def batch_badge_creator(names):
    badges = ["Hello, my name is {}.".format(name) for name in names]
    return badges

def assign_rooms(speakers):
    room_assignments = ["Hello, {}! You'll be assigned to room {}!".format(speaker, room) for room, speaker in enumerate(speakers, start=1)]
    return room_assignments

    

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
