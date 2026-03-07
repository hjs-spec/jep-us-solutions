#!/usr/bin/env python3
"""
NIST AI RMF Financial Services Example
========================================

This example demonstrates a complete fair lending compliance system
for a financial institution, showing how JEP implements all four
NIST AI RMF functions in a real-world banking scenario.

Regulatory Compliance:
- Equal Credit Opportunity Act (ECOA)
- Fair Lending laws
- CFPB requirements
- NIST AI RMF
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from nist-ai-rmf.implementation.nist_tracker import NISTComplianceTracker


class FairLendingSystem:
    """
    Complete fair lending compliance system for financial institutions.
    
    Demonstrates NIST AI RMF implementation for:
    - Fair lending decisions
    - Regulatory reporting
    - Audit trails
    - Risk management
    """
    
    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self.tracker = NISTComplianceTracker(
            organization=bank_name,
            sector="financial"
        )
        
        self.loan_applications = []
        self.approved_loans = []
        self.declined_loans = []
        
        print("="*80)
        print(f"🏦 Fair Lending System - {bank_name}")
        print("="*80)
    
    def setup_governance_framework(self):
        """
        Set up NIST GOVERN function for fair lending.
        
        Covers:
        - GOVERN 1.1: Accountability policies
        - GOVERN 1.2: Roles and responsibilities
        - GOVERN 1.3: Governance structure
        - GOVERN 3.1: Risk tolerance
        - GOVERN 3.2: Escalation paths
        """
        print("\n📋 Setting up NIST GOVERN Framework")
        
        # GOVERN 1.1 & 1.3: Accountability framework
        governance = self.tracker.log_governance_framework(
            framework_version="2.1",
            effective_date="2026-01-01",
            accountability_principles=[
                {
                    "principle": "fair_lending",
                    "implementation": "All credit decisions must be fair and non-discriminatory",
                    "owner": "Chief Compliance Officer"
                },
                {
                    "principle": "explainability",
                    "implementation": "All decisions must be explainable to regulators",
                    "owner": "Model Risk Team"
                },
                {
                    "principle": "human_oversight",
                    "implementation": "All HIGH risk decisions require human approval",
                    "owner": "Credit Committee"
                }
            ],
            governance_structure={
                "oversight_committee": "Fair Lending Committee",
                "members": ["CCO", "Chief Credit Officer", "Chief Data Officer"],
                "meeting_frequency": "monthly",
                "reporting_chain": ["Loan Officer", "Risk Manager", "CCO", "Board"]
            }
        )
        print(f"   ✅ Governance framework: {governance['framework_id']}")
        
        # GOVERN 1.2: Roles and responsibilities
        roles = self.tracker.log_roles([
            {
                "role": "loan_officer",
                "responsibilities": ["initial_review", "document_verification"],
                "approval_limit": 100000
            },
            {
                "role": "senior_underwriter",
                "responsibilities": ["risk_assessment", "exception_approval"],
                "approval_limit": 500000
            },
            {
                "role": "credit_committee",
                "responsibilities": ["policy_review", "high_risk_approval"],
                "approval_limit": "unlimited"
            },
            {
                "role": "fair_lending_officer",
                "responsibilities": ["bias_testing", "regulatory_reporting"],
                "approval_limit": "oversight_only"
            }
        ])
        print(f"   ✅ Roles defined: {len(roles['roles'])} positions")
        
        # GOVERN 3.1: Risk thresholds
        thresholds = self.tracker.set_risk_thresholds({
            "LOW": {"max_impact": 5000, "auto_approve": True},
            "MEDIUM": {"max_impact": 25000, "human_review": True},
            "HIGH": {"max_impact": 100000, "manager_approval": True},
            "CRITICAL": {"max_impact": float('inf'), "committee_approval": True}
        })
        print(f"   ✅ Risk thresholds configured")
        
        # GOVERN 3.2: Approval workflows
        workflow = self.tracker.log_approval_workflow(
            risk_level="HIGH",
            approvers=["loan_officer", "senior_underwriter"],
            conditions=["amount > 25000", "first_time_applicant"]
        )
        print(f"   ✅ Approval workflow: {workflow['workflow_id']}")
        
        return governance
    
    def process_loan_application(self, application: dict) -> dict:
        """
        Process a single loan application with full NIST compliance.
        
        Covers:
        - MAP 1.1-1.3: Context
        - MAP 2.1-2.3: Data
        - MAP 3.1-3.3: Risks
        - MEASURE 1.1: Performance
        - MEASURE 2.1-2.4: Trustworthiness
        - MEASURE 3.1-3.3: Human oversight
        """
        print(f"\n📄 Processing Application: {application['id']}")
        print(f"   Applicant: {application['name']}")
        print(f"   Amount: ${application['amount']:,.0f}")
        print(f"   Credit Score: {application['credit_score']}")
        
        # Calculate risk level
        risk_level = self._calculate_risk_level(application)
        print(f"   Risk Level: {risk_level}")
        
        # Check if human approval required
        human_approver = None
        if risk_level in ["HIGH", "CRITICAL"]:
            human_approver = self._get_approver(risk_level, application)
            print(f"   Human Approver: {human_approver}")
        
        # Determine decision
        decision = self._make_decision(application, risk_level)
        
        # Prepare decision factors for explainability
        decision_factors = self._prepare_decision_factors(application)
        
        # Log the decision with full NIST compliance
        receipt = self.tracker.log_decision(
            operation="LOAN_UNDERWRITING",
            resource=f"application/{application['id']}",
            actor_id="fair-lending-engine-v2",
            risk_level=risk_level,
            amount=application['amount'],
            human_approver=human_approver,
            reasoning=self._generate_explanation(application, decision_factors),
            
            # MAP 1: Context
            purpose="mortgage_lending",
            stakeholders=[
                {"role": "borrower", "rights": ["fair_lending", "explanation"]},
                {"role": "regulator", "oversight": "CFPB, ECOA"},
                {"role": "investor", "interest": "loan_performance"}
            ],
            deployment_context={
                "environment": "production",
                "date": datetime.now().isoformat(),
                "version": "fair-lending-v2.1",
                "geography": "United States"
            },
            
            # MAP 2: Data
            data_sources=[
                {
                    "source": "credit_bureau",
                    "data_elements": ["credit_score", "payment_history"],
                    "verification": "third-party"
                },
                {
                    "source": "application_form",
                    "data_elements": ["income", "employment", "assets"],
                    "verification": "document_review"
                },
                {
                    "source": "internal_records",
                    "data_elements": ["existing_relationships"],
                    "verification": "system"
                }
            ],
            data_quality={
                "completeness": 0.99,
                "accuracy": 0.98,
                "timeliness": "real_time",
                "last_verified": datetime.now().isoformat()
            },
            data_governance={
                "privacy_compliant": True,
                "retention_policy": "7_years",
                "consent_obtained": application.get('consent', True),
                "data_minimization": True
            },
            
            # MAP 3: Risks
            risk_factors=[
                {
                    "factor": "credit_risk",
                    "assessment": decision_factors['credit_score']['assessment'],
                    "mitigation": "collateral_requirement"
                },
                {
                    "factor": "income_volatility",
                    "assessment": decision_factors['income_stability']['assessment'],
                    "mitigation": "reserve_requirement"
                }
            ],
            risk_likelihood=risk_level,
            risk_context={
                "regulatory_scrutiny": "high",
                "market_conditions": "stable",
                "portfolio_impact": "moderate"
            },
            
            # MEASURE 1: Performance
            performance_metrics={
                "accuracy": 0.97,
                "precision": 0.96,
                "recall": 0.98,
                "f1_score": 0.97,
                "auc_roc": 0.99,
                "measurement_date": datetime.now().isoformat()
            },
            
            # MEASURE 2: Trustworthiness
            fairness_metrics={
                "disparate_impact": 0.98,
                "equal_opportunity": 0.97,
                "demographic_parity": 0.96,
                "test_date": datetime.now().isoformat(),
                "protected_classes": ["race", "gender", "age"]
            },
            explanation=decision_factors,
            robustness={
                "adversarial_testing": "passed",
                "edge_case_testing": "passed",
                "stress_testing": "passed",
                "monitoring_frequency": "daily"
            },
            
            metadata={
                "application": application,
                "decision": decision,
                "loan_purpose": application.get('purpose', 'purchase'),
                "property_type": application.get('property_type', 'single_family')
            }
        )
        
        # Store application result
        application['decision'] = decision
        application['risk_level'] = risk_level
        application['receipt_id'] = receipt['decision_id']
        application['processed_at'] = time.time()
        
        self.loan_applications.append(application)
        if decision == "APPROVED":
            self.approved_loans.append(application)
        else:
            self.declined_loans.append(application)
        
        print(f"   Decision: {decision}")
        print(f"   Receipt: {receipt['decision_id'][:16]}...")
        
        return receipt
    
    def _calculate_risk_level(self, application: dict) -> str:
        """Calculate risk level based on application data."""
        credit_score = application.get('credit_score', 0)
        amount = application.get('amount', 0)
        dti = application.get('dti_ratio', 100)
        
        if credit_score >= 750 and amount <= 500000 and dti <= 36:
            return "LOW"
        elif credit_score >= 700 and amount <= 1000000 and dti <= 43:
            return "MEDIUM"
        elif credit_score >= 650 and amount <= 2000000 and dti <= 50:
            return "HIGH"
        else:
            return "CRITICAL"
    
    def _get_approver(self, risk_level: str, application: dict) -> str:
        """Get appropriate approver based on risk level."""
        if risk_level == "HIGH":
            return "senior_underwriter-456"
        elif risk_level == "CRITICAL":
            return "credit_committee"
        return None
    
    def _make_decision(self, application: dict, risk_level: str) -> str:
        """Make lending decision based on risk assessment."""
        if risk_level in ["LOW", "MEDIUM"]:
            return "APPROVED"
        elif risk_level == "HIGH":
            # High risk may still be approved with conditions
            if application.get('additional_collateral'):
                return "APPROVED_WITH_CONDITIONS"
            return "DECLINED"
        else:  # CRITICAL
            return "DECLINED"
    
    def _prepare_decision_factors(self, application: dict) -> dict:
        """Prepare explainable decision factors."""
        return {
            "credit_score": {
                "value": application.get('credit_score', 0),
                "weight": 0.4,
                "threshold": ">=680",
                "assessment": "positive" if application.get('credit_score', 0) >= 680 else "negative"
            },
            "dti_ratio": {
                "value": application.get('dti_ratio', 0),
                "weight": 0.3,
                "threshold": "<=43",
                "assessment": "positive" if application.get('dti_ratio', 0) <= 43 else "negative"
            },
            "income_stability": {
                "value": f"{application.get('employment_years', 0)} years",
                "weight": 0.2,
                "threshold": ">=2 years",
                "assessment": "positive" if application.get('employment_years', 0) >= 2 else "negative"
            },
            "ltv_ratio": {
                "value": application.get('ltv_ratio', 0),
                "weight": 0.1,
                "threshold": "<=80",
                "assessment": "positive" if application.get('ltv_ratio', 0) <= 80 else "negative"
            }
        }
    
    def _generate_explanation(self, application: dict, factors: dict) -> str:
        """Generate human-readable explanation."""
        explanations = []
        for factor, data in factors.items():
            explanations.append(f"{factor}: {data['value']} ({data['assessment']})")
        
        return f"Decision based on: {', '.join(explanations)}"
    
    def run_fair_lending_analysis(self):
        """Run fair lending analysis across all applications."""
        print("\n" + "="*80)
        print("📊 Fair Lending Analysis")
        print("="*80)
        
        # Calculate approval rates by demographic
        demographics = {
            "race": {},
            "gender": {},
            "age_group": {}
        }
        
        for app in self.loan_applications:
            for dim in demographics.keys():
                group = app.get(dim, 'unknown')
                if group not in demographics[dim]:
                    demographics[dim][group] = {"total": 0, "approved": 0}
                
                demographics[dim][group]["total"] += 1
                if app['decision'] == "APPROVED" or app['decision'] == "APPROVED_WITH_CONDITIONS":
                    demographics[dim][group]["approved"] += 1
        
        # Calculate disparate impact
        print("\n📈 Approval Rates by Demographic:")
        for dim, groups in demographics.items():
            print(f"\n   {dim.upper()}:")
            for group, stats in groups.items():
                rate = (stats['approved'] / stats['total']) * 100 if stats['total'] > 0 else 0
                print(f"      {group}: {rate:.1f}% ({stats['approved']}/{stats['total']})")
        
        # Check for disparate impact
        for dim, groups in demographics.items():
            rates = [stats['approved']/stats['total'] for stats in groups.values() if stats['total'] > 0]
            if len(rates) > 1:
                max_rate = max(rates)
                min_rate = min(rates)
                disparate_impact = min_rate / max_rate if max_rate > 0 else 1
                
                print(f"\n   {dim} Disparate Impact Ratio: {disparate_impact:.3f}")
                if disparate_impact < 0.8:
                    print(f"   ⚠️  Potential {dim} discrimination detected!")
        
        return demographics
    
    def generate_regulatory_report(self):
        """Generate CFPB/ECOA regulatory report."""
        print("\n" + "="*80)
        print("📋 Generating Regulatory Report")
        print("="*80)
        
        report = self.tracker.generate_nist_report(
            start_date="2026-01-01",
            end_date="2026-03-31"
        )
        
        # Add fair lending metrics
        report["fair_lending_metrics"] = {
            "total_applications": len(self.loan_applications),
            "approved": len(self.approved_loans),
            "declined": len(self.declined_loans),
            "approval_rate": len(self.approved_loans) / len(self.loan_applications) * 100,
            "average_loan_amount": sum(a['amount'] for a in self.approved_loans) / len(self.approved_loans) if self.approved_loans else 0,
            "human_oversight_rate": len([a for a in self.loan_applications if a.get('risk_level') in ['HIGH', 'CRITICAL']]) / len(self.loan_applications)
        }
        
        # Save report
        filename = f"fair_lending_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Report saved: {filename}")
        
        return report


def run_fair_lending_demo():
    """Run complete fair lending demonstration."""
    
    # Initialize system
    system = FairLendingSystem("Community First Bank")
    
    # Set up governance
    system.setup_governance_framework()
    
    # Sample loan applications with diverse demographics
    applications = [
        # Low-risk applications
        {
            "id": "APP-001",
            "name": "John Smith",
            "amount": 250000,
            "credit_score": 780,
            "dti_ratio": 32,
            "employment_years": 8,
            "ltv_ratio": 75,
            "income": 120000,
            "race": "white",
            "gender": "male",
            "age_group": "35-50",
            "purpose": "purchase",
            "property_type": "single_family",
            "consent": True
        },
        {
            "id": "APP-002",
            "name": "Maria Garcia",
            "amount": 180000,
            "credit_score": 760,
            "dti_ratio": 35,
            "employment_years": 5,
            "ltv_ratio": 78,
            "income": 95000,
            "race": "hispanic",
            "gender": "female",
            "age_group": "30-45",
            "purpose": "refinance",
            "property_type": "condo",
            "consent": True
        },
        
        # Medium-risk applications
        {
            "id": "APP-003",
            "name": "James Johnson",
            "amount": 350000,
            "credit_score": 720,
            "dti_ratio": 40,
            "employment_years": 3,
            "ltv_ratio": 82,
            "income": 110000,
            "race": "black",
            "gender": "male",
            "age_group": "40-55",
            "purpose": "purchase",
            "property_type": "single_family",
            "consent": True
        },
        {
            "id": "APP-004",
            "name": "Yuki Tanaka",
            "amount": 320000,
            "credit_score": 710,
            "dti_ratio": 42,
            "employment_years": 4,
            "ltv_ratio": 80,
            "income": 105000,
            "race": "asian",
            "gender": "female",
            "age_group": "35-50",
            "purpose": "purchase",
            "property_type": "single_family",
            "consent": True
        },
        
        # High-risk applications
        {
            "id": "APP-005",
            "name": "Robert Brown",
            "amount": 450000,
            "credit_score": 680,
            "dti_ratio": 45,
            "employment_years": 2,
            "ltv_ratio": 85,
            "income": 130000,
            "race": "white",
            "gender": "male",
            "age_group": "45-60",
            "purpose": "investment",
            "property_type": "multi_family",
            "additional_collateral": True,
            "consent": True
        },
        {
            "id": "APP-006",
            "name": "Chen Wei",
            "amount": 480000,
            "credit_score": 670,
            "dti_ratio": 47,
            "employment_years": 1.5,
            "ltv_ratio": 88,
            "income": 125000,
            "race": "asian",
            "gender": "male",
            "age_group": "35-50",
            "purpose": "purchase",
            "property_type": "single_family",
            "consent": True
        },
        
        # Critical-risk applications
        {
            "id": "APP-007",
            "name": "Sarah Williams",
            "amount": 650000,
            "credit_score": 620,
            "dti_ratio": 52,
            "employment_years": 1,
            "ltv_ratio": 92,
            "income": 140000,
            "race": "white",
            "gender": "female",
            "age_group": "35-50",
            "purpose": "purchase",
            "property_type": "single_family",
            "consent": True
        },
        {
            "id": "APP-008",
            "name": "Carlos Rodriguez",
            "amount": 600000,
            "credit_score": 630,
            "dti_ratio": 50,
            "employment_years": 1,
            "ltv_ratio": 90,
            "income": 135000,
            "race": "hispanic",
            "gender": "male",
            "age_group": "40-55",
            "purpose": "refinance",
            "property_type": "single_family",
            "consent": True
        }
    ]
    
    # Process all applications
    print("\n" + "="*80)
    print("📋 Processing Loan Applications")
    print("="*80)
    
    for app in applications:
        system.process_loan_application(app)
    
    # Run fair lending analysis
    system.run_fair_lending_analysis()
    
    # Generate regulatory report
    report = system.generate_regulatory_report()
    
    print("\n" + "="*80)
    print("✅ Fair Lending Demo Complete")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Total Applications: {len(system.loan_applications)}")
    print(f"   Approved: {len(system.approved_loans)}")
    print(f"   Declined: {len(system.declined_loans)}")
    print(f"   Approval Rate: {len(system.approved_loans)/len(system.loan_applications)*100:.1f}%")


if __name__ == "__main__":
    run_fair_lending_demo()
