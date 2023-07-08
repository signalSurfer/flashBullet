import random
from pushbullet import Pushbullet #remember to pip install pushbullet.py!

#Pushbullet API key required to use pushbullet:
API_KEY = 'yourapikeyhere'

# Example dictionary, feel free to PR dictionary files!
cards = {
    'Percentage': 'proportion x 100',
    'ratio': 'freq divided by another freq',
    'Outlier': 'Extreme Value, distant from the rest of the distribution.',
    'proportion': 'Data points make a bell/hill curve.',
    'Bimodal': 'A distribution with two modes',
    'Mean': 'freq divided by total, drastically affected by outliers.',
    'Quartiles': 'Quartiles mark 1/4 of data points. q1=25%,q2=50%,etc.',
    'Median': 'this is the middle point of a dataset. Less affected by outliers.',
    'Skewed Distribution': 'Data with a tail in either direction.',
    'Correlation Coefficient': 'a number between −1 and +1 calculated so as to represent the linear dependence of two variables or sets of data.',
    'interquartile range (IQR)': 'q3 minus q1. A value of its own, half of the value is distance from median.',    
}

# Select a random entry from the dictionary
random_entry = random.choice(list(cards.items()))
title, body = random_entry

# Create a Pushbullet object
pb = Pushbullet(API_KEY)

# Send the Pushbullet notification
push = pb.push_note(title, body)

#Schedule this script at the frequency you want, and enjoy your studies!
