from ..models import IndexPage


class IndexPageRepository:
    def get(self):
        return IndexPage.objects.prefetch_related('contacts').first()
