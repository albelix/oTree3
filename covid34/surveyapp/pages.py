from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class pageone(Page):
    form_model = "player"
    form_fields = ["decision",
                   "occupation",
                   "other",
                   "edu",
                   "ocu_type",
                   "other2",
                   "kindofjob",
                   "slaves",
                   "ifbeliv",
                   "youbeliv"]
    pass
class pagetwo(Page):
    form_model = "player"
    form_fields = ["fambeliv",
                   "neighbeliv",
                   "persbeliv",
                   "strangbeliv"]
    pass
class pagethree(Page):
    form_model = "player"
    form_fields = ['churchbeliv',
                   'armybeliv',
                   'pressbeliv',
                   'tvbeliv',
                   'policebeliv',
                   'courtbeliv',
                   'govbeliv',
                   'partybeliv',
                   'putinbeliv',
                   'parlbeliv',
                   'reggovbeliv',
                   'localgovbeliv',
                   'humcharbeliv']
    pass
class pagefour(Page):
    form_model='player'
    form_fields = ['putincov',
                   'govcov',
                   'parlcov',
                   'regcov',
                   'localcov',
                   'medcov',
                   'mediacov',
                   'internetcov',
                   'foreigncov',
                   'WHOcov']
    pass

class pagefive(Page):
    form_model = 'player'
    form_fields = ['if_free',
                   'if_risk',
                   'if_tru']
    pass

class pagesix(Page):
    form_model = 'player'
    form_fields = ['finrisk',
                   'freesportrisk',
                   'profrisk',
                   'helrisk',
                   'strangrisk']

class pageseven(Page):
    form_model = 'player'
    form_fields = ['preventagree',
                   'dangagree',
                   'accuragree',
                   'epidagree',
                   'realagree',
                   'immuagree',
                   'medhelpagree',
                   'govepidagree']
    pass
class pageeight(Page):
    form_model = 'player'
    form_fields = ['athome',
                   'restrict',
                   'workcov',
                   'other3',
                   'anysence',
                   'other4',
                   'whatimportant',
                   'other5',
                   'disadv',
                   'other6',
                   'income',
                   'spendings',
                   'ifnice']
    pass
class pagenine(Page):
    form_model = 'player'
    form_fields = ['fluvac', 'other7', 'covvac', 'other8', 'aboutvac', 'other9', 'illfriend', 'somedesease', 'other10', 'healthstuff', 'ifflubefore', 'other11']
    pass

class pageten(Page):
    form_model = 'player'
    form_fields = ['name',
                   'sex',
                   'age',
                   'famstats',
                   'housing',
                   'other12',
                   'kids',
                   'headsinhouse',
                   'dependent',
                   'incshare',
                   'finstat',
                   'relig',
                   'other13',
                   'polit',
                   'other14']
class Results(Page):
    pass


page_sequence = [pageone,
                  pagetwo,
                  pagethree,
                  pagefour,
                  pagefive,
                  pagesix,
                 pageseven,
                 pageeight,
                  pagenine,
                 pageten,
                  Results
]
