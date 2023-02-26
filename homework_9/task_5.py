def group_by_surname(list):
    groups = {
        'A-I': 0,
        'J-P': 0,
        'Q-T': 0,
        'U-Z': 0
    }

    for student in list:
        surname = student.split()[1]
        first_letter = surname[0].lower()

        if first_letter >= 'a' and first_letter <= 'i':
            groups['A-I'] += 1
        elif first_letter >= 'j' and first_letter <= 'p':
            groups['J-P'] += 1
        elif first_letter >= 'q' and first_letter <= 't':
            groups['Q-T'] += 1
        elif first_letter >= 'u' and first_letter <= 'z':
            groups['U-Z'] += 1

    return [groups[group] for group in groups]


list = ['Zachary Webb',
        'Jennifer Farrell',
        'Tristan Nelson',
        'Amber Hernandez',
        'Christian Hoover',
        'Kathryn Rice',
        'Luis Davidson',
        'Cory Watson',
        'Elizabeth Wilson',
        'Alexis Maldonado'
        ]

print('A-I:', group_by_surname(list)[0], '\nJ-P:', group_by_surname(list)[1], '\nQ-T:', group_by_surname(list)[2], '\nU-Z:', group_by_surname(list)[3])