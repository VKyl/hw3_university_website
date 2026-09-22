from ..models import Tutor


class TutorRepository:
    def get_all(self):
        return Tutor.objects.select_related('departament')

    def get_by_id(self, id):
        return Tutor.objects.select_related('departament').filter(pk=id).first()
