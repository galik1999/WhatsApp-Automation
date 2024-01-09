import requests
import os
from dotenv import load_dotenv
from Scraper import DailyScraper
from MessageBuilder import DailyMessageBuilder
from MessageTranslator import MsgTranslator


# Load environment variables into programming variables.
load_dotenv()
bot_api_key = os.environ.get('BOT_API_KEY')
if not bot_api_key:
    raise RuntimeError('BOT_API_KEY var is not set!')
phone = os.environ.get('PHONE')
if not phone:
    raise RuntimeError('BOT_API_KEY var is not set!')

dailyScraper = DailyScraper()
dailyScraper.get_first_part_from_data()
dailyScraper.get_second_part_from_data()
msgBuilder = DailyMessageBuilder(dailyScraper)
msgBuilder.build_intro_data_message()
msgBuilder.build_main_data_message()
MsgTranslator().translate_messages(msgBuilder)
msgBuilder.filter_messages()

print("The length of the messages which are sent to the user:", len(msgBuilder.messages))
print(dailyScraper.intro_data_dict.keys())
for msg in msgBuilder.messages:
    print(len(msg) > msgBuilder.MAX_LEN)

for msg in msgBuilder.messages:
    api_url = f"""https://api.callmebot.com/whatsapp.php?phone={phone}&text={msg}&apikey={bot_api_key}"""
    # Send the whatsapp message by sending a GET request for the API.
    response = requests.get(api_url)
    print(response, api_url)
