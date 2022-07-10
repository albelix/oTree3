from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

   def play_round(self):
       if self.round_number == 1:
           yield Submission(pages.Welcome, check_html=False)
       if self.round_number == 1:
           yield Submission(pages.Instructions, check_html=False)
       yield (pages.Contribution, {'contribution': c(42)})
       yield Submission(pages.Results0, check_html=False)
       if self.player.id_in_group == 1:
            yield pages.PunPage, dict(pun_2=3,pun_3=0,pun_4=3,pun_5=4)
       if self.player.id_in_group == 2:
            yield pages.PunPage, dict(pun_1=3, pun_3=0, pun_4=3, pun_5=4)
       if self.player.id_in_group == 3:
            yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_4=3, pun_5=4)
       if self.player.id_in_group == 4:
            yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_3=3, pun_5=4)
       if self.player.id_in_group == 5:
            yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_3=3, pun_4=4)
       yield Submission(pages.Results1, check_html=False)
       yield Submission(pages.Results, check_html=False)
       if self.round_number == Constants.num_rounds:
           yield Submission(pages.ResultsSummary, check_html=False)
       if self.round_number == Constants.num_rounds:
           yield Submission(pages.ResultsFinalPayoff, check_html=False)
