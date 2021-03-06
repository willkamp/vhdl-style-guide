import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

lFilePrefix = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'subtype_prefix_test_input.vhd'))
oFilePrefix = vhdlFile.vhdlFile(lFilePrefix)

class testRuleSubtypeMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = subtype.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [51]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = subtype.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [65]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_w_2_spaces(self):
        oRule = subtype.rule_003()
        oRule.spaces = 2
        dExpected = [51]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_with_default(self):
        oRule = subtype.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [7,8,10,11]
        oRule.analyze(oFilePrefix)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_with_multiple_override(self):
        oRule = subtype.rule_004()
        oRule.prefixes = ['st_', 'subt_']
        dExpected = [10,11]
        oRule.analyze(oFilePrefix)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_with_single_override(self):
        oRule = subtype.rule_004()
        oRule.prefixes = ['subt_']
        dExpected = [4,5,10,11]
        oRule.analyze(oFilePrefix)
        self.assertEqual(oRule.violations, dExpected)
