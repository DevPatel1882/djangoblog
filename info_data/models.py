
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedback = models.TextField()
    Short_Summery = models.CharField(max_length=400)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.feedback


# Funny Videos models
class Viral_Video(models.Model):
    Video = models.FileField(upload_to="info_data/Viral_Videos")
    Thumbnail = models.ImageField(upload_to="info_data/Viral_Videos_thumbnail",default='',null=True,blank=True)
    Date = models.DateField(auto_now=True)
    Author = models.CharField(max_length=200)
    Published = models.BooleanField(default=True)
    Aside_Show = models.BooleanField(default=False)

    def __str__(self):
        return self.Author

# funny images model
class Funny_Images(models.Model):
    Img = models.FileField(upload_to="info_data/Funny_Img")
    Date = models.DateField(auto_now=True)
    Published = models.BooleanField(default=True)
    Aside_Show = models.BooleanField(default=True)

CATEGORY_CHOICE = (
    ('CAR_NEWS','CAR_NEWS'),
    ('ENTERTAINMENT','ENTERTAINMENT'),
    ('GEDGETS','GEDGETS'),
    ('TRAVEL','TRAVEL'),
    ('WORLDWIDE','WORLDWIDE'),
)

STATUS = (
       (0,"Draft"),
       (1,"Publish"),
    )
# main post table models
class Blog_Post(models.Model):
    Category = models.CharField(max_length=500, default='', choices=CATEGORY_CHOICE)
    Img = models.ImageField(upload_to="info_data/Blog_Posts_Images",default='',null=True,blank=True)
    Title = models.CharField(max_length=1000)
    hindi_title = models.CharField(max_length=500,default='',blank=True,null=True)
    Date = models.DateField(auto_now=True)
    Author = models.CharField(max_length=100)
    intro = RichTextUploadingField(blank=True,null=True,default='')
    Content = RichTextUploadingField(blank=True,null=True)
    Published = models.BooleanField(default=True)
    Aside_Show = models.BooleanField(default=True)
    Show_In_Navigation = models.BooleanField(default=True)
    slug = models.SlugField(default='',max_length=500,null=True,blank=True,unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post", kwargs={'slug': self.slug})

    class Meta:
        db_table = "info_data_Blog_Post"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.Title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog_Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Blog_Post)


class Leave_a_Reply(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=200)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name
