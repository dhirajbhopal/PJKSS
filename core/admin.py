from django.contrib import admin
#from student.models import student
#from faculty.models import faculty
from core.models import User,letterserialno, donation
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.

"""@admin.register(faculty)
class facultyAdmin(admin.ModelAdmin):
	list_display=['id','name'  ,  'email',  'mobileno'  ,  'subject'  ,  'image']"""




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{"fields": ("username","email","password")}),
        (("Personal info"), {"fields": ("first_name", "last_name","role","image", "address")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions",)
    readonly_fields = ('password','email','username')



@admin.register(letterserialno)
class letterserialnoAdmin(admin.ModelAdmin):
    list_display=['serialno','issuername','issuedto','subject','issuedate']


@admin.register(donation)
class registerAdmin(admin.ModelAdmin):
    list_display=['name','lastname','address','Amount']




