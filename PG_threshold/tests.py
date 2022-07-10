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
       yield Submission(pages.Results, check_html=False)
       if self.round_number == Constants.num_rounds:
           yield Submission(pages.ResultsSummary, check_html=False)
