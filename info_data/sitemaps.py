from django.contrib.sitemaps import Sitemap
from info_data.models import Blog_Post



class Blog_PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog_Post.objects.filter(status=1)


    def lastmod(self, obj):
        return obj.Date


