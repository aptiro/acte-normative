from haystack import indexes

from .models import Bill


class BillIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='title', document=True)

    def get_model(self):
        return Bill
