from django.contrib import admin 
from library.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	list_display=('first_name', 'second_name', 'e_mail')
	search_fields=('first_name', 'second_name')

class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'publisher', 'publication_date')
	list_filter=('publication_date',)
	#date_hierarchy = 'publication_date'

	fields= ('title', 'authors', 'publisher')
	ordering = ('-publication_date',)
	filter_horizontal=('authors',)
	raw_id_fields = ('publisher',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)


