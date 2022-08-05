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
        """Read zeek file"""
        df = read_zeek("tests/files/ssl.log")
        assert type(df) is pd.core.frame.DataFrame, "Fail to read zeekfile"
    
    def test_001_read_zeek_with_usecols(self):
        """Test usecols"""
        df = read_zeek("tests/files/ssl.log", usecols=['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p'])
        assert len(df.keys()) == 6, "Fail to use usecols"

    def test_002_read_zeek_in_chunks(self):
        df = read_zeek("tests/files/ssl.log", chunksize=10)
        print(type(df))
