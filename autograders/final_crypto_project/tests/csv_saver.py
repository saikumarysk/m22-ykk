### THIS IS AN OLD FILE FROM W22
### NOT USED IN S22!

import csv
to_save = [([{
        'name': 'get groceries',
        'description': 'buy some jam and peanut butter',
        'deadline': '02/23/2022',
        'priority': 2,
        'completed': False
        }, {
        'name': 'get some sleep',
        'description': '8 hours of sleep is necessary',
        'deadline': '02/03/2022',
        'priority': 3,
        'completed': True
}],"my_csv.csv"),
    ([{
        'name': 'get some sleep',
        'description': '8 hours of sleep is necessary',
        'deadline': '02/03/2022',
        'priority': 3,
        'completed': True
}], "one_line.csv"),
    ([{
            'name': 'get groceries',
            'description': 'buy some jam and peanut butter',
            'deadline': '02/23/2022',
            'priority': 2,
            'completed': False
        }, {
            'name': 'get some sleep',
            'description': 'is necessary',
            'deadline': '02/03/2022',
            'priority': 2,
            'completed': True
        },
         {
             'name': 'get some sleep',
             'description': '10 hours',
             'deadline': '02/03/2022',
             'priority': 4,
             'completed': True
         },
         {
             'name': 'get some sleep',
             'description': '8 hours',
             'deadline': '02/03/2022',
             'priority': 5,
             'completed': True
         }
        ], "long_csv.csv")]



def save_to_csv(task_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile)
        for current_dict in task_list:
            task_data = list(current_dict.values())
            task_writer.writerow(task_data)


for param in to_save:
    save_to_csv(*param)