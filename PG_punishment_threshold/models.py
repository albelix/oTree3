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
PG threshold game with punishment 
"""


class Constants(BaseConstants):
    name_in_url = 'PG_punishment_threshold'
    players_per_group = 5
    num_rounds = 8
    endowment = c(100)
#    lumpsum = c(160)
    threshold = c(2400)
    loss_factor = 0.25
    contribution_limits = currency_range(0, endowment, 1) #define range of contribs
    num_decisions_per_round = 2


class Subsession(BaseSubsession):
    thresh = models.IntegerField()
    def creating_session(self):
        self.thresh = randint(1, 2400)
#    flood = models.FloatField()
#    total_payoff = models.FloatField()
#    def creating_subsession(self):


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    contribution = models.CurrencyField()
    current_share = models.IntegerField()
    puncost = models.CurrencyField()
    punall = models.CurrencyField()
    profit = models.CurrencyField()
    my_profit = models.CurrencyField()
    punishment = models.CurrencyField(verbose_name="Вычет у участника")
    global_contribution=models.CurrencyField()
    flood = models.CurrencyField()
    success=models.BooleanField()
    thresh = models.IntegerField()
    my_payoff = models.CurrencyField()
    my_contribution = models.CurrencyField()
    my_pun = models.CurrencyField()
    my_puncost = models.CurrencyField()
    total_payoff = models.CurrencyField()


# before punishment
    def g_set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        # self.individual_share = self.total_contribution * Constants.efficiency_factor /
        # Constants.players_per_group
        self.global_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
        self.current_share = int(self.global_contribution * 100 / Constants.threshold)
#        self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
#        self.my_payoff = ([p.payoff for p in self.get_players()])
#        self.mean_contribution=sum([p.contribution for p in self.get_players()])/5
        for p in self.get_players():
           p.profit = sum([ + Constants.endowment - p.contribution ])
#               - (p.pun or 0),
#               - (p.puncost or 0),
           p.my_profit = sum([me.profit for me in p.in_all_rounds()]) #from FC
           # print('p.payoff_is', p.payoff)

    # punishment
    def g_set_pun(self):
        for p in self.get_players():
            p.p_punpay()
#            p.profit = self.payoff - p.pun - p.puncost
            p.payoff = sum([ + p.profit,
                             - (p.pun or 0),
                             - (p.puncost or 0), ])
            print('p.payoff_is', p.payoff)

        for p in self.get_players():
            p.my_payoff = sum([me.payoff for me in p.in_all_rounds()]) # get_players()])
            p.my_pun = sum([me.pun for me in p.in_all_rounds()])
            p.my_puncost = sum([me.puncost for me in p.in_all_rounds()])

# after punishment
#     def set_punpay(self):
#         for p in self.get_players():
#             p.profit = p.payoff - p.pun - p.puncost
#             print('p.payoff_is', p.profit)


class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", min=0, max=100)
    cumulative_profit = models.CurrencyField(initial=0)
    punishment = models.CurrencyField(initial=0)
    my_contribution = models.CurrencyField(doc="""The amount contributed by the player""", )
    summy_contribution = models.CurrencyField(doc="""Total amount contributed by the player""")
    my_payoff = models.CurrencyField()
    my_cut_payoff = models.CurrencyField()
    pun=models.CurrencyField(initial=0)
    pun_1 = models.CurrencyField(min=0,max=4,initial=0, verbose_name="Вычет у участника 1")
    pun_2 = models.CurrencyField(min=0,max=4,initial=0, verbose_name="Вычет у участника 2")
    pun_3 = models.CurrencyField(min=0,max=4,initial=0, verbose_name="Вычет у участника 3")
    pun_4 = models.CurrencyField(min=0,max=4,initial=0, verbose_name="Вычет у участника 4")
    pun_5 = models.CurrencyField(min=0,max=4,initial=0, verbose_name="Вычет у участника 5")
    profit = models.CurrencyField()
    pun = models.CurrencyField()
    mean_contribution = models.CurrencyField()
    puncost = models.CurrencyField()
    flood = models.FloatField()
    total_payoff = models.CurrencyField()
    my_pun = models.CurrencyField()
    my_puncost = models.CurrencyField()
    my_profit = models.CurrencyField()

    #
    # before punishment
    def p_mypayoff_method(self):
        self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
        self.my_profit = sum([p.profit for p in self.in_all_rounds()])
        # for p in self.group.get_players():
        #     self.my_contribution = p.contribution
        # for p in self.group.get_players():
        #     self.my_payoff =
        self.mean_contribution=sum([self.contribution for p in self.group.get_players()])/Constants.players_per_group
 #       self.my_cut_profit = self.my_profit * 0.25
        # return self.subsession.round_number

# after punishment
#    def my_method_tim(self):

    def p_punpay(self):
        if self.id_in_group == 1:
            self.pun = sum([p.pun_1 for p in self.group.get_players()])  # if p.id_in_group == 3])
            print('p.punishment_is', self.pun)
        if self.id_in_group == 2:
            self.pun = sum([p.pun_2 for p in self.group.get_players()])  # if p.id_in_group == 3])
            print('p.punishment_is', self.pun)
        if self.id_in_group == 3:
            self.pun = sum([p.pun_3 for p in self.group.get_players()])  # if p.id_in_group == 3])
            print('p.punishment_is', self.pun)
        if self.id_in_group == 4:
            self.pun = sum([p.pun_4 for p in self.group.get_players()])  # if p.id_in_group == 4])
            print('p.punishment_is', self.pun)
        if self.id_in_group == 5:
            self.pun = sum([p.pun_5 for p in self.group.get_players()])  # if p.id_in_group == 5])
            print('p.punishment_is', self.pun)

        self.punishment = sum([self.pun for p in self.group.get_players()])
        self.puncost = (self.pun_1 + self.pun_2 + self.pun_3 + self.pun_4 + self.pun_5) * 0.2
    #    self.payoff = sum([self.payoff for p in self.in_all_rounds()])

    def p_set_finalpayoff(self):
        if self.round_number == Constants.num_rounds:
            self.flood = float(self.group.global_contribution / Constants.threshold)
            for p in self.group.get_players():
                # self.thresh=int(self.flood)
                if self.flood >= self.subsession.thresh:
                    self.participant.payoff = self.my_payoff # sum([self.payoff for p in self.in_all_rounds()])
                else:
                    self.participant.payoff = self.my_payoff * Constants.loss_factor
                return self.participant.payoff
