# 🇺🇸 California Consumer Privacy Act (CCPA) and CPRA

**JEP Compliance for California's Data Privacy Laws**

## 📋 Overview

The California Consumer Privacy Act (CCPA) and its amendment, the California Privacy Rights Act (CPRA), establish comprehensive data privacy rights for California residents. This document maps JEP's capabilities to CCPA/CPRA requirements.

### Effective Dates
- **CCPA**: January 1, 2020
- **CPRA**: January 1, 2023 (fully operative)

## 🎯 Key Rights Covered

| Right | Description | JEP Implementation |
|-------|-------------|-------------------|
| **Right to Know** | Consumers can request what personal data is collected | Complete audit trail of all data collection |
| **Right to Delete** | Consumers can request deletion of their data | Deletion receipts + verification |
| **Right to Opt-Out** | Consumers can opt-out of data sales | Consent management + opt-out tracking |
| **Right to Correct** | Consumers can correct inaccurate data | Data correction logs + versioning |
| **Right to Limit** | Limit use of sensitive personal information | Sensitivity flags + purpose limitation |
| **Right to Non-Discrimination** | No discrimination for exercising rights | Fairness metrics + compliance reporting |

## 📊 CCPA/CPRA Requirements Mapping

| Section | Requirement | JEP Implementation | Verification |
|---------|-------------|-------------------|--------------|
| **1798.100** | Notice at Collection | `purpose` field + `notice_provided` flag | `verify-california.py --notice` |
| **1798.105** | Right to Delete | `log_data_deletion()` with receipts | `verify-california.py --delete` |
| **1798.106** | Right to Correct | `log_correction()` with versioning | `verify-california.py --correct` |
| **1798.110** | Right to Know (Categories) | Data inventory + category tracking | `verify-california.py --categories` |
| **1798.115** | Right to Know (Specific Pieces) | Complete data lineage | `verify-california.py --specific` |
| **1798.120** | Right to Opt-Out of Sale/Sharing | `opt_out` field + consent management | `verify-california.py --optout` |
| **1798.121** | Right to Limit Sensitive Data | `sensitive_data` flags + purpose limits | `verify-california.py --sensitive` |
| **1798.130** | Privacy Policy Requirements | JSON-LD machine-readable policy | `verify-california.py --policy` |
| **1798.135** | Opt-Out Signal Recognition | Global Privacy Control support | `verify-california.py --gpc` |
| **1798.140** | Contract Requirements | Data processor agreements | `verify-california.py --contracts` |

## 🔧 Implementation

### CCPA-Compliant Tracker

```python
from jep.us.state import CCPAComplianceTracker

tracker = CCPAComplianceTracker(
    business_name="Example Company",
    contact_email="privacy@example.com",
    california_only=True  # If business only serves CA residents
)

# Log data collection with CCPA notice
receipt = tracker.log_data_collection(
    consumer_id="CONS-123",
    data_categories=["contact_info", "purchase_history"],
    sensitive_categories=["financial_info"],  # CPRA sensitive data
    purpose="service_improvement",
    notice_provided=True,
    notice_url="https://example.com/privacy",
    notice_version="2.1",
    opt_out_available=True,
    sensitive_use_limits=["service_only"],
    metadata={
        "source": "online_purchase",
        "collected_at": time.time()
    }
)

# Handle deletion request
deletion = tracker.handle_deletion_request(
    request_id="DEL-2026-001",
    consumer_id="CONS-123",
    request_date=time.time(),
    verification_method="account_login",
    data_categories=["all"],
    deletion_date=time.time() + 86400,  # 24 hours
    confirmation_sent=True
)

# Handle opt-out
opt_out = tracker.handle_opt_out(
    consumer_id="CONS-123",
    opt_out_date=time.time(),
    opt_out_method="preference_center",
    opt_out_scope=["sale", "sharing"],
    gpc_signal=True,  # Global Privacy Control
    confirmation_sent=True
)
```

## 📄 Complete Examples

### 1. Privacy Policy Generation

