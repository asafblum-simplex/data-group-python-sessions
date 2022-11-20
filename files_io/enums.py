from enum import Enum
from typing import Dict


class Decision(Enum):
    FORBIDDEN = 'forbidden'
    NO_DECISION = 'no_decision'
    APPROVED = 'approved'


RuleDecision = Decision
ProcessorDecision = Decision
DeicisionMapping = Dict[Decision, str]

rule_decisions: DeicisionMapping = {
    RuleDecision.FORBIDDEN: "PROCESSOR_FORBIDDEN",
    RuleDecision.NO_DECISION: "NO_DECISION",
    RuleDecision.APPROVED: "APPROVED"
}

processor_decisions: DeicisionMapping = {
    ProcessorDecision.FORBIDDEN: "approved_processors",
    ProcessorDecision.NO_DECISION: "no_decision_processors",
    ProcessorDecision.APPROVED: "forbidden_processors"
}

processor_decision = Decision.NO_DECISION
rule_decision = Decision.FORBIDDEN


def test(rule_d: RuleDecision, proces_d: ProcessorDecision):
    return rule_d == proces_d
