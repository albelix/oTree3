from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

   def play_round(self):
        yield (pages.Contribution, {'contribution': c(42)})
        yield (pages.Results0)
        if self.player.id_in_group == 1:
             yield pages.PunPage, dict(pun_2=3, pun_3=0, pun_4=3, pun_5=4)
        if self.player.id_in_group == 2:
             yield pages.PunPage, dict(pun_1=3, pun_3=0, pun_4=3, pun_5=4)
        if self.player.id_in_group == 3:
             yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_4=3, pun_5=4)
        if self.player.id_in_group == 4:
             yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_3=3, pun_5=4)
        if self.player.id_in_group == 5:
             yield pages.PunPage, dict(pun_1=3, pun_2=0, pun_3=3, pun_4=4)
        yield (pages.Results1)
        yield (pages.Results)
        if self.round_number == Constants.num_rounds:
             yield (pages.ResultsSummary)
