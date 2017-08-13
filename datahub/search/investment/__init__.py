from .models import InvestmentProject

from ..apps import SearchApp


class InvestmentSearchApp(SearchApp):
    """SearchApp for investment"""

    name = 'investment_project'
    plural_name = 'investment_projects'
    ESModel = InvestmentProject