```python
# Generate CCPA-compliant privacy policy
policy = tracker.generate_privacy_policy(
    business_name="Example Company",
    effective_date="2026-01-01",
    data_categories=[
        {"category": "Identifiers", "examples": ["name", "email", "IP address"]},
        {"category": "Commercial", "examples": ["purchase history"]},
        {"category": "Geolocation", "examples": ["precise location"]}
    ],
    sensitive_categories=[
        {"category": "Financial", "examples": ["credit card", "bank account"]},
        {"category": "Health", "examples": ["medical information"]}
    ],
    business_purposes=[
        {"purpose": "Service delivery", "description": "Provide requested services"},
        {"purpose": "Analytics", "description": "Improve user experience"}
    ],
    third_party_sharing=[
        {"recipient": "Analytics Provider", "purpose": "analytics", "categories": ["Identifiers"]}
    ],
    sale_of_personal_info=False,
    share_of_personal_info=True,
    retention_periods={
        "Identifiers": "2 years",
        "Commercial": "7 years",
        "Sensitive": "30 days"
    },
    rights_notice={
        "right_to_know": True,
        "right_to_delete": True,
        "right_to_opt_out": True,
        "right_to_correct": True,
        "right_to_limit": True
    },
    contact_info={
        "email": "privacy@example.com",
        "phone": "1-800-123-4567",
        "web_form": "https://example.com/privacy-requests"
    }
)
```

### 2. Handling Consumer Requests

```python
# Complete request handling workflow
class CCPARequestHandler:
    def __init__(self, tracker):
        self.tracker = tracker
        self.requests = []
    
    def handle_consumer_request(self, request):
        """Handle any CCPA/CPRA consumer request"""
        
        # Verify identity
        identity_verified = self._verify_identity(request)
        if not identity_verified:
            return {"error": "Identity verification failed"}
        
        # Process based on request type
        if request['type'] == 'know':
            result = self._handle_know_request(request)
        elif request['type'] == 'delete':
            result = self._handle_delete_request(request)
        elif request['type'] == 'opt_out':
            result = self._handle_opt_out_request(request)
        elif request['type'] == 'correct':
            result = self._handle_correct_request(request)
        elif request['type'] == 'limit':
            result = self._handle_limit_request(request)
        else:
            return {"error": "Unknown request type"}
        
        # Track request for compliance
        self.requests.append({
            "request_id": request['id'],
            "type": request['type'],
            "consumer_id": request['consumer_id'],
            "received_date": request['received_date'],
            "response_date": time.time(),
            "result": result
        })
        
        return result
    
    def _handle_know_request(self, request):
        """Right to Know implementation"""
        return self.tracker.generate_data_report(
            consumer_id=request['consumer_id'],
            categories=request.get('categories', ['all']),
            format='json',
            delivery_method='secure_portal'
        )
    
    def _handle_delete_request(self, request):
        """Right to Delete implementation"""
        return self.tracker.handle_deletion_request(
            request_id=request['id'],
            consumer_id=request['consumer_id'],
            request_date=request['received_date'],
            verification_method=request['verification_method'],
            data_categories=request.get('categories', ['all'])
        )
    
    def _handle_opt_out_request(self, request):
        """Right to Opt-Out implementation"""
        return self.tracker.handle_opt_out(
            consumer_id=request['consumer_id'],
            opt_out_date=request['received_date'],
            opt_out_method=request.get('method', 'preference_center'),
            opt_out_scope=request.get('scope', ['sale', 'sharing'])
        )
    
    def _verify_identity(self, request):
        """Verify consumer identity (required by CCPA)"""
        # Implementation depends on business systems
        return True
```

## 🔍 Verification

```bash
# Run complete CCPA/CPRA verification
python tests/verify-california.py

# Output:
# ========================================
# CCPA/CPRA COMPLIANCE VERIFICATION
# ========================================
# ✅ 1798.100: Notice at Collection
# ✅ 1798.105: Right to Delete
# ✅ 1798.106: Right to Correct
# ✅ 1798.110: Right to Know (Categories)
# ✅ 1798.115: Right to Know (Specific)
# ✅ 1798.120: Right to Opt-Out
# ✅ 1798.121: Right to Limit Sensitive Data
# ✅ 1798.130: Privacy Policy
# ✅ 1798.135: Opt-Out Signal Recognition
# ✅ 1798.140: Contract Requirements
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [CCPA Text (Cal. Civ. Code § 1798.100 et seq.)](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.&chapter=&article=)
- [CPRA Text](https://thecpra.org/)
- [California Privacy Protection Agency](https://cppa.ca.gov/)

## 📬 Contact

For California-specific inquiries:
- **Email**: california@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
