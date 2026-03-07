# JEP Mapping to NIST AI Risk Management Framework

**Detailed Function-by-Function Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and the **NIST AI Risk Management Framework (AI RMF 1.0)** . The NIST AI RMF is organized into four functions: **GOVERN**, **MAP**, **MEASURE**, and **MANAGE**. Each function contains categories that are further broken down into specific actions and outcomes.

JEP directly addresses all four functions and their associated categories through its cryptographic primitives, audit trails, and governance features.

---

## 📊 NIST AI RMF Functions Overview

| Function | Focus Area | JEP Coverage |
|----------|------------|--------------|
| **GOVERN** | Culture, processes, and accountability | ✅ **Complete** - Four primitives, signatures, governance docs |
| **MAP** | Context, data, and risk identification | ✅ **Complete** - UUIDv7 traceability, resource mapping |
| **MEASURE** | Performance, trustworthiness, and impact | ✅ **Complete** - Risk levels, human oversight, fairness metrics |
| **MANAGE** | Risk treatment and incident response | ✅ **Complete** - Incident logs, audit trails, remediation |

---

## 🏛️ GOVERN: Govern the AI Lifecycle

### Overview

The GOVERN function establishes a culture of risk management and accountability throughout the AI lifecycle.

### Category GOVERN 1: Accountability Infrastructure

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **GOVERN 1.1** - Establish accountability policies | Four primitives (Judge/Delegate/Terminate/Verify) | `tracker.log_governance_framework()` | `verify-nist.py --govern-1.1` |
| **GOVERN 1.2** - Define roles and responsibilities | `actor_id` + `human_approver` fields | `receipt["actor_id"] = "loan-agent-v2"` | `verify-nist.py --govern-1.2` |
| **GOVERN 1.3** - Document governance structure | Governance receipts | `tracker.log_governance_structure()` | `verify-nist.py --govern-1.3` |

**Code Example:**
```python
from jep.us import NISTComplianceTracker

tracker = NISTComplianceTracker(organization="Example Bank")

# Document accountability framework (GOVERN 1.1)
governance = tracker.log_governance_framework(
    framework_version="2.0",
    effective_date="2026-01-01",
    accountability_principles=[
        {
            "principle": "clear_attribution",
            "implementation": "Every decision has attributable actor_id"
        },
        {
            "principle": "non_repudiation",
            "implementation": "Ed25519 signatures for all decisions"
        },
        {
            "principle": "human_oversight",
            "implementation": "All HIGH risk decisions require human approval"
        }
    ]
)

# Define roles (GOVERN 1.2)
roles = tracker.log_roles(
    roles=[
        {"role": "ai_developer", "responsibilities": ["model_development", "testing"]},
        {"role": "risk_officer", "responsibilities": ["risk_assessment", "approval"]},
        {"role": "compliance_officer", "responsibilities": ["audit", "reporting"]}
    ]
)
```

### Category GOVERN 2: Transparency

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **GOVERN 2.1** - Document AI system purpose | `purpose` field in receipts | `receipt["purpose"] = "credit_scoring"` | `verify-nist.py --govern-2.1` |
| **GOVERN 2.2** - Document limitations | `limitations` field | `receipt["limitations"] = ["requires_retraining"]` | `verify-nist.py --govern-2.2` |
| **GOVERN 2.3** - Document deployment context | `target_resource` field | `target_resource = "mortgage_applications/2026"` | `verify-nist.py --govern-2.3` |

**Code Example:**
```python
# Log decision with full transparency (GOVERN 2.1-2.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    purpose="mortgage_underwriting",
    limitations=[
        "Requires retraining every 6 months",
        "Less accurate for self-employed applicants"
    ],
    deployment_context={
        "environment": "production",
        "date": "2026-03-01",
        "version": "2.1.0"
    },
    target_resource="mortgage_applications/2026"
)
```

