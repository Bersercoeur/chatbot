from ._builtin import Page, WaitPage
import csv

from ._builtin import Page, WaitPage


#surveys

class Surveyz(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['h1', 'h2', 'h3', 'c1', 'wt1']
        random.shuffle(form_fields)
        return form_fields


class Surveya(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['m1', 'm2', 'm3', 'm4', 'm5']
        random.shuffle(form_fields)
        return form_fields

class Surveyb(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['s1', 's2', 's3', 's4', 's5']
        random.shuffle(form_fields)
        return form_fields
    
class Surveyc(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['pv1', 'pv2', 'pv3', 'pv4', 'pv5']
        random.shuffle(form_fields)
        return form_fields
    
class Surveyd(Page):
    form_model = 'player'

    def get_form_fields(self):
        import random
        form_fields = ['wtb1', 'wtb2', 'wtb3', 'wtb4', 'wtb5']
        random.shuffle(form_fields)
        return form_fields

class Intro(Page):
    pass

class Debriefing(Page):
    pass

class GeneralInformation(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'educational_background', 'employment']

class Feedback(Page):
    pass

class Scenario(Page):
    pass

class Start(Page):
    pass

class chat(Page):
    form_model = 'player'
    form_fields = ['chatLog']
    timeout_seconds = 600


page_sequence = [Intro, Start, GeneralInformation, Surveyz, Scenario, chat, Surveya,Surveyb, Surveyd, Surveyc, Feedback, Debriefing]
