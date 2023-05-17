import random

aliens = []

alien_0 = {'color': 'green',
           'points': 5}

aliens.append(alien_0)

alien_1 = {'color': 'yellow',
           'points': 10}

aliens.append(alien_1)

alien_2 = {'color': 'red',
           'points': 15}

aliens.append( alien_2)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'slow'

alien_1['x_position'] = 1
alien_1['y_position'] = 15
alien_1['speed'] = 'medium'

alien_2['x_position'] = 5
alien_2['y_position'] = 20
alien_2['speed'] = 'fast'

# Move the alien.
# Determine how far to move the alien based on its current speed.

for alien in aliens:
    print(alien)



