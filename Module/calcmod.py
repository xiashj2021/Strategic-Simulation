from os import urandom # The urandom function is invoked to generate real random number.
from functools import reduce # The reduce() function is invoked to accumulate elements in a sequence.
from math import ceil # The ceil function is invoked to round values.
import matplotlib.pyplot as plt # The pyplot method is invoked to create image.


class Politics(object):
    """
    The Politics module of the strategic simulation system

    Attributes:
        Stability
        Government Support
        Political Expenditures
        Military Expenditures
        Labor Expenditures
        Domestic Taxes
        Number of Incumbents
        Salary of Personnel
        Taxpayers
        Starting Tax Amount
        Personnel Tax Rate
        State Policy Pricing
        Number of National Policies
        Expenditures Buff
        Revenue Buff
        Global Expenditure Effect
        Global Revenue Effect
        National Political Characteristics Revision
        Government Expenditure Effect
        Domestic Taxes Revenue Effect
        Extra Domestic Taxes Revenue Effect
    """

    def __init__(self, stability, government, policy, revision, population, soldier, soldierpay, salary, tax) -> object:
        """
        This part defines the basic parameters of the politics module.

        :param stability: Degree of stability: -50~100 (float)
        :param government: Level of government support: 0~100 (float)
        :param policy: National policy: 
            {
                Type of State policy 
                ('Politics', 'Economics', 'Military', 'Intelligence'): 
                Policy level (1, 2, 3, 4, 5)), ...
            } 
            (dict)
        :param revision: Policy implementation cost revisions (float)
        :param population: The population of the country 
            (in 10,000 persons)(float)
        :param soldier: Number of soldiers (in 10,000 persons) (float)
        :param soldierpay: Pay and provisions for soldiers (float)
        :param salary: Salaries of civil servants (float)
        :param tax: Personal income tax rate (float)
        """
        self.stability = stability
        self.government = government
        self.policy = policy
        self.revision = revision
        self.population = population
        self.soldier = soldier
        self.functionary = self.population * 0.001
        self.taxpayers = self.population * 0.005
        self.soldierpay = soldierpay
        self.salary = salary
        self.tax = tax
    
    def implementation(self) -> list:
        """
        This section defines the specific mechanics of policy implementation.

        :return: 
            stability, social expenditure (policy, military, and employee), 
            Internal revenue, Effects of stability values
        """
        effects = {'government expenditure': 0, 'global production': 0, 'global revenue': 0, 'fiscal expenditure': 0, 
                   'domestic taxes': 0, 'global expenditures': 0, 'extra domestic taxes': 0, 'extra trade revenue': 0, 
                   'factory': 0, 'stability': 0, 'civilian factory': 0, 'military factory': 0}
        economics_value = {1: -0.5, 2: -0.75, 3: -1}
        factory_value = {1: -1, 2: -2, 3: -4}
        stability_value = {1: -5, 2: -10, 3: -20}
        percent_value = {0.25: (1), 0.5: (1, 2), 0.75: (1, 2, 3), 1: (1, 2, 3, 4)}
        cases_number = {1: 2, 2: 3, 3: 5}
        factory_number = {1: {1: {'civilian factory': -1}, 2: {'military factory': -1}}, 
                          2: {1: {'civilian factory': -2}, 2: {'military factory': -2}, 
                              3: {'civilian factory': -1, 'military factory': -1}}, 
                          3: {1: {'civilian factory': -4}, 2: {'military factory': -4}, 
                              3: {'civilian factory': -1, 'military factory': -3}, 
                              4: {'civilian factory': -2, 'military factory': -2}, 
                              5: {'civilian factory': -3, 'military factory': -1}}
        }

        def add_effect(factor, value):
            """
            This nested function defines the storage operation 
            for the effect corresponding to the stabilization level.

            :param factor: Aspects of the effect of stabilization (str)
            :param value: Specific effects value (float)
            """
            effects[factor] = value
        
        def unrest(level, percent):
            """
            This nested function defines the generation 
            of turbulence events and their random effects.
            
            :param level: The level of the destabilizing event (int)
            :param percent: 
                The probability of the occurrence of a destabilizing event 
                (float)
            """
            economic = economics_value[level]
            factory = factory_value[level]
            stability = stability_value[level]
            rate = percent_value[percent]
            
            random = ord(urandom(1)) % 4 + 1; choice = ord(urandom(1)) % 4 + 1
            if random in rate:
                add_effect({1: 'extra domestic taxes', 2: 'extra trade revenue', 3: 'factory', 4: 'stability'}[choice], 
                           {1: economic, 2: economic, 3: factory, 4: stability}[choice])
                if choice == 3:
                    factory_effect = factory_number[level][ord(urandom(1)) % cases_number[level] + 1]
                    for key, value in factory_effect.items():
                        add_effect(key, value)

        if 50 <= self.stability < 60:
            pass
        elif 40 <= self.stability < 50:
            add_effect('government expenditure', 0.05); add_effect('global production', -0.05)
        elif 60 <= self.stability < 70:
            add_effect('government expenditure', -0.05); add_effect('global production', 0.05)
        elif 30 <= self.stability < 40:
            add_effect('fiscal expenditure', 0.1); add_effect('global production', -0.1); add_effect('domestic taxes', -0.1)
        elif 70 <= self.stability < 80:
            add_effect('fiscal expenditure', -0.1); add_effect('global production', 0.1); add_effect('domestic taxes', 0.1)
        elif 20 <= self.stability < 30:
            add_effect('fiscal expenditure', 0.2); add_effect('global production', -0.2); add_effect('domestic taxes', -0.2)
        elif 80 <= self.stability < 90:
            add_effect('fiscal expenditure', -0.2); add_effect('global production', 0.2); add_effect('domestic taxes', 0.2)
        elif 10 <= self.stability < 20:
            add_effect('fiscal expenditure', 0.3); add_effect('global production', -0.3); add_effect('domestic taxes', -0.3)
        elif 90 <= self.stability <= 100:
            add_effect('fiscal expenditure', -0.3); add_effect('global production', 0.3); add_effect('domestic taxes', 0.3)
        elif 0 <= self.stability < 10:
            add_effect('global expenditures', 0.1); add_effect('global production', -0.3); add_effect('global revenue', -0.1)
            unrest(1, 0.25)
        elif -10 <= self.stability < 0:
            add_effect('global expenditures', 0.2); add_effect('global production', -0.4); add_effect('global revenue', -0.2)
            unrest(1, 0.5); unrest(2, 0.25)
        elif -20 <= self.stability < -10:
            add_effect('global expenditures', 0.3); add_effect('global production', -0.5); add_effect('global revenue', -0.3)
            unrest(1, 0.75); unrest(2, 0.5); unrest(3, 0.25)
        elif -30 <= self.stability < -20:
            add_effect('global expenditures', 0.4); add_effect('global production', -0.6); add_effect('global revenue', -0.4)
            unrest(1, 1); unrest(2, 0.75); unrest(3, 0.5)
        elif -40 <= self.stability < -30:
            add_effect('global expenditures', 0.5); add_effect('global production', -0.8); add_effect('global revenue', -0.5)
            unrest(1, 1); unrest(2, 1); unrest(3, 0.75)
        elif -50 <= self.stability < -40:
            add_effect('global expenditures', 0.6); add_effect('global production', -1); add_effect('global revenue', -0.6)
            unrest(1, 1); unrest(2, 1); unrest(3, 1)
        print(effects)

        def stability_production(value):
            """
            This nested function defines the natural output 
            of stabilization per turn.

            :param value: 
                The value of government support for the current turn (float)
            """
            if value >= 50: y_value = value / 50
            else: y_value = (value - 50) / 2
            return y_value
        
        change = stability_production(self.government)
        stability = self.stability + change + effects['stability']
        
        policy = sum([value * 10000 for value in self.policy.values()]) * (
            1 + self.revision) * (
            1 + effects['government expenditure'] + effects['global expenditures'])
        military = self.soldier * self.soldierpay * (1 + effects['global expenditures'])
        employee = self.functionary * self.salary * (1 + effects['government expenditure'] + effects['global expenditures'])
        social_expenditure = policy + military + employee
        internal_revenue = self.taxpayers * self.tax * (
            1 + effects['global revenue'] + effects['domestic taxes']) * (
                1 + effects['extra domestic taxes'])
        
        return stability, social_expenditure, internal_revenue, effects, self.soldier


