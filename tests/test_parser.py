from pcpartpicker.handler import Handler
from pcpartpicker.scraper import Scraper
from pcpartpicker.parser import Parser, tokenize, html_to_tokens
from pcpartpicker.mappings import part_classes

import asyncio
import unittest


class ParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = {}

        handler = Handler()
        loop = asyncio.get_event_loop()
        for region in handler._regions:
            scraper = Scraper(region)
            results = loop.run_until_complete(scraper.retrieve(handler._supported_parts))
            region_data = dict((x, (x, y)) for x, y in zip(handler._supported_parts, results))
            cls.test_data.update({region: region_data})

    def test_us_tokens(self):
        parser = Parser("us")
        data = self.test_data["us"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_uk_tokens(self):
        parser = Parser("uk")
        data = self.test_data["uk"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_nz_tokens(self):
        parser = Parser("nz")
        data = self.test_data["nz"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_it_tokens(self):
        parser = Parser("it")
        data = self.test_data["it"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_ie_tokens(self):
        parser = Parser("ie")
        data = self.test_data["ie"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_in_tokens(self):
        parser = Parser("in")
        data = self.test_data["in"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_se_tokens(self):
        parser = Parser("se")
        data = self.test_data["se"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_fr_tokens(self):
        parser = Parser("fr")
        data = self.test_data["fr"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_es_tokens(self):
        parser = Parser("es")
        data = self.test_data["es"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_de_tokens(self):
        parser = Parser("de")
        data = self.test_data["de"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_ca_tokens(self):
        parser = Parser("ca")
        data = self.test_data["ca"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_be_tokens(self):
        parser = Parser("be")
        data = self.test_data["be"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])

    def test_au_tokens(self):
        parser = Parser("au")
        data = self.test_data["au"]
        for part in data.keys():
            part_id, tags = html_to_tokens(data[part])
            for page in tags:
                for token in tokenize(part, page):
                    with self.subTest(part=part, token=token):
                        product = parser._parse_token(part, token)
                        self.assertIsInstance(product, part_classes[part])
