from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    @property
    def play_round(self):
        yield (pages.Introduction, {{}}) # this is not working: remove Introduction page to test with bots from everywhere
        yield (pages.Contribution, {'contribution': c(8)})

        if self.player.id_in_group == 1:
            yield (pages.PunPage, dict(pun_2=1, pun_3=1, pun_4=3, pun_5=1, pun_6=0))
        elif self.player.id_in_group == 2:
            yield (pages.PunPage, dict(pun_1=1, pun_3=1, pun_4=3, pun_5=1, pun_6=0))
        elif self.player.id_in_group == 3:
            yield (pages.PunPage, dict(pun_1=1, pun_2=1, pun_4=3, pun_5=1, pun_6=0))
        elif self.player.id_in_group == 4:
            yield (pages.PunPage, dict(pun_1=1, pun_2=1, pun_3=3, pun_5=1, pun_6=0))
        elif self.player.id_in_group == 5:
            yield (pages.PunPage, dict(pun_1=1, pun_2=1, pun_3=1, pun_4=3, pun_6=0))
        elif self.player.id_in_group == 6:
            yield (pages.PunPage, dict(pun_1=1, pun_2=0, pun_3=1, pun_4=3, pun_5=1))

        # if self.player.id_in_group == 1:
        #     yield (pages.EmoPage_Sat, {'satis_2': c(5), 'satis_3': c(1), 'satis_4': c(5), 'satis_5': c(1), 'satis_6': c(3)})
        # elif self.player.id_in_group == 2:
        #     yield (pages.EmoPage_Sat, {'satis_1': c(2), 'satis_3': c(1), 'satis_4': c(5), 'satis_5': c(1), 'satis_6': c(3)})
        # elif self.player.id_in_group == 3:
        #     yield (pages.EmoPage_Sat, {'satis_1': c(2), 'satis_2': c(5), 'satis_4': c(5), 'satis_5': c(1), 'satis_6': c(3)})
        # elif self.player.id_in_group == 4:
        #     yield (pages.EmoPage_Sat, {'satis_1': c(2), 'satis_2': c(5), 'satis_3': c(1), 'satis_5': c(1), 'satis_6': c(3)})
        # elif self.player.id_in_group == 5:
        #     yield (pages.EmoPage_Sat, {'satis_1': c(2), 'satis_2': c(5), 'satis_3': c(1), 'satis_4': c(5), 'satis_6': c(3)})
        # elif self.player.id_in_group == 6:
        #     yield (pages.EmoPage_Sat, {'satis_1': c(2), 'satis_2': c(5), 'satis_3': c(1), 'satis_4': c(5), 'satis_5': c(2.5)})

        # if self.player.id_in_group == 1:
        #     yield (pages.Emoest_Ang, {'eang_2': c(5), 'eang_3': c(1), 'eang_4': c(5), 'eang_5': c(1), 'eang_6': c(3)})
        # elif self.player.id_in_group == 2:
        #     yield (pages.Emoest_Ang, {'eang_1': c(2), 'eang_3': c(1), 'eang_4': c(5), 'eang_5': c(1), 'eang_6': c(3)})
        # elif self.player.id_in_group == 3:
        #     yield (pages.Emoest_Ang, {'eang_1': c(2), 'eang_2': c(5), 'eang_4': c(5), 'eang_5': c(1), 'eang_6': c(3)})
        # elif self.player.id_in_group == 4:
        #     yield (pages.Emoest_Ang, {'eang_1': c(2), 'eang_2': c(5), 'eang_3': c(1), 'eang_5': c(1), 'eang_6': c(3)})
        # elif self.player.id_in_group == 5:
        #     yield (pages.Emoest_Ang, {'eang_1': c(2), 'eang_2': c(5), 'eang_3': c(1), 'eang_4': c(5), 'eang_6': c(3)})
        # elif self.player.id_in_group == 6:
        #     yield (pages.Emoest_Ang, {'eang_1': c(2), 'eang_2': c(5), 'eang_3': c(1), 'eang_4': c(5), 'eang_5': c(2.5)})
        #
        # if self.player.id_in_group == 1:
        #     yield (pages.Emoest_Sat, {'esat_2': c(5), 'esat_3': c(1), 'esat_4': c(5), 'esat_5': c(1), 'esat_6': c(3)})
        # elif self.player.id_in_group == 2:
        #     yield (pages.Emoest_Sat, {'esat_1': c(2), 'esat_3': c(1), 'esat_4': c(5), 'esat_5': c(1), 'esat_6': c(3)})
        # elif self.player.id_in_group == 3:
        #     yield (pages.Emoest_Sat, {'esat_1': c(2), 'esat_2': c(5), 'esat_4': c(5), 'esat_5': c(1), 'esat_6': c(3)})
        # elif self.player.id_in_group == 4:
        #     yield (pages.Emoest_Sat, {'esat_1': c(2), 'esat_2': c(5), 'esat_3': c(1), 'esat_5': c(1), 'esat_6': c(3)})
        # elif self.player.id_in_group == 5:
        #     yield (pages.Emoest_Sat, {'esat_1': c(2), 'esat_2': c(5), 'esat_3': c(1), 'esat_4': c(5), 'esat_6': c(3)})
        # elif self.player.id_in_group == 6:
        #     yield (pages.Emoest_Sat, {'esat_1': c(2), 'esat_2': c(5), 'esat_3': c(1), 'esat_4': c(5), 'esat_5': c(2.5)})

        if self.round_number == Constants.num_rounds:
            yield (pages.ResultsSummary)