class Economy(object):
    """
    The Economy module of the strategic simulation system

    Attributes:
        Production
        Construction Expenditures
        Restoration Expenditures
        Political Expenditures
        National Product Demand
        Military Training Demand
        Logistic Demand
        Import Tariff
        Days
        Yield
        Number of Tasks
        Cost
        Number of Province
        Number of Divisions
        Expenditures Buff
        Revenue Buff
        Production Buff
        Global Expenditure Effect
        Global Revenue Effect
        Global Production Effect
        Fiscal Expenditure Effect
        Extra Trade Revenue Effect
        Factory Production Cost Revisions
    """

    def __init__(
            self, facility, product, equipment, social_expenditure, internal_revenue, effects, currency, tax, trade, revision, time
        ) -> object:
        """
        This part defines the basic parameters of the economy module.

        :param facility: Number of facilities of each type in the country: 
            {
                'civilian factory': float, 'military factory': float, 
                'army fortress': float, 'anti-aircraft gun': float
            } 
            (values in block) (dict)
        :param poduct: Quantity of each type of product in the country: 
            {
                'agro-pastoral': float, 'synthetic fiber': float, 
                'chemicals': float, 'light industrial': float
            } 
            (values in kilograms) (dict)
        :param equipment: Quantity of each type of equipment in the country: {
            '7.63mm automatic pistol': int,
            '7.62mm semi-automatic rifle': int,
            '9mm submachine gun': int,
            '7.92mm heavy and light machine gun': int,
            '82mm mortar': int,
            '75mm field artillery': int,
            '115mm howitzer': int,
            '37mm anti-tank gun': int,
            'PzKpfw I light tank': int,
            'T-26 light tank': int,
            'truck': int,
            'fighter aircraft': int
        } (dict)
        :param social_expenditure: 
            Policy, military, and employee expenditure (float)
        :param internal_revenue: Domestic taxes (float)
        :param effects: 
            Implications of aspects derived from the political module: {
            'global expenditures': float,
            'global production': float,
            'global revenue': float, 
            'fiscal expenditure': float,
            'extra trade revenue': float
        }
        :param currency: 
            Current volume of currency (in tens of thousands) (float)
        :param tax: Import tariff rate (float)
        :param trade: Transactions of goods and funds through trade: {
            'agro-pastoral': (import, export) (float, float),
            'synthetic fiber': (import, export) (float, float),
            'chemicals': (import, export) (float, float),
            'light industrial': (import, export) (float, float),
            '7.63mm automatic pistol': (import, export) (int, int),
            '7.62mm semi-automatic rifle': (import, export) (int, int),
            '9mm submachine gun': (import, export) (int, int),
            '7.92mm heavy and light machine gun': (import, export) (int, int),
            '82mm mortar': (import, export) (int, int),
            '75mm field artillery': (import, export) (int, int),
            '115mm howitzer': (import, export) (int, int),
            '37mm anti-tank gun': (import, export) (int, int),
            'PzKpfw I light tank': (import, export) (int, int),
            'T-26 light tank': (import, export) (int, int),
            'truck': (import, export) (int, int),
            'fighter aircraft': (import, export) (int, int)
        } (dict)
        :param revision: Factory production cost revisions {
            yield: float,
            cost: float,
            income: float
        } (dict)
        :param time: Number of days the turn lasts (int)
        """
        self.facility = facility
        self.product = product
        self.equipment = equipment
        self.social_expenditure = social_expenditure
        self.internal_revenue = internal_revenue
        self.effects = effects
        self.currency = currency
        self.tax =tax
        self.trade = trade
        self.revision = revision
        self.time = time
    
    def production(self, production) -> list:
        """
        This section defines the specific mechanics of production tasks.

        :param production: 
            Storage of goods produced and number of plants allocated 
            {product type: factory number, product type: factory number, ...}
        :return: Product, Product expenditure
        """
        product_info = { # (yield, cost)
            # (day, kilograme)
            'agro-pastoral': (150, 0.01),
            'synthetic fiber': (30, 0.2),
            'chemicals': (20, 1),
            'light industrial': (4, 2.5),
            # (day, piece)
            'reserve divisions equipments': (0.02, 245000),
            'garrison division equipment': (0.01, 492000),
            'field division equipment': (0.008, 2955500),
            'truck': (0.05, 3000),
            'fighter aircraft': (0.01, 3000)
        }
        equipment_info = { # Production of equipment for each type of military unit corresponds to the production on the weapons
            # yield in day
            'reserve divisions equipments': {
                '7.63mm automatic pistol': 30,
                '7.62mm semi-automatic rifle': 10,
                '82mm mortar': 1
            },
            'garrison division equipment': {
                '7.62mm semi-automatic rifle': 10,
                '9mm submachine gun': 3,
                '7.92mm heavy and light machine gun': 1.5,
                '82mm mortar': 1,
                '75mm field artillery': 0.5
            },
            'field division equipment': {
                '7.62mm semi-automatic rifle': 10,
                '9mm submachine gun': 3,
                '7.92mm heavy and light machine gun': 1.5,
                '82mm mortar': 1,
                '75mm field artillery': 0.5,
                '115mm howitzer': 0.03,
                '37mm anti-tank gun': 0.05,
                'PzKpfw I light tank': 0.005,
                'T-26 light tank': 0.005
            }
        }
        expenditure = []
        product = {
            '7.63mm automatic pistol': 0, 
            '7.62mm semi-automatic rifle': 0, 
            '9mm submachine gun': 0, 
            '7.92mm heavy and light machine gun': 0,
            '82mm mortar': 0,
            '75mm field artillery': 0,
            '115mm howitzer': 0,
            '37mm anti-tank gun': 0,
            'PzKpfw I light tank': 0,
            'T-26 light tank': 0
        }

        for key, value in production.items():
            item_cost = product_info[key][1] * value * self.time * (
                1 + self.effects['global expenditures'] + self.effects['fiscal expenditure']) * self.revision['cost']
            expenditure.append(item_cost)
        
        for key, value in production.items():
            if key in ('reserve divisions equipments', 'garrison division equipment', 'field division equipment'):
                for i, weapon in equipment_info[key].items():
                    item_yield = weapon * value * self.time * (1 + self.effects['global production']) * self.revision['yield']
                    product[i] += item_yield
            else:
                item_yield = product_info[key][0] * value * self.time * (
                    1 + self.effects['global production']) * self.revision['yield']
                product[key] = item_yield
        
        product_expenditure = sum(expenditure) / 10000 # unit conversions
        return product, product_expenditure
    
    def construction(self, construction) -> list:
        """
        This section defines the specific mechanics of construction tasks.

        :param construction: Type and number of facilities built for storage 
            {facility type: number, facility type: number, ...}
        :return: Construction progress, Construction expenditure
        """
        construction_info = { # (yield, cost)
            # (day, block)
            'civilian factory': (0.1, 5000),
            'military factory': (0.05, 10000),
            # (turn, block)
            'army fortress': (1, 300),
            'anti-aircraft gun': (1, 600)
        }
        expenditure = []; progress = {}

        for key, value in construction.items():
            if key in ('civilian factory', 'military factory'):
                item_cost = construction_info[key][1] * value * self.time * (
                    1 + self.effects['global expenditures'] + self.effects['fiscal expenditure']) * self.revision['cost']
                expenditure.append(item_cost)
            else:
                item_cost = construction_info[key][1] * value * (
                    1 + self.effects['global expenditures'] + self.effects['fiscal expenditure']) * self.revision['cost']
                expenditure.append(item_cost)
        
        for key, value in construction.items():
            if key in ('civilian factory', 'military factory'):
                item_yield = construction_info[key][0] * value * self.time * (
                    1 + self.effects['global production']) * self.revision['yield']
                progress[key] = item_yield
            else:
                item_yield = construction_info[key][0] * value * (1 + self.effects['global production']) * self.revision['yield']
                progress[key] = item_yield
        
        construction_expenditure = sum(expenditure) / 10000 # unit conversions
        return progress, construction_expenditure
    
    def restoration(self, restoration) -> list:
        """
        This section defines the specific mechanics of restoration tasks.

        :param restoration: Type and number of facilities restored for storage 
            {facility type: number, facility type: number, ...}
        :return: Restoration progress, Restoration expenditure
        """
        restoration_info = { # (yield, cost)
            # (turn, block)
            'civilian factory': (0.5, 2500),
            'military factory': (0.5, 5000),
            'army fortress': (1, 150),
            'anti-aircraft gun': (1, 300),
        }
        expenditure = []; progress = {}

        for key, value in restoration.items():
            item_cost = restoration_info[key][1] * value * (
                1 + self.effects['global expenditures'] + self.effects['fiscal expenditure']) * self.revision['cost']
            expenditure.append(item_cost)
            item_yield = restoration_info[key][0] * value * (1 + self.effects['global production']) * self.revision['yield']
            progress[key] = item_yield
        
        restoration_expenditure = sum(expenditure) / 10000 # unit conversions
        return progress, restoration_expenditure
    
    def implementation(self, *args) -> list:
        """
        This section defines the specific mechanics of economic implementation.

        :param args: 
            Includes other expenditure: 
                product, construction, restoration (tuple)
        :return: 
            Total expenditure 
                (social, product, construction, restoration, trade), 
            Total revenue (tax, tariff), Volume of change in currency
        """
        if not args:
            economic_expenditure = 0
        else:
            economic_expenditure = sum(args)
        
        trade_info = {
            'agro-pastoral': 0.02,
            'synthetic fiber': 0.4,
            'chemicals': 2,
            'light industrial': 4,
            '7.63mm automatic pistol': 50,
            '7.62mm semi-automatic rifle': 50,
            '9mm submachine gun': 50,
            '7.92mm heavy and light machine gun': 800,
            '82mm mortar': 6000,
            '75mm field artillery': 10000,
            '115mm howitzer': 30000,
            '37mm anti-tank gun': 20000,
            'PzKpfw I light tank': 25000,
            'T-26 light tank': 25000,
            'truck': 5000,
            'fighter aircraft': 5000,
        }
        expenditure = []; revenue = []

        for key, value in self.trade.items(): # (import, export)
            expenditure.append(trade_info[key] * value[0] * (
                1 *(
                    1 + self.effects['global expenditures'] + self.effects['fiscal expenditure']) - self.tax * (
                        1 + self.effects['global revenue']) * (1 + self.effects['extra trade revenue']) * self.revision['income']))
            revenue.append(trade_info[key] * value[1] * (
                1 + self.effects['global revenue']) * (1 + self.effects['extra trade revenue']) * self.revision['income'])
        
        total_expenditure = self.social_expenditure + economic_expenditure + sum(expenditure)
        total_revenue = self.internal_revenue + sum(revenue)
        delcur = total_revenue - total_expenditure
        return total_expenditure, total_revenue, delcur
    
    def demand(self, province) -> dict:
        """
        This section defines 
        the specific mechanics of domestic economic demand.

        :param province: Number of provinces (int)
        :return: National product demand
        """
        demand_info = {
            # demand in day
            'agro-pastoral': 400,
            'synthetic fiber': 80,
            'chemicals': 40,
            'light industrial': 8,
        }
        demand = {}

        for key, value in demand_info.items():
            demand[key] = value * province
        return demand
    
    def training(self, training, soldier) -> list:
        """
        This section defines the specific mechanics of military training.

        :param training: Type of army and number for storage 
            {military type: number, military type: number, ...} (dict)
        :param soldier: Number of soldiers (in 10,000 persons) (float)
        :return: Military training demand, Solider
        """
        training_info = {
            'reserve division': {
                '7.63mm automatic pistol': 300,
                '7.62mm semi-automatic rifle': 1200,
                '82mm mortar': 40
            },
            'garrison division': {
                '7.62mm semi-automatic rifle': 1100,
                '9mm submachine gun': 300,
                '7.92mm heavy and light machine gun': 100,
                '82mm mortar': 40,
                '75mm field artillery': 25
            },
            'field division': {
                '7.62mm semi-automatic rifle': 1000,
                '9mm submachine gun': 350,
                '7.92mm heavy and light machine gun': 150,
                '82mm mortar': 40,
                '75mm field artillery': 25,
                '115mm howitzer': 30,
                '37mm anti-tank gun': 40,
                'PzKpfw I light tank': 25,
                'T-26 light tank': 25
            }
        }
        soldier_info = {'reserve division': 2300, 'garrison division': 3100, 'field division': 6200}
        manpower = []
        train = {
            '7.63mm automatic pistol': 0, 
            '7.62mm semi-automatic rifle': 0, 
            '9mm submachine gun': 0, 
            '7.92mm heavy and light machine gun': 0,
            '82mm mortar': 0,
            '75mm field artillery': 0,
            '115mm howitzer': 0,
            '37mm anti-tank gun': 0,
            'PzKpfw I light tank': 0,
            'T-26 light tank': 0
        }

        for key, value in training.items():
            for i, weapon in training_info[key].items():
                train[i] += value * weapon
        
        for key, value in training.items():
            manpower.append(soldier_info[key] * value)
        
        soldier = soldier + sum(manpower) / 10000 # unit conversions
        return train, soldier
    
    def logistic(self, logistic) -> list:
        """
        This section defines the specific mechanics of military logistic.

        :param logistic: 
            Type of stockpiled military forces and replenishment base: 
            [(military type, base), (military type, base), ...] (list)
        """
        logistic_info = {
            'reserve division': {
                'agro-pastoral': 7.5,
                'light industrial': 0.25
            },
            'garrison division': {
                'agro-pastoral': 10,
                'light industrial': 0.5
            },
            'field division': {
                'agro-pastoral': 15,
                'light industrial': 1
            }
        }
        demand = {'agro-pastoral': 0, 'light industrial': 0}
        
        for item in logistic:
            military_type, base = item
            for key, value in logistic_info[military_type].items():
                demand[key] += value * base
        return demand
    
    def update(
            self, product, construction_progress, restoration_progress, economic_demand, training_demand, logistic_demand
        ) -> list:
        """
        This section defines the specific mechanics of state warehouse.

        :param product: (dict)
        :param construction_progress: (dict)
        :param restoration_progress: (dict)
        :param economic_demand: (dict)
        :param training_demand: (dict)
        :param logistic_demand: (dict)
        :return: facility, product, equipment
        """
        trade = {}
        for key, value in self.trade.items(): # (import, export)
            trade[key] = value[0] - value[1]
        
        def value(y_dict, dict, operation_type):
            """
            This nested function defines 
            the generation of the value update of the dictionary.

            :param y_dict: Value to be updated (dict)
            :param dict: Amount of change in value (dict)
            :param operation_type: addition, subtraction (str)
            """
            for key in y_dict.keys():
                if key in dict:
                    if operation_type == 'addition':
                        y_dict[key] += dict[key]
                    elif operation_type == 'subtraction':
                        y_dict[key] -= dict[key]
        
        value(self.product, product, 'addition')
        value(self.product, trade, 'addition')
        value(self.equipment, product, 'addition')
        value(self.equipment, trade, 'addition')
        value(self.facility, construction_progress, 'addition')
        value(self.facility, restoration_progress, 'addition')
        value(self.product, economic_demand, 'subtraction')
        value(self.product, logistic_demand, 'subtraction')
        value(self.equipment, training_demand, 'subtraction')
        
        return self.facility, self.product, self.equipment


