# Function to generate a random file name in the format "Name Adjective three numbers"
def generate_file_name():
    names = ['Dog', 'Cat', 'Bird', 'Fish', 'Lion']
    adjectives = ['Shy', 'Brave', 'Clever', 'Swift', 'Gentle']

    name = random.choice(names)
    adjective = random.choice(adjectives)
    
    numbers = ''.join(random.choices('0123456789', k=3))
    
    file_name = f'{name}{adjective}{numbers}'
    
    return file_name