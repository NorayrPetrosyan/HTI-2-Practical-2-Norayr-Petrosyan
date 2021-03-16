import csv
import pandas as pd

class Laptops:
    def __init__(self, manufacturer, model_name, category, screen_size, screen, cpu, ram, storage, gpu,
                 operating_system,
                 operating_system_version, weight, price):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.category = category
        self.screen_size = float(screen_size.rstrip('"'))
        self.screen = screen
        self.cpu = cpu
        self.ram = int(ram.rstrip("GB"))
        self.storage = storage
        self.gpu = gpu
        self.operating_system = operating_system
        self.operating_system_version = operating_system_version
        self.weight = float(weight.rstrip("kgs"))
        self.price = float(price.replace(",", "."))


def laptops():
    with open('laptops.csv') as laptopcsv:
        reader = csv.DictReader(laptopcsv)
        for row in reader:
            yield Laptops(
                manufacturer=row['Manufacturer'],
                model_name=row['Model Name'],
                category=row['Category'],
                screen_size=row['Screen Size'],
                screen=row['Screen'],
                cpu=row['CPU'],
                ram=row['RAM'],
                storage=row['Storage'],
                gpu=row['GPU'],
                operating_system=row['Operating System'],
                operating_system_version=row['Operating System Version'],
                weight=row['Weight'],
                price=row['Price (Euros)'],
            )


def operating_systems():
    os = {}
    for laptop in laptops():
        if laptop.operating_system in os.keys():
            os[laptop.operating_system] += 1
        else:
            os[laptop.operating_system] = 1

    return pd.DataFrame.from_dict(os, orient='index', columns=['Operating Systems'])


def rams():
    ram = {}
    for laptop in laptops():
        laptop.ram = str(laptop.ram) + 'GB'
        if laptop.ram in ram.keys():
            ram[laptop.ram] += 1
        else:
            ram[laptop.ram] = 1

    return pd.DataFrame.from_dict(ram, orient='index', columns=['RAMs'])


def brands():
    brand = {}
    for laptop in laptops():
        if laptop.manufacturer in brand.keys():
            brand[laptop.manufacturer] += 1
        else:
            brand[laptop.manufacturer] = 1

    return pd.DataFrame.from_dict(brand, orient='index', columns=['Brands'])


def screen_size():
    scr_size = {
        'Up to 10"': 0,
        '10"-13"': 0,
        '13"-15"': 0,
        '15" or more': 0,
    }
    for laptop in laptops():
        if laptop.screen_size < 10:
            scr_size['Up to 10"'] += 1
        elif laptop.screen_size < 13:
            scr_size['10"-13"'] += 1
        elif laptop.screen_size < 15:
            scr_size['13"-15"'] += 1
        else:
            scr_size['15" or more'] += 1

    return pd.DataFrame.from_dict(scr_size, orient='index', columns=['Screen Size'])


def the_most_expensive_laptops():
    expensive_laptops = []
    for _ in range(int(input('How many do you want to see? '))):
        all_laptops = laptops()
        maximum = next(all_laptops)
        for laptop in all_laptops:
            if laptop.price > maximum.price and (laptop.price, laptop.model_name) not in expensive_laptops:
                maximum = laptop
        expensive_laptops.append((maximum.price, maximum.model_name))
        yield maximum

def the_cheapest_laptops():
    cheap_laptops = []
    for _ in range(int(input('How many do you want to see? '))):
        all_laptops = laptops()
        minimum = next(all_laptops)
        for laptop in all_laptops:
            if laptop.price < minimum.price and (laptop.price, laptop.model_name) not in cheap_laptops:
                minimum = laptop
        cheap_laptops.append((minimum.price, minimum.model_name))
        yield minimum

def the_heaviest_laptops():
    heavy_laptops = []
    for _ in range(int(input('How many do you want to see? '))):
        all_laptops = laptops()
        maximum = next(all_laptops)
        for laptop in all_laptops:
            if laptop.weight > maximum.weight and (laptop.weight, laptop.model_name) not in heavy_laptops:
                maximum = laptop
        heavy_laptops.append((maximum.weight, maximum.model_name))
        yield maximum

def the_most_powerful_rams():
    powerful_rams = []
    for _ in range(int(input('How many do you want to see? '))):
        all_laptops = laptops()
        maximum = next(all_laptops)
        for laptop in all_laptops:
            if laptop.ram > maximum.ram and (laptop.ram, laptop.model_name) not in powerful_rams:
                maximum = laptop
        powerful_rams.append((maximum.ram, maximum.model_name))
        yield maximum



if __name__ == '__main__':
    print("Hello․ This program performs the following functions․")
    print(
        'Enter\n'
        '1 if you want to see the most expensive laptops,\n'
        '2 if you want to see the cheapest laptops,\n'
        '3 if you want to see all operating systems with their number,\n'
        '4 if you want to see the heaviest laptops,\n'
        '5 if you want to see laptops with the most powerful RAM,\n'
        '6 if you want to see all sizes of RAMs and the number of their models,\n'
        '7 if you want to see screen sizes with the number of their models,\n'
        '8 if you want to see all brands and the number of their models.'
    )

    input_number = input("Enter the number: ")

    if input_number == '1':
        for exp_laptop in the_most_expensive_laptops():
            print(f'{exp_laptop.manufacturer} {exp_laptop.model_name} {exp_laptop.price} Euros')

    elif input_number == '2':
        for chp_laptop in the_cheapest_laptops():
            print(f'{chp_laptop.manufacturer} {chp_laptop.model_name} {chp_laptop.price} Euros')

    elif input_number == '3':
        print(operating_systems())

    elif input_number == '4':
        for hvy_laptop in the_heaviest_laptops():
            print(f'{hvy_laptop.manufacturer} {hvy_laptop.model_name} {hvy_laptop.weight}kg')

    elif input_number == '5':
        for pwf_ram in the_most_powerful_rams():
            print(f'{pwf_ram.manufacturer} {pwf_ram.model_name} {pwf_ram.ram}GB')

    elif input_number == '6':
        print(rams())

    elif input_number == '7':
        print(screen_size())

    elif input_number == '8':
        print(brands())

    else:
        print("Please enter the number correctly.")