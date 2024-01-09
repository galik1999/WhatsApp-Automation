from bs4 import BeautifulSoup
import requests
import datetime


class DailyScraper:
    _months_names_list = [
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

    def __init__(self):
        # Get today's day and month and convert the month into a string-month.
        self.main_data_dict = None
        self.intro_data_dict = {}
        self._current_month = datetime.datetime.now().month
        self._current_day = datetime.datetime.now().day

        def get_daily_html():
            music_hist_url = f"https://www.thisdayinmusic.com/on-this-day-in-music-{self._months_names_list[self._current_month - 1]}-{self._current_day}"
            scrape_response = requests.get(music_hist_url)
            return scrape_response.content

        self._soup = BeautifulSoup(get_daily_html(), 'html.parser')

    def get_first_part_from_data(self):
        titles = [title.get_text() for title in self._soup.find_all(['h2', 'h3'], limit=2)]
        musical_data = [data.get_text() for data in self._soup.find(id='mvp-content-main').find_all('p')]

        pre_index = musical_data.index(
            f'Looking for more artists born on this day?\nKeep scrolling for all of our {self._months_names_list[self._current_month - 1]} {self._current_day} birthdays.')
        musical_data.remove(
            f'Looking for more things that happened on this day in music?\nKeep scrolling for all of the headlines for {self._months_names_list[self._current_month - 1]} {self._current_day}.')
        musical_data.remove(
            f'Looking for more artists born on this day?\nKeep scrolling for all of our {self._months_names_list[self._current_month - 1]} {self._current_day} birthdays.')

        years_index = pre_index - 2

        self.intro_data_dict[titles[0]] = [data for index, data in enumerate(musical_data) if index < years_index]
        self.intro_data_dict[titles[1]] = [birthday for birthday in musical_data[years_index].split('\n')]

    def get_second_part_from_data(self):
        titles = [title.get_text(strip=True) for title in self._soup.findAll(class_='search-results-date')]
        titles = list(map(lambda t: t.replace(' ', '').replace('\n', ' '), titles))
        music_data = [data.get_text().replace('\n', '').strip() for data in
                      self._soup.findAll(class_='search-results-description')]

        self.main_data_dict = dict(zip(titles, music_data))


    def getMonthsNamesList(self):
        return self._months_names_list

    def getCurrentDay(self):
        return self._current_day

    def getCurrentMonth(self):
        return self._current_month

