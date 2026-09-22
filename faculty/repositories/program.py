from ..models import Program


class ProgramRepository:
    def get_all(self):
        return Program.objects.select_related('coordinator', 'department')

    def get_by_id(self, id):
        return Program.objects.select_related('coordinator', 'department').filter(pk=id).first()
