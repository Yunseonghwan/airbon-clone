from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # 같은 위치에있는 models를 불러옴


# Register your models here.


@admin.register(models.User)  # 데코레이터  models.User위에 CustomUserAdmin적용시키겟다는의미
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
