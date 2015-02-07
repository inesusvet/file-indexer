from django import forms

SEARCH_QUERY_MAX_LENGTH = 100


class SearchForm(forms.Form):
    query = forms.CharField(max_length=SEARCH_QUERY_MAX_LENGTH)
