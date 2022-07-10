from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# from django.forms.models import inlineformset_factory
# from django import forms

# class Introduction(Page):
#     def is_displayed(self):
#         return self.round_number == 1


class Normative(Page):
    timeout_seconds = 60
    form_model = models.Player
    form_fields = ['normative']

    def vars_for_template(self):
        return {
            'current_round': self.subsession.round_number
        }


class BeforeContrib(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_normative()
        # self.group.set_pgg_self()

class Results0(Page):
    pass

class Contribution(Page):
    timeout_seconds = 60
    form_model = models.Player
    form_fields = ['contribution']

    def vars_for_template(self):
        return {
            'current_round': self.subsession.round_number
        }

class BeforeGuess(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.group.set_pgg_payoffs()

class Results1(Page):
    pass

class Guess(Page):
    timeout_seconds = 60
    form_model = models.Player
    form_fields = ['guess']

    def vars_for_template(self):
        return {
            'current_round': self.subsession.round_number
        }


class BeforeResults(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_pgg()
            p.set_guess()


class EmoPage_Ang(Page):
    form_model = models.Player
    form_fields = 'anger'

    def vars_for_template(self):
        frm = self.get_form()
        others = self.player.get_others_in_group()
        return {
            'datang': zip(frm, others),
            'current_round': self.subsession.round_number
        }

    def get_form_fields(self):
        return ['anger_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]


class EmoPage_Sat(Page):
    form_model = models.Player
    form_fields = 'satis'

    def vars_for_template(self):
        frm = self.get_form()
        others = self.player.get_others_in_group()
        return {
            'datsat': zip(frm, others),
            'current_round': self.subsession.round_number
        }

    def get_form_fields(self):
        return ['satis_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]


class EmoWaitPage1(WaitPage):
    def after_all_players_arrive(self):
#        self.group.set_pgg_payoffs()
        for p in self.group.get_players():
#            p.set_pgg() #_payoffs()
            p.set_anger()
            p.set_satis()

class Results2(Page):
    pass

class Emoest_Ang(Page):
    form_model = models.Player
    form_fields = ['eang_1','eang_2','eang_3','eang_4','eang_5','eang_6']

    def vars_for_template(self):
        self.player.my_method()
        frma = self.get_form()  # this adds form to fill
        others = self.player.get_others_in_group()
        # oth_payoffs = [sum([p.payoff for p in i.in_all_rounds()]) for i in others]  # final_payoff
        # oth_contributions = [sum([p.contribution for p in i.in_all_rounds()]) for i in others]
        return {'other_players_data': zip(frma, others),  # oth_payoffs, oth_contributions),
            'current_round': self.subsession.round_number
        }

    # def get_form_fields(self):
    #     return ['eang_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]
    # noinspection PyUnreachableCode
    def get_form_fields(self):
        return ['eang_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]

#             ('esat_{}'.format(i.id_in_group)) for i in self.player.get_others_in_group())]

class Emoest_Sat(Page):
    form_model = models.Player
    form_fields = ['esat_1','esat_2','esat_3','esat_4','esat_5','esat_6']

    def vars_for_template(self):
        self.player.my_method()
        frma = self.get_form()  # this adds form to fill
        others = self.player.get_others_in_group()
        # oth_payoffs = [sum([p.payoff for p in i.in_all_rounds()]) for i in others]  # final_payoff
        # oth_contributions = [sum([p.contribution for p in i.in_all_rounds()]) for i in others]
        return {'other_players_data': zip(frma, others),  # oth_payoffs, oth_contributions),
            'current_round': self.subsession.round_number
        }

    # def get_form_fields(self):
    #     return ['eang_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]
    # noinspection PyUnreachableCode

    def get_form_fields(self):
        return ['esat_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]
#             ('esat_{}'.format(i.id_in_group)) for i in self.player.get_others_in_group())]

        #    ['esat_{}'.format(i.id_in_group) for i in (self.player.get_others_in_group()]


class EmoWaitPage2(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_anger_reward()
            p.set_satis_reward()
            p.set_guess_reward()
            p.set_reward()
            p.set_guess_payoff()
            p.set_payoff
            p.set_final_payoff()

class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'total_pgg_payoff': sum([p.pgg_payoff for p in self.player.in_all_rounds()]),
            'total_contribution': sum([p.contribution for p in self.player.in_all_rounds()]),
            #            'total_punishment_received': sum([p.punishment_received for p in self.player.in_all_rounds()]),
            #            'total_punishment_sent': sum([p.punishment_sent for p in self.player.in_all_rounds()]),
            'total_pay': self.player.in_round(self.session.vars['paying_round']).payoff,
            'guess_pay': self.player.reward_payoff,
            'guess_paying_round': self.session.vars['paying_round'],
            'participant_payoff': self.participant.payoff + self.player.reward_payoff, # sum([p.payoff for p in self.player.in_all_rounds()]),
            #            'player_in_all_rounds': self.player.in_all_rounds(),
        }
    # def is_displayed(self):
    #    return self.subsession.round_number == Constants.num_rounds


page_sequence = [
#    Introduction,
    Normative,
    BeforeContrib,
    Results0,
    Contribution,
    BeforeGuess,
    Results1,
    Guess,
    BeforeResults,
    EmoPage_Ang,
    EmoPage_Sat,
    EmoWaitPage1,
    Results2,
    Emoest_Ang,
    Emoest_Sat,
    EmoWaitPage2,
    ResultsSummary
]
