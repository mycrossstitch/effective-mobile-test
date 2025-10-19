from selenium.webdriver.common.by import By

class MainPageLocators():

    LOCATORS_FULL_MENU = {
        "logo_header": (By.XPATH, "(//a[@href='#main' and text()='Effective Mobile'])[1]"),
        "logo_footer": (By.XPATH, "(//a[@href='#main' and text()='Effective Mobile'])[2]"),
        "about": (By.XPATH, "//a[@href='#about' and text()='[ О нас ]']"),
        "services": (By.XPATH, "//a[@href='#moreinfo' and text()='[ Услуги ]']"),
        "cases": (By.XPATH, "//a[@href='#cases' and text()='[ Проекты ]']"),
        "Reviews": (By.XPATH, "//a[@href='#Reviews' and text()='[ Отзывы ]']"),
        "contacts": (By.XPATH, "//a[@href='#contacts' and text()='[ Контакты ]']"),
        "specialists": (By.XPATH, "//a[@href='#specialists']"),
        "cooperation": (By.XPATH, "(//a[@href='#contacts'])[3]"),
        "moreinfo": (By.XPATH, "//a[@href='#moreinfo' and text()='Подробнее']")
    }

    LOCATORS_BURGER_MENU = {
        "burger_button" : (By.CSS_SELECTOR, "button.t-menuburger.t-menuburger_first"),
        "container" : (By.CLASS_NAME, "t450__container"),
        "logo_header": (By.CSS_SELECTOR, ".t450__logo.t-heading.t-heading_xs"),
        "about": (By.CSS_SELECTOR, "a.t-menu__link-item[href='#about']"),
        "services": (By.CSS_SELECTOR, "a.t-menu__link-item[href='#moreinfo']"),
        "cases": (By.CSS_SELECTOR, "a.t-menu__link-item[href='#cases']"),
        "Reviews": (By.CSS_SELECTOR, "a.t-menu__link-item[href='#Reviews']"),
        "contacts": (By.CSS_SELECTOR, "a.t-menu__link-item[href='#contacts']"),
        "specialists": (By.XPATH, "//a[@href='#specialists']"),
        "cooperation": (By.XPATH, "(//a[@href='#contacts'])[3]"),
        "moreinfo": (By.XPATH, "//a[@href='#moreinfo' and text()='Подробнее']"),
        "logo_footer": (By.XPATH, "(//a[@href='#main' and text()='Effective Mobile'])[2]"),

    }

    MENU_LINKS = {

        "logo_header": "/#main",
        "about": "/#about",
        "services": "/#moreinfo",
        "cases": "/#cases",
        "Reviews": "/#Reviews",
        "contacts": "/#contacts",

    }

    PAGE_LINKS = {
        "logo_footer": "/#main",
        "specialists": "/#specialists",
        "cooperation": "/#contacts",
        "moreinfo": "/#moreinfo",
    }

    LINKS = {**MENU_LINKS, **PAGE_LINKS}