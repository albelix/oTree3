import random

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Petrov Nikita'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'covid'
    players_per_group = None
    num_rounds = 1
    p=0.5
    p_vacH=0.1
    p_novH=0.5

    vacpen=15
    endow=100
    vacH=60
    vacL=20
    novH=80
    novL=40


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    # def setstatus(self):
    #     for p in self.get_players():
    #         if self.vac == 1:
    #             self.status=random.sample(Constants.p_vac, 1)
    #         else:
    #             self.status=random.sample(Constants.p_nov, 1)
    #
    # pass
    pass

class Player(BasePlayer):
    vac=models.IntegerField(label='Примите решение о вакцинации',
                            choices=[[0, 'Не вакцинироваться'],
                                     [1, 'Вакцинироваться']],
                            widget=widgets.RadioSelectHorizontal)
    status=models.IntegerField()

    hardorlight=models.IntegerField()

    check1=models.IntegerField(label='Допустим, вы приняли решение вакцинироваться и заболели в тяжелой форме, сколько составит ваша выплата?',
                               choices=[[1, '100 у.е.'],
                                        [2, '85 у.е.'],
                                        [3, '25 у.е.'],
                                        [4, '20 у.е.']],
                               widget=widgets.RadioSelectHorizontal)

    check2=models.IntegerField(label='Какова вероятность заболеть?',
                               choices=[[1, '50%'],
                                        [2, '5%'],
                                        [3, '25%'],
                                        [4, '45%']],
                               widget=widgets.RadioSelectHorizontal)

    check3=models.IntegerField(label='Какова вероятность заболеть в тяжелой форме, если вы не вакцинировались?',
                               choices=[[1, '50%'],
                                        [2, '5%'],
                                        [3, '25%'],
                                        [4, '45%']],
                               widget=widgets.RadioSelectHorizontal)



    # def setstatus(self):
    #     for p in self.get_players():
    #         if self.vac == 1:
    #             self.status=random.sample(Constants.p_vac, 1)
    #         else:
    #             self.status=random.sample(Constants.p_nov, 1)
    #
    # def ifhard(self):
    #     if self.vac==1:
    #         if self.status==1:
    #             self.hardorlight=random.sample(Constants.p_vacH, 1)
    #         else:
    #             self.hardorlight=0
    #     else:
    #         if self.status==1:
    #             self.hardorlight=random.sample(Constants.p_novH, 1)
    #         else:
    #             self.hardorlight=0
    #
    # def set_payoff(self):
    #     if self.vac==1:
    #         if self.status==1:
    #             if self.hardorlight==1:
    #                 self.payoff=Constants.endow-Constants.vacpen-Constants.vacH
    #             else:
    #                 self.payoff=Constants.endow-Constants.vacpen-Constants.vacL
    #         else:
    #             self.payoff=Constants.endow-Constants.vacpen
    #     else:
    #         if self.status==1:
    #             if self.hardorlight==1:
    #                 self.payoff=Constants.endow-Constants.novH
    #             else:
    #                 self.payoff = Constants.endow - Constants.novL
    #         else:
    #             self.payoff = Constants.endow





    # def setstatus(player):
    #     player=player
    #     if player.vac>1/2:
    #         player.status=random.sample(Constants.p_vac, 1)
    #     else:
    #         player.status=random.sample(Constants.p_nov, 1)
    pass
    pass
