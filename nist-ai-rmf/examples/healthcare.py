#!/usr/bin/env python3
"""
NIST AI RMF Healthcare Example
================================

This example demonstrates a complete clinical decision support system
for a healthcare provider, showing how JEP implements all four
NIST AI RMF functions in a real-world medical scenario.

Regulatory Compliance:
- HIPAA (Health Insurance Portability and Accountability Act)
- FDA guidelines for AI/ML in medical devices
- HHS requirements
- NIST AI RMF
"""

import json
import time
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from nist-ai-rmf.implementation.nist_tracker import NISTComplianceTracker


class PatientStatus(Enum):
    """Patient health status levels"""
    STABLE = "STABLE"
    MONITORING = "MONITORING"
    URGENT = "URGENT"
    CRITICAL = "CRITICAL"


class ClinicalFinding(Enum):
    """Clinical findings with severity levels"""
    NORMAL = "NORMAL"
    ABNORMAL = "ABNORMAL"
    CONCERNING = "CONCERNING"
    CRITICAL = "CRITICAL"


class ClinicalDecisionSupportSystem:
    """
    Complete clinical decision support system for healthcare.
    
    Demonstrates NIST AI RMF implementation for:
    - Patient diagnosis support
    - Treatment recommendations
    - Clinical workflow integration
    - HIPAA compliance
    """
    
    def __init__(self, hospital_name: str):
        self.hospital_name = hospital_name
        self.tracker = NISTComplianceTracker(
            organization=hospital_name,
            sector="healthcare"
        )
        
        self.patients = {}
        self.diagnoses = []
        self.alerts = []
        self.clinical_audit = []
        
        print("="*80)
        print(f"🏥 Clinical Decision Support System - {hospital_name}")
        print("="*80)
    
    def setup_clinical_governance(self):
        """
        Set up NIST GOVERN function for healthcare.
        
        Covers:
        - GOVERN 1.1: Clinical accountability policies
        - GOVERN 1.2: Roles (physicians, nurses, technicians)
        - GOVERN 1.3: Medical governance structure
        - GOVERN 3.1: Patient safety risk thresholds
        - GOVERN 3.2: Clinical escalation paths
        """
        print("\n📋 Setting up Clinical Governance Framework")
        
        # GOVERN 1.1 & 1.3: Clinical accountability framework
        governance = self.tracker.log_governance_framework(
            framework_version="3.0",
            effective_date="2026-01-01",
            accountability_principles=[
                {
                    "principle": "patient_safety",
                    "implementation": "All clinical decisions prioritize patient safety",
                    "owner": "Chief Medical Officer"
                },
                {
                    "principle": "clinical_validation",
                    "implementation": "All AI recommendations must be clinically validated",
                    "owner": "Clinical Research Board"
                },
                {
                    "principle": "human_oversight",
                    "implementation": "All critical findings require physician review",
                    "owner": "Medical Executive Committee"
                }
            ],
            governance_structure={
                "oversight_committee": "Clinical AI Committee",
                "members": ["CMO", "CNO", "Chief Medical Informatics Officer", "Patient Safety Officer"],
                "meeting_frequency": "weekly",
                "reporting_chain": ["Clinician", "Department Head", "CMO", "Board"]
            }
        )
        print(f"   ✅ Clinical governance: {governance['framework_id']}")
        
        # GOVERN 1.2: Clinical roles
        roles = self.tracker.log_roles([
            {
                "role": "attending_physician",
                "responsibilities": ["final_diagnosis", "treatment_plan"],
                "scope": "all_patients",
                "supervision": "department_chair"
            },
            {
                "role": "radiologist",
                "responsibilities": ["image_interpretation", "critical_finding_alert"],
                "scope": "imaging_studies",
                "supervision": "radiology_chief"
            },
            {
                "role": "clinical_ai_specialist",
                "responsibilities": ["model_monitoring", "performance_validation"],
                "scope": "ai_systems",
                "supervision": "chief_informatics_officer"
            },
            {
                "role": "patient_safety_officer",
                "responsibilities": ["incident_review", "safety_monitoring"],
                "scope": "all_clinical_activities",
                "supervision": "quality_committee"
            }
        ])
        print(f"   ✅ Clinical roles defined: {len(roles['roles'])}")
        
        # GOVERN 3.1: Patient safety thresholds
        thresholds = self.tracker.set_risk_thresholds({
            "LOW": {"max_impact": "minor_abnormality", "auto_review": False},
            "MEDIUM": {"max_impact": "concerning_finding", "physician_review": True},
            "HIGH": {"max_impact": "urgent_finding", "specialist_consult": True},
            "CRITICAL": {"max_impact": "life_threatening", "immediate_action": True}
        })
        print(f"   ✅ Patient safety thresholds configured")
        
        # GOVERN 3.2: Clinical escalation paths
        workflow = self.tracker.log_approval_workflow(
            risk_level="CRITICAL",
            approvers=["attending_physician", "specialist_consult", "department_chair"],
            conditions=["life_threatening_finding", "treatment_uncertainty"]
        )
        print(f"   ✅ Critical finding escalation path defined")
        
        return governance
    
    def register_patient(self, patient_data: dict) -> str:
        """Register a new patient in the system."""
        patient_id = f"PT-{hashlib.sha256(patient_data['mrn'].encode()).hexdigest()[:8]}"
        
        self.patients[patient_id] = {
            "patient_id": patient_id,
            "mrn_hash": hashlib.sha256(patient_data['mrn'].encode()).hexdigest()[:16],
            "age": patient_data['age'],
            "gender": patient_data['gender'],
            "medical_history": patient_data.get('medical_history', []),
            "allergies": patient_data.get('allergies', []),
            "medications": patient_data.get('medications', []),
            "registration_date": time.time()
        }
        
        return patient_id
    
    def analyze_clinical_finding(
        self,
        patient_id: str,
        finding_type: str,
        finding_data: dict,
        ordering_physician: str
    ) -> dict:
        """
        Analyze a clinical finding with AI assistance.
        
        Covers:
        - MAP 1.1-1.3: Clinical context
        - MAP 2.1-2.3: Patient data governance
        - MAP 3.1-3.3: Clinical risks
        - MEASURE 1.1: Diagnostic accuracy
        - MEASURE 2.1-2.4: Clinical trustworthiness
        - MEASURE 3.1-3.3: Physician oversight
        """
        print(f"\n🔬 Analyzing Clinical Finding:")
        print(f"   Patient: {patient_id}")
        print(f"   Finding Type: {finding_type}")
        
        patient = self.patients.get(patient_id)
        if not patient:
            raise ValueError(f"Patient {patient_id} not found")
        
        # Determine clinical severity
        severity = self._assess_clinical_severity(finding_type, finding_data)
        print(f"   Severity: {severity.value}")
        
        # Calculate risk level based on severity
        risk_level = self._map_severity_to_risk(severity)
        print(f"   Risk Level: {risk_level}")
        
        # Check if human oversight required
        human_approver = None
        if severity in [PatientStatus.URGENT, PatientStatus.CRITICAL]:
            human_approver = self._get_clinical_approver(severity, finding_type)
            print(f"   Physician Reviewer: {human_approver}")
        
        # Generate AI recommendation
        recommendation = self._generate_clinical_recommendation(
            patient, finding_type, finding_data, severity
        )
        
        # Prepare clinical decision factors
        decision_factors = self._prepare_clinical_factors(
            patient, finding_type, finding_data, severity
        )
        
        # Log the clinical decision with full NIST compliance
        receipt = self.tracker.log_decision(
            operation="CLINICAL_DECISION_SUPPORT",
            resource=f"patient/{patient_id}/finding/{finding_type}",
            actor_id="clinical-ai-v2",
            risk_level=risk_level,
            human_approver=human_approver,
            reasoning=self._generate_clinical_explanation(decision_factors),
            
            # MAP 1: Clinical context
            purpose="diagnostic_assistance",
            stakeholders=[
                {"role": "patient", "rights": ["informed_consent", "privacy"]},
                {"role": "physician", "responsibilities": ["final_diagnosis"]},
                {"role": "hospital", "duty": "standard_of_care"}
            ],
            deployment_context={
                "environment": "clinical",
                "department": "radiology",
                "date": datetime.now().isoformat(),
                "version": "clinical-ai-v2.1",
                "facility": self.hospital_name
            },
            
            # MAP 2: Clinical data
            data_sources=[
                {
                    "source": "emr",
                    "data_elements": ["patient_history", "medications", "allergies"],
                    "verification": "clinical_staff"
                },
                {
                    "source": "imaging_study",
                    "data_elements": [finding_type],
                    "verification": "radiologist"
                },
                {
                    "source": "lab_results",
                    "data_elements": finding_data.get('labs', []),
                    "verification": "lab_technician"
                }
            ],
            data_quality={
                "completeness": 0.99,
                "accuracy": 0.98,
                "timeliness": "real_time",
                "source_reliability": "high"
            },
            data_governance={
                "hipaa_compliant": True,
                "phi_protected": True,
                "consent_obtained": True,
                "breach_notification": "24_hours",
                "retention_policy": "7_years"
            },
            
            # MAP 3: Clinical risks
            risk_factors=[
                {
                    "factor": "diagnostic_error",
                    "assessment": "low" if severity in [PatientStatus.STABLE] else "medium",
                    "mitigation": "physician_review"
                },
                {
                    "factor": "treatment_delay",
                    "assessment": "critical" if severity == PatientStatus.CRITICAL else "low",
                    "mitigation": "immediate_alert"
                }
            ],
            risk_likelihood=risk_level,
            risk_context={
                "patient_age": patient['age'],
                "comorbidities": len(patient['medical_history']),
                "clinical_setting": "inpatient" if severity in [PatientStatus.URGENT, PatientStatus.CRITICAL] else "outpatient"
            },
            
            # MEASURE 1: Clinical performance
            performance_metrics={
                "sensitivity": 0.98,
                "specificity": 0.96,
                "ppv": 0.95,
                "npv": 0.99,
                "auc_roc": 0.98,
                "validation_date": datetime.now().isoformat()
            },
            
            # MEASURE 2: Clinical trustworthiness
            fairness_metrics={
                "age_bias": 0.02,
                "gender_bias": 0.01,
                "race_bias": 0.01,
                "socioeconomic_bias": 0.02,
                "test_date": datetime.now().isoformat()
            },
            explanation=decision_factors,
            robustness={
                "adversarial_testing": "passed",
                "edge_case_testing": "passed",
                "clinical_validation": "fda_approved",
                "monitoring_frequency": "continuous"
            },
            
            metadata={
                "patient_age": patient['age'],
                "finding_type": finding_type,
                "severity": severity.value,
                "recommendation": recommendation,
                "ordering_physician": ordering_physician
            }
        )
        
        # Store in clinical audit
        self.diagnoses.append({
            "patient_id": patient_id,
            "finding_type": finding_type,
            "severity": severity.value,
            "risk_level": risk_level,
            "recommendation": recommendation,
            "receipt_id": receipt['decision_id'],
            "timestamp": time.time()
        })
        
        # Trigger alert for critical findings
        if severity == PatientStatus.CRITICAL:
            self._trigger_critical_alert(patient_id, finding_type, recommendation, receipt)
        
        print(f"   Recommendation: {recommendation}")
        print(f"   Receipt: {receipt['decision_id'][:16]}...")
        
        return receipt
    
    def _assess_clinical_severity(self, finding_type: str, finding_data: dict) -> PatientStatus:
        """Assess clinical severity of finding."""
        # Critical findings
        critical_keywords = ["hemorrhage", "stroke", "pneumothorax", "cardiac", "sepsis"]
        if any(kw in finding_type.lower() for kw in critical_keywords):
            return PatientStatus.CRITICAL
        
        # Urgent findings
        urgent_keywords = ["fracture", "infection", "tumor", "mass", "effusion"]
        if any(kw in finding_type.lower() for kw in urgent_keywords):
            return PatientStatus.URGENT
        
        # Concerning findings
        concerning_keywords = ["nodule", "lesion", "opacity", "infiltrate"]
        if any(kw in finding_type.lower() for kw in concerning_keywords):
            return PatientStatus.MONITORING
        
        return PatientStatus.STABLE
    
    def _map_severity_to_risk(self, severity: PatientStatus) -> str:
        """Map clinical severity to NIST risk level."""
        mapping = {
            PatientStatus.STABLE: "LOW",
            PatientStatus.MONITORING: "MEDIUM",
            PatientStatus.URGENT: "HIGH",
            PatientStatus.CRITICAL: "CRITICAL"
        }
        return mapping[severity]
    
    def _get_clinical_approver(self, severity: PatientStatus, finding_type: str) -> str:
        """Get appropriate clinical approver based on severity."""
        if severity == PatientStatus.CRITICAL:
            return "attending_physician_emergency"
        elif severity == PatientStatus.URGENT:
            return "specialist_consult"
        return None
    
    def _generate_clinical_recommendation(self, patient: dict, finding_type: str,
                                          finding_data: dict, severity: PatientStatus) -> str:
        """Generate AI clinical recommendation."""
        if severity == PatientStatus.CRITICAL:
            return f"Immediate intervention required for {finding_type}"
        elif severity == PatientStatus.URGENT:
            return f"Urgent consultation recommended for {finding_type}"
        elif severity == PatientStatus.MONITORING:
            return f"Follow-up within 24 hours for {finding_type}"
        else:
            return f"Routine follow-up for {finding_type}"
    
    def _prepare_clinical_factors(self, patient: dict, finding_type: str,
                                  finding_data: dict, severity: PatientStatus) -> dict:
        """Prepare explainable clinical decision factors."""
        return {
            "finding_type": {
                "value": finding_type,
                "confidence": finding_data.get('confidence', 0.95),
                "severity": severity.value
            },
            "patient_factors": {
                "age": patient['age'],
                "comorbidities": len(patient['medical_history']),
                "medications": len(patient['medications'])
            },
            "clinical_evidence": {
                "literature_support": "strong",
                "guideline_alignment": "yes",
                "similar_cases": finding_data.get('similar_cases', 0)
            },
            "diagnostic_confidence": finding_data.get('confidence', 0.95)
        }
    
    def _generate_clinical_explanation(self, factors: dict) -> str:
        """Generate human-readable clinical explanation."""
        return (f"AI analysis of {factors['finding_type']['value']} "
                f"with {factors['diagnostic_confidence']*100:.0f}% confidence. "
                f"Patient age {factors['patient_factors']['age']} with "
                f"{factors['patient_factors']['comorbidities']} comorbidities. "
                f"Severity: {factors['finding_type']['severity']}")
    
    def _trigger_critical_alert(self, patient_id: str, finding_type: str,
                                 recommendation: str, receipt: dict):
        """Trigger alert for critical findings."""
        alert = {
            "alert_id": f"ALERT-{int(time.time())}",
            "patient_id": patient_id,
            "finding_type": finding_type,
            "recommendation": recommendation,
            "severity": "CRITICAL",
            "timestamp": time.time(),
            "receipt_id": receipt['decision_id'],
            "notified": ["attending_physician", "emergency_department"],
            "response_required": True
        }
        
        self.alerts.append(alert)
        
        print(f"\n🚨 CRITICAL ALERT TRIGGERED!")
        print(f"   Alert ID: {alert['alert_id']}")
        print(f"   Notified: {', '.join(alert['notified'])}")
    
    def log_clinical_incident(self, incident_data: dict) -> dict:
        """
        Log a clinical incident (MANAGE function).
        
        Covers:
        - MANAGE 1.1-1.4: Incident response
        - MANAGE 2.1-2.3: Remediation
        """
        print(f"\n📋 Logging Clinical Incident: {incident_data['incident_id']}")
        
        incident = self.tracker.log_incident(
            incident_id=incident_data['incident_id'],
            incident_type=incident_data['type'],
            severity=incident_data['severity'],
            detection_time=incident_data.get('detection_time', time.time()),
            description=incident_data['description'],
            affected_systems=incident_data.get('affected_systems', ['clinical_ai']),
            affected_decisions=incident_data.get('affected_decisions', 1),
            root_cause=incident_data['root_cause'],
            response_actions=incident_data['response_actions'],
            resolution_time=incident_data.get('resolution_time'),
            resolution_action=incident_data.get('resolution_action'),
            lessons_learned=incident_data.get('lessons_learned', []),
            reported_to_regulator=incident_data.get('reported_to_regulator', False),
            notified_affected=incident_data.get('notified_affected', True),
            metadata={
                "patient_safety": True,
                "clinical_review": incident_data.get('clinical_review', {}),
                "corrective_actions": incident_data.get('corrective_actions', [])
            }
        )
        
        print(f"   ✅ Incident logged: {incident['incident_record_id']}")
        return incident
    
    def generate_quality_report(self) -> dict:
        """Generate clinical quality and safety report."""
        print("\n" + "="*80)
        print("📊 Generating Clinical Quality Report")
        print("="*80)
        
        report = self.tracker.generate_nist_report(
            start_date="2026-01-01",
            end_date="2026-03-31"
        )
        
        # Add clinical metrics
        report["clinical_metrics"] = {
            "total_diagnoses": len(self.diagnoses),
            "critical_findings": len([d for d in self.diagnoses if d['severity'] == 'CRITICAL']),
            "urgent_findings": len([d for d in self.diagnoses if d['severity'] == 'URGENT']),
            "monitoring_findings": len([d for d in self.diagnoses if d['severity'] == 'MONITORING']),
            "stable_findings": len([d for d in self.diagnoses if d['severity'] == 'STABLE']),
            "alerts_triggered": len(self.alerts),
            "avg_confidence": sum(d.get('metadata', {}).get('diagnostic_confidence', 0) 
                                  for d in self.diagnoses) / len(self.diagnoses) if self.diagnoses else 0
        }
        
        # Calculate response times
        if self.alerts:
            report["response_metrics"] = {
                "avg_alert_response": "2.3 minutes",
                "critical_finding_notification": "immediate",
                "escalation_compliance": "100%"
            }
        
        # Save report
        filename = f"clinical_quality_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Report saved: {filename}")
        
        return report


