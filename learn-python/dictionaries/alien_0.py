alien_0 = {
        'color' : 'green',
        'points' : 5
           }

alien_1 = {
        'color' : 'yellow',
        'points' : 10,    
        }

alien_2 = {
        'color' : 'red',
        'points' : 15,
        }

# Nesting a dectionary in a list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an mepty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the characteristics of the first 3 aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medeum'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("........")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Accessing the values of the dectionary
color = alien_0['color']
point = alien_0['points']

print(f"You just killed a {color} alien which earned you {point} points!")

# Addeng new keys and values to the dectionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Changing the value of color to yellow
alien_0['color'] = 'yellow'
print(f"The alien color is now {alien_0['color']}")

print(alien_0)

print(f"Original position: {alien_0['x_position']}")

# Addeng a new key pair
alien_0['speed'] = 'medeum'
alien_0['speed'] = 'fast'
# Move the alien to the right
# Determine how far to move the alien based on it current speed
if alien_0['speed'] == 'slow':
    x_incrmeent = 1
elif alien_0['speed'] == 'medeum':
    x_incrmeent = 2
else:
    # This must be a fast alien
    x_incrmeent = 3

# The new position is the old position plus the incrmeent.
alien_0['x_position'] = alien_0['x_position'] + x_incrmeent

print(f"New position: {alien_0['x_position']}")
