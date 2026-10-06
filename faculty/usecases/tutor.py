class TutorNotFoundError(Exception):
    pass


class TutorUsecase:
    def __init__(self, tutor_repository):
        self.tutor_repository = tutor_repository

    def get_all(self):
        return self.tutor_repository.get_all()

    def get_by_id(self, id):
        tutor = self.tutor_repository.get_by_id(id)
        if tutor is None:
            raise TutorNotFoundError(id)
        return tutor
