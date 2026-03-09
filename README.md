# 🇺🇸 JEP US Solutions

**AI Accountability for the American Market**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-blue)](https://www.nist.gov/itl/ai-risk-management-framework)

## 📋 Overview

This repository provides a complete **Judgment Event Protocol (JEP)** implementation aligned with US AI governance frameworks, including the NIST AI Risk Management Framework, state regulations, and federal guidelines.

### Why JEP for the US?

| Challenge | JEP Solution |
|-----------|-------------|
| **NIST AI RMF Compliance** | Direct mapping to all 4 functions and 9 categories |
| **Multi-State Regulations** | One codebase for CCPA, Colorado AI Act, VCDPA |
| **Federal Guidance** | Alignment with AI Bill of Rights and FTC guidelines |
| **Audit Readiness** | Cryptographic proof of compliance |
| **Cost Efficiency** | Free, open-source, 3-line integration |

## 🎯 Covered Frameworks

| Framework | Issuer | JEP Solution | Status |
|-----------|--------|--------------|--------|
| **NIST AI Risk Management Framework** | NIST | [NIST AI RMF →](/nist-ai-rmf) | ✅ **Complete** |
| **CCPA/CPRA (California)** | State of CA | [California Compliance →](/state-regulations/california.md) | ✅ **Complete** |
| **Colorado AI Act** | State of CO | [Colorado Compliance →](/state-regulations/colorado.md) | ✅ **Complete** |
| **VCDPA (Virginia)** | State of VA | [Virginia Compliance →](/state-regulations/virginia.md) | ✅ **Complete** |
| **AI Bill of Rights** | White House | [Federal Guidelines →](/federal/ai-bill-of-rights.md) | ✅ **Complete** |
| **FTC AI Guidelines** | FTC | [FTC Compliance →](/federal/ftc.md) | ✅ **Complete** |

## 🔍 Why JEP?

### ✅ **NIST AI RMF Alignment**

Direct mapping to all four NIST functions:

| NIST Function | JEP Implementation | Verification |
|---------------|-------------------|--------------|
| **GOVERN** | Four primitives (Judge/Delegate/Terminate/Verify) | `verify-nist.py --govern` |
| **MAP** | UUIDv7 traceability + PII protection | `verify-nist.py --map` |
| **MEASURE** | Risk levels + human oversight | `verify-nist.py --measure` |
| **MANAGE** | Incident response + audit trails | `verify-nist.py --manage` |

### ✅ **State-by-State Compliance**

| State | Regulation | JEP Feature |
|-------|------------|-------------|
| **California** | CCPA/CPRA | Consumer rights, opt-out, deletion |
| **Colorado** | Colorado AI Act | Algorithmic impact assessments |
| **Virginia** | VCDPA | Data protection assessments |

### ✅ **Cryptographic Guarantees**

```python
# Every decision is signed and cannot be repudiated
signature = tracker.sign_payload(decision_data)
is_valid = tracker.verify_payload(decision_data, signature)  # False if tampered
```

### ✅ **Privacy by Design**

```json
{
  "evidence_snapshot": {
    "privacy_check": "No PII detected in audit trail",
    "comment": "Only metadata hashes are stored"
  }
}
```

## 🏢 Industry Use Cases

| Industry | Regulator | Example | Solution |
|----------|-----------|---------|----------|
| **Financial Services** | CFPB, SEC | Fair lending compliance | [View →](/nist-ai-rmf/examples/financial_services.py) |
| **Healthcare** | HHS, FDA | Clinical decision support | [View →](/nist-ai-rmf/examples/healthcare.py) |
| **Critical Infrastructure** | CISA | Infrastructure monitoring | [View →](/nist-ai-rmf/examples/critical_infrastructure.py) |
| **Consumer Services** | FTC | Algorithmic transparency | [View →](/nist-ai-rmf/examples/consumer_services.py) |

## 🚀 Quick Start

### Installation

```bash
pip install jep-us
```

### 3-Line Integration

```python
from jep.us import NISTComplianceTracker

# Initialize for your organization
tracker = NISTComplianceTracker(
    organization="Your Company",
    sector="financial"  # or healthcare, critical-infrastructure, consumer
)

# Log any AI decision with full NIST compliance
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    resource="consumer-data",
    actor_id="ai-agent-v2",
    risk_level="MEDIUM",
    human_approver="supervisor-123",  # For HIGH risk decisions
    nist_functions={
        "govern": ["accountability", "transparency"],
        "map": ["traceability"],
        "measure": ["fairness", "human_oversight"],
        "manage": ["risk_assessment"]
    }
)

print(f"Receipt ID: {receipt['receipt_id']}")
print(f"NIST Compliance: {receipt['nist_compliant']}")
```

### Multi-State Compliance Example

```python
from jep.us import MultiStateComplianceTracker

# Initialize for multiple states
tracker = MultiStateComplianceTracker(
    states=["CA", "CO", "VA"],  # California, Colorado, Virginia
    organization="Your Company"
)

# One receipt, compliant with all three states
receipt = tracker.log_decision(
    operation="CREDIT_SCORING",
    resource="consumer-data",
    actor_id="ai-agent",
    consumer_consent=True,
    privacy_notice_provided=True
)
```

## 📁 Repository Structure

```
jep-us-solutions/
├── README.md                          # This file
├── nist-ai-rmf/                        # NIST AI RMF
│   ├── README.md
│   ├── mapping.md                       # Detailed mapping to NIST framework
│   ├── implementation/
│   │   └── nist_tracker.py               # Core NIST implementation
│   └── examples/
│       ├── financial_services.py
│       ├── healthcare.py
│       └── critical_infrastructure.py
├── state-regulations/                   # State-by-state compliance
│   ├── california.md                     # CCPA/CPRA
│   ├── colorado.md                        # Colorado AI Act
│   └── virginia.md                        # VCDPA
├── federal/                              # Federal guidelines
│   ├── ai-bill-of-rights.md               # White House AI Bill of Rights
│   └── ftc.md                              # FTC AI guidelines
└── tests/                                # Verification scripts
    ├── verify-nist.py
    ├── verify-california.py
    ├── verify-colorado.py
    └── verify-virginia.py
```

## 🏛️ Governance

JEP is stewarded by **HJS Foundation LTD** (Singapore CLG), a non-profit organization with permanent asset lock. The foundation's constitution explicitly prohibits:

- Distribution of profits to members (Article 7B)
- Transfer or sale of core assets (trademarks, domains, copyrights) (Article 67A)
- Private distribution of assets upon dissolution (Article 68)

**Registered Address**: 101 Thomson Road #28-03A, United Square, Singapore 307591

## 🔍 Verification

### One-Command NIST Compliance Check

```bash
python tests/verify-nist.py

# Output:
# ================================
# NIST AI RMF COMPLIANCE VERIFICATION
# ================================
# ✅ GOVERN: All 3 categories met
# ✅ MAP: All 2 categories met
# ✅ MEASURE: All 3 categories met
# ✅ MANAGE: All 1 categories met
# ================================
# FULL COMPLIANCE VERIFIED
# ================================
```

### State-by-State Verification

```bash
# California
python tests/verify-california.py

# Colorado
python tests/verify-colorado.py

# Virginia
python tests/verify-virginia.py
```

## 📊 Comparison: JEP vs Traditional Approaches

| Aspect | Traditional Approach | JEP US Solutions |
|--------|---------------------|------------------|
| **Integration** | Months of development | **3 lines of code** |
| **NIST Coverage** | Manual mapping | **Automated verification** |
| **Multi-State** | Separate systems | **One codebase** |
| **Audit Trail** | Ordinary logs | **Cryptographic proof** |
| **Cost** | $100k+ | **Free, open-source** |
| **Privacy** | May store PII | **No PII by design** |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

## 📬 Contact

- **Email**: us@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)
- **Foundation**: HJS Foundation LTD (Singapore CLG)

## 📄 License

Apache 2.0 - See [LICENSE](LICENSE) for details.

---

*Designed for the United States 🇺🇸, serving global AI accountability*
