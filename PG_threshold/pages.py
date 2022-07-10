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
    def after_all_players_arrive(self):
        self.group.g_set_payoffs()

class Results0(Page):
    wait_for_all_players=True
    def vars_for_template(self):
        self.player.p_mypayoff_method()

class Results(Page):

    def vars_for_template(self):
#        self.player.my_method()
        return {
            'my_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'me_in_all_rounds_1': self.group.get_player_by_id(1).my_payoff,
            'me_in_all_rounds_2': self.group.get_player_by_id(2).my_payoff,
            'me_in_all_rounds_3': self.group.get_player_by_id(3).my_payoff,
            'me_in_all_rounds_4': self.group.get_player_by_id(4).my_payoff,
            'me_in_all_rounds_5': self.group.get_player_by_id(5).my_payoff,
            'p1_contr': self.group.get_player_by_id(1).my_contribution,
            'p2_contr': self.group.get_player_by_id(2).my_contribution,
            'p3_contr': self.group.get_player_by_id(3).my_contribution,
            'p4_contr': self.group.get_player_by_id(4).my_contribution,
            'p5_contr': self.group.get_player_by_id(5).my_contribution,
            'current_round': self.subsession.round_number
        }


class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_payoff_full': sum(
                [p.payoff for p in self.player.in_all_rounds()]),
            'total_payoff_cut': sum([p.payoff for p in self.player.in_all_rounds()])*0.25,
            'player_in_all_rounds': self.player.in_all_rounds(),
            # 'global_outcome': self.success(),
        }

page_sequence = [
    Welcome,
    Instructions,
    Contribution,
    ResultsWaitPage,
    Results0,
    Results,
    ResultsSummary
]
