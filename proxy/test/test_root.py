#!/usr/bin/python
"""Test the main method."""
from cherrypy.test import helper
from proxy.root import Root
from proxy.test.test_common import CommonCPSetup


class TestRootObject(helper.CPWebCase, CommonCPSetup):
    """Test the uploader policy service."""

    PORT = 8180
    HOST = '127.0.0.1'
    headers = [('Content-Type', 'application/json')]

    def test_root(self):
        """Test the root object."""
        root = Root()
        self.assertFalse(root is None)