### Category GOVERN 3: Risk Management Policies

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **GOVERN 3.1** - Define risk tolerance | `risk_level` thresholds | `tracker.set_risk_thresholds()` | `verify-nist.py --govern-3.1` |
| **GOVERN 3.2** - Establish escalation paths | Approval workflow | `tracker.log_approval_workflow()` | `verify-nist.py --govern-3.2` |
| **GOVERN 3.3** - Document risk policies | Policy receipts | `tracker.log_risk_policy()` | `verify-nist.py --govern-3.3` |

**Code Example:**
```python
# Define risk thresholds (GOVERN 3.1)
tracker.set_risk_thresholds({
    "LOW": {"max_amount": 10000, "auto_approve": True},
    "MEDIUM": {"max_amount": 50000, "human_review": True},
    "HIGH": {"max_amount": 100000, "manager_approval": True},
    "CRITICAL": {"max_amount": float('inf'), "committee_approval": True}
})

# Log approval workflow (GOVERN 3.2)
workflow = tracker.log_approval_workflow(
    risk_level="HIGH",
    approvers=["loan_officer", "risk_manager"],
    conditions=["amount > 50000", "first_time_applicant"]
)
```

---

## 🗺️ MAP: Map the AI Lifecycle

### Overview

The MAP function establishes the context for AI risk management by understanding the AI system, its data, and its deployment context.

### Category MAP 1: Context

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MAP 1.1** - Identify AI system purpose | `operation` + `purpose` fields | `receipt["purpose"] = "credit_scoring"` | `verify-nist.py --map-1.1` |
| **MAP 1.2** - Identify stakeholders | `stakeholder` field | `receipt["stakeholders"] = ["borrower", "lender"]` | `verify-nist.py --map-1.2` |
| **MAP 1.3** - Identify deployment context | `deployment_context` field | `receipt["deployment_context"] = {...}` | `verify-nist.py --map-1.3` |

**Code Example:**
```python
# Map AI system context (MAP 1.1-1.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    purpose="mortgage_underwriting",
    stakeholders=[
        {"role": "borrower", "rights": ["access", "correction"]},
        {"role": "lender", "responsibilities": ["fair_lending"]},
        {"role": "regulator", "oversight": "CFPB"}
    ],
    deployment_context={
        "geography": "United States",
        "sector": "financial_services",
        "regulatory_framework": "ECOA, FCRA"
    }
)
```

### Category MAP 2: Data

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MAP 2.1** - Identify data sources | `data_sources` field | `receipt["data_sources"] = ["credit_bureau", "application"]` | `verify-nist.py --map-2.1` |
| **MAP 2.2** - Document data quality | `data_quality` metrics | `receipt["data_quality"] = {"completeness": 0.99}` | `verify-nist.py --map-2.2` |
| **MAP 2.3** - Document data governance | `data_governance` field | `receipt["data_governance"] = {...}` | `verify-nist.py --map-2.3` |

**Code Example:**
```python
# Map data context (MAP 2.1-2.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    data_sources=[
        {
            "source": "credit_bureau",
            "data_elements": ["credit_score", "payment_history"],
            "frequency": "monthly"
        },
        {
            "source": "application_form",
            "data_elements": ["income", "employment", "assets"],
            "verification": "document_review"
        }
    ],
    data_quality={
        "completeness": 0.98,
        "accuracy": 0.99,
        "timeliness": "real_time"
    },
    data_governance={
        "privacy_compliant": True,
        "retention_policy": "7_years",
        "consent_obtained": True
    }
)
```

### Category MAP 3: Risks

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MAP 3.1** - Identify potential risks | `risk_factors` field | `receipt["risk_factors"] = ["bias", "drift"]` | `verify-nist.py --map-3.1` |
| **MAP 3.2** - Assess risk likelihood | `risk_likelihood` field | `receipt["risk_likelihood"] = "MEDIUM"` | `verify-nist.py --map-3.2` |
| **MAP 3.3** - Document risk context | `risk_context` field | `receipt["risk_context"] = {...}` | `verify-nist.py --map-3.3` |

**Code Example:**
```python
# Map risks (MAP 3.1-3.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    risk_factors=[
        {
            "factor": "algorithmic_bias",
            "description": "Potential disparate impact on protected groups",
            "mitigation": "regular_bias_testing"
        },
        {
            "factor": "model_drift",
            "description": "Performance degradation over time",
            "mitigation": "continuous_monitoring"
        }
    ],
    risk_likelihood="MEDIUM",
    risk_impact="HIGH",
    risk_context={
        "regulatory_scrutiny": "CFPB oversight",
        "public_visibility": "consumer_facing",
        "stakeholder_concerns": ["fairness", "transparency"]
    }
)
```

---

## 📏 MEASURE: Measure the AI Lifecycle

### Overview

The MEASURE function assesses the trustworthiness and impact of AI systems through quantitative and qualitative metrics.

### Category MEASURE 1: Performance

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MEASURE 1.1** - Measure system performance | `performance_metrics` field | `receipt["performance"] = {"accuracy": 0.97}` | `verify-nist.py --measure-1.1` |
| **MEASURE 1.2** - Track performance over time | Performance trends | `tracker.log_performance_trends()` | `verify-nist.py --measure-1.2` |
| **MEASURE 1.3** - Document performance baselines | `baseline_metrics` field | `receipt["baseline"] = {...}` | `verify-nist.py --measure-1.3` |

**Code Example:**
```python
# Measure performance (MEASURE 1.1-1.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    performance_metrics={
        "accuracy": 0.97,
        "precision": 0.96,
        "recall": 0.98,
        "f1_score": 0.97,
        "auc_roc": 0.99
    },
    baseline_metrics={
        "accuracy": 0.95,
        "date": "2026-01-01",
        "version": "2.0.0"
    }
)

# Track trends (MEASURE 1.2)
trends = tracker.log_performance_trends(
    metric="accuracy",
    measurements=[
        {"date": "2026-01-01", "value": 0.95},
        {"date": "2026-02-01", "value": 0.96},
        {"date": "2026-03-01", "value": 0.97}
    ],
    trend_direction="improving",
    action_required=False
)
```

### Category MEASURE 2: Trustworthiness

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MEASURE 2.1** - Measure fairness | `fairness_metrics` field | `receipt["fairness"] = {"disparate_impact": 0.98}` | `verify-nist.py --measure-2.1` |
| **MEASURE 2.2** - Measure explainability | `explainability` field | `receipt["explanation"] = "Decision factors..."` | `verify-nist.py --measure-2.2` |
| **MEASURE 2.3** - Measure robustness | `robustness` field | `receipt["robustness"] = {"adversarial": "tested"}` | `verify-nist.py --measure-2.3` |
| **MEASURE 2.4** - Measure transparency | `transparency` field | JSON-LD machine-readable metadata | `verify-nist.py --measure-2.4` |

**Code Example:**
```python
# Measure trustworthiness (MEASURE 2.1-2.4)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    fairness_metrics={
        "disparate_impact": 0.98,
        "equal_opportunity": 0.97,
        "demographic_parity": 0.96,
        "test_date": "2026-03-01"
    },
    explanation={
        "credit_score": {"value": 750, "weight": 0.4, "threshold": ">=680"},
        "dti_ratio": {"value": 35, "weight": 0.3, "threshold": "<=40"},
        "employment": {"value": "5_years", "weight": 0.2, "threshold": ">=2"},
        "collateral": {"value": "property", "weight": 0.1, "ltv": 80}
    },
    robustness={
        "adversarial_testing": "passed",
        "edge_case_testing": "passed",
        "stress_testing": "passed",
        "last_test_date": "2026-02-15"
    }
)

# JSON-LD provides machine-readable transparency (MEASURE 2.4)
print(receipt["@context"])  # https://schema.org
print(receipt["@type"])      # FinancialProduct
```

