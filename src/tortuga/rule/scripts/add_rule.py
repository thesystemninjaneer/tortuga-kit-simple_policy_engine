#!/usr/bin/env python

# Copyright 2008-2018 Univa Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tortuga.exceptions.invalidCliRequest import InvalidCliRequest
from ..ruleCli import RuleCli
from ..ruleObjectFactory import RuleObjectFactory


class AddRuleCli(RuleCli):
    """
    Add rule command line interface.

    """
    def __init__(self):
        super().__init__()
        self.addOption('--desc-file', dest='descriptionFile',
                       help=_('Rule description file'))

    def runCommand(self):
        self.parseArgs(_("""
    add-rule --desc-file=DESCRIPTIONFILE

Description:
    The add-rule tool adds a rule to the Tortuga Simple Policy Engine.
"""))

        if not self.getOptions().descriptionFile:
            raise InvalidCliRequest(
                _('Missing required --desc-file argument'))

        parser = RuleObjectFactory().getParser()
        rule = parser.parse(self.getOptions().descriptionFile)
        self.get_rule_api().addRule(rule)


def main():
    AddRuleCli().run()
