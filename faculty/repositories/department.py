from ..models import Department


class DepartmentRepository:
    def get_all(self):
        return Department.objects.prefetch_related('programs', 'tutors')

    def get_by_id(self, id):
        return Department.objects.prefetch_related('programs', 'tutors').filter(pk=id).first()
