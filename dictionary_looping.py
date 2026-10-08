"""
Examples of looping through a dictionary dataset.

Run with:
    python dictionary_looping.py --source local
    python dictionary_looping.py --source json
"""

import argparse
import json
from pathlib import Path


# This dictionary contains the same records as dictionary_looping.json.
LOCAL_STUDENTS = {
    'S001': {'name': 'Amina', 'course': 'Cloud Computing', 'year': 1},
    'S002': {'name': 'Ben', 'course': 'Software Engineering', 'year': 2},
    'S003': {
        'name': 'Cara',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 1,
    },
    'S004': {'name': 'Diego', 'course': 'Networks', 'year': 2},
    'S005': {'name': 'Ella', 'course': 'Programming', 'year': 1},
    'S006': {'name': 'Farah', 'course': 'Big Data and Databases', 'year': 3},
    'S007': {'name': 'Gabriel', 'course': 'Cloud Computing', 'year': 2},
    'S008': {'name': 'Hana', 'course': 'Software Engineering', 'year': 1},
    'S009': {
        'name': 'Idris',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 2,
    },
    'S010': {'name': 'Julia', 'course': 'Networks', 'year': 3},
    'S011': {'name': 'Kai', 'course': 'Programming', 'year': 2},
    'S012': {'name': 'Leila', 'course': 'Big Data and Databases', 'year': 1},
    'S013': {'name': 'Mateo', 'course': 'Cloud Computing', 'year': 3},
    'S014': {'name': 'Nora', 'course': 'Software Engineering', 'year': 2},
    'S015': {
        'name': 'Omar',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 1,
    },
    'S016': {'name': 'Priya', 'course': 'Networks', 'year': 2},
    'S017': {'name': 'Quentin', 'course': 'Programming', 'year': 3},
    'S018': {'name': 'Rosa', 'course': 'Big Data and Databases', 'year': 2},
    'S019': {'name': 'Samir', 'course': 'Cloud Computing', 'year': 1},
    'S020': {'name': 'Talia', 'course': 'Software Engineering', 'year': 3},
    'S021': {
        'name': 'Umar',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 2,
    },
    'S022': {'name': 'Vera', 'course': 'Networks', 'year': 1},
    'S023': {'name': 'William', 'course': 'Programming', 'year': 2},
    'S024': {'name': 'Xena', 'course': 'Big Data and Databases', 'year': 3},
    'S025': {'name': 'Yusuf', 'course': 'Cloud Computing', 'year': 2},
    'S026': {'name': 'Zara', 'course': 'Software Engineering', 'year': 1},
    'S027': {
        'name': 'Adam',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 3,
    },
    'S028': {'name': 'Bella', 'course': 'Networks', 'year': 2},
    'S029': {'name': 'Carlos', 'course': 'Programming', 'year': 1},
    'S030': {'name': 'Dina', 'course': 'Big Data and Databases', 'year': 2},
    'S031': {'name': 'Ethan', 'course': 'Cloud Computing', 'year': 3},
    'S032': {'name': 'Fatima', 'course': 'Software Engineering', 'year': 2},
    'S033': {
        'name': 'George',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 1,
    },
    'S034': {'name': 'Holly', 'course': 'Networks', 'year': 3},
    'S035': {'name': 'Imran', 'course': 'Programming', 'year': 2},
    'S036': {'name': 'Jade', 'course': 'Big Data and Databases', 'year': 1},
    'S037': {'name': 'Kareem', 'course': 'Cloud Computing', 'year': 1},
    'S038': {'name': 'Lara', 'course': 'Software Engineering', 'year': 3},
    'S039': {
        'name': 'Marcus',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 2,
    },
    'S040': {'name': 'Nadia', 'course': 'Networks', 'year': 1},
    'S041': {'name': 'Oliver', 'course': 'Programming', 'year': 3},
    'S042': {'name': 'Paula', 'course': 'Big Data and Databases', 'year': 2},
    'S043': {'name': 'Rafi', 'course': 'Cloud Computing', 'year': 2},
    'S044': {'name': 'Sofia', 'course': 'Software Engineering', 'year': 1},
    'S045': {
        'name': 'Tariq',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 3,
    },
    'S046': {'name': 'Uma', 'course': 'Networks', 'year': 2},
    'S047': {'name': 'Victor', 'course': 'Programming', 'year': 1},
    'S048': {'name': 'Wendy', 'course': 'Big Data and Databases', 'year': 3},
    'S049': {'name': 'Yara', 'course': 'Cloud Computing', 'year': 1},
    'S050': {'name': 'Zain', 'course': 'Software Engineering', 'year': 2},
    'S051': {
        'name': 'Amelia',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 1,
    },
    'S052': {'name': 'Bilal', 'course': 'Networks', 'year': 3},
    'S053': {'name': 'Chloe', 'course': 'Programming', 'year': 2},
    'S054': {'name': 'Darius', 'course': 'Big Data and Databases', 'year': 1},
    'S055': {'name': 'Elena', 'course': 'Cloud Computing', 'year': 3},
    'S056': {'name': 'Faisal', 'course': 'Software Engineering', 'year': 2},
    'S057': {
        'name': 'Grace',
        'course': 'Introduction to Computers and Operating Systems',
        'year': 2,
    },
    'S058': {'name': 'Hamza', 'course': 'Networks', 'year': 1},
    'S059': {'name': 'Isabel', 'course': 'Programming', 'year': 3},
    'S060': {'name': 'Jamal', 'course': 'Big Data and Databases', 'year': 2},
}


def load_students(source):
    if source == 'local':
        return LOCAL_STUDENTS

    data_file = Path(__file__).with_name('dictionary_looping.json')
    with data_file.open(encoding='utf-8') as file:
        return json.load(file)


def display_students(students):
    print('Student IDs:')
    # Looping over a dictionary directly visits its keys.
    for student_id in students:
        print('  {}'.format(student_id))

    print('\nStudent names:')
    # .values() visits each value without its key.
    for student in students.values():
        print('  {}'.format(student['name']))

    print('\nStudent records:')
    # .items() gives each key and its corresponding value.
    for student_id, student in students.items():
        print(
            '  {}: {}, {} (year {})'.format(
                student_id,
                student['name'],
                student['course'],
                student['year'],
            )
        )

    print('\nEvery field in each record:')
    # Each student value is itself a dictionary, so it can also be looped over.
    for student_id, student in students.items():
        print('  {}:'.format(student_id))
        for field, value in student.items():
            print('    {}: {}'.format(field, value))


def main():
    parser = argparse.ArgumentParser(
        description='Loop through a student dictionary dataset.'
    )
    parser.add_argument(
        '--source',
        choices=('local', 'json'),
        default='local',
        help='load the Python dictionary or the matching JSON file',
    )
    args = parser.parse_args()

    students = load_students(args.source)
    print('Loaded {} students from {} data.'.format(len(students), args.source))
    display_students(students)


if __name__ == '__main__':
    main()


# TODO:
# * Count how many students are in year 2.
# * Display the names and IDs of students studying Cloud Computing.
# * Count how many students are enrolled in each course.
# * Find and display the student who is in the highest year.
# * Ask the user for a student ID and display that student's details.
#
# TODO (extra):
# * After loading the JSON data, display the number of students in each year.
