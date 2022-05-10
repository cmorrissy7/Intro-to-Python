# Programming Exercise 1 - Course Information

def main():
    # Create a dictionary for room numbers
    rooms = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755',
            'NT110':'1244', 'CM241':'1411'}

    # Create a dictionary for Instructors
    instructors = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich',
                   'NT110':'Burke', 'CM241':'Lee'}

    # Create a dictionary for meeting times
    meeting_times = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.',
                     'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

    # Ask user for course number
    course = input('Enter a course number: ')

    # Display course information using course variable as the key
    if course in rooms:
        print(f'Room number: {rooms[course]}')
    else:
        print('Course not found.')

    if course in instructors:
        print(f'Instructor: {instructors[course]}')

    if course in meeting_times:
        print(f'Meeting time: {meeting_times[course]}')

    # Add extra line in output
    print()

# Call main function
main()
