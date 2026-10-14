club = { 
    'name': 'Python Explorers', 
    'room': 'lab 1',
    'meeting_day': 'Monday', 
    'teacher': 'Mr Tan', 
}

members = {
    'alice': {
        'age': 12,
        'languages': ['python', 'scratch'], 
        'points': 15,
    },
    'ben': {
        'age': 13,
        'languages': ['scratch'], 
        'points': 8,
    },
    'chloe': {
        'age': 12,
        'languages': ['python', 'javascript'],
        'points': 20,
    }
}

projects = [ 
    {'name': 'Quiz Game', 'leader': 'alice', 'status': 'complete'}, 
    {'name': 'Space Adventure', 'leader': 'ben', 'status': 'in progress'}
    
]
invited_students = ['alice', 'daniel', 'ben', 'emma']
    #  meeting_day => Meeting day
if club. get('room') == 'lab 1': 
    club['room'] = 'lab 2'
club['meeting_time'] = '3:00 pm'
del club['teacher']
for key, value in club.items():
    clean_keys = (key.replace("_", " ").title())
    print(f"{clean_keys}: {value}.")
new_teacher = club.get("teacher", "not assigned")
print(f"Teacher: {new_teacher}")
members['alice']['points'] = 20
members['alice']['badge'] = 'Gold'
a = members['alice']
loopy = ", ".join(a['languages'])
print(f"Alice | Age: {a['age']} | Points: {a['points']} | Languages: {loopy} | Badge: {a['badge']}")
members['ben']['languages'] = 'python'
members['ben']['badge'] = 'beginner'
b = members['ben']

fat_loopy = ", ".join(a['languages'])
print(f"Ben | Age: {b['age']} | Points: {b['points']} |  Languages: {b['languages']} | Badge: {b['badge']}")


    
    


