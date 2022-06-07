from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]


# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
