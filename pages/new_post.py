from selenium.webdriver.common.by import By

from browser import Browser

class PostNewEntry(Browser):
    locator_dictionary = {
    'post_btn': (By.CSS_SELECTOR, 'span.s-header-item-post--short'),
    'last_draft_pop_up': (By.CSS_SELECTOR, '[class="_10h"]'),
    'close_icon': (By.CSS_SELECTOR, '[class="svgicon svgicon--close-rounded"]'),
    'title_field': (By.CSS_SELECTOR, '[class="_xk"]'),
    'text_field': (By.CSS_SELECTOR, '[class="public-DraftEditor-content"]'),
    'draft_msg': (By.CSS_SELECTOR, '[class="_wt"]'),
    'draft_btn': (By.CSS_SELECTOR, 'footer > div > nav > a:nth-child(1)'),
    'draft_tab': (By.CSS_SELECTOR, '[aria-label="Drafts"]'),
    'tune_and_publish_btn': (By.CSS_SELECTOR, 'div:nth-child(2) > button > span'),
    'publish_btn': (By.CSS_SELECTOR, 'footer > div > button > span'),
    'error_msg': (By.CSS_SELECTOR, '[class="_w5"]')
    }
    def go_to_post_new_entry_page(self):
        self.driver.execute_script("arguments[0].click();", self.post_btn)

    def close_popup(self):
        self.last_draft_pop_up
        self.close_icon.click()

    def fill_fields(self, title, text):
        self.title_field.send_keys(title)
        self.text_field.send_keys(text)
        self.draft_msg

    def go_to_draft(self):
        self.draft_btn.click()

    def saved_as_a_draft(self, title):
        self.draft_tab
        self.find_element(By.PARTIAL_LINK_TEXT, title)

    def published(self):
        self.tune_and_publish_btn.click()
        self.publish_btn.click()

    def error(self):
        self.error_msg
