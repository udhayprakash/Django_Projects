from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]



# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)



# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



admin.site.site_header = "LocalLibrary Admin"
admin.site.site_title = "LocalLibrary Admin Portal"
admin.site.index_title = "Welcome to LocalLibrary Portal"

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


# Not to show default apps in admin site 
from django.contrib.auth.models import User, Group

# admin.site.unregister(User)
# admin.site.unregister(Group)