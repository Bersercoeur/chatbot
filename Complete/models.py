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
import json
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'aexperiment'
    players_per_group = None
    num_rounds = 1


"""    with open('experimentNudge/products3.json', 'r', encoding='utf-8') as jsonfile:
        data=jsonfile.read()
        shoppinglist = json.loads(data)"""

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
    choice100 = models.StringField(blank=True)
    choice101 = models.StringField(blank=True)
    choice102 = models.StringField(blank=True)
    choice103 = models.StringField(blank=True)
    choice104 = models.StringField(blank=True)
    choice105 = models.StringField(blank=True)
    choice200 = models.StringField(blank=True)
    choice201 = models.StringField(blank=True)
    choice202 = models.StringField(blank=True)
    choice203 = models.StringField(blank=True)
    choice204 = models.StringField(blank=True)
    choice205 = models.StringField(blank=True)
    choice110 = models.StringField(blank=True)
    choice111 = models.StringField(blank=True)
    choice112 = models.StringField(blank=True)
    choice113 = models.StringField(blank=True)
    choice114 = models.StringField(blank=True)
    choice115 = models.StringField(blank=True)
    choice210 = models.StringField(blank=True)
    choice211 = models.StringField(blank=True)
    choice212 = models.StringField(blank=True)
    choice213 = models.StringField(blank=True)
    choice214 = models.StringField(blank=True)
    choice215 = models.StringField(blank=True)
    choice120 = models.StringField(blank=True)
    choice121 = models.StringField(blank=True)
    choice122 = models.StringField(blank=True)
    choice123 = models.StringField(blank=True)
    choice124 = models.StringField(blank=True)
    choice125 = models.StringField(blank=True)
    choice220 = models.StringField(blank=True)
    choice221 = models.StringField(blank=True)
    choice222 = models.StringField(blank=True)
    choice223 = models.StringField(blank=True)
    choice224 = models.StringField(blank=True)
    choice225 = models.StringField(blank=True)
    choice130 = models.StringField(blank=True)
    choice131 = models.StringField(blank=True)
    choice132 = models.StringField(blank=True)
    choice133 = models.StringField(blank=True)
    choice134 = models.StringField(blank=True)
    choice135 = models.StringField(blank=True)
    choice230 = models.StringField(blank=True)
    choice231 = models.StringField(blank=True)
    choice232 = models.StringField(blank=True)
    choice233 = models.StringField(blank=True)
    choice234 = models.StringField(blank=True)
    choice235 = models.StringField(blank=True)
    choice140 = models.StringField(blank=True)
    choice141 = models.StringField(blank=True)
    choice142 = models.StringField(blank=True)
    choice143 = models.StringField(blank=True)
    choice144 = models.StringField(blank=True)
    choice145 = models.StringField(blank=True)
    choice240 = models.StringField(blank=True)
    choice241 = models.StringField(blank=True)
    choice242 = models.StringField(blank=True)
    choice243 = models.StringField(blank=True)
    choice244 = models.StringField(blank=True)
    choice245 = models.StringField(blank=True)
    cheese = models.BooleanField(default=False)
    bread = models.BooleanField(default=False)
    soft_drink = models.BooleanField(default=False)
    chips = models.BooleanField(default=False)
    mustard = models.BooleanField(default=False)

    # record time
    # time0 = models.StringField(blank=True)
    # time1 = models.StringField(blank=True)
    # time2 = models.StringField(blank=True)
    # time3 = models.StringField(blank=True)
    # time4 = models.StringField(blank=True)
    time10 = models.StringField(blank=True)
    time11 = models.StringField(blank=True)
    time12 = models.StringField(blank=True)
    time13 = models.StringField(blank=True)
    time14 = models.StringField(blank=True)
    time20 = models.StringField(blank=True)
    time21 = models.StringField(blank=True)
    time22 = models.StringField(blank=True)
    time23 = models.StringField(blank=True)
    time24 = models.StringField(blank=True)
    product00 = models.StringField(blank=True)
    product01 = models.StringField(blank=True)
    product10 = models.StringField(blank=True)
    product11 = models.StringField(blank=True)
    product20 = models.StringField(blank=True)
    product21 = models.StringField(blank=True)
    product30 = models.StringField(blank=True)
    product31 = models.StringField(blank=True)
    product40 = models.StringField(blank=True)
    product41 = models.StringField(blank=True)

    #payoff
    #money = models.FloatField(blank=True)

    #email
    email = models.StringField(
        label="E-mail address:"
    )

    #feedback
feedback = models.LongStringField(
         blank=True,
         label = 'Feel free to leave a feedback!'
        )


    # #receiveOrder
    # receive_order = models.StringField(
    #     choices=["2 days delivery (+5,00 €)","Normal delivery (no fee)","Pick up yourself (no fee)"],
    #     widget=widgets.RadioSelect,
    #     label="How would you like to receive your order?")
    # transport_mode = models.StringField(
    #     choices=["Walking","Public transport","Bike","Car"],
    #     widget = widgets.RadioSelect,
    #     label = "If you choose to pick up your order, what mode of transportation would you use?")

    #surveys
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

    # EA
