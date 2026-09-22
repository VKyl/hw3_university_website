class ProgramNotFoundError(Exception):
    pass


class ProgramUsecase:
    def __init__(self, program_repository):
        self.program_repository = program_repository

    def get_all(self):
        return self.program_repository.get_all()

    def get_by_id(self, id):
        program = self.program_repository.get_by_id(id)
        if program is None:
            raise ProgramNotFoundError(id)
        return program
