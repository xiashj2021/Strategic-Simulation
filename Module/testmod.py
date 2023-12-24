from calcmod import *


country = Politics(50, 60, {'Politics': 1, 'Military': 2}, 0.5, 1000, 9.67, 10, 10, 0.11)
stability, social_expenditure, internal_revenue, effects, soldier = country.implementation()

print(stability, social_expenditure, internal_revenue, effects, soldier)
print('-' * 100)



country = Economy(
    {'civilian factory': 25, 'military factory': 20, 'army fortress': 0, 'anti-aircraft gun': 0},
    {'agro-pastoral': 10000, 'synthetic fiber': 6000, 'chemicals': 3000, 'light industrial': 2000},
    {
        '7.63mm automatic pistol': 5000, '7.62mm semi-automatic rifle': 10000, '9mm submachine gun': 5000,
        '7.92mm heavy and light machine gun': 200, '82mm mortar': 100, '75mm field artillery': 80,
        '115mm howitzer': 60, '37mm anti-tank gun': 40, 'PzKpfw I light tank': 10, 'T-26 light tank': 10,
        'truck': 200, 'fighter aircraft': 50
    },
    117, 120,
    {'global expenditures': 0, 'global production': 0, 'global revenue': 0, 'fiscal expenditure': 0, 'extra trade revenue': 0},
    20, 0.1,
    {
        'agro-pastoral': (0, 0), 'synthetic fiber': (0, 0), 'chemicals': (0, 0), 'light industrial': (0, 0),
        '7.63mm automatic pistol': (0, 0), '7.62mm semi-automatic rifle': (0, 0), '9mm submachine gun': (0, 0),
        '7.92mm heavy and light machine gun': (0, 0), '82mm mortar': (0, 0), '75mm field artillery': (0, 0),
        '115mm howitzer': (0, 0), '37mm anti-tank gun': (0, 0), 'PzKpfw I light tank': (0, 0), 'T-26 light tank': (0, 0),
        'truck': (0, 0), 'fighter aircraft': (0, 0)
    },
    {'yield': 0, 'cost': 0, 'income': 0}, 30
)

product, product_expenditure = country.production({
    'agro-pastoral': 8, 'synthetic fiber': 5, 'chemicals': 3, 'light industrial': 3, 'reserve divisions equipments': 1,
    'garrison division equipment': 1, 'field division equipment': 1, 'truck': 1, 'fighter aircraft': 1
})
construction_progress, construction_expenditure = country.construction({
    'civilian factory': 1, 'military factory': 1, 'army fortress': 1, 'anti-aircraft gun': 1
})
restoration_progress, restoration_expenditure = country.restoration({
    'civilian factory': 0, 'military factory': 0, 'army fortress': 0, 'anti-aircraft gun': 0
})
total_expenditure, total_revenue, delcur = country.implementation(product_expenditure, construction_expenditure, restoration_expenditure)
demand = country.demand(22)
weapon = country.training({'reserve division': 1, 'garrison division': 1, 'field division': 1}, 9.67)
supply = country.logistic([
    ('reserve division', 1), ('reserve division', 1), ('garrison division', 1), ('field division', 2)
])
facility, product, equipment = country.update(product, construction_progress, restoration_progress, demand, weapon, supply)

print(total_expenditure, total_revenue, delcur, facility, product, equipment)
print('-' * 100)


country = Military(
    {'Reserve': 3, 'Garrison': 4, 'Field': 3},
    {'Reserve': ((200, 0.7), (100, 0.8)), 'Garrison': ((50, 0.9), ), 'Field': ((300, 0.8), )},
    'Hilly', 'attack', 2, 1, False, 30,
    supply=1.2,
    air_power=0.8,
    tactic=1.05,
    national_specificities=1.25
)
attacker, a, thra, nona = country.correction()
u = country.support()

print(attacker, a, thra, nona, u)
print('-' * 100)


country = Intelligence(1, 'sabotage', 'Republic of Spain')
result = country.verdict()
print(result)
print('-' * 100)