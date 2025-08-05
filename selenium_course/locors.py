# Файл locators.py с XPath-локаторами для страницы tracks на hyperskill.org

# Основные элементы страницы
TRACKS_PAGE_HEADER = ("xpath", "//h1[contains(text(), 'Tracks')]")
TRACKS_CONTAINER = ("xpath", "//div[@class='tracks']")
SEARCH_INPUT = ("xpath", "//input[@placeholder='Search tracks']")

# Элементы для каждого трека
TRACK_CARD = ("xpath", "//div[contains(@class, 'track-card')]")
TRACK_TITLE = ("xpath", "//div[contains(@class, 'track-card')]//h3")
TRACK_DESCRIPTION = ("xpath", "//div[contains(@class, 'track-card')]//p[contains(@class, 'description')]")
TRACK_DIFFICULTY = ("xpath", "//div[contains(@class, 'difficulty')]")
TRACK_TOPICS_COUNT = ("xpath", "//div[contains(text(), 'topics')]")
TRACK_PROGRESS_BAR = ("xpath", "//div[contains(@class, 'progress-bar')]")
TRACK_ENROLL_BUTTON = ("xpath", "//button[contains(text(), 'Enroll')]")

# Фильтры
FILTERS_SECTION = ("xpath", "//div[contains(@class, 'filters')]")
FILTER_BY_DIFFICULTY = ("xpath", "//div[contains(text(), 'Difficulty')]")
FILTER_BY_LANGUAGE = ("xpath", "//div[contains(text(), 'Language')]")
FILTER_EASY = ("xpath", "//label[contains(text(), 'Easy')]")
FILTER_MEDIUM = ("xpath", "//label[contains(text(), 'Medium')]")
FILTER_HARD = ("xpath", "//label[contains(text(), 'Hard')]")
FILTER_PYTHON = ("xpath", "//label[contains(text(), 'Python')]")
FILTER_JAVA = ("xpath", "//label[contains(text(), 'Java')]")
FILTER_KOTLIN = ("xpath", "//label[contains(text(), 'Kotlin')]")

# Пагинация
PAGINATION = ("xpath", "//ul[contains(@class, 'pagination')]")
NEXT_PAGE_BUTTON = ("xpath", "//li[contains(@class, 'next')]")
PREV_PAGE_BUTTON = ("xpath", "//li[contains(@class, 'previous')]")

# Дополнительные элементы
SORTING_DROPDOWN = ("xpath", "//select[@id='sorting']")
TRACK_COUNTER = ("xpath", "//div[contains(@class, 'tracks-count')]")
