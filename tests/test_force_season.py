#!/usr/bin/env python

"""Test ability to set the season number
"""

from functional_runner import run_tvnamer, verify_out_data
from helpers import attr


@attr("functional")
def test_season():
    """Test --season argument
    """

    conf = """
    {"always_rename": true,
    "select_first": true}
    """

    out_data = run_tvnamer(
        with_files = ['Scrubs.s01e01.avi', 'Scrubs.s03e02.avi'],
        with_config = conf,
        with_flags = ["--season", '2'],
        with_input = "")

    expected_files = ['Scrubs - [02x01] - My Overkill.avi', 'Scrubs - [02x02] - My Nightingale.avi']

    verify_out_data(out_data, expected_files)
