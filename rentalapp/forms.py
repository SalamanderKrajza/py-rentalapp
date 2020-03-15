from django import forms

class SearchBooksForm(forms.Form):
    given_title = forms.CharField(label='Title of the book', required=False)
    given_title.widget.attrs['placeholder'] = 'Give the title of desired book (could be part of the title)'
    given_title.widget.attrs['name'] = 'given_title'

    given_author_name = forms.CharField(label='Author name', required=False)
    given_author_name.widget.attrs['placeholder'] = 'Give author name)'
    given_author_name.widget.attrs['name'] = 'given_author_name'

    given_author_surname = forms.CharField(label='Author surname', required=False)
    given_author_surname.widget.attrs['placeholder'] = 'Give author surname)'
    given_author_surname.widget.attrs['name'] = 'given_author_surname'
    