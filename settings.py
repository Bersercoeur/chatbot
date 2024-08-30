from os import environ


SESSION_CONFIGS = [
    dict(
        name="Complete",
        num_demo_participants=4,
        num_rounds=8,
        app_sequence=['Complete']
    )
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []


# rooms
ROOMS = [
    dict(
        name='ChatbotStudy',
        display_name='Chatbot Study',
        participant_label_file='_rooms/ChatbotStudy.txt',
        use_secure_urls=False
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'g9s=z=%@6fhf=vw^(x(-yhadi@3yk^hep#uts87^w@)&0m-$*f'

INSTALLED_APPS = ['otree']
