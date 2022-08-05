#!/usr/bin/env python

"""Tests for `zeeklog2pandas` package."""


import unittest

from .. zeeklog2pandas import read_zeek
import pandas as pd

class TestZeeklog2pandas(unittest.TestCase):
    """Tests for `zeeklog2pandas` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_read_zeek(self):
        """Test something."""
        df = read_zeek("tests/files/ssl.log")
        assert type(df) is pd.core.frame.DataFrame, "Fail to read zeekfile" 
