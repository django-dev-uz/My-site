from .models import GetInfo
from .models import PhotoFor
from .models import AddProject
from .models import AddInformation
from .models import AddInformation1
from .models import ProjectCategory

from django.contrib import admin

admin.site.register(GetInfo)
admin.site.register(PhotoFor)
admin.site.register(AddProject)
admin.site.register(ProjectCategory)
admin.site.register(AddInformation)
admin.site.register(AddInformation1)
