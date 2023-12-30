import requests
import os
from dotenv import load_dotenv
import datetime


def main():
    # Load environment variables into programming variables.
    # load_dotenv()
    # bot_api_key = os.environ.get('BOT_API_KEY')
    # if not bot_api_key:
    #     raise RuntimeError('BOT_API_KEY var is not set!')
    # phone = os.environ.get('PHONE')
    # if not phone:
    #     raise RuntimeError('BOT_API_KEY var is not set!')
    bot_api_key = '4617880'
    phone = '972548325125'

    # Get today's day and month and convert the month into a string-month.
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    months_to_names = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    # Inject today's day and month into the url.
    link_url = f"""
        *{current_day}/{current_month} Musical History:*
        https://www.thisdayinmusic.com/on-this-day-in-music-{months_to_names[current_month - 1]}-{current_day}/
    """
    # Construct the callmebot API url with today's parameters.
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={link_url}&apikey={bot_api_key}"

    # Send the whatsapp message by sending a GET request for the API.
    response = requests.get(url)

    print(response, url)


if __name__ == '__main__':
    main()
