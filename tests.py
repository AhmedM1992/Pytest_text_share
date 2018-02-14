import pytest

from source_code import *
from languages_list import available_languages
from hamcrest import *


class TestCreatePaste:

    def setup(self):
        self.paste_text = 'this is my text'
        self.paste_title = 'This is my title'
        self.paste_name = 'My name'
        self.paste_private = 0
        self.paste_lang = 'Text'
        self.paste_expire = 10
        self.paste_url = create_paste(text=self.paste_text,
                                      title=self.paste_title,
                                      name=self.paste_name,
                                      private=self.paste_private,
                                      lang=self.paste_lang)
        self.paste_id = get_paste_id(self.paste_url)

    def test_create_paste(self):
        '''Verify that user can create a paste and get url'''
        assert_that(self.paste_url, contains_string('http://text-share.com/view/'))

    def test_get_paste_id(self):
        '''Verify that user can get paste id'''
        assert_that(self.paste_id, matches_regexp("[a-zA-Z0-9_]{8}"))

    def test_get_paste(self):
        '''Verify that user gets paste with required parameters'''
        paste = get_paste(self.paste_id)
        assert_that(paste['raw'], equal_to(self.paste_text))
        assert_that(paste['title'], equal_to(self.paste_title))
        assert_that(paste['name'], equal_to(self.paste_name))
        assert_that(paste['lang_code'], equal_to(self.paste_lang))


class TestLanguagesList:

    def setup(self):
        self.lang_url = get_list_available_languages()

    def test_available_languages(self):
        '''Verify that user can get list of available languages'''
        assert_that(self.lang_url, has_entries(available_languages))


class TestRandomPaste:

    def setup(self):
        self.random_paste = get_random_paste()

    def test_get_random_paste(self):
        PASTE_KEYS = ['created', 'hits', 'hits_updated', 'lang', 'lang_code',
                    'name', 'paste', 'pid', 'raw', 'snipurl', 'title', 'url']
        paste_keys = sorted(self.random_paste.keys())
        assert_that(paste_keys, is_(PASTE_KEYS))

    def test_get_random_paste_url(self):
        paste_url = self.random_paste['url']
        assert_that(paste_url, contains_string('http://text-share.com/view/'))
