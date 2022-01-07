
import os
import datetime

txt_dir = os.getcwd() + '/txt'

def generate_and_save(filename):
    with open(filename, 'w') as file:
        now = datetime.datetime.now()
        file.write(now.strftime("%d-%m-%Y %H:%M:%S"))

data_count = 100

for i in range(data_count):
    filename = txt_dir + '/data' + str(i) + '.txt'
    generate_and_save(filename)

print('Generated ' + str(data_count) + ' files')
