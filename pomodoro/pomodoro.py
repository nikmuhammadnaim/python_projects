import csv
import string
import time
from datetime import datetime
from pomo_engine import *

print("\n-------------------------------------------")
print("Welcome to Nik Muhammad Naim's Pomodoro App")
print("-------------------------------------------")

start_time = 0
end_time = 0
paused_time = []
PATH = 'data\\'

# Read the subjects and learning materials available
with open(PATH + 'subjects.txt') as subjects:
    subject_list = subjects.read().splitlines()

with open(PATH + 'learning_materials.txt') as learning_materials:
    material_list = learning_materials.read().splitlines()

# Create dictionary for subject and learning materials
subj_dict = {alpha:subject for alpha, subject in zip(string.ascii_lowercase,
                subject_list)}

mat_dict = {alpha:material for alpha, material in zip(string.ascii_lowercase,
                material_list)}

# Select subject and learning material
while True:
    subject = input('\nPlease select one subject that you would ' +
                    'like to study today:' + print_dict(subj_dict) +
                    '\n=> ')
    if subject.lower() in subj_dict.keys():
        while True:
            source = input('\nPlease specify the learning material you will' +
                           ' be using:' + print_dict(mat_dict) +
                           '\n=> ')
            if source.lower() in mat_dict.keys():
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
print('Subject:', subj_dict.get(subject))
print('Source:', mat_dict.get(source))
print('Start time:', start_time)
print('End time:', end_time)
print('Paused:', paused_time)
print('Total time:', total_time)

# Important informations to write in csv:
# Start time, end time, number of paused time, total time, subject, material
completed = [start_time,
             end_time,
             len(paused_time),
             total_time,
             subj_dict.get(subject),
             mat_dict.get(source)]

with open(PATH + 'study_data.csv', mode='a', newline='') as study_data:
    writer = csv.writer(study_data)
    writer.writerow(completed)