### Category MEASURE 3: Human Oversight

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MEASURE 3.1** - Document human oversight | `human_approver` field | `receipt["human_approver"] = "supervisor-123"` | `verify-nist.py --measure-3.1` |
| **MEASURE 3.2** - Track oversight effectiveness | Oversight metrics | `tracker.log_oversight_metrics()` | `verify-nist.py --measure-3.2` |
| **MEASURE 3.3** - Document oversight decisions | `oversight_notes` field | `receipt["oversight_notes"] = "Verified documents"` | `verify-nist.py --measure-3.3` |

**Code Example:**
```python
# Log decision with human oversight (MEASURE 3.1-3.3)
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    amount=75000,  # HIGH risk
    human_approver="supervisor-456",
    oversight_notes="Verified income documents, LTV within limit",
    oversight_time=time.time()
)

# Track oversight metrics (MEASURE 3.2)
metrics = tracker.log_oversight_metrics(
    period_start="2026-01-01",
    period_end="2026-03-31",
    total_high_risk_decisions=150,
    human_approved=150,
    average_response_time_minutes=12.5,
    oversight_effectiveness="100%"
)
```

---

## 🔧 MANAGE: Manage the AI Lifecycle

### Overview

The MANAGE function addresses the treatment of AI risks through incident response, remediation, and continuous improvement.

### Category MANAGE 1: Incident Response

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MANAGE 1.1** - Establish incident response plan | Incident response docs | `tracker.log_incident_response_plan()` | `verify-nist.py --manage-1.1` |
| **MANAGE 1.2** - Document incidents | `incident` logs | `tracker.log_incident()` | `verify-nist.py --manage-1.2` |
| **MANAGE 1.3** - Track incident resolution | `incident_resolution` field | `receipt["resolution"] = {...}` | `verify-nist.py --manage-1.3` |
| **MANAGE 1.4** - Document lessons learned | `lessons_learned` field | `tracker.log_lessons_learned()` | `verify-nist.py --manage-1.4` |

**Code Example:**
```python
# Log incident (MANAGE 1.2-1.4)
incident = tracker.log_incident(
    incident_id="INC-2026-001",
    incident_type="model_drift",
    severity="MEDIUM",
    detection_time=time.time(),
    description="Credit scoring accuracy dropped from 97% to 92%",
    affected_systems=["credit_scoring_engine"],
    affected_decisions=1234,
    root_cause="data_drift in income verification feature",
    response_actions=[
        {"action": "alert_risk_team", "time": time.time()},
        {"action": "temporary_shadow_mode", "time": time.time() + 600},
        {"action": "model_retraining_initiated", "time": time.time() + 1800}
    ],
    resolution_time=time.time() + 86400,
    resolution_action="model_retrained_and_deployed",
    lessons_learned=[
        "Implement automated drift detection",
        "Add feature importance monitoring",
        "Update retraining schedule from monthly to weekly"
    ],
    reported_to_regulator=False,
    notified_affected=False
)
```

### Category MANAGE 2: Remediation

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **MANAGE 2.1** - Implement risk treatments | Risk mitigation logs | `tracker.log_risk_mitigation()` | `verify-nist.py --manage-2.1` |
| **MANAGE 2.2** - Track remediation effectiveness | Remediation metrics | `tracker.log_remediation_metrics()` | `verify-nist.py --manage-2.2` |
| **MANAGE 2.3** - Document changes | Change logs | `tracker.log_change()` | `verify-nist.py --manage-2.3` |

