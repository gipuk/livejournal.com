from selenium.webdriver.common.by import By

from browser import Browser

class SettingsTab(Browser):
    locator_dictionary = {
    'menu_btn': (By.CSS_SELECTOR, '.s-nav-item__name'),
    'settings_tab': (By.CSS_SELECTOR,
                    '[href="https://www.livejournal.com/manage/settings"]'
    ),
    'display_tab': (By.CSS_SELECTOR, '[href*="settings/?cat=display"]'),
    'history_tab': (By.CSS_SELECTOR, '[href*="settings/?cat=history"]'),
    'mng_tab': (By.CSS_SELECTOR, '[href*="manage/logins.bml"]'),
    'language_dropdown': (By.ID, "LJ__Setting__Language_lang"),
    'save_btn': (By.CSS_SELECTOR, '[class="b-flatbutton"]'),
    'change_msg': (By.XPATH, """//div[contains(text(),
        'Du hast deine Account-Einstellungen erfolgreich geändert.')]"""),
    'end_activity_btn': (By.CSS_SELECTOR, '[name="submit"]')
    }


    def go_to_settings(self):
        self.hover_over(menu_btn)
        self.settings_tab.click()

    def go_to_display(self):
        self.display_tab.click()

    def go_to_history(self):
        self.history_tab.click()
        self.mng_tab.click()

    def change_language(self, language):
        self.select(self.language_dropdown, language)

    def save_settings(self):
        self.save_btn.click()

    def de_language_set(self):
        self.change_msg

    def closed_session(self):
        element = self.find_elements(By.CSS_SELECTOR, '[name="submit"]')
        count = len(element)
        self.end_activity_btn.click()
        len(element) == count-1
