from nomine import Nomine
from random import randrange

for i in range(0, 300):
    print(f"{Nomine(preset='english').get(randrange(4,8))}", end=" ")
