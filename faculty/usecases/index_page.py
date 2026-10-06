class IndexPageUsecase:
    def __init__(self, index_page_repository):
        self.index_page_repository = index_page_repository

    def get(self):
        return self.index_page_repository.get()
