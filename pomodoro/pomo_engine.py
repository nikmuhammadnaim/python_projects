import time

# Function for printing dictionary contents
def print_dict(my_dict):
    ready_list = ''
    for key, value in my_dict.items():
        ready_list += "\n{}) {}".format(key, value)
    return ready_list

# Countdown function
def pomodoro_timer(t_minutes):
    '''
    Countdown clock function.
    This function will display the time on the console.
    '''
    t_seconds = t_minutes * 60
    while t_seconds:
        minutes, seconds = divmod(t_seconds, 60)
        # format integer to a field of minimum width 2 with 0 left paddings
        t_display = '{:02d}:{:02d}'.format(minutes, seconds)
        print(t_display, end='\r')
        time.sleep(1)
        t_seconds -= 1

    print('Pomodoro set completed!')
