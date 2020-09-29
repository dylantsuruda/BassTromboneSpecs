from django.contrib import admin
from .models import Brand
from .models import ValveType
from .models import BellSize
from .models import BellMaterial
from .models import Finish
from .models import OuterSlideMaterial
from .models import BassTrombone
from .models import CustomizableBassTrombone

# Register your models here.

admin.site.register(Brand)
admin.site.register(ValveType)
admin.site.register(BellSize)
admin.site.register(BellMaterial)
admin.site.register(Finish)
admin.site.register(OuterSlideMaterial)
admin.site.register(BassTrombone)
admin.site.register(CustomizableBassTrombone)
