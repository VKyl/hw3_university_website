from django.http import Http404
from django.shortcuts import render

from .repositories.department import DepartmentRepository
from .repositories.exchange_program import ExchangeProgramRepository
from .repositories.index_page import IndexPageRepository
from .repositories.program import ProgramRepository
from .usecases.department import DepartmentNotFoundError, DepartmentUsecase
from .usecases.exchange_program import ExchangeProgramUsecase
from .usecases.index_page import IndexPageUsecase
from .usecases.program import ProgramNotFoundError, ProgramUsecase


def index(request):
    page = IndexPageUsecase(IndexPageRepository()).get()
    return render(request, 'faculty/index.html', {'page': page})


def programs(request):
    programs = ProgramUsecase(ProgramRepository()).get_all()
    return render(request, 'faculty/programs.html', {'programs': programs})


def program_detail(request, id):
    try:
        program = ProgramUsecase(ProgramRepository()).get_by_id(id)
    except ProgramNotFoundError:
        raise Http404('Спеціальність не знайдено')
    return render(request, 'faculty/program_detail.html', {'program': program})


def departments(request):
    departments = DepartmentUsecase(DepartmentRepository()).get_all()
    return render(request, 'faculty/departments.html', {'departments': departments})


def department_detail(request, id):
    try:
        department = DepartmentUsecase(DepartmentRepository()).get_by_id(id)
    except DepartmentNotFoundError:
        raise Http404('Кафедру не знайдено')
    return render(request, 'faculty/department_detail.html', {'department': department})


def exchange_programs(request):
    exchange_programs = ExchangeProgramUsecase(ExchangeProgramRepository()).get_all()
    return render(request, 'faculty/exchange_programs.html', {'exchange_programs': exchange_programs})
