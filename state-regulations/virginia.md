# 🇺🇸 Virginia Consumer Data Protection Act (VCDPA)

**JEP Compliance for Virginia's Data Privacy Law**

## 📋 Overview

The Virginia Consumer Data Protection Act (VCDPA) is Virginia's comprehensive data privacy law, effective January 1, 2023. It grants consumers rights over their personal data and imposes obligations on businesses that process personal data. This document maps JEP's capabilities to VCDPA requirements.

### Effective Date
- **January 1, 2023**

## 🎯 Key Rights Covered

| Right | Description | JEP Implementation |
|-------|-------------|-------------------|
| **Right to Access** | Consumers can confirm whether their data is processed and access it | Complete data inventory + access API |
| **Right to Correct** | Consumers can correct inaccuracies in their data | Data correction logs + versioning |
| **Right to Delete** | Consumers can delete their data | Deletion receipts + verification |
| **Right to Data Portability** | Consumers can obtain their data in portable format | JSON-LD export + standardized format |
| **Right to Opt-Out** | Consumers can opt-out of data processing for targeted advertising, sale, or profiling | Consent management + opt-out tracking |
| **Right to Non-Discrimination** | No discrimination for exercising rights | Fairness metrics + compliance reporting |

## 📊 VCDPA Requirements Mapping

| Section | Requirement | JEP Implementation | Verification |
|---------|-------------|-------------------|--------------|
| **§ 59.1-575** | Definitions | Data category classification | `verify-virginia.py --definitions` |
| **§ 59.1-576** | Applicability | Jurisdiction tracking | `verify-virginia.py --applicability` |
| **§ 59.1-577** | Consumer Rights - Access | `data_access_request()` | `verify-virginia.py --access` |
| **§ 59.1-577** | Consumer Rights - Correction | `log_correction()` | `verify-virginia.py --correct` |
| **§ 59.1-577** | Consumer Rights - Deletion | `handle_deletion_request()` | `verify-virginia.py --delete` |
| **§ 59.1-577** | Consumer Rights - Portability | `export_consumer_data()` | `verify-virginia.py --portability` |
| **§ 59.1-578** | Opt-Out Rights | `handle_opt_out()` | `verify-virginia.py --optout` |
| **§ 59.1-579** | Appeals Process | `handle_appeal()` | `verify-virginia.py --appeal` |
| **§ 59.1-580** | Data Protection Assessments | `conduct_dpia()` | `verify-virginia.py --dpia` |
| **§ 59.1-581** | De-identified Data | De-identification controls | `verify-virginia.py --deidentify` |
| **§ 59.1-582** | Contracts with Processors | Processor agreements | `verify-virginia.py --contracts` |

## 🔧 Implementation

### VCDPA-Compliant Tracker

```python
from jep.us.state import VCDPAComplianceTracker

tracker = VCDPAComplianceTracker(
    business_name="Example Company",
    contact_email="privacy@example.com",
    data_protection_officer="dpo@example.com",
    effective_date="2023-01-01"
)

# Log data collection with VCDPA notice
receipt = tracker.log_data_collection(
    consumer_id="CONS-123",
    data_categories=[
        {"category": "identifiers", "data": ["name", "email", "address"]},
        {"category": "commercial", "data": ["purchase_history"]},
        {"category": "internet_activity", "data": ["browsing_history"]}
    ],
    sensitive_data=[],  # No sensitive data for this collection
    processing_purposes=[
        {"purpose": "service_provision", "legal_basis": "contract"},
        {"purpose": "analytics", "legal_basis": "legitimate_interest"}
    ],
    notice_provided=True,
    notice_url="https://example.com/privacy",
    notice_version="2.0",
    opt_out_methods=["preference_center", "do_not_sell_link"],
    metadata={
        "source": "website_registration",
        "collected_at": time.time()
    }
)

# Handle data access request
access_response = tracker.handle_access_request(
    request_id="ACCESS-2026-001",
    consumer_id="CONS-123",
    request_date=time.time(),
    verification_method="email_verification",
    response_format="json",
    data_categories=["all"],
    response_deadline=time.time() + 2592000  # 45 days
)

# Handle opt-out request
opt_out = tracker.handle_opt_out(
    consumer_id="CONS-123",
    opt_out_date=time.time(),
    opt_out_method="do_not_sell_link",
    opt_out_purposes=["targeted_advertising", "sale"],
    confirmation_sent=True,
    confirmation_method="email"
)

# Handle appeal
appeal = tracker.handle_appeal(
    appeal_id="APPEAL-2026-001",
    consumer_id="CONS-123",
    original_request_id="ACCESS-2026-001",
    appeal_date=time.time(),
    appeal_reason="Request not fulfilled in time",
    review_status="IN_PROGRESS",
    reviewer="privacy_officer-456",
    appeal_deadline=time.time() + 1728000,  # 20 days
    notification_method="email"
)
```

## 📄 Complete Examples

### 1. Data Portability Implementation

