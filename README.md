# TensorFlow Probability Intersphinx

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

----

This repository contains a scapper that crawls the tensorflow probability 
documentation to generate a sphinx inventory file. For now, we will provide
the inventory corresponding to June 2020, but we plan to extend it to automatically
keep up to date with the latest TFP releases and also have different tagged inventory
files for the desired TFP version.

This code is completely inspired and mostly copied from [mrubik's](https://github.com/mr-ubik)
[tensorflow-intersphinx](https://github.com/mr-ubik/tensorflow-intersphinx).

## Intersphinx Usage

The github repository will house the `objects.inv` inventory file that intersphinx
needs to link the documentation with the TFP docs page, so there is no need to insall
or download the entire `tensorflow-probability-intersphinx` pacakge. It should be
enough to add the following entry to the `intersphinx_mapping` dictionary:

```python
"tensorflow_probability": (
    "https://www.tensorflow.org/probability/api_docs/python",
    "https://github.com/lucianopaz/tensorflow-probability-intersphinx/raw/master/objects.inv",
)
```

## Installation

At the moment, there repository is not exposed as a pip installable package. You must
copy or clone the repository, and run `pip install -r requirements.txt`.

## Usage

```bash
cd tfp_docs_scraper
scrapy crawl tfp_docs -o core_symbols.json
cd ..
python inventipy.py
```
