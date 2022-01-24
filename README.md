# WebScriptingWiki

The repository contains 3 different projects that collaborate with each other for generating xlsx files that contains for each wikipedia word its description.


- Get_wikimedia: The script get_wikimedia.sh allows to download the dump of the latest version of wikipedia available for the selected language.
- WikiExtractor: WikiExtractor.py is a Python script that extracts and cleans text from a Wikipedia database backup dump. The script generetes as output a set of compressed file.
- WikiExtractorContent: The script WikiExtractContent.py decrompresses set of documents and generates a set of xlsx files. Each file contains set of words with its description.