class Military(object):
    """
    The Military module of the strategic simulation system

    Attributes:
        Strength
        Support Ratio
        Attrition Rate Threshold
        Combat Effectiveness Factor
        Non-Combatant Attrition Factor
        Initial Troops
        Division of Troops
        Division of Strength
        Morale of Troops
        Topography Modification
        Experience Modification
        Supply Modification
        Air Power Modification
        Tactic Modification
        Non-Combatant Attrition Baseline
        Attrition Rate Baseline
        National Specificities Effect
    """

    def __init__(self, divisions, reinforcement, topography, combatant, experience, morale, surround, time, **kwargs) -> object:
        """
        This part defines the basic parameters of the military module.

        :param divisions: 
            Components of military units: 
                {'Reserve': int, 'Garrison': int, 'Field': int} (dict)
        :param reinforcement: Components of reinforcement units: 
            {
                'Reserve': ((distance, speed correction), ...), 
                'Garrison': ((distance, speed correction), ...), 
                'Field': ((distance, speed correction), ...)
            } (dict)
        :param topography: 
            Situation of the terrain where the fighting took place: 
                Hilly, Mountain, Forest, Swamp, Desert, City, Fortress (str)
        :param combatant: Battle type: attack, defence (str)
        :param experience: Soldier's experience level: 1, 2, 3, 4, 5 (int)
        :param morale: Warrior morale index: 0.8~1.2 (float)
        :param surround: 
            Whether or not the troops are surrounded: True, False (bool)
        :param time: Number of days the turn lasts (int)
        :param kwargs: Includes other factors: 
            supply, air power, tactic, national specificities, 
            whose values are filled in artificially (dict)
        """
        self.divisions = divisions
        self.reinforcement = reinforcement
        self.troop = 2300 * self.divisions['Reserve'] + 3100 * self.divisions['Garrison'] + 6200 * self.divisions['Field']
        self.strength = (
            0.0217 * 2300 * self.divisions[
                'Reserve'] + 0.0253 * 3100 * self.divisions['Garrison'] + 0.0306 * 6200 * self.divisions['Field']) / self.troop
        self.topography = topography
        self.combatant = combatant
        self.experience = experience
        self.morale = morale
        self.surround = surround
        self.time = time
        if not kwargs:
            self.kwargs = 1
        else:
            self.kwargs = reduce(lambda x, y: x * y, kwargs.values())
    
    def correction(self) -> list:
        """
        This section defines 
        the specific mechanics of combat power modification.
        
        :return: 
            Initial troops, Combat effectiveness factor, 
            Attrition rate threshold, Non-combatant attrition factor
        """
        experience_modification = {1: -0.05, 2: 0, 3: 0.01, 4: 0.025, 5: 0.05}[self.experience]
        
        if self.combatant == 'attack':
            topography_modification = {
                'Hilly': 0, 'Mountain': -0.2, 'Forest': -0.15, 'Swamp': -0.3, 'Desert': -0.15, 'City': -0.1, 'Fortress': -0.05
                }[self.topography]
        elif self.combatant == 'defence':
            topography_modification = {
                'Hilly': 0.1, 'Mountain': 0.25, 'Forest': 0.2, 'Swamp': -0.3, 'Desert': -0.2, 'City': 0.15, 'Fortress': 0.05
                }[self.topography]
        factor = (self.strength ** self.morale) * (1 + topography_modification) * (1 + experience_modification) * self.kwargs
        if not self.surround:
            threshold = (0.3 ** self.morale) * self.kwargs
        else:
            threshold = (0.3 ** self.morale) * (1 + topography_modification) * self.kwargs
        
        attrition = (0.005 ** self.morale) * self.kwargs
        
        return self.troop, factor, threshold, attrition
    
    def support(self) -> list:
        """
        This section defines the specific mechanics of support ratio.
        
        :return: 
            support ratio: 
                [
                    (day 1 troop, day 1 Combat factor), 
                    (day 2 troop, day 2 Combat factor), ...
                ]
        """
        marching_time = 8 # Hours of marching per day
        military_info = { # (troop, strength, speed)
            'reserve infantry regiment': (1500, 0.02, 4), 
            'mortar battalion': (800, 0.025, 3), 
            'garrison infantry regiment': (1500, 0.023, 4),
            'field artillery battalion': (800, 0.03, 2.5),
            'field infantry regiment': (1500, 0.025, 4),
            'heavy howitzer regiment': (1500, 0.04, 2),
            'anti-tank gun battalion': (800, 0.035, 2.5),
            'armor battalion': (800, 0.035, 10)
        }
        reinforcements = [] # [(troop, strength, days required to reach the battlefield), ...]

        for key, value in self.reinforcement.items():
            for division in value: # (distance, speed correction)
                if key == 'Reserve':
                    regiments = ['reserve infantry regiment', 'mortar battalion']
                elif key == 'Garrison':
                    regiments = ['garrison infantry regiment', 'mortar battalion', 'field artillery battalion']
                elif key == 'Field':
                    regiments = ['field infantry regiment', 'mortar battalion', 'field artillery battalion', 
                                 'heavy howitzer regiment', 'anti-tank gun battalion', 'armor battalion']
                
                for regiment in regiments:
                    distance = division[0]
                    speed_correction = division[1]
                    troop = military_info[regiment][0]
                    strength = military_info[regiment][1]
                    days = ceil(distance / (military_info[regiment][2] * speed_correction * marching_time))
                    reinforcements.append((troop, strength, days))
        
        rate = []
        
        for i in range(self.time):
            troop = sum([x[0] for x in reinforcements if x[2] == i])
            
            if not troop:
                rate.append((0, 0))
            else:
                strength = sum([x[0] * x[1] for x in reinforcements if x[2] == i]) / troop
                experience_modification = {1: -0.05, 2: 0, 3: 0.01, 4: 0.025, 5: 0.05}[self.experience]
                
                if self.combatant == 'attack':
                    topography_modification = {
                        'Hilly': 0, 'Mountain': -0.2, 'Forest': -0.15, 'Swamp': -0.3, 'Desert': -0.15, 'City': -0.1, 'Fortress': -0.05
                        }[self.topography]
                elif self.combatant == 'defence':
                    topography_modification = {
                        'Hilly': 0.1, 'Mountain': 0.25, 'Forest': 0.2, 'Swamp': -0.3, 'Desert': -0.2, 'City': 0.15, 'Fortress': 0.05
                        }[self.topography]
                
                factor = (strength ** self.morale) * (1 + topography_modification) * (1 + experience_modification) * self.kwargs
                rate.append((troop, factor))
        
        return rate


