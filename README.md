#User Engagement Chatbot Experiment
This repository contains a user engagement chatbot experiment built using oTree. The experiment involves participants interacting with a chatbot that uses either a neutral or humorous tone. The aim is to study user satisfaction, willingness to buy, and perceived value of a snack and drink menu based on the chatbot's language style.

##System Prompt
The system randomizes participants to interact with one of two chatbot versions: neutral or humorous. Each version has predefined responses tailored to the study's objectives. You can adjust the chatbot's responses and behavior by modifying the prompts and conversation flow within the code.

##API Key
While this project does not require an external API key (such as OpenAI's API) as it does not rely on external NLP services, all chatbot logic and responses are handled within oTree.

##Data Collection
The experiment saves data on participants' interactions with the chatbot, including chat logs and responses to survey questions. This data is stored in the database and can be exported for analysis through oTree's data export features.

##Variables Collected
Chatbot Version: Neutral or humorous version used.
Chat Logs: All participant interactions with the chatbot.
Survey Responses: Includes mood, satisfaction, willingness to buy, perceived value, and demographic data.
Menu Selection: Whether the participant opted for the snack and drink menu (binary variable).
Customization
You can modify the chatbot's responses by editing the conversation flow in the HTML and JavaScript files. The chatbot’s behavior can be adjusted by editing the scripts provided.

##Citation
Please consider citing this project if you find it useful in your research:

Faijean, P., (2024). User Engagement Chatbot Experiment. https://github.com/Bersercoeur/chatbot.git
As part of oTree's installation agreement, be sure to cite their paper:

Chen, D.L., Schonger, M., Wickens, C., 2016. oTree - An open-source platform for laboratory, online and field experiments. Journal of Behavioral and Experimental Finance, vol 9: 88-97.
License
This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgements
This project was inspired by the work of McKenna, C., (2023). oTree GPT. Special thanks to the oTree community for their support and contributions.