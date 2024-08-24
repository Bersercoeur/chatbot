from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field(label):
    return models.IntegerField(
        choices=[5,4,3,2,1],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field2(label):
    return models.IntegerField(
        choices=[6,5,4,3,2,1],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field3(label):
    return models.IntegerField(
        choices=[7,6,5,4,3,2,1],
        label=label,
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    #IBT - 2,4-6 should be reverse coded
    ib1 = make_field("I usually only buy things that I intended to buy.")
    ib2 = make_field("If I buy something, I usually do that spontaneously.")
    ib3 = make_field("Most of my purchases are planned in advance.")
    ib4 = make_field("I only buy things that I really need.")
    ib5 = make_field("It is not my style to just buy things.")
    ib6 = make_field("I am used to buying things 'on the spot'.")
    ib7 = make_field("I often buy things without thinking.")
    ib8 = make_field("I sometimes cannot suppress the feeling of wanting to buy something.")
    ib9 = make_field("I find it difficult to pass up a bargain.")
    ib10 = make_field("I am a bit reckless in buying things.")

    #EcoGuilt
    eg1 = make_field2("Consume nonrenewable natural resources.")
    eg2 = make_field2("Contribute to global warming.")
    eg3 = make_field2("Know that you can do more to minimize the environmental impact that you have on the earth.")
    eg4 = make_field2("Do not always recycle items like cans or paper.")
    eg5 = make_field2("Waste natural resources.")

    #comprehension questions
    question1 = models.StringField(
        choices=['True','False'],
        widget=widgets.RadioSelectHorizontal,
        label="1. You can buy more than one item per product category.")
    question2 = models.StringField(
        choices=['You can choose to buy them if you want.',
                 'You have to buy them.'],
        widget=widgets.RadioSelectHorizontal,
        label="2. Which statement is true about the products not on the shopping list?")
    question3 = models.StringField(
        choices=['The tastiest items','The most expensive items'],
        widget=widgets.RadioSelectHorizontal,
        label="3. Which items should you choose if you want a chance to earn a bonus of €0.5?")
    question4= models.StringField(
        choices=['True','False'],
        widget=widgets.RadioSelectHorizontal,
        label="4. You have a chance to earn a bonus of €0.5 if you purchase a tasty option for any of the products. ")
    question5 = models.StringField(
        choices=['True','False'],
        widget=widgets.RadioSelectHorizontal,
        label="5. I can choose to not buy anything if I want to.")
    question6 = models.StringField(
        choices=['True','False'],
        widget=widgets.RadioSelectHorizontal,
        label="6. I get a better chance at the bonus by buying as many products as possible.")

    #mood
    vas = models.IntegerField()