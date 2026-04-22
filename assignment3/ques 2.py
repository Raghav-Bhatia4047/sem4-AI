import random
inbound=random.choice([0,1])
outbound=random.choice([0,1])
obstacle=random.choice([0,1])
emergency=random.choice(['Neutral','Active'])
status=['No',  'Yes']
conditions={
    'Train' : status[(inbound and outbound)],
    'obstacle' : status[obstacle],
    'emergency' : emergency

}    
alert={
    ('Yes','Yes','Active') : ('LOWER','OFF','RED'),
    ('Yes','Yes','Neutral') : ('LOWER','ON','RED'),
    ('Yes','No','Active') : ('LOWER','OFF','RED'),
    ('Yes','No','Neutral') : ('LOWER','ON','GREEN'),
    ('No','Yes','Active') : ('LOWER','OFF','RED'),
    ('No','Yes','Neutral') : ('RAISE','OFF','GREEN'),
    ('No','No','Active') : ('LOWER', 'OFF', 'RED'),
    ('No','No','Neutral') : ('RAISE','OFF','GREEN')
}
print("Conditions:")
for key, value in conditions.items():
    print(f"{key}: {value}")
gate,siren,signal=alert[(conditions['Train'],conditions['obstacle'],conditions['emergency'])]
action={
    'Gate': gate,
    'Siren': siren,
    'Signal': signal
}
print("\nAction to be taken:")
for key, value in action.items():
    print(f"{key}: {value}")

