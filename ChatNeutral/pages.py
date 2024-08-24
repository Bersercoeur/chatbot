from ._builtin import Page, WaitPage
from .models import Constants
import csv

from ._builtin import Page, WaitPage
from .models import Constants


#surveys
class ChatSurvey(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['ib1', 'ib2', 'ib3', 'ib4', 'ib5', 'ib6', 'ib7', 'ib8', 'ib9', 'ib10']
        random.shuffle(form_fields)
        return form_fields


class Surveyh(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['q1', 'q3', 'q9', 'q11', 'q13', 'q15', 'q17', 'q19', 'q23']
        random.shuffle(form_fields)
        return form_fields


class Surveyi(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['q4', 'q6', 'q8', 'q14', 'q16', 'q20', 'q22', 'q24', 'q26']
        random.shuffle(form_fields)
        return form_fields


class Surveyj(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['q2', 'q5', 'q7', 'q10', 'q12', 'q18', 'q21', 'q25']
        random.shuffle(form_fields)
        return form_fields

class Surveyf(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['m2', 'm4', 'm6', 'm8', 'm10', 'm12', 'm14', 'm16', 'm17']
        random.shuffle(form_fields)
        return form_fields


class Surveyg(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['m1', 'm3', 'm5', 'm7', 'm9', 'm11', 'm13', 'm15']
        random.shuffle(form_fields)
        return form_fields


class Surveyc(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['s1', 's3', 's11', 's13', 's14']
        random.shuffle(form_fields)
        return form_fields


class Surveyd(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['s4', 's5', 's8', 's10', 's12']
        random.shuffle(form_fields)
        return form_fields

class Surveye(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['s2', 's6', 's7', 's9', 's15']
        random.shuffle(form_fields)
        return form_fields

class Start(Page):
    pass

class Debriefing(Page):
    pass

class GeneralInformation(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'educational_background', 'employment']

class Mood(Page):
    form_model = 'player'
    form_fields = ['vas2']


page_sequence = [Start, Surveyc, Surveyd, Surveye, Surveyf, Surveyg, Surveyh, Surveyi, Surveyj,  GeneralInformation, Debriefing]
