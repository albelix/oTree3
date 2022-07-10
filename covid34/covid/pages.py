import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class intro (Page):

    pass


class firstpage(Page):

    form_model = 'player'

    form_fields = ['vac']

    pass

class checkcheck(Page):
    form_model = 'player'
    form_fields = ['check1',
                   'check2',
                   'check3'
                   ]
    pass


class result(Page):


    pass


page_sequence = [intro, checkcheck, firstpage, result]