**Code Example:**
```python
# Log risk mitigation (MANAGE 2.1)
mitigation = tracker.log_risk_mitigation(
    risk_id="RISK-2026-001",
    mitigation_action="implemented_drift_detection",
    implementation_date=time.time(),
    effectiveness_metrics={
        "drift_detection_latency": "5 minutes",
        "false_positive_rate": 0.02,
        "coverage": "100%"
    },
    residual_risk="LOW",
    next_review_date=time.time() + 7776000  # 90 days
)

# Log change (MANAGE 2.3)
change = tracker.log_change(
    change_id="CHG-2026-001",
    change_type="model_update",
    description="Updated credit scoring model to version 2.2.0",
    reason="Address model drift",
    risk_assessment="LOW",
    approval_workflow=[
        {"approver": "data_scientist", "date": time.time()},
        {"approver": "risk_manager", "date": time.time() + 3600},
        {"approver": "change_board", "date": time.time() + 86400}
    ],
    implementation_date=time.time() + 172800,
    rollback_plan="Revert to version 2.1.0"
)
```

---

## ✅ Complete Verification

```bash
# Run complete NIST AI RMF verification
python tests/verify-nist.py --all

# Output:
# ========================================
# NIST AI RMF COMPLIANCE VERIFICATION
# ========================================
# 
# 📋 GOVERN Function
#   ✅ GOVERN 1.1: Accountability policies
#   ✅ GOVERN 1.2: Roles and responsibilities
#   ✅ GOVERN 1.3: Governance structure
#   ✅ GOVERN 2.1: System purpose
#   ✅ GOVERN 2.2: Limitations
#   ✅ GOVERN 2.3: Deployment context
#   ✅ GOVERN 3.1: Risk tolerance
#   ✅ GOVERN 3.2: Escalation paths
#   ✅ GOVERN 3.3: Risk policies
# 
# 📋 MAP Function
#   ✅ MAP 1.1: System purpose
#   ✅ MAP 1.2: Stakeholders
#   ✅ MAP 1.3: Deployment context
#   ✅ MAP 2.1: Data sources
#   ✅ MAP 2.2: Data quality
#   ✅ MAP 2.3: Data governance
#   ✅ MAP 3.1: Potential risks
#   ✅ MAP 3.2: Risk likelihood
#   ✅ MAP 3.3: Risk context
# 
# 📋 MEASURE Function
#   ✅ MEASURE 1.1: System performance
#   ✅ MEASURE 1.2: Performance trends
#   ✅ MEASURE 1.3: Performance baselines
#   ✅ MEASURE 2.1: Fairness
#   ✅ MEASURE 2.2: Explainability
#   ✅ MEASURE 2.3: Robustness
#   ✅ MEASURE 2.4: Transparency
#   ✅ MEASURE 3.1: Human oversight
#   ✅ MEASURE 3.2: Oversight effectiveness
#   ✅ MEASURE 3.3: Oversight decisions
# 
# 📋 MANAGE Function
#   ✅ MANAGE 1.1: Incident response plan
#   ✅ MANAGE 1.2: Incident documentation
#   ✅ MANAGE 1.3: Incident resolution
#   ✅ MANAGE 1.4: Lessons learned
#   ✅ MANAGE 2.1: Risk treatments
#   ✅ MANAGE 2.2: Remediation effectiveness
#   ✅ MANAGE 2.3: Change documentation
# 
# ========================================
# ✅ FULL NIST AI RMF COMPLIANCE VERIFIED
# ========================================
```

## 📁 Directory Contents

| File | Description |
|------|-------------|
| [README.md](README.md) | NIST AI RMF overview |
| [mapping.md](mapping.md) | This file - detailed mapping |
| [implementation/nist_tracker.py](implementation/nist_tracker.py) | Core NIST implementation |
| [examples/financial_services.py](examples/financial_services.py) | Financial services example |
| [examples/healthcare.py](examples/healthcare.py) | Healthcare example |
| [examples/critical_infrastructure.py](examples/critical_infrastructure.py) | Critical infrastructure example |

## 📬 Contact

For NIST-specific inquiries:
- **Email**: nist@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
