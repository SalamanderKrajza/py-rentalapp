from django import template
register = template.Library()

# register.filter('by_author', by_author) #Needed to use our filter
@register.filter
def by_author(querry, author):
    """Removes all values of arg from the given string"""
    return querry.filter(author=author)