def combat(attacker, defender, a, d, nona, nond, thra, thrd, u, v, time, title) -> list:
    """
    Conduct a combat assessment
    
    :param aggressor: Attacker's initial strength
    :param defender: Defender's initial strength
    :param a: Attacker's combat attrition rate
    :param d: Defense's combat attrition rate
    :param nona: Offense's non-combat attrition rate
    :param nond: Defense's non-combat attrition rate
    :param thra: Maximum attrition rate threshold for the offense
    :param thrd: Maximum attrition rate threshold for the defense
    :param u: 
        Attacker's reinforcement rate: 
            [
                (day 1 troop, day 1 Combat factor), 
                (day 2 troop, day 2 Combat factor), ...
            ]
    :param v: 
        Defender's reinforcement rate: 
        [
            (day 1 troop, day 1 Combat factor), 
            (day 2 troop, day 2 Combat factor), ...
        ]
    :param time: Battle duration
    :param title: Image title
    :return: Offensive losses, Defensive losses
    """
    attackers = [attacker]
    atta = []
    
    defenders = [defender]
    attd = []
    
    duration = None

    for i in range(time):
        D = defender - a * attacker + v[i][0]
        defenders.append(D)
        attd.append(a * attacker)
        
        A = attacker - d * defender + u[i][0]
        attackers.append(A)
        atta.append(d * defender)
        
        ratea = sum(atta) / A
        rated = sum(attd) / D

        if (ratea > thra) or (rated > thrd):
            dela = ratea - thra; deld = rated - thrd
            if dela > deld: print('Attacker lost the battle.')
            elif dela < deld: print('Defender lost the battle.')
            else: print('The battle was evenly matched.')
            duration = i
            break

        a = (a * (attacker - d * defender) + u[i][0] * u[i][1]) / A
        d = (d * (defender - a * attacker) + v[i][0] * v[i][1]) / D
        
        attacker = A
        defender = D
        
        duration = i
    
    print('The attacking side committed', 
        f'{attackers[0] + sum([reinforcement[0] for reinforcement in u[:duration]])} men, lost', 
            f'{sum(atta) + nona * attackers[0]}.')
    print('The defense side committed', 
        f'{defenders[0] + sum([reinforcement[0] for reinforcement in v[:duration]])} men, lost', 
            f'{sum(attd) + nond * defenders[0]}.')
    
    plt.rcParams['font.family'] = 'Times New Roman'
    
    plt.plot(range(time + 1), attackers, label='Attacker')
    plt.plot(range(time + 1), defenders, label='Defender')
    
    plt.grid()
    
    plt.xlabel('Days')
    plt.ylabel('Troops')
    plt.title(title)
    
    plt.legend()
    plt.show()
    
    attacker_losses = sum(atta) + nona * attackers[0]
    defender_losses = sum(attd) + nond * defenders[0]
    
    return attacker_losses, defender_losses


