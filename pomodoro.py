from datetime import datetime

print("-------------------------------------------")
print("Welcome to Nik Muhammad Naim's Pomodoro App")
print("-------------------------------------------")

start_time = 0
end_time = 0
paused_time = []

# Subject
while True:
    subject = input('\nSelect one subject that you would like to study:' +
                    '\na) Python\nb) R\nc)Deep Learning\n=> ')
    if subject.lower() in ('a', 'b' 'c'):
        source = input('\nPlease specify the learning materials you will' +
                       ' be using (i.e. books, online, etc.)\n=> ')
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
    pomo_input = input("\nPlease pick 1 command:\n a) Stop\n b) Pause\n=> ")
    if pomo_input.lower() == "stop":
        end_time = datetime.now()
        break
    elif pomo_input.lower() == 'pause':
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
print('#######################')
print('Summary Report')
print('#######################')
print('Subject:', subject.title())
print('Source:', source.title())
print('Start time:', start_time)
print('End time:', end_time)
print('Paused:', paused_time)
print('Total time:', total_time)

# # TODO:
# - Dictionary for the subjects and sources
# - Include pause time in the total time calculation
