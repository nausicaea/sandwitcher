#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import random
import gzip

import click

from ._version import get_versions

@click.command()
@click.option("-c", "--capitalize", is_flag=True, help="Capitalize the first letter of each word.")
@click.option("-l", "--word-length", type=int, default=5, help="The length of words to use.")
@click.option("-n", "--word-number", type=int, default=2, help="The number of words to generate.")
@click.option("-d", "--word-delimiter", type=str, default=" ", help="The word delimiter.")
@click.option("-b", "--beginning", type=str, default="", help="The start of the password.")
@click.option("-f", "--first-interstitial", type=str, default="", help="The first insterstitial string.")
@click.option("-s", "--second-interstitial", type=str, default="", help="The second insterstitial string.")
@click.option("-e", "--end", type=str, default="", help="The end of the password.")
@click.version_option(get_versions()["version"])
def main(capitalize, word_length, word_number, word_delimiter, beginning, first_interstitial, second_interstitial, end):
    """
    Generate a sandwich password from random words.
    """
    project_dir = os.path.dirname(os.path.realpath(__file__))
    dict_file = os.path.join(project_dir, "dictionary.txt.gz")
    with gzip.open(dict_file, "rt") as f:
        word_selection = [word.strip() for word in f.readlines() if len(word.strip()) == word_length]

    if len(word_selection) > 0:
        final_words = list()
        for n in range(word_number):
            if capitalize:
                final_words.append(random.choice(word_selection).capitalize())
            else:
                final_words.append(random.choice(word_selection))

        print("{}{}{}{}{}".format(beginning, first_interstitial, word_delimiter.join(final_words), second_interstitial, end))
    else:
        print("No words of that length available.")


if __name__ == "__main__":
    main()