q1 = make_field("I try to separate trash for recycling on a regular basis.")
q2 = make_field("I prefer to use environmentally-friendly products.")
q3 = make_field("I want to use products that I currently have as long as possible.")
q4 = make_field("Global warming can be avoided by my pro-environmental behavior.")
q5 = make_field("Everyone's small daily efforts will lead to CO2 emission reduction.")
q6 = make_field(
    "Using daily necessities carefully over a long period will be effective in avoiding global warming.")
q7 = make_field("A lot of CO2 is emitted as a result of my activities.")
q8 = make_field("I am responsible for global warming.")
q9 = make_field("My life is one of the causes of infectious diseases, abnormal weather, and a decrease in species.")
q10 = make_field("It is not difficult to reduce CO2 emission in my daily life.")
q11 = make_field("It is not hard to change my life in order to avoid global warming.")
q12 = make_field("I can give up a few things I want in order to solve the global warming problem.")
q13 = make_field("There are many opportunities and ways in my life to avoid global warming.")
q14 = make_field("I can easily come up with what I can do for reducing CO2 emission.")
q15 = make_field("Everyone can select environmentally-friendly products or take action for reduction CO2 emission.")
q16 = make_field("Global warming is a critical issue.")
q17 = make_field("We have to take measures against global warming as soon as possible.")
q18 = make_field("It is not allowed to put off measures against global warming.")
q19 = make_field("CO2 emitted from factories and power plants are related to daily necessities around me.")
q20 = make_field(
    "My daily activities have impacts on CO2 emission due to resource use, product manufacturing, and product transportation.")
q21 = make_field("I myself have to make efforts to reduce CO2 emission associated with product manufacturing.")
q22 = make_field("I would like to know the amount of CO2 emission associated with my product and service use.")
q23 = make_field("Information on environmentally-conscious products should be disclosed more actively.")
q24 = make_field("More information is needed to take appropriate actions for reducing CO2 emission.")
q25 = make_field("I consider myself to be an environmentally aware person.")
q26 = make_field("I am reading through the questions attentively, choose strongly disagree for this question.")

    # EcoGuilt
    # eg1 = make_field2("Consume nonrenewable natural resources.")
    # eg2 = make_field2("Contribute to global warming.")
    # eg3 = make_field2("Know that you can do more to minimize the environmental impact that you have on the earth.")
    # eg4 = make_field2("Do not always recycle items like cans or paper.")
    # eg5 = make_field2("Waste natural resources.")

"""""
    # ShoppingMotives
m1 = make_field3("Going shopping is truly a joy.")
m2 = make_field3("I continue to shop, not because I have to, but because I want to.")
m3 = make_field3("Compared to other things I could have done, the time spent shopping is truly enjoyable.")
m4 = make_field3("I enjoy a shopping trip for its own sake, not just for the items I may have purchased.")
m5 = make_field3("I have a good time during a shopping trip because I am able to act on the “spur of the moment”.")
m6 = make_field3("While shopping, I am able to forget my problems.")
m7 = make_field3("During a shopping trip, I feel the excitement of the hunt.")
m8 = make_field3("Going shopping is not a very nice time out.")
m9 = make_field3("Going shopping truly feels like an escape.")
m10 = make_field3("While shopping, I feel a sense of adventure.")
m11 = make_field3("I enjoy being immersed in exciting new products.")
m12 = make_field3("I accomplish just what I want to on a shopping trip.")
m13 = make_field3("I am disappointed because I have to go to another store(s) to complete my shopping.")
m14 = make_field3("A good store visit to me is one that is quick.")
m15 = make_field3("While shopping, I find just the item(s) I am looking for.")
m16 = make_field3("I feel smart about my shopping decisions.")
m17 = make_field3("I can buy what I really need.")"""

""""
    # social norm
s1 = make_field3("Most people who are important to me think that I should talk with my friends and family about "
                    "sustainable consumption.")
s2 = make_field3("Most people whose opinion I value consider that I should talk with my friends and family about "
                    "sustainable consumption.")
s3 = make_field3("It is expected of me that I talk with my friends and family about sustainable consumption.")
s4 = make_field3(
    "Most people who are important to me have talked with their friends and family about sustainable consumption.")
s5 = make_field3(
    "Most people whose opinion I value have talked with their friends and family about sustainable consumption.")
s6 = make_field3(
    "Most people who are important to me had discussions with friends and family about sustainable consumption.")
s7 = make_field3("Most people whose opinion I value would approve of my talking with my friends and family about "
                    "sustainable consumption.")
s8 = make_field3("Most people who are important to me would endorse my talking with my friends and family about "
                    "sustainable consumption.")
s9 = make_field3("Most people who are important to me would support that I express to my friends and family my "
                    "opinions about sustainable consumption.")
s10 = make_field3(
    "A majority of people where you live have talked with their friends and family about sustainable consumption.")
s11 = make_field3("A majority of people in Europe have expressed to their friends and family their wishes to "
                    "practice sustainable consumption")
s12 = make_field3(
    "A majority of people where you live have engaged in friends and family discussions about sustainable consumption.")
s13 = make_field3(
    "A majority of people where you live approve of talking with friends and family about sustainable consumption.")
s14 = make_field3(
    "A majority of people where you live endorse discussions with friends and family about sustainable consumption.")
s15 = make_field3(
    "A majority of people where you live support that individuals express to their friends and family their "
    "wishes to practice sustainable consumption.")"""

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

    #mood
