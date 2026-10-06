class DepartmentNotFoundError(Exception):
    pass


class DepartmentUsecase:
    def __init__(self, department_repository):
        self.department_repository = department_repository

    def get_all(self):
        return self.department_repository.get_all()

    def get_by_id(self, id):
        department = self.department_repository.get_by_id(id)
        if department is None:
            raise DepartmentNotFoundError(id)
        return department
