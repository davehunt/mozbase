#!/usr/bin/env python

import os
from time import sleep
import unittest

import mozrunnertest


class MozrunnerStartTestCase(mozrunnertest.MozrunnerTestCase):

    def test_start_process(self):
        """Start the process and test properties"""
        self.runner.start()

        self.assertTrue(self.runner.is_running())
        self.assertIsNotNone(self.runner.process_handler)

    def test_start_process_called_twice(self):
        """Start the process twice and test that first process is gone"""
        pid1 = self.runner.start()
        # Bug 925480
        # Make a copy until mozprocess can kill a specific process
        process_handler = self.runner.process_handler

        pid2 = self.runner.start()

        try:
            self.assertNotIn(process_handler.wait(1), [None, 0])
        finally:
            process_handler.kill()

    @unittest.skip("Bug 962495 - Mozrunner fails in handling timeout parameter")
    def test_start_with_timeout(self):
        """Start the process and set a timeout"""
        self.runner.start(timeout=2)
        sleep(5)

        self.assertFalse(self.runner.is_running())

    @unittest.skip("Bug 962495 - Mozrunner fails in handling outputTimeout parameter")
    def test_start_with_outputTimeout(self):
        """Start the process and set a timeout"""
        self.runner.start(outputTimeout=2)
        sleep(5)

        self.assertFalse(self.runner.is_running())