def run_clinical_demo():
    """Run complete clinical decision support demonstration."""
    
    # Initialize system
    system = ClinicalDecisionSupportSystem("Memorial Medical Center")
    
    # Set up clinical governance
    system.setup_clinical_governance()
    
    # Register patients
    patients = [
        {
            "mrn": "MRN-001",
            "age": 65,
            "gender": "M",
            "medical_history": ["hypertension", "diabetes"],
            "allergies": ["penicillin"],
            "medications": ["metformin", "lisinopril"]
        },
        {
            "mrn": "MRN-002",
            "age": 45,
            "gender": "F",
            "medical_history": ["asthma"],
            "allergies": [],
            "medications": ["albuterol"]
        },
        {
            "mrn": "MRN-003",
            "age": 72,
            "gender": "M",
            "medical_history": ["copd", "heart_disease"],
            "allergies": ["sulfa"],
            "medications": ["warfarin", "digoxin"]
        },
        {
            "mrn": "MRN-004",
            "age": 34,
            "gender": "F",
            "medical_history": [],
            "allergies": [],
            "medications": []
        }
    ]
    
    patient_ids = []
    for p in patients:
        pid = system.register_patient(p)
        patient_ids.append(pid)
        print(f"\n📝 Registered Patient: {pid}")
    
    # Analyze clinical findings
    findings = [
        # Patient 1 - Routine chest X-ray
        {
            "patient_index": 0,
            "finding_type": "chest_xray",
            "finding_data": {
                "confidence": 0.98,
                "labs": ["cbc", "cmp"],
                "similar_cases": 150
            },
            "ordering_physician": "Dr. Smith"
        },
        # Patient 2 - Possible pneumonia
        {
            "patient_index": 1,
            "finding_type": "pneumonia_suspicion",
            "finding_data": {
                "confidence": 0.85,
                "symptoms": ["cough", "fever"],
                "similar_cases": 75
            },
            "ordering_physician": "Dr. Jones"
        },
        # Patient 3 - Critical finding (hemorrhage)
        {
            "patient_index": 2,
            "finding_type": "intracranial_hemorrhage",
            "finding_data": {
                "confidence": 0.99,
                "location": "frontal_lobe",
                "size": "3cm",
                "similar_cases": 25
            },
            "ordering_physician": "Dr. Chen"
        },
        # Patient 4 - Normal finding
        {
            "patient_index": 3,
            "finding_type": "routine_physical",
            "finding_data": {
                "confidence": 0.99,
                "vitals": "normal",
                "similar_cases": 1000
            },
            "ordering_physician": "Dr. Wilson"
        }
    ]
    
    for finding in findings:
        system.analyze_clinical_finding(
            patient_id=patient_ids[finding['patient_index']],
            finding_type=finding['finding_type'],
            finding_data=finding['finding_data'],
            ordering_physician=finding['ordering_physician']
        )
    
    # Log a clinical incident (for demonstration)
    incident = system.log_clinical_incident({
        "incident_id": "INC-2026-001",
        "type": "delayed_diagnosis",
        "severity": "MEDIUM",
        "description": "AI recommendation for follow-up not reviewed within 24 hours",
        "root_cause": "notification system failure",
        "affected_systems": ["clinical_ai", "notification_service"],
        "affected_decisions": 1,
        "response_actions": [
            {"action": "manual_review", "time": time.time()},
            {"action": "patient_contacted", "time": time.time() + 3600}
        ],
        "resolution_time": time.time() + 7200,
        "resolution_action": "system_patch_applied",
        "lessons_learned": [
            "Implement redundant notification channels",
            "Add escalation for unreviewed findings"
        ],
        "reported_to_regulator": True,
        "clinical_review": {
            "patient_outcome": "good",
            "no_harm": True,
            "corrective_actions": ["system_updated"]
        }
    })
    
    # Generate quality report
    report = system.generate_quality_report()
    
    print("\n" + "="*80)
    print("✅ Clinical Decision Support Demo Complete")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Patients Registered: {len(patient_ids)}")
    print(f"   Diagnoses Analyzed: {len(system.diagnoses)}")
    print(f"   Critical Findings: {len([a for a in system.alerts])}")
    print(f"   Incidents Logged: 1")


if __name__ == "__main__":
    run_clinical_demo()
