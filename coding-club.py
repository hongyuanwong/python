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

# Part 1
if club. get('room') == 'lab 1': 
    club['room'] = 'lab 2'
club['meeting_time'] = '3:00 pm'
del club['teacher']
print("=== CLUB INFORMATION ===")
for key, value in club.items():
    clean_keys = (key.replace("_", " ").title())
    print(f"{clean_keys}: {value}.")
new_teacher = club.get("teacher", "not assigned")
print(f"Teacher: {new_teacher}")

# Part 2
members['alice']['points'] = 20
members['daniel'] = {}
members['daniel']['age'] = 12
members['daniel']['languages'] = ['python']
members['daniel']['points'] = 0 

print("\n=== MEMBER REPORT ===")
for name, info in members.items():

    if info['points'] >= 20:
            badge = 'Gold'
    elif 10 <= info['points'] <= 19:
            badge = 'Silver'
    else:
            badge = 'Beginner'
    
    print("\n")
    print(f"{name.title()} | Age: {info['age']} | Points: {info['points']}")
    print(f"Languages: {', '.join(info['languages'])}")
    print(f"Badge: {badge}")

    
#for 
    
    
#members['alice']['points'] = 20
#a = members['alice']
#loopy = ", ".join(a['languages'])
#b = members['ben']
#fat_loopy = ", ".join(a['languages'])
#members['[daniel]'] = {}
#members['[daniel]']['age'] = 12
#members['[daniel]']['languages'] = 'python'
#members['[daniel]']['points'] = 0 
#dingus = members['[daniel]']
#dumbass_students = ['alice', 'ben', 'daniel']
#for dumb in dumbass_students:
#    info = members.get(dumb)
#info in members.items()
#if info['points'] >= 20:
#        info['badge'] = 'Gold'
#elif info['points'] >= 10:
#        info['badge'] = 'Silver'
#else:info['badge'] = 'Beginner'
#print(f"{dumb.title()} Badge: {info['badge']}")
#print(f"Alice | Age: {a['age']} | Points: {a['points']} | Languages: {loopy} | Badge: {info['badge']}")
#print(f"Ben | Age: {b['age']} | Points: {b['points']} |  Languages: {b['languages']} | Badge: {info['badge']}")
#print(f"Daniel | Age: {dingus['age']} | Points: {dingus['points']} | Languages: {dingus['languages']} | Badge: {info['badge']}")