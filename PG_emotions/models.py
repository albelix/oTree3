from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from tables import group

import random
import itertools

#from otree.constants import BaseConstants
#from otree.models import BaseSubsession, BaseGroup, BasePlayer
#from otree.db import models

# from otree import widgets
# from otree.common import Currency as c, currency_range, safe_json

author = 'Alexis Belianin'

doc = """
PG game with emotions 
"""


class Constants(BaseConstants):
    name_in_url = 'PG_2021'
    players_per_group = 6
    num_rounds = 8
    endowment = c(20)
    lumpsum = c(150)
    efficiency_factor = 2
    contribution_limits = currency_range(0, endowment, 1)  # define range of contribs
    num_decisions_per_round = 2
    guess_endowment = 75  # resources to guess
    rewval = 16 # constant to calculate reward for estimates

    EmotionS=[
        [1, '1: Точно нет'],
        [2, '2: Скорее нет'],
        [3, '3: И да и нет'],
        [4, '4: Скорее да'],
        [5, '5: Точно да']
    ]


class Subsession(BaseSubsession):
    paying_round = models.IntegerField()
    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round

    # def vars_for_admin_report(selfщекуу):
    #     participant_payoffs = sorted([p.participant.payoff for p in self.get_players()])
    #     return {'payoffs': participant_payoffs}

class Group(BaseGroup):
    mean_normative = models.CurrencyField(doc="""Mean normative contribution expected ex ante""")
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
#    mean_anger = models.FloatField(doc="""Mean anger about contributions ex post""")
#    mean_satis = models.FloatField(doc="""Mean satisfaction of contributions ex post""")

    def set_normative(self):
        self.mean_normative = sum([p.normative for p in self.get_players()]) / Constants.players_per_group

    def set_pgg_payoffs(self):
        print("contribution", sum([p.contribution for p in self.get_players()]))
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.pgg_payoff = Constants.endowment - p.contribution + self.individual_share

    # def set_anger_mean(self):
    #     for p in self.get_players():
    #         p.mean_anger()
    #
    # def set_satis_mean(self):
    #     for p in self.get_players():
    #         p.mean_satis()

#    def set_satis_mean(self):
#        self.mean_satis = sum([p.satis for p in self.get_players()]) / Constants.players_per_group

    # def set_payoffs(self):
    #     for p in self.get_players():
    #         p.period_final_payoffs = Constants.endowment - p.contribution + self.individual_share
    #         print('p.payoff_is', p.period_final_payoffs)


class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", min=0, max=Constants.endowment)
    pgg_payoff = models.CurrencyField(doc='to store intermediary profit from pgg per se', initial=0)
    my_contribution = models.CurrencyField(doc="""rolling cumulative contributions""", min=0, max=Constants.endowment)
    my_payoff = models.CurrencyField(doc="""rolling participant total payoff""")

    normative = models.CurrencyField(doc='amount due to be contributed to PG', min=0, max=Constants.endowment)
    guess = models.FloatField(doc='guessed mean amount contributed to PG', min=0, max=Constants.endowment)
    mean_guess = models.FloatField(doc="""Mean guess about contribution ex post""")

#    cumulative_intermediate_profit = models.CurrencyField(doc='profit accumulated before punishment', min=0)
    #final_payoff = models.CurrencyField(doc='payoffs after all punishments', min=0)  # suppressed

    anger_1 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 1',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    anger_2 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 2',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    anger_3 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 3',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    anger_4 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 4',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    anger_5 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 5',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    anger_6 = models.PositiveIntegerField(verbose_name='До какой степени Вас возмущает решение Участника 6',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())


    satis_1 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 1',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    satis_2 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 2',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    satis_3 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 3',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    satis_4 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 4',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    satis_5 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 5',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
    satis_6 = models.PositiveIntegerField(verbose_name='До какой степени Вас удовлетворяет решение Участника 6',
                                          choices=Constants.EmotionS,
                                          widget=widgets.RadioSelectHorizontal())
#    ownestim =  models.CurrencyField(doc="""own estimatior of anger""")
#    anger_stated = models.FloatField(doc="""anger vector""")
#    satis_stated = models.FloatField(doc="""satisfaction vector""")

    mean_anger = models.FloatField(doc="""mean anger""")
    mean_satis = models.FloatField(doc="""mean satisfaction""")

    eang_1=models.FloatField(label='eang_1', min=1, max=5)
    eang_2=models.FloatField(label='eang_2', min=1, max=5)
    eang_3=models.FloatField(label='eang_3', min=1, max=5)
    eang_4=models.FloatField(label='eang_4', min=1, max=5)
    eang_5=models.FloatField(label='eang_5', min=1, max=5)
    eang_6=models.FloatField(label='eang_6', min=1, max=5)

    esat_1 = models.FloatField(label='esat_1', min=1, max=5)
    esat_2 = models.FloatField(label='esat_2', min=1, max=5)
    esat_3 = models.FloatField(label='esat_3', min=1, max=5)
    esat_4 = models.FloatField(label='esat_4', min=1, max=5)
    esat_5 = models.FloatField(label='esat_5', min=1, max=5)
    esat_6 = models.FloatField(label='esat_6', min=1, max=5)

    reward_guess = models.CurrencyField(doc="""reward for guess about contributions""")

    reward_anger_1 = models.CurrencyField(label='ra_1', min=1, max=5)
    reward_anger_2 = models.CurrencyField(label='ra_2', min=1, max=5)
    reward_anger_3 = models.CurrencyField(label='ra_3', min=1, max=5)
    reward_anger_4 = models.CurrencyField(label='ra_4', min=1, max=5)
    reward_anger_5 = models.CurrencyField(label='ra_5', min=1, max=5)
    reward_anger_6 = models.CurrencyField(label='ra_6', min=1, max=5)

    reward_satis_1 = models.CurrencyField(label='rs_1', min=1, max=5)
    reward_satis_2 = models.CurrencyField(label='rs_2', min=1, max=5)
    reward_satis_3 = models.CurrencyField(label='rs_3', min=1, max=5)
    reward_satis_4 = models.CurrencyField(label='rs_4', min=1, max=5)
    reward_satis_5 = models.CurrencyField(label='rs_5', min=1, max=5)
    reward_satis_6 = models.CurrencyField(label='rs_6', min=1, max=5)

    reward_anger = models.CurrencyField(doc="""reward for anger estimation""")
    reward_satis = models.CurrencyField(doc="""reward for satisfaction estimation""")

    reward_payoff = models.CurrencyField(doc="""reward for guesses""")

    def set_pgg(self):
        self.pgg_payoff = Constants.endowment - self.contribution + self.group.individual_share

    def set_guess(self):
        self.mean_guess = sum([p.guess for p in self.group.get_players()]) / Constants.players_per_group

    def set_guess_reward(self):
        self.reward_guess = (400-(self.mean_guess - self.guess)**2) / 10

    def set_anger(self):
        anger_stated = [getattr(i, 'anger_{}'.format(self.id_in_group)) for i in self.get_others_in_group()]
        print('anger_stated is', anger_stated)
        self.mean_anger = sum(anger_stated)/Constants.players_per_group
        print('mean anger is', self.mean_anger)

    def set_satis(self):
        satis_stated = [getattr(i, 'satis_{}'.format(self.id_in_group)) for i in self.get_others_in_group()]
        self.mean_satis = sum(satis_stated)/Constants.players_per_group

    def get_form_fields(self):
        return ['eang_()'.format(i) for i in self.get_others_in_group()]

    def set_anger_reward(self):
        #listang = ['eang_1', 'eang_2', 'eang_3', 'eang_4', 'eang_5', 'eang_6']
        for p in self.group.get_players(): #self.anger_estimated = sum([getattr(i, 'eang_{}'.format(self.id_in_group)) for i in self.group.get_players()])/ (Constants.players_per_group)
           #for i in self.get_others_in_group():
        #    p.reward_anger_[p] = 25 - ((getattr(p, 'eang_{}'.format(self.id_in_group))) - self.mean_anger[p]) ** 2
            # p.reward_anger_1 = 25 - (self.eang_1 - self.mean_anger) ** 2
            # p.reward_anger_2 = 25 - (self.eang_2 - self.mean_anger) ** 2
            # p.reward_anger_3 = 25 - (self.eang_3 - self.mean_anger) ** 2
            # p.reward_anger_4 = 25 - (self.eang_4 - self.mean_anger) ** 2
            # p.reward_anger_5 = 25 - (self.eang_5 - self.mean_anger) ** 2
            # p.reward_anger_6 = 25 - (self.eang_6 - self.mean_anger) ** 2
            if self.id_in_group==1:
                self.reward_anger_1 = 0
                self.reward_anger_2 = (Constants.rewval - (self.eang_2 - self.mean_anger)**2)/2
                self.reward_anger_3 = (Constants.rewval - (self.eang_3 - self.mean_anger)**2)/2
                self.reward_anger_4 = (Constants.rewval - (self.eang_4 - self.mean_anger)**2)/2
                self.reward_anger_5 = (Constants.rewval - (self.eang_5 - self.mean_anger)**2)/2
                self.reward_anger_6 = (Constants.rewval - (self.eang_6 - self.mean_anger)**2)/2
            elif self.id_in_group==2:
                self.reward_anger_1 = (Constants.rewval - (self.eang_1 - self.mean_anger) ** 2)/2
                self.reward_anger_2 = 0
                self.reward_anger_3 = (Constants.rewval - (self.eang_3 - self.mean_anger) ** 2)/2
                self.reward_anger_4 = (Constants.rewval - (self.eang_4 - self.mean_anger) ** 2)/2
                self.reward_anger_5 = (Constants.rewval - (self.eang_5 - self.mean_anger) ** 2)/2
                self.reward_anger_6 = (Constants.rewval - (self.eang_6 - self.mean_anger) ** 2)/2
            elif self.id_in_group==3:
                self.reward_anger_1 = (Constants.rewval - (self.eang_1 - self.mean_anger) ** 2)/2
                self.reward_anger_2 = (Constants.rewval - (self.eang_2 - self.mean_anger) ** 2)/2
                self.reward_anger_3 = 0
                self.reward_anger_4 = (Constants.rewval - (self.eang_4 - self.mean_anger) ** 2)/2
                self.reward_anger_5 = (Constants.rewval - (self.eang_5 - self.mean_anger) ** 2)/2
                self.reward_anger_6 = (Constants.rewval - (self.eang_6 - self.mean_anger) ** 2)/2
            elif self.id_in_group==4:
                self.reward_anger_1 = (Constants.rewval - (self.eang_1 - self.mean_anger) ** 2)/2
                self.reward_anger_2 = (Constants.rewval - (self.eang_2 - self.mean_anger) ** 2)/2
                self.reward_anger_3 = (Constants.rewval - (self.eang_3 - self.mean_anger) ** 2)/2
                self.reward_anger_4 = 0
                self.reward_anger_5 = (Constants.rewval - (self.eang_5 - self.mean_anger) ** 2)/2
                self.reward_anger_6 = (Constants.rewval - (self.eang_6 - self.mean_anger) ** 2)/2
            elif self.id_in_group==5:
                self.reward_anger_1 = (Constants.rewval - (self.eang_1 - self.mean_anger) ** 2)/2
                self.reward_anger_2 = (Constants.rewval - (self.eang_2 - self.mean_anger) ** 2)/2
                self.reward_anger_3 = (Constants.rewval - (self.eang_3 - self.mean_anger) ** 2)/2
                self.reward_anger_4 = (Constants.rewval - (self.eang_4 - self.mean_anger) ** 2)/2
                self.reward_anger_5 = 0
                self.reward_anger_6 = (Constants.rewval - (self.eang_6 - self.mean_anger) ** 2)/2
            elif self.id_in_group==6:
                self.reward_anger_1 = Constants.rewval - (self.eang_1 - self.mean_anger) ** 2
                self.reward_anger_2 = Constants.rewval - (self.eang_2 - self.mean_anger) ** 2
                self.reward_anger_3 = Constants.rewval - (self.eang_3 - self.mean_anger) ** 2
                self.reward_anger_4 = Constants.rewval - (self.eang_4 - self.mean_anger) ** 2
                self.reward_anger_5 = Constants.rewval - (self.eang_5 - self.mean_anger) ** 2
                self.reward_anger_6 = 0
            self.reward_anger = self.reward_anger_1 + self.reward_anger_2 + self.reward_anger_3+ self.reward_anger_4+ self.reward_anger_5 + self.reward_anger_6
            print('reward anger', self.reward_anger) #return {self.reward_anger}

    def set_satis_reward(self):
        for p in self.group.get_players(): #self.satis_estimated = sum([getattr(i, 'esat_{}'.format(self.id_in_group)) for i in self.group.get_players()])/ (Constants.players_per_group)
            if self.id_in_group == 1:
                self.reward_satis_1 = 0
                self.reward_satis_2 = (Constants.rewval - (self.esat_2 - self.mean_satis) ** 2)/2
                self.reward_satis_3 = (Constants.rewval - (self.esat_3 - self.mean_satis) ** 2)/2
                self.reward_satis_4 = (Constants.rewval - (self.esat_4 - self.mean_satis) ** 2)/2
                self.reward_satis_5 = (Constants.rewval - (self.esat_5 - self.mean_satis) ** 2)/2
                self.reward_satis_6 = (Constants.rewval - (self.esat_6 - self.mean_satis) ** 2)/2
            elif self.id_in_group == 2:
                self.reward_satis_1 = (Constants.rewval - (self.esat_1 - self.mean_satis) ** 2)/2
                self.reward_satis_2 = 0
                self.reward_satis_3 = (Constants.rewval - (self.esat_3 - self.mean_satis) ** 2)/2
                self.reward_satis_4 = (Constants.rewval - (self.esat_4 - self.mean_satis) ** 2)/2
                self.reward_satis_5 = (Constants.rewval - (self.esat_5 - self.mean_satis) ** 2)/2
                self.reward_satis_6 = (Constants.rewval - (self.esat_6 - self.mean_satis) ** 2)/2
            elif self.id_in_group == 3:
                self.reward_satis_1 = (Constants.rewval - (self.esat_1 - self.mean_satis) ** 2)/2
                self.reward_satis_2 = (Constants.rewval - (self.esat_2 - self.mean_satis) ** 2)/2
                self.reward_satis_3 = 0
                self.reward_satis_4 = (Constants.rewval - (self.esat_4 - self.mean_satis) ** 2)/2
                self.reward_satis_5 = (Constants.rewval - (self.esat_5 - self.mean_satis) ** 2)/2
                self.reward_satis_6 = (Constants.rewval - (self.esat_6 - self.mean_satis) ** 2)/2
            elif self.id_in_group == 4:
                self.reward_satis_1 = (Constants.rewval - (self.esat_1 - self.mean_satis) ** 2)/2
                self.reward_satis_2 = (Constants.rewval - (self.esat_2 - self.mean_satis) ** 2)/2
                self.reward_satis_3 = (Constants.rewval - (self.esat_3 - self.mean_satis) ** 2)/2
                self.reward_satis_4 = 0
                self.reward_satis_5 = (Constants.rewval - (self.esat_5 - self.mean_satis) ** 2)/2
                self.reward_satis_6 = (Constants.rewval - (self.esat_6 - self.mean_satis) ** 2)/2
            elif self.id_in_group == 5:
                self.reward_satis_1 = (Constants.rewval - (self.esat_1 - self.mean_satis) ** 2)/2
                self.reward_satis_2 = (Constants.rewval - (self.esat_2 - self.mean_satis) ** 2)/2
                self.reward_satis_3 = (Constants.rewval - (self.esat_3 - self.mean_satis) ** 2)/2
                self.reward_satis_4 = (Constants.rewval - (self.esat_4 - self.mean_satis) ** 2)/2
                self.reward_satis_5 = 0
                self.reward_satis_6 = (Constants.rewval - (self.esat_6 - self.mean_satis) ** 2)/2
            elif self.id_in_group == 6:
                self.reward_satis_1 = (Constants.rewval - (self.esat_1 - self.mean_satis) ** 2)/2
                self.reward_satis_2 = (Constants.rewval - (self.esat_2 - self.mean_satis) ** 2)/2
                self.reward_satis_3 = (Constants.rewval - (self.esat_3 - self.mean_satis) ** 2)/2
                self.reward_satis_4 = (Constants.rewval - (self.esat_4 - self.mean_satis) ** 2)/2
                self.reward_satis_5 = (Constants.rewval - (self.esat_5 - self.mean_satis) ** 2)/2
                self.reward_satis_6 = 0
            self.reward_satis = self.reward_satis_1 + self.reward_satis_2 + self.reward_satis_3 + self.reward_satis_4 + self.reward_satis_5 + self.reward_satis_6
            print('reward satis', self.reward_satis)  # return {self.reward_satis}

    def set_reward(self):
        self.set_anger_reward()
        self.set_satis_reward()

    def set_guess_payoff(self):
        self.reward_payoff = self.reward_guess + self.reward_anger + self.reward_satis #.in_round(self.session.vars['paying_round']) # .payoff

    def set_payoff(self):
        self.payoff = self.pgg_payoff
            #= self.pgg_payoff + self.reward_payoff

    def set_final_payoff(self):
        self.participant.payoff = self.participant.payoff # + self.reward_payoff(self.session.vars['paying_round'])
        print('partic_final_payoff', self.participant.payoff)
    #     self.pay_round = self.subsession.vars['paying_round']
    #     return{
    #         'pay_round': self.subsession.vars['paying_round']
    #     }

    def my_method(self):
       self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
       self.my_payoff = sum([p.payoff for p in self.in_all_rounds()]) # + self.retained_income  # final_payoff


    def custom_export(players):
        # header row
        yield ['session', 'participant_code', 'round_number', 'id_in_group', 'partcipant_payoff']
        for p in players:
            participant = p.participant
            session = p.session
            yield [session.code, participant.code, p.round_number, p.id_in_group, p.participant_payoff]

# for i in range(1, Constants.players_per_group + 1):
#     Player.add_to_class('pun_{}'.format(i),
#                         models.CurrencyField(min=0,
#                                              max=Constants.pun_endowment,
#                                              verbose_name="Вычет у участника {}".format(i)))
