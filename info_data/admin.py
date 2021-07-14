from django.contrib import admin

# Register your models here.
from .models import Contact_us
from .models import Feedback

from .models import Viral_Video
from .models import Funny_Images

from .models import Blog_Post



from .models import Leave_a_Reply





# Function Of Models
class Blog_PostAdmin(admin.ModelAdmin):
        list_display = ('Title', 'Category', 'Date', 'Author', 'Published', 'Aside_Show', 'Show_In_Navigation')
        list_editable = ('Published', 'Aside_Show', 'Show_In_Navigation')
        list_per_page = 5
        search_fields = ('Category', 'Title',)


class Contact_usAdmin(admin.ModelAdmin):
        list_display = ('email','name', 'subject', 'message')
        list_per_page = 5

class FeedbackAdmin(admin.ModelAdmin):
        list_display = ('feedback','Short_Summery', 'email')
        list_per_page = 5

class Funny_ImagesAdmin(admin.ModelAdmin):
        list_display = ('Img','Date', 'Published','Aside_Show')
        list_editable = ('Published', 'Aside_Show')
        list_per_page = 5

class Viral_VideoAdmin(admin.ModelAdmin):
        list_display = ('Video','Date', 'Published','Aside_Show')
        list_editable = ('Published', 'Aside_Show')
        list_per_page = 5

admin.site.register(Contact_us,Contact_usAdmin)
admin.site.register(Feedback,FeedbackAdmin)

admin.site.register(Viral_Video,Viral_VideoAdmin)
admin.site.register(Funny_Images,Funny_ImagesAdmin)

admin.site.register(Blog_Post,Blog_PostAdmin)

admin.site.register(Leave_a_Reply)
# Admin Change here






