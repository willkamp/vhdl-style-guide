
from vsg.rules.architecture import architecture_rule


class rule_007(architecture_rule):
    '''Architecture rule 007 checks for spaces at the beginning of the line for the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                self._check_indent(oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])