class Intelligence(object):
    """
    The Intelligence module of the strategic simulation system

    Attributes:
        Intelligence Network Level
        Intelligence Action
        Target
    """
    
    def __init__(self, network, action, target) -> object:
        """
        This part defines the basic parameters of the intelligence module.
        
        :param network: 
            Intelligence network level in the target country: 0~4 (float)
        :param action: 
            Type of intelligence action: obstruction, sabotage, defense (str)
        :param target: 
            The country targeted by intelligence action (str)
        """
        self.network = network
        self.action = action
        self.target = target
    
    def verdict(self) -> bool:
        """
        This section defines 
        the specific mechanics of intelligence action verdict.

        :return: The output: True, False
        """
        random_byte = ord(urandom(1))
        random_number = random_byte % 6 + 1
        
        if self.action == 'defense': 
            return True
        
        if 0 <= self.network < 1:
            if random_number in (1, 2, 3): 
                return True
            else: 
                return False
        elif 1 <= self.network < 2:
            if random_number in (1, 2, 3, 4): 
                return True
            else: 
                return False
        elif 2 <= self.network < 3:
            if random_number in (1, 2, 3, 4, 5): 
                return True
            else: 
                return False
        elif 3 <= self.network <= 4:
            return True


def judgment(resa) -> bool:
    """
    After successful obstruction and sabotage operations 
    by the intelligence initiating country, 
    a secondary determination is required 
    if the target country engages in defense of the intelligence.

    :param resa: 
        Results of intelligence operations determinations 
        by intelligence attacking state: True, False (bool)
    """
    if not resa: 
        pass
    else:
        attack_point = ord(urandom(1)) % 6 + 1
        defense_point = ord(urandom(1)) % 6 + 1
        
        if defense_point < attack_point < 3:
            print('No implementation, no information.')
            return False, False
        elif defense_point < 3 < attack_point:
            print('Implement, not inform.')
            return True, False
        elif 3 < defense_point < attack_point:
            print('Implement, inform.')
            return True, True
        else:
            print('Not implement, inform.')
            return False, True