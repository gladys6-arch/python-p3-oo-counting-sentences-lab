#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split on ., ?, ! and filter out empty items
        parts = [segment for segment in
                 __import__('re').split(r'[.?!]', self.value)
                 if segment.strip()]
        return len(parts)

