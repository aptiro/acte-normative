from django import forms
from haystack.forms import SearchForm


class SimpleSearchForm(SearchForm):
    load_all = True