```python
# VCDPA data portability - export consumer data in portable format
class DataPortabilityService:
    def __init__(self, tracker):
        self.tracker = tracker
        self.export_formats = ["json", "csv", "json-ld"]
    
    def export_consumer_data(self, consumer_id: str, format: str = "json-ld") -> dict:
        """Export consumer data in requested format"""
        
        # Collect all data for consumer
        consumer_data = self._collect_consumer_data(consumer_id)
        
        # Format based on request
        if format == "json-ld":
            export = self._format_json_ld(consumer_data, consumer_id)
        elif format == "json":
            export = self._format_json(consumer_data)
        elif format == "csv":
            export = self._format_csv(consumer_data)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        # Log the export for compliance
        receipt = self.tracker.log_decision(
            operation="DATA_PORTABILITY_EXPORT",
            resource=f"consumer/{consumer_id}",
            actor_id="portability-service",
            risk_level="LOW",
            reasoning=f"Data export requested via VCDPA",
            metadata={
                "consumer_id": consumer_id,
                "export_format": format,
                "record_count": len(consumer_data),
                "export_date": time.time()
            }
        )
        
        return {
            "consumer_id": consumer_id,
            "export_date": time.time(),
            "format": format,
            "data": export,
            "receipt_id": receipt['decision_id']
        }
    
    def _format_json_ld(self, data: dict, consumer_id: str) -> dict:
        """Format data as JSON-LD (machine-readable)"""
        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "identifier": consumer_id,
            "data": data,
            "exportDate": datetime.now().isoformat(),
            "exporter": "VCDPA Compliance Service"
        }
    
    def _collect_consumer_data(self, consumer_id: str) -> dict:
        """Collect all data for a consumer from various systems"""
        # In production, this would query databases, data warehouses, etc.
        return {
            "profile": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "created_at": "2020-01-01"
            },
            "transactions": [
                {"id": "TXN-001", "amount": 100, "date": "2026-01-15"},
                {"id": "TXN-002", "amount": 250, "date": "2026-02-20"}
            ],
            "preferences": {
                "language": "en",
                "notifications": True,
                "marketing_opt_in": False
            }
        }
```

### 2. Data Protection Impact Assessment (DPIA)

```python
# VCDPA requires Data Protection Impact Assessments for high-risk processing
class DPIAService:
    def __init__(self, tracker):
        self.tracker = tracker
        self.dpias = []
    
    def conduct_dpia(self, processing_activity: dict) -> dict:
        """Conduct a Data Protection Impact Assessment"""
        
        dpia = {
            "dpia_id": f"DPIA-{int(time.time())}",
            "activity_name": processing_activity['name'],
            "activity_description": processing_activity['description'],
            "conducted_date": time.time(),
            "conducted_by": processing_activity.get('assessor', 'privacy_team'),
            "data_categories": processing_activity.get('data_categories', []),
            "processing_purposes": processing_activity.get('purposes', []),
            "risk_assessment": self._assess_risks(processing_activity),
            "mitigations": [],
            "residual_risk": "UNASSESSED",
            "review_date": time.time() + 31536000  # 1 year
        }
        
        # Identify risks and mitigations
        risks = self._identify_risks(processing_activity)
        dpia['risk_assessment']['risks'] = risks
        
        for risk in risks:
            mitigation = self._propose_mitigation(risk)
            dpia['mitigations'].append(mitigation)
        
        # Assess residual risk
        dpia['residual_risk'] = self._assess_residual_risk(risks, dpia['mitigations'])
        
        # Log the DPIA
        receipt = self.tracker.log_decision(
            operation="DPIA_CONDUCTED",
            resource=f"dpia/{dpia['dpia_id']}",
            actor_id=dpia['conducted_by'],
            risk_level=dpia['residual_risk'],
            reasoning=f"DPIA for {dpia['activity_name']}",
            metadata=dpia
        )
        
        dpia['receipt_id'] = receipt['decision_id']
        self.dpias.append(dpia)
        
        return dpia
    
    def _assess_risks(self, activity: dict) -> dict:
        """Assess risks of processing activity"""
        return {
            "overall_risk": "MEDIUM",
            "risk_factors": []
        }
    
    def _identify_risks(self, activity: dict) -> list:
        """Identify specific risks"""
        return [
            {
                "risk": "Unauthorized access",
                "likelihood": "MEDIUM",
                "impact": "HIGH",
                "risk_score": 0.7
            },
            {
                "risk": "Data breach",
                "likelihood": "LOW",
                "impact": "CRITICAL",
                "risk_score": 0.5
            }
        ]
    
    def _propose_mitigation(self, risk: dict) -> dict:
        """Propose mitigation for identified risk"""
        return {
            "risk": risk['risk'],
            "mitigation": "Implement access controls and encryption",
            "implementation_status": "PLANNED",
            "completion_date": time.time() + 2592000  # 30 days
        }
    
    def _assess_residual_risk(self, risks: list, mitigations: list) -> str:
        """Assess residual risk after mitigations"""
        return "LOW"
    
    def generate_dpia_report(self) -> dict:
        """Generate DPIA summary report"""
        return {
            "total_dpias": len(self.dpias),
            "recent_dpias": [d for d in self.dpias if d['conducted_date'] > time.time() - 7776000],
            "high_risk_activities": [d for d in self.dpias if d['residual_risk'] in ['HIGH', 'CRITICAL']],
            "compliance_status": "ACTIVE"
        }
```

## 🔍 Verification

```bash
# Run complete VCDPA verification
python tests/verify-virginia.py

# Output:
# ========================================
# VCDPA COMPLIANCE VERIFICATION
# ========================================
# ✅ § 59.1-577: Right to Access
# ✅ § 59.1-577: Right to Correct
# ✅ § 59.1-577: Right to Delete
# ✅ § 59.1-577: Right to Portability
# ✅ § 59.1-578: Right to Opt-Out
# ✅ § 59.1-579: Appeals Process
# ✅ § 59.1-580: Data Protection Assessments
# ✅ § 59.1-581: De-identified Data
# ✅ § 59.1-582: Processor Contracts
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [VCDPA Text (Va. Code Ann. § 59.1-575 et seq.)](https://law.lis.virginia.gov/vacode/title59.1/chapter53/)
- [Virginia Attorney General Guidance](https://www.oag.state.va.us/)

## 📬 Contact

For Virginia-specific inquiries:
- **Email**: virginia@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
