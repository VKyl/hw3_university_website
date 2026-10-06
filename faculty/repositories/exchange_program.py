from ..models import ExchangeProgram


class ExchangeProgramRepository:
    def get_all(self):
        return ExchangeProgram.objects.all()

    def get_by_id(self, id):
        return ExchangeProgram.objects.filter(pk=id).first()
