class ExchangeProgramNotFoundError(Exception):
    pass


class ExchangeProgramUsecase:
    def __init__(self, exchange_program_repository):
        self.exchange_program_repository = exchange_program_repository

    def get_all(self):
        return self.exchange_program_repository.get_all()

    def get_by_id(self, id):
        exchange_program = self.exchange_program_repository.get_by_id(id)
        if exchange_program is None:
            raise ExchangeProgramNotFoundError(id)
        return exchange_program
