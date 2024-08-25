from otree.api import (
    models,
    widgets,
    Currency as c,
)
import json
import random

author = 'Pauline'

doc = """
Your app description
"""


def make_field3(label):
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

def make_field(label):
    return models.IntegerField(
        choices=[7,6,5,4,3,2,1],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_currency_field(label):
    return models.CurrencyField(
        label=label,
        min=0,  # Optional: Set a minimum value, e.g., no negative amounts
        max=100,  # Optional: Set a maximum value
        widget=widgets.Input(attrs={'placeholder': '€0.00'}),
    )


    #feedback
feedback = models.LongStringField(
         blank=True,
         label = 'Feel free to leave a feedback!'
        )



    #surveys pre scenario
    #control variable: humour
h1 = make_field("I prefer situations where people are free to express their sense of humour")
h2 = make_field("I enjoy being with people who tell jokes or funny stories.")
h3 = make_field("I often read jokes and funny stories.")

    #survey pre scenario - survey z
    #control on importance to buy a menu
c1 = make_field("If you go to the cinema, how important is it for you to get a snack (popcorn or other) and a drink?")

#WTB for menu
wt1 = make_currency_field("How much do you expect to pay for a snack and drink menu at the cinema?")

#survey post experiment

#Manipulation check - surveya
m1 = make_field("The response of chatbot was humorous.")
m2 = make_field("The response of chatbot was funny.")
m3 = make_field("The response of chatbot was playfulness.")
m4 = make_field("The response of chatbot was amusing.")
m5 = make_field("The response of chatbot made me smile.")

#satisfaction - surveyb
s1 = make_field("I am satisfied with the chatbot service agent.")
s2 = make_field("I am content with the chatbot service agent.")
s3 = make_field("The chatbot service agent did a good job.")
s4 = make_field("The chatbot service agent did what I expected.")
s5 = make_field("I am happy with the chatbot service agent.")

#perceived value - surveyc 
pv1 = make_field("The snack and drink menu is:")
pv2 = make_field("At the price shown the snack and drink menu is:")
pv3 = make_field("The snack and drink menu is considered to be a good buy.")
pv4 = make_field("The snack and drink menu appears to be a bargain.")
pv5 = make_field("The price shown for the snack and drink menu is:")

#WTB - survey d
wtb1 = make_field("The likelihood to purchase a snack and drink menu with my cinema ticket is:")
wtb5 = make_field("The probability that I would consider buying a menu with my cinema ticket is:")
wtb3 = make_field("My willingness to buy the snack and drink menu is:")
wtb4 = make_field("If I were going to buy this menu, I would consider buying it at the price shown.")
wtb5 = make_field("How much would you be willing to pay for the snack and drink menu presented in the previous section?")

    #demographic data
age = models.StringField(
choices=["18-24", "25-34","35-44","45-54","55 and over", "Prefer not to say"],
label="Please select your age")
gender = models.StringField(
    choices=["Male", "Female","Other","Prefer not to say"],
    widget=widgets.RadioSelectHorizontal,
    label="What is your gender?")
educational_background = models.StringField(
    choices=["High school diploma/A-levels", "Bachelor's degree", "Master's degree", "Doctorate", "Other"],
    widget=widgets.RadioSelect,
    label="What is your highest academic level?")
employment = models.StringField(
    choices=["Employed full-time (40+ hours a week)", "Employed part-time (less than 40 hours a week)", "Student",
                "Unemployed", "Other"],
    widget=widgets.RadioSelect,
    label="What is your current employment status?")

