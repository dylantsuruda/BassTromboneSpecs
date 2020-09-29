# This script is not meant to be run from the directory it's in (InitialData).
# Rather, it's meant to be run from the parent directory, and it's meant
# to be run in the Python interpreter provided by this command:
#     python manage.py shell
# After opening the interpreter, this script can then be run using this statement:
#     >>> exec(open("InitialData/importcsvdata.py").read())

import csv
import os
from specs.models import Brand
from specs.models import ValveType
from specs.models import BellSize
from specs.models import BellMaterial
from specs.models import Finish
from specs.models import OuterSlideMaterial
from specs.models import BassTrombone
from specs.models import CustomizableBassTrombone


with open(os.path.join('InitialData', 'BassTrombones.csv')) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        brand = Brand.objects.get_or_create(brand=row[0])
        valve_type = ValveType.objects.get_or_create(valve_type=row[4])
        bell_size = BellSize.objects.get_or_create(bell_size=row[6])
        bell_material = BellMaterial.objects.get_or_create(bell_material=row[7])
        finish = Finish.objects.get_or_create(finish=row[9])
        outer_slide_material = OuterSlideMaterial.objects.get_or_create(outer_slide_material=row[10])
        create = BassTrombone.objects.get_or_create(
            brand=brand[0],
            model=row[1],
            number_of_valves=row[2],
            valve_configuration=row[3],
            valve_type=valve_type[0],
            wrap=row[5],
            bell_size=bell_size[0],
            bell_material=bell_material[0],
            dual_bore=row[8],
            finish=finish[0],
            outer_slide_material=outer_slide_material[0],
        )

with open(os.path.join('InitialData', 'CustomizableBassTrombones.csv')) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        create = CustomizableBassTrombone.objects.get_or_create(
            bass_trombone=row[0],
        )
