def generator_data(list_: list = [], need: int = 1):
    from faker import Faker
    from random import randint

    fake = Faker()

    while need > 0:
        need -= 1
        list_.append((fake.name(), fake.email(), randint(0, 100)))

    return list_