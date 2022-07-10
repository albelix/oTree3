from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from random import random, randint

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.db import models
#from otree import widgets
from otree.common import Currency as c, currency_range, safe_json

author = 'Alexis Belianin'

doc = """
PG game for EDots
"""

class Constants(BaseConstants):
    name_in_url = 'PG_threshold'
    players_per_group = 5
    num_rounds = 8
    endowment = c(100)
    threshold = c(2400)
    loss_factor = 0.25
    contribution_limits = currency_range(0, endowment, 1) #define range of contribs


class Subsession(BaseSubsession):
    flood = models.FloatField()
    def creating_session(self):
        for p in self.get_players():
            Group.flood = randint(1, Constants.threshold)/Constants.threshold

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    # individual_share = models.CurrencyField()
    # round_number=models.IntegerField()
    current_share=models.IntegerField()
    # p1 = models.IntegerField()
    # p2 = models.IntegerField()
    # p3 = models.IntegerField()
    # p1_payoff = models.CurrencyField()
    # p2_payoff = models.CurrencyField()
    my_payoff = models.CurrencyField()
    global_contribution=models.CurrencyField()
    success=models.BooleanField()
    # glob_cont=models.CurrencyField()

    # def round_number(self):
    #     return self.subsession.round_number

    def g_set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        # self.individual_share = self.total_contribution * Constants.efficiency_factor /
        # Constants.players_per_group
        self.global_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
        self.current_share=int(self.global_contribution * 100 / Constants.threshold)

        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution # + self.individual_share
            p.my_payoff = sum([me.payoff for me in p.in_all_rounds()])
            print('p.payoff_is', p.payoff)

class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", min=0,max=100)
#    payoff = models.CurrencyField()
    total_contribution = models.CurrencyField()
    my_contribution = models.CurrencyField(doc="""The amount contributed by the player""", )
    my_payoff = models.CurrencyField()
    my_cut_payoff = models.CurrencyField()
    # prof = models.CurrencyField()
    # contr = models.CurrencyField()
    # par1 = models.IntegerField()
    # par2 = models.IntegerField()
    # par3 = models.IntegerField()

    def p_mypayoff_method(self):
        self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
        self.my_payoff = sum([p.payoff for p in self.in_all_rounds()])
        self.my_cut_payoff = self.my_payoff*Constants.loss_factor
