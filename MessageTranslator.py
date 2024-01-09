from MessageBuilder import DailyMessageBuilder
import translators as ts


class MsgTranslator:
    def translate_messages(self, msgBuilder: DailyMessageBuilder):
        key = f"BORN ON {str.upper(msgBuilder.daily_scraper.getMonthsNamesList()[msgBuilder.daily_scraper.getCurrentMonth() - 1])} {msgBuilder.daily_scraper.getCurrentDay()}:"
        birthdays_index = msgBuilder.messages.index(key)
        print(birthdays_index)
        birthdays_count = len(msgBuilder.daily_scraper.intro_data_dict[key])
        print(birthdays_count)
        for i, msg in enumerate(msgBuilder.messages):
            if not birthdays_index < i <= birthdays_index + birthdays_count:
                msgBuilder.messages[i] = ts.translate_text(msg, from_language='en', to_language='ru') + '\n'
        msgBuilder.messages[birthdays_index + birthdays_count] += '\n'
