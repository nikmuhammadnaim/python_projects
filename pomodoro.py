import string
from datetime import datetime

print("\n-------------------------------------------")
print("Welcome to Nik Muhammad Naim's Pomodoro App")
print("-------------------------------------------\n")

start_time = 0
end_time = 0
paused_time = []

# Read the subjects and learning materials available
with open('data\\pomodoro_files\\subjects.txt') as subjects:
    subject_list = subjects.read().splitlines()

with open('data\\pomodoro_files\\learning_materials.txt') as learning_materials:
    learning_list = learning_materials.read().splitlines()

# Function for printing list
def print_list(my_list):
    ready_list = ''
    for num, item in zip(string.ascii_lowercase, my_list):
        ready_list += "\n{}) {}".format(num, item)
    return ready_list

# Select subject and learning material
while True:
    subject = input('Please select one subject that you would ' +
                    'like to study today:' + print_list(subject_list) +
                    '\n=> ')
    if subject.lower() in ('a', 'b', 'c'):
        while True:
            source = input('\nPlease specify the learning material you will' +
                           ' be using:' + print_list(learning_list) +
                           '\n=> ') 
            if source in ('a', 'b', 'c'):
                break
            else:
                print('Please enter a valid input!')
        break
    else:
        print('Please enter a valid input!')

# Start time
while True:
    pomo_input = input("\nType 'Start' when you are ready.\n=>")

    if pomo_input.lower() == 'start':
        start_time = datetime.now()
        break
    else:
        print('Please enter a valid input!')

# Take input from user
while True:
    pomo_input = input('\nTime is currently running. ' +
                       'Please select 1 command:\n a) Stop\n b) Pause\n=> ')
    if pomo_input.lower() in ('stop', 'a'):
        end_time = datetime.now()
        break
    elif pomo_input.lower() in ('pause', 'b'):
        pause_start = datetime.now()
        pause_end = 0

        while True:
            unpause_check = input("Time is paused." +
                        "Press y when you are ready to continue" +
                        "\n=> ")
            if unpause_check.lower() == 'y':
                pause_end = datetime.now()
                break

        paused_time.append(pause_end - pause_start)
    else:
        print('Please enter a correct input')

# Calculate the total time
total_time = end_time - start_time
print('\n=======================')
print('Summary Report')
print('=======================\n')
print('Subject:', subject.title())
print('Source:', source.title())
print('Start time:', start_time)
print('End time:', end_time)
print('Paused:', paused_time)
print('Total time:', total_time)

# # TODO:
# - Dictionary for the subjects and sources
# - Include pause time in the total time calculation
