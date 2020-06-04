"""Simple Spider for scraping the TensorFlow Probability Documentation."""

from typing import Dict, Iterable

import scrapy


class TensorFlowProbabilityDocSpider(scrapy.Spider):
    no_compat = True
    name = "tfp_docs"
    start_urls = ["https://www.tensorflow.org/probability/api_docs/python"]

    def parse(self, response):
        for uri in self._parse_symbols_index(response):
            if (self.no_compat) & ("compat" not in uri.split("/")):
                yield response.follow(uri, callback=self._parse_role)
            else:
                self.log("Skipping compat symbol.")

    @staticmethod
    def _parse_symbols_index(response) -> Iterable[str]:
        """
        Extract URI of each TensorFlow symbols.

        Args:
            response: PLACEHOLDER.

        Returns:
            Parsed URIs.

        """
        uri_query = "//code/parent::a/@href"
        symbols_uri = response.xpath(uri_query).getall()
        for uri in symbols_uri:
            yield uri

    @staticmethod
    def _parse_role(response: scrapy.http.response.Response) -> Dict[str, str]:
        """
        Extract Sphinx role from a crawled page.

        Valid roles:
            - function
            - class
            - module

        Args:
            response: PLACEHOLDER.

        Returns:
            String containing the role.

        """
        url = response.url

        if response.url == "https://www.tensorflow.org/probability/api_docs/python/tfp":
            return "package"

        name_query = "//h1/text()"
        name = response.xpath(name_query).get()

        class_selector = response.xpath("//h2/text()").get()

        if "Module" in name.split(": "):
            role = "module"
            name = name.split(": ")[-1]
        elif class_selector == "Class ":
            role = "class"
        else:
            # If the object is not a Module or a Class then it is a function.
            role = "function"

        return {"name": name, "url": url, "role": role}
