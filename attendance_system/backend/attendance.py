from datetime import date, datetime
from .csv_writer import create_empty_file_if_not_exists, read_file_content

def get_file_name():
    current_date = str(date.today()).replace('-',"_")
    return 'attendance_results/attendance_' + current_date + '.csv'

def read_all_names(filename):
    file_content = read_file_content(filename)
    names = []
    for line in file_content:
        entry = line.split(',')
        names.append(entry[0])
    return names

def take_attendance(name):
    filename = get_file_name()
    create_empty_file_if_not_exists(filename)

    # check duplicate
    existing_names = read_all_names(filename)

    # Debugger
    # print('calling take attendance for name - ' + name)
    # print(existing_names)

    

    if name not in existing_names:
        with open(filename, 'a+') as f:
            time_now = datetime.now()
            current_time = time_now.strftime('%H:%M:%S')
            current_date = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{current_time},{current_date}')