vas2 = models.IntegerField()

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
    
"""""
    #optional items buying intention
wnb = models.StringField(
    choices=['Yes.','No.'],
    widget=widgets.RadioSelect,
    label="" )
wnb2 = models.StringField(
    choices=['Yes.', 'No.'],
    widget=widgets.RadioSelect,
    label="")
wnb3 = models.StringField(
    choices=['Yes.', 'No.'],
    widget=widgets.RadioSelect,
    label="")
wnb4 = models.StringField(
    choices=['Yes.', 'No.'],
    widget=widgets.RadioSelect,
    label="")
wnb5 = models.StringField(
    choices=['Yes.', 'No.'],
    widget=widgets.RadioSelect,
    label="")

   #purchasenopurchase
chep1 = make_field("I bought the product because of the discount.")
chep2 = make_field("I bought the product because I just felt like it.")
chep3 = make_field("The environmental impact of the product influenced my decision to buy.")
chep4 = make_field("I would always buy products of the same category for a barbecue.")
chep5 = make_field("The decision to buy was spontaneous.")
chenp1 = make_field("I did not buy the product because they were too expensive.")
chenp2 = make_field("I did not buy the product because I just did not feel like it.")
chenp3 = make_field("I did not buy the product because I was worried about the environmental impact.")
chenp4 = make_field("I would never buy products of this category for a barbecue.")
chenp5 = make_field("I do not like products of this category.")
bp1 = make_field("I bought the product because of the discount.")
bp2 = make_field("I bought the product because I just felt like it.")
bp3 = make_field("The environmental impact of the product influenced my decision to buy.")
bp4 = make_field("I would always buy products of the same category for a barbecue.")
bp5 = make_field("The decision to buy was spontaneous.")
bnp1 = make_field("I did not buy the product because they were too expensive.")
bnp2 = make_field("I did not buy the product because I just did not feel like it.")
bnp3 = make_field("I did not buy the product because I was worried about the environmental impact.")
bnp4 = make_field("I would never buy products of this category for a barbecue.")
bnp5 = make_field("I do not like products of this category.")
sp1 = make_field("I bought the product because of the discount.")
sp2 = make_field("I bought the product because I just felt like it.")
sp3 = make_field("The environmental impact of the product influenced my decision to buy.")
sp4 = make_field("I would always buy products of the same category for a barbecue.")
sp5 = make_field("The decision to buy was spontaneous.")
snp1 = make_field("I did not buy the product because they were too expensive.")
snp2 = make_field("I did not buy the product because I just did not feel like it.")
snp3 = make_field("I did not buy the product because I was worried about the environmental impact.")
snp4 = make_field("I would never buy products of this category for a barbecue.")
snp5 = make_field("I do not like products of this category.")
chip1 = make_field("I bought the product because of the discount.")
chip2 = make_field("I bought the product because I just felt like it.")
chip3 = make_field("The environmental impact of the product influenced my decision to buy.")
chip4 = make_field("I would always buy products of the same category for a barbecue.")
chip5 = make_field("I swim across the pacific ocean to work everyday.")
chip6 = make_field("The decision to buy was spontaneous.")
chinp1 = make_field("I did not buy the product because they were too expensive.")
chinp2 = make_field("I did not buy the product because I just did not feel like it.")
chinp3 = make_field("I did not buy the product because I was worried about the environmental impact.")
chinp4 = make_field("I would never buy products of this category for a barbecue.")
chinp5 = make_field("I swim across the pacific ocean to work everyday.")
chinp6 = make_field("I do not like products of this category.")
mp1 = make_field("I bought the product because of the discount.")
mp2 = make_field("I bought the product because I just felt like it.")
mp3 = make_field("The environmental impact of the product influenced my decision to buy.")
mp4 = make_field("I would always buy products of the same category for a barbecue.")
mp5 = make_field("The decision to buy was spontaneous.")
mnp1 = make_field("I did not buy the product because they were too expensive.")
mnp2 = make_field("I did not buy the product because I just did not feel like it.")
mnp3 = make_field("I did not buy the product because I was worried about the environmental impact.")
mnp4 = make_field("I would never buy products of this category for a barbecue.")
mnp5 = make_field("I do not like products of this category.")"""