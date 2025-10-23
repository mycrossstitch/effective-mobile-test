from selenium.webdriver.common.by import By

class MainPageLocators():

    LOCATORS_FULL_MENU = {
        "logo_header": (By.CSS_SELECTOR, "#rec573054532 a[href='#main']"),
        "about": (By.CSS_SELECTOR, "#rec573054532 a[href='#about']"),
        "services": (By.CSS_SELECTOR, "#rec573054532 a[href='#moreinfo']"),
        "cases": (By.CSS_SELECTOR, "#rec573054532 a[href='#cases']"),
        "reviews": (By.CSS_SELECTOR, "#rec573054532 a[href='#Reviews']"),
        "contacts": (By.CSS_SELECTOR, "#rec573054532 a[href='#contacts']"),
        "specialists": (By.CSS_SELECTOR, "#rec573054532 a[href='#specialists']"),
    }

    LOCATORS_BURGER_MENU = {
        "burger_button" : (By.CSS_SELECTOR, "button.t-menuburger_first"),
        "logo_header": (By.CSS_SELECTOR, ".t450__container .t450__logo.t-heading"),
        "about": (By.CSS_SELECTOR, ".t450__container a[href='#about']"),
        "services": (By.CSS_SELECTOR, ".t450__container a[href='#moreinfo']"),
        "cases": (By.CSS_SELECTOR, ".t450__container a[href='#cases']"),
        "reviews": (By.CSS_SELECTOR, ".t450__container a[href='#Reviews']"),
        "contacts": (By.CSS_SELECTOR, ".t450__container a[href='#contacts']"),
    }

    LOCATORS_PAGE = {
        "cooperation": (By.CSS_SELECTOR, "#sbs-572374517-1680509731311 a[href='#contacts']"),
        "moreinfo": (By.CSS_SELECTOR, "#sbs-571993583-1680426641483 a[href='#moreinfo']"),
        "logo_footer": (By.CSS_SELECTOR, "#rec572471347 a[href='#main']"),
    }

    MENU_LINKS = {
        "logo_header": "/#main",
        "about": "/#about",
        "services": "/#moreinfo",
        "cases": "/#cases",
        "reviews": "/#Reviews",
        "contacts": "/#contacts",
        "specialists": "/#specialists",  # ⚠️ отсутствует на странице с бургер-меню (ожидаемое поведение/баг)
    }

    PAGE_LINKS = {
        "logo_footer": "/#main",
        "cooperation": "/#contacts",
        "moreinfo": "/#moreinfo",
    }

    LINKS = {**MENU_LINKS, **PAGE_LINKS}
