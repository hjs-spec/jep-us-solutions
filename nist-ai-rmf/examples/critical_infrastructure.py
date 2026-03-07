#!/usr/bin/env python3
"""
NIST AI RMF Critical Infrastructure Example
=============================================

This example demonstrates a complete AI-powered critical infrastructure
monitoring system for a power grid operator, showing how JEP implements all four
NIST AI RMF functions in a high-stakes infrastructure environment.

Regulatory Compliance:
- CISA Guidelines for Critical Infrastructure
- NERC CIP (Critical Infrastructure Protection) standards
- DHS AI Risk Management for Infrastructure
- NIST AI RMF
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from nist-ai-rmf.implementation.nist_tracker import NISTComplianceTracker


class InfrastructureSector(Enum):
    """Critical infrastructure sectors"""
    ENERGY = "energy"
    WATER = "water"
    TRANSPORTATION = "transportation"
    COMMUNICATIONS = "communications"
    FINANCIAL = "financial_services"
    HEALTHCARE = "healthcare"
    NUCLEAR = "nuclear"


class AlertSeverity(Enum):
    """Alert severity levels for infrastructure"""
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    EMERGENCY = "EMERGENCY"


class InfrastructureStatus(Enum):
    """Infrastructure component status"""
    NORMAL = "NORMAL"
    DEGRADED = "DEGRADED"
    OFFLINE = "OFFLINE"
    UNDER_ATTACK = "UNDER_ATTACK"
    MAINTENANCE = "MAINTENANCE"


class CriticalInfrastructureMonitor:
    """
    Complete critical infrastructure monitoring system.
    
    Demonstrates NIST AI RMF implementation for:
    - Power grid monitoring and control
    - Anomaly detection
    - Incident response
    - Safety-critical decisions
    """
    
    def __init__(self, utility_name: str, sector: InfrastructureSector = InfrastructureSector.ENERGY):
        self.utility_name = utility_name
        self.sector = sector
        self.tracker = NISTComplianceTracker(
            organization=utility_name,
            sector="critical_infrastructure"
        )
        
        self.components = {}
        self.incidents = []
        self.alerts = []
        self.maintenance_events = []
        
        print("="*80)
        print(f"⚡ Critical Infrastructure Monitor - {utility_name}")
        print(f"   Sector: {sector.value}")
        print("="*80)
    
    def setup_infrastructure_governance(self):
        """
        Set up NIST GOVERN function for critical infrastructure.
        
        Covers:
        - GOVERN 1.1: Safety accountability policies
        - GOVERN 1.2: Roles (operators, engineers, security)
        - GOVERN 1.3: Emergency governance structure
        - GOVERN 3.1: Risk thresholds for infrastructure
        - GOVERN 3.2: Escalation paths for emergencies
        """
        print("\n📋 Setting up Infrastructure Governance Framework")
        
        # GOVERN 1.1 & 1.3: Safety governance framework
        governance = self.tracker.log_governance_framework(
            framework_version="3.0",
            effective_date="2026-01-01",
            accountability_principles=[
                {
                    "principle": "public_safety",
                    "implementation": "All decisions prioritize public safety",
                    "owner": "Chief Safety Officer"
                },
                {
                    "principle": "grid_reliability",
                    "implementation": "Maintain N-1 redundancy at all times",
                    "owner": "Chief Engineer"
                },
                {
                    "principle": "emergency_response",
                    "implementation": "15-minute response for critical alerts",
                    "owner": "Incident Commander"
                }
            ],
            governance_structure={
                "oversight_committee": "Infrastructure Reliability Council",
                "members": ["CEO", "CISO", "Chief Engineer", "Safety Officer"],
                "meeting_frequency": "weekly",
                "emergency_protocol": "Immediate escalation to Incident Command"
            }
        )
        print(f"   ✅ Safety governance: {governance['framework_id']}")
        
        # GOVERN 1.2: Infrastructure roles
        roles = self.tracker.log_roles([
            {
                "role": "grid_operator",
                "responsibilities": ["real_time_monitoring", "load_balancing"],
                "certification": "NERC Certified Operator",
                "supervision": "shift_supervisor"
            },
            {
                "role": "security_analyst",
                "responsibilities": ["threat_detection", "incident_response"],
                "certification": "CISSP",
                "supervision": "CISO"
            },
            {
                "role": "maintenance_engineer",
                "responsibilities": ["equipment_inspection", "repair_coordination"],
                "certification": "Professional Engineer",
                "supervision": "chief_engineer"
            },
            {
                "role": "incident_commander",
                "responsibilities": ["emergency_coordination", "stakeholder_comms"],
                "certification": "ICS-300",
                "supervision": "director_operations"
            }
        ])
        print(f"   ✅ Critical roles defined: {len(roles['roles'])} positions")
        
        # GOVERN 3.1: Infrastructure risk thresholds
        thresholds = self.tracker.set_risk_thresholds({
            "LOW": {"max_impact": "minor_outage", "response_time": 60},
            "MEDIUM": {"max_impact": "local_outage", "response_time": 30},
            "HIGH": {"max_impact": "regional_outage", "response_time": 15},
            "CRITICAL": {"max_impact": "grid_instability", "response_time": 5}
        })
        print(f"   ✅ Risk thresholds configured")
        
        # GOVERN 3.2: Emergency escalation paths
        workflow = self.tracker.log_approval_workflow(
            risk_level="CRITICAL",
            approvers=["grid_operator", "incident_commander", "executive_director"],
            conditions=["grid_instability", "cyber_attack", "equipment_failure"]
        )
        print(f"   ✅ Emergency escalation path defined")
        
        return governance
    
    def register_infrastructure_component(self, component_data: dict) -> str:
        """Register an infrastructure component for monitoring."""
        component_id = f"COMP-{component_data['type']}-{int(time.time())}"
        
        self.components[component_id] = {
            "component_id": component_id,
            "type": component_data['type'],
            "location": component_data['location'],
            "capacity": component_data.get('capacity', 0),
            "status": InfrastructureStatus.NORMAL.value,
            "last_maintenance": component_data.get('last_maintenance'),
            "next_maintenance": component_data.get('next_maintenance'),
            "registration_date": time.time(),
            "metadata": component_data.get('metadata', {})
        }
        
        print(f"   ✅ Component registered: {component_id} ({component_data['type']})")
        return component_id
    
    def monitor_component(
        self,
        component_id: str,
        sensor_readings: dict,
        operator_id: str
    ) -> dict:
        """
        Monitor infrastructure component with AI-powered anomaly detection.
        
        Covers:
        - MAP 1.1-1.3: Infrastructure context
        - MAP 2.1-2.3: Sensor data governance
        - MAP 3.1-3.3: Infrastructure risks
        - MEASURE 1.1: System performance
        - MEASURE 2.1-2.4: Reliability metrics
        - MEASURE 3.1-3.3: Operator oversight
        """
        print(f"\n📡 Monitoring Component: {component_id}")
        
        component = self.components.get(component_id)
        if not component:
            raise ValueError(f"Component {component_id} not found")
        
        # Analyze sensor data for anomalies
        analysis = self._analyze_sensor_data(component, sensor_readings)
        print(f"   Status: {analysis['status']}")
        print(f"   Confidence: {analysis['confidence']:.1%}")
        
        # Determine risk level
        risk_level = self._determine_infrastructure_risk(analysis)
        print(f"   Risk Level: {risk_level}")
        
        # Check if human intervention required
        human_approver = None
        if risk_level in ["HIGH", "CRITICAL"]:
            human_approver = self._get_emergency_approver(risk_level)
            print(f"   Emergency Approver: {human_approver}")
        
        # Generate recommendation
        recommendation = self._generate_infrastructure_recommendation(
            component, analysis, risk_level
        )
        
        # Trigger alert if needed
        if analysis['status'] != InfrastructureStatus.NORMAL.value:
            self._trigger_alert(component_id, analysis, risk_level, recommendation)
        
        # Log the monitoring decision with full NIST compliance
        receipt = self.tracker.log_decision(
            operation="INFRASTRUCTURE_MONITORING",
            resource=f"component/{component_id}",
            actor_id=f"ai-monitor-{operator_id}",
            risk_level=risk_level,
            human_approver=human_approver,
            reasoning=self._generate_monitoring_explanation(analysis, recommendation),
            
            # MAP 1: Infrastructure context
            purpose="critical_infrastructure_monitoring",
            stakeholders=[
                {"role": "public", "safety": "primary"},
                {"role": "regulator", "oversight": "CISA, NERC"},
                {"role": "utility", "responsibility": "reliability"}
            ],
            deployment_context={
                "environment": "critical_infrastructure",
                "sector": self.sector.value,
                "facility": component['location'],
                "date": datetime.now().isoformat(),
                "version": "infrastructure-ai-v3.1"
            },
            
            # MAP 2: Sensor data
            data_sources=[
                {
                    "source": "scada_system",
                    "data_elements": list(sensor_readings.keys()),
                    "frequency": "real_time"
                },
                {
                    "source": "weather_service",
                    "data_elements": ["temperature", "wind", "precipitation"],
                    "frequency": "5_minutes"
                }
            ],
            data_quality={
                "completeness": 0.99,
                "accuracy": 0.98,
                "timeliness": "real_time",
                "calibration_date": time.time() - 86400  # Last 24h
            },
            data_governance={
                "nerc_cip_compliant": True,
                "data_retention": "5_years",
                "access_controlled": True,
                "audit_enabled": True
            },
            
            # MAP 3: Infrastructure risks
            risk_factors=analysis.get('risk_factors', []),
            risk_likelihood=risk_level,
            risk_context={
                "grid_impact": analysis.get('grid_impact', 'none'),
                "public_safety": analysis.get('public_safety_impact', 'none'),
                "economic_impact": analysis.get('economic_impact', 'none')
            },
            
            # MEASURE 1: Performance
            performance_metrics={
                "detection_accuracy": analysis['confidence'],
                "false_positive_rate": 0.02,
                "response_time_ms": analysis.get('response_time', 100),
                "uptime": "99.99%"
            },
            
            # MEASURE 2: Trustworthiness
            fairness_metrics={
                "geographic_coverage": "complete",
                "demographic_impact": "none",
                "reliability_by_region": 0.99
            },
            explanation={
                "sensor_analysis": analysis,
                "recommendation": recommendation
            },
            robustness={
                "redundancy": "N-1",
                "failover_tested": True,
                "cyber_防护": "NIST CSF compliant",
                "physical_security": "enforced"
            },
            
            metadata={
                "component_id": component_id,
                "component_type": component['type'],
                "sensor_readings": sensor_readings,
                "analysis": analysis,
                "recommendation": recommendation
            }
        )
        
        # Update component status
        component['status'] = analysis['status']
        component['last_check'] = time.time()
        
        return receipt
    
    def _analyze_sensor_data(self, component: dict, readings: dict) -> dict:
        """Analyze sensor data for anomalies."""
        # Simulate AI analysis
        status = InfrastructureStatus.NORMAL.value
        confidence = 0.99
        risk_factors = []
        
        # Check for anomalies (simplified)
        for sensor, value in readings.items():
            if sensor == "temperature" and value > 100:
                status = InfrastructureStatus.DEGRADED.value
                confidence = 0.95
                risk_factors.append({"factor": "overheating", "value": value})
            elif sensor == "vibration" and value > 0.5:
                status = InfrastructureStatus.DEGRADED.value
                confidence = 0.90
                risk_factors.append({"factor": "excessive_vibration", "value": value})
            elif sensor == "load" and value > 0.95:
                status = InfrastructureStatus.DEGRADED.value
                confidence = 0.92
                risk_factors.append({"factor": "high_load", "value": value})
            elif sensor == "cyber_threat" and value > 0:
                status = InfrastructureStatus.UNDER_ATTACK.value
                confidence = 0.98
                risk_factors.append({"factor": "cyber_threat_detected", "value": value})
        
        return {
            "status": status,
            "confidence": confidence,
            "risk_factors": risk_factors,
            "grid_impact": "local" if status != InfrastructureStatus.NORMAL.value else "none",
            "public_safety_impact": "none",
            "economic_impact": "low" if status != InfrastructureStatus.NORMAL.value else "none",
            "response_time": 150,
            "analysis_time": time.time()
        }
    
    def _determine_infrastructure_risk(self, analysis: dict) -> str:
        """Determine risk level based on analysis."""
        status = analysis['status']
        
        if status == InfrastructureStatus.UNDER_ATTACK.value:
            return "CRITICAL"
        elif status == InfrastructureStatus.DEGRADED.value:
            if analysis['confidence'] > 0.95:
                return "HIGH"
            return "MEDIUM"
        elif status == InfrastructureStatus.OFFLINE.value:
            return "CRITICAL"
        else:
            return "LOW"
    
    def _get_emergency_approver(self, risk_level: str) -> str:
        """Get emergency approver based on risk level."""
        if risk_level == "HIGH":
            return "shift_supervisor-456"
        elif risk_level == "CRITICAL":
            return "incident_commander-789"
        return None
    
    def _generate_infrastructure_recommendation(self, component: dict, analysis: dict, risk_level: str) -> str:
        """Generate recommendation based on analysis."""
        if risk_level == "CRITICAL":
            if analysis['status'] == InfrastructureStatus.UNDER_ATTACK.value:
                return "IMMEDIATE ISOLATION: Disconnect component from grid and initiate cybersecurity incident response"
            return "IMMEDIATE SHUTDOWN: Component requires emergency maintenance"
        elif risk_level == "HIGH":
            return "URGENT: Schedule maintenance within 24 hours"
        elif risk_level == "MEDIUM":
            return "Monitor closely; schedule maintenance within 7 days"
        else:
            return "Normal operation; continue routine monitoring"
    
    def _generate_monitoring_explanation(self, analysis: dict, recommendation: str) -> str:
        """Generate human-readable explanation."""
        return f"AI analysis detected {analysis['status']} with {analysis['confidence']:.1%} confidence. {recommendation}"
    
    def _trigger_alert(self, component_id: str, analysis: dict, risk_level: str, recommendation: str):
        """Trigger alert for infrastructure event."""
        alert = {
            "alert_id": f"ALERT-{int(time.time())}",
            "component_id": component_id,
            "timestamp": time.time(),
            "severity": AlertSeverity.CRITICAL.value if risk_level in ["HIGH", "CRITICAL"] else AlertSeverity.WARNING.value,
            "status": analysis['status'],
            "risk_factors": analysis['risk_factors'],
            "recommendation": recommendation,
            "notified": ["grid_operator", "incident_commander"] if risk_level == "CRITICAL" else ["grid_operator"],
            "response_required": risk_level in ["HIGH", "CRITICAL"]
        }
        
        self.alerts.append(alert)
        
        print(f"\n🚨 ALERT TRIGGERED!")
        print(f"   Alert ID: {alert['alert_id']}")
        print(f"   Severity: {alert['severity']}")
        print(f"   Notified: {', '.join(alert['notified'])}")
    
    def log_infrastructure_incident(self, incident_data: dict) -> dict:
        """
        Log infrastructure incident (MANAGE function).
        
        Covers:
        - MANAGE 1.1-1.4: Incident response
        - MANAGE 2.1-2.3: Remediation
        """
        print(f"\n📋 Logging Infrastructure Incident: {incident_data['incident_id']}")
        
        incident = self.tracker.log_incident(
            incident_id=incident_data['incident_id'],
            incident_type=incident_data['type'],
            severity=incident_data['severity'],
            detection_time=incident_data.get('detection_time', time.time()),
            description=incident_data['description'],
            affected_systems=incident_data.get('affected_systems', []),
            affected_decisions=incident_data.get('affected_decisions', 0),
            root_cause=incident_data['root_cause'],
            response_actions=incident_data['response_actions'],
            resolution_time=incident_data.get('resolution_time'),
            resolution_action=incident_data.get('resolution_action'),
            lessons_learned=incident_data.get('lessons_learned', []),
            reported_to_regulator=incident_data.get('reported_to_regulator', True),
            notified_affected=incident_data.get('notified_affected', True),
            metadata={
                "infrastructure_sector": self.sector.value,
                "components_affected": incident_data.get('components_affected', []),
                "customer_outage_minutes": incident_data.get('customer_outage_minutes', 0),
                "economic_impact": incident_data.get('economic_impact', 0)
            }
        )
        
        self.incidents.append(incident)
        print(f"   ✅ Incident logged: {incident['incident_record_id']}")
        
        return incident
    
    def schedule_maintenance(self, component_id: str, maintenance_data: dict) -> dict:
        """Schedule and track infrastructure maintenance."""
        
        maintenance = {
            "maintenance_id": f"MAINT-{int(time.time())}",
            "component_id": component_id,
            "scheduled_date": maintenance_data['scheduled_date'],
            "duration_hours": maintenance_data['duration_hours'],
            "type": maintenance_data['type'],
            "reason": maintenance_data['reason'],
            "technician": maintenance_data['technician'],
            "approver": maintenance_data['approver'],
            "status": "SCHEDULED",
            "created_at": time.time()
        }
        
        # Log maintenance decision
        receipt = self.tracker.log_decision(
            operation="SCHEDULE_MAINTENANCE",
            resource=f"component/{component_id}",
            actor_id=maintenance_data['technician'],
            risk_level="MEDIUM",
            human_approver=maintenance_data['approver'],
            reasoning=f"Scheduled {maintenance_data['type']} maintenance: {maintenance_data['reason']}",
            metadata=maintenance
        )
        
        maintenance['receipt_id'] = receipt['decision_id']
        self.maintenance_events.append(maintenance)
        
        # Update component
        if component_id in self.components:
            self.components[component_id]['status'] = InfrastructureStatus.MAINTENANCE.value
            self.components[component_id]['next_maintenance'] = maintenance_data['scheduled_date']
        
        print(f"\n🔧 Maintenance Scheduled:")
        print(f"   Component: {component_id}")
        print(f"   Date: {datetime.fromtimestamp(maintenance['scheduled_date'])}")
        print(f"   Technician: {maintenance['technician']}")
        
        return maintenance
    
    def generate_reliability_report(self) -> dict:
        """Generate infrastructure reliability report."""
        print("\n" + "="*80)
        print("📊 Generating Infrastructure Reliability Report")
        print("="*80)
        
        report = self.tracker.generate_nist_report(
            start_date="2026-01-01",
            end_date="2026-03-31"
        )
        
        # Add infrastructure-specific metrics
        report["infrastructure_metrics"] = {
            "total_components": len(self.components),
            "components_by_status": {
                "NORMAL": len([c for c in self.components.values() if c['status'] == 'NORMAL']),
                "DEGRADED": len([c for c in self.components.values() if c['status'] == 'DEGRADED']),
                "OFFLINE": len([c for c in self.components.values() if c['status'] == 'OFFLINE']),
                "MAINTENANCE": len([c for c in self.components.values() if c['status'] == 'MAINTENANCE'])
            },
            "alerts_triggered": len(self.alerts),
            "alerts_by_severity": {
                "INFO": len([a for a in self.alerts if a['severity'] == 'INFO']),
                "WARNING": len([a for a in self.alerts if a['severity'] == 'WARNING']),
                "CRITICAL": len([a for a in self.alerts if a['severity'] == 'CRITICAL']),
                "EMERGENCY": len([a for a in self.alerts if a['severity'] == 'EMERGENCY'])
            },
            "incidents": len(self.incidents),
            "maintenance_events": len(self.maintenance_events),
            "average_response_time_minutes": 4.5,
            "reliability_score": 0.9999,
            "n_1_compliant": True
        }
        
        # Save report
        filename = f"reliability_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Report saved: {filename}")
        
        return report


def run_infrastructure_demo():
    """Run complete critical infrastructure monitoring demonstration."""
    
    # Initialize system
    monitor = CriticalInfrastructureMonitor(
        utility_name="Regional Power Grid",
        sector=InfrastructureSector.ENERGY
    )
    
    # Set up governance
    monitor.setup_infrastructure_governance()
    
    # Register infrastructure components
    components = [
        {
            "type": "transformer",
            "location": "Substation A",
            "capacity": 100,
            "last_maintenance": time.time() - 7776000,  # 90 days ago
            "next_maintenance": time.time() + 7776000,  # 90 days from now
            "metadata": {"voltage": "138kV", "manufacturer": "Siemens"}
        },
        {
            "type": "generator",
            "location": "Power Plant 1",
            "capacity": 500,
            "last_maintenance": time.time() - 15552000,  # 180 days ago
            "next_maintenance": time.time() + 15552000,  # 180 days from now
            "metadata": {"fuel": "natural_gas", "efficiency": 0.92}
        },
        {
            "type": "transmission_line",
            "location": "Corridor 7",
            "capacity": 200,
            "last_maintenance": time.time() - 31104000,  # 360 days ago
            "next_maintenance": time.time() + 31104000,  # 360 days from now
            "metadata": {"length": "50km", "voltage": "345kV"}
        },
        {
            "type": "substation",
            "location": "Substation B",
            "capacity": 300,
            "last_maintenance": time.time() - 10368000,  # 120 days ago
            "next_maintenance": time.time() + 10368000,  # 120 days from now
            "metadata": {"breakers": 12, "transformers": 4}
        }
    ]
    
    component_ids = []
    for comp in components:
        cid = monitor.register_infrastructure_component(comp)
        component_ids.append(cid)
    
    # Normal monitoring scenario
    print("\n" + "="*80)
    print("📋 Normal Monitoring Scenario")
    print("="*80)
    
    monitor.monitor_component(
        component_id=component_ids[0],
        sensor_readings={
            "temperature": 75,
            "vibration": 0.1,
            "load": 0.65,
            "oil_pressure": 95,
            "cyber_threat": 0
        },
        operator_id="operator-123"
    )
    
    # Anomaly detection scenario
    print("\n" + "="*80)
    print("⚠️ Anomaly Detection Scenario")
    print("="*80)
    
    monitor.monitor_component(
        component_id=component_ids[1],
        sensor_readings={
            "temperature": 112,  # Overheating
            "vibration": 0.6,     # Excessive vibration
            "load": 0.98,         # High load
            "fuel_pressure": 85,
            "cyber_threat": 0
        },
        operator_id="operator-123"
    )
    
    # Cyber threat scenario
    print("\n" + "="*80)
    print("🚨 Cyber Threat Scenario")
    print("="*80)
    
    monitor.monitor_component(
        component_id=component_ids[2],
        sensor_readings={
            "temperature": 65,
            "vibration": 0.2,
            "load": 0.45,
            "anomaly_score": 0.95,
            "cyber_threat": 1  # Cyber threat detected
        },
        operator_id="operator-123"
    )
    
    # Schedule maintenance
    print("\n" + "="*80)
    print("🔧 Maintenance Scheduling")
    print("="*80)
    
    monitor.schedule_maintenance(
        component_id=component_ids[0],
        maintenance_data={
            "scheduled_date": time.time() + 604800,  # 7 days
            "duration_hours": 8,
            "type": "preventive",
            "reason": "Routine transformer maintenance",
            "technician": "engineer-456",
            "approver": "chief_engineer-789"
        }
    )
    
    # Log an infrastructure incident
    print("\n" + "="*80)
    print("📋 Infrastructure Incident")
    print("="*80)
    
    monitor.log_infrastructure_incident({
        "incident_id": "INC-2026-001",
        "type": "equipment_failure",
        "severity": "HIGH",
        "detection_time": time.time() - 7200,  # 2 hours ago
        "description": "Transformer failure at Substation A causing local outage",
        "affected_systems": ["Substation A", "Feeder 7", "Feeder 8"],
        "affected_decisions": 15000,
        "components_affected": [component_ids[0]],
        "customer_outage_minutes": 45,
        "economic_impact": 250000,
        "root_cause": "Insulation breakdown due to age",
        "response_actions": [
            {"action": "Isolate transformer", "time": time.time() - 7100},
            {"action": "Reroute power", "time": time.time() - 7000},
            {"action": "Deploy repair crew", "time": time.time() - 6800}
        ],
        "resolution_time": time.time() - 3600,
        "resolution_action": "Transformer repaired and returned to service",
        "lessons_learned": [
            "Implement more frequent thermography",
            "Update maintenance schedule",
            "Add redundant monitoring"
        ],
        "reported_to_regulator": True
    })
    
    # Generate reliability report
    report = monitor.generate_reliability_report()
    
    print("\n" + "="*80)
    print("✅ Critical Infrastructure Demo Complete")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Components Monitored: {len(component_ids)}")
    print(f"   Alerts Triggered: {len(monitor.alerts)}")
    print(f"   Incidents Logged: {len(monitor.incidents)}")
    print(f"   Maintenance Scheduled: {len(monitor.maintenance_events)}")


if __name__ == "__main__":
    run_infrastructure_demo()
