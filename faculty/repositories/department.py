from ..models import Department


class DepartmentRepository:
    def get_all(self):
        return Department.objects.all()

    def get_by_id(self, id):
        return Department.objects.filter(pk=id).first()
