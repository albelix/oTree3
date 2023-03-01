from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions(Page):
        def is_displayed(self):
            return self.subsession.round_number == 1

class Contribution(Page):
    form_model = models.Player
    form_fields = ['contribution']
    def vars_for_template(self):
        return {
           'current_round': self.subsession.round_number
       }

class ResultsWaitPage(WaitPage):
    wait_for_all_players=True
    after_all_players_arrive = 'g_set_payoffs'

class Results0(Page):
    wait_for_all_players=True
    def after_all_players_arrive(self):
        self.player.p_mypayoff_method()

class PunPage(Page):
    wait_for_all_players = True
    form_model = models.Player
    def vars_for_template(self):
        self.player.p_mypayoff_method()
        return {
            'me_in_all_rounds_1': self.group.get_player_by_id(1).profit,
            'me_in_all_rounds_2': self.group.get_player_by_id(2).profit,
            'me_in_all_rounds_3': self.group.get_player_by_id(3).profit,
            'me_in_all_rounds_4': self.group.get_player_by_id(4).profit,
            'me_in_all_rounds_5': self.group.get_player_by_id(5).profit,
            'p1_contr': self.group.get_player_by_id(1).contribution,
            'p2_contr': self.group.get_player_by_id(2).contribution,
            'p3_contr': self.group.get_player_by_id(3).contribution,
            'p4_contr': self.group.get_player_by_id(4).contribution,
            'p5_contr': self.group.get_player_by_id(5).contribution,
            'current_round': self.subsession.round_number
        }


    def get_form_fields(self):
        # pun_i is punishment by some player to player i
        if self.player.id_in_group == 1:
            return ['pun_2', 'pun_3', 'pun_4', 'pun_5']
        if self.player.id_in_group == 2:
            return ['pun_1', 'pun_3', 'pun_4', 'pun_5']
        if self.player.id_in_group == 3:
            return ['pun_1', 'pun_2', 'pun_4', 'pun_5']
        if self.player.id_in_group == 4:
            return ['pun_1', 'pun_2', 'pun_3', 'pun_5']
        if self.player.id_in_group == 5:
            return ['pun_1', 'pun_2', 'pun_3', 'pun_4']

class ResultsWaitPage1(WaitPage):
    wait_for_all_players = True
#    after_all_players_arrive = set_pun
    # wait_for_all_players=True
    after_all_players_arrive = 'g_set_pun'
#        self.p_punpay()


class Results1(Page):
    wait_for_all_players = True
    after_all_players_arrive = 'g_set_pun'

class Results(Page):
    wait_for_all_players=True
    form_model = models.Player
    after_all_players_arrive = 'p_punpay'
    #form_fields = ['pun_{}'.format(i) for i in range(1, 6)]
    def vars_for_template(self):
        self.player.p_punpay()
        return {
        #    'my_profit': sum([p.my_profit for p in self.player.in_all_rounds()]),
            'p1_payoff': self.group.get_player_by_id(1).my_payoff,
            'p2_payoff': self.group.get_player_by_id(2).my_payoff,
            'p3_payoff': self.group.get_player_by_id(3).my_payoff,
            'p4_payoff': self.group.get_player_by_id(4).my_payoff,
            'p5_payoff': self.group.get_player_by_id(5).my_payoff,
            'p1_contr': self.group.get_player_by_id(1).my_contribution,
            'p2_contr': self.group.get_player_by_id(2).my_contribution,
            'p3_contr': self.group.get_player_by_id(3).my_contribution,
            'p4_contr': self.group.get_player_by_id(4).my_contribution,
            'p5_contr': self.group.get_player_by_id(5).my_contribution,
            'pun1_round': self.group.get_player_by_id(1).pun,
            'pun2_round': self.group.get_player_by_id(2).pun,
            'pun3_round': self.group.get_player_by_id(3).pun,
            'pun4_round': self.group.get_player_by_id(4).pun,
            'pun5_round': self.group.get_player_by_id(5).pun,
            'current_round': self.subsession.round_number
        }


class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds



    def vars_for_template(self):
        return {
            'current_round': self.subsession.round_number,
            'total_payoff_full':  self.player.my_payoff,  # format(float(self.player.my_payoff), '.2f'),
            # - displays 2 decimals, not rounded if USE POINT=True
            'total_payoff_cut': self.player.my_payoff*Constants.loss_factor, #format(float(
            # self.player.my_payoff*Constants.loss_factor), '.2f'),
            'player_in_all_rounds': self.player.in_all_rounds(),
            'total_contribution': self.player.my_contribution,
            'total_punishment': self.player.my_pun,
            'total_puncost': self.player.my_puncost
        }


class Results2(WaitPage):
    after_all_players_arrive = 'g_set_pun'


class ResultsFinalPayoff(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.p_set_finalpayoff()
        self.group.g_set_pun()
        return {
            'total_payoff_full': self.player.my_payoff,  # sum([p.my_payoff for p in
            # self.player.in_all_rounds( )]),
            'total_payoff_cut': self.player.my_payoff * Constants.loss_factor,
            'total_payoff': self.participant.payoff # for p in self.group.get_players()
        }

page_sequence = [
    Welcome,
    Instructions,
    Contribution,
    ResultsWaitPage,
    Results0,
    PunPage,
    ResultsWaitPage1,
    Results1,
    Results,
    ResultsSummary,
    Results2,
    ResultsFinalPayoff
]
