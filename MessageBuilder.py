from Scraper import DailyScraper


class DailyMessageBuilder:
    messages = []
    MAX_LEN = 767

    def __init__(self, daily_scraper: DailyScraper):
        self.daily_scraper = daily_scraper
        self.link = f"""*{daily_scraper.getCurrentDay()}/{daily_scraper.getCurrentMonth()} Musical History:*\nhttps://www.thisdayinmusic.com/on-this-day-in-music-{daily_scraper.getMonthsNamesList()[daily_scraper.getCurrentMonth() - 1]}-{daily_scraper.getCurrentDay()}/"""

    def build_intro_data_message(self):
        list_keys = list(self.daily_scraper.intro_data_dict.keys())

        def createMsg(keyIndex):
            self.messages.append(list_keys[keyIndex])
            for paragraph in self.daily_scraper.intro_data_dict[list_keys[keyIndex]]:
                pre_message = ''
                if keyIndex == 0:
                    pre_message += paragraph + '\n'
                else:
                    pre_message += paragraph
                message = ''
                for letter in pre_message:
                    if letter == '&':
                        message += 'and'
                    else:
                        message += letter
                self.messages.append(message)

        for i in range(len(list_keys)):
            createMsg(i)

    def build_main_data_message(self):
        for title in self.daily_scraper.main_data_dict:
            msg = title + ':\n'
            msg += self.daily_scraper.main_data_dict[title] + '\n \n'
            self.messages.append(msg)

    def filter_messages(self):
        def shorten(message: str):
            flag = False
            while len(message) >= self.MAX_LEN:
                reversed_message = message[::-1]
                index = reversed_message.find('.')
                message = message[:len(message) - index]
                flag = True
            if flag:
                return message + '.'
            else:
                return message

        for i, msg in enumerate(self.messages):
            if len(msg) >= self.MAX_LEN:
                print('before: ', self.messages[i])
                self.messages[i] = shorten(msg)
                print('after: ', self.messages[i])

        if len(self.messages) > 50:
            self.messages = self.messages[:51]
