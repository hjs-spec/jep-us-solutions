#!/usr/bin/env python3
"""
NIST AI RMF Consumer Services Example
========================================

This example demonstrates a complete AI-powered consumer service platform
for a retail company, showing how JEP implements all four NIST AI RMF functions
in a consumer-facing environment.

Regulatory Compliance:
- FTC Consumer Protection Guidelines
- CCPA/CPRA (California)
- VCDPA (Virginia)
- Colorado Privacy Act
- NIST AI RMF
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum
import hashlib

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from nist-ai-rmf.implementation.nist_tracker import NISTComplianceTracker


class ConsumerSegment(Enum):
    """Consumer segments for personalization"""
    GENERAL = "general"
    PREMIUM = "premium"
    NEW = "new"
    LOYAL = "loyal"
    VIP = "vip"


class RecommendationType(Enum):
    """Types of consumer recommendations"""
    PRODUCT = "product"
    CONTENT = "content"
    SERVICE = "service"
    PROMOTION = "promotion"
    CROSS_SELL = "cross_sell"
    UP_SELL = "up_sell"


class ConsumerInteraction(Enum):
    """Types of consumer interactions"""
    PURCHASE = "purchase"
    VIEW = "view"
    SEARCH = "search"
    CART_ADD = "cart_add"
    CART_REMOVE = "cart_remove"
    WISHLIST = "wishlist"
    REVIEW = "review"
    COMPLAINT = "complaint"


class ConsumerServicesPlatform:
    """
    Complete consumer services platform with AI-powered personalization.
    
    Demonstrates NIST AI RMF implementation for:
    - Product recommendations
    - Personalized marketing
    - Consumer preference management
    - Purchase predictions
    - Consumer rights management
    """
    
    def __init__(self, company_name: str, platform_name: str = "ConsumerAI"):
        self.company_name = company_name
        self.platform_name = platform_name
        self.tracker = NISTComplianceTracker(
            organization=company_name,
            sector="consumer"
        )
        
        self.consumers = {}
        self.recommendations = []
        self.interactions = []
        self.consents = []
        self.opt_outs = []
        self.complaints = []
        
        print("="*80)
        print(f"🛍️ Consumer Services Platform - {company_name}")
        print(f"   Platform: {platform_name}")
        print("="*80)
    
    def setup_consumer_governance(self):
        """
        Set up NIST GOVERN function for consumer services.
        
        Covers:
        - GOVERN 1.1: Consumer protection policies
        - GOVERN 1.2: Roles (data scientists, privacy officers)
        - GOVERN 1.3: Consumer governance structure
        - GOVERN 3.1: Risk thresholds for consumer impact
        - GOVERN 3.2: Consumer complaint escalation
        """
        print("\n📋 Setting up Consumer Governance Framework")
        
        # GOVERN 1.1 & 1.3: Consumer protection framework
        governance = self.tracker.log_governance_framework(
            framework_version="2.0",
            effective_date="2026-01-01",
            accountability_principles=[
                {
                    "principle": "consumer_privacy",
                    "implementation": "All consumer data handled with care",
                    "owner": "Chief Privacy Officer"
                },
                {
                    "principle": "fair_personalization",
                    "implementation": "Recommendations must not discriminate",
                    "owner": "Ethics Committee"
                },
                {
                    "principle": "transparency",
                    "implementation": "Consumers must understand data use",
                    "owner": "Consumer Advocate"
                }
            ],
            governance_structure={
                "oversight_committee": "Consumer Trust Council",
                "members": ["CPO", "CDO", "Legal Counsel", "Consumer Advocate"],
                "meeting_frequency": "monthly",
                "consumer_complaint_escalation": "24_hours"
            }
        )
        print(f"   ✅ Consumer governance: {governance['framework_id']}")
        
        # GOVERN 1.2: Consumer service roles
        roles = self.tracker.log_roles([
            {
                "role": "data_scientist",
                "responsibilities": ["model_development", "personalization"],
                "supervision": "chief_data_officer"
            },
            {
                "role": "privacy_officer",
                "responsibilities": ["consent_management", "data_protection"],
                "supervision": "chief_privacy_officer"
            },
            {
                "role": "consumer_advocate",
                "responsibilities": ["complaint_resolution", "rights_enforcement"],
                "supervision": "consumer_relations_director"
            },
            {
                "role": "marketing_manager",
                "responsibilities": ["campaign_approval", "audience_selection"],
                "supervision": "cmo"
            }
        ])
        print(f"   ✅ Consumer roles defined: {len(roles['roles'])} positions")
        
        # GOVERN 3.1: Consumer impact thresholds
        thresholds = self.tracker.set_risk_thresholds({
            "LOW": {"max_impact": "minor_inconvenience", "review_notice": False},
            "MEDIUM": {"max_impact": "moderate_annoyance", "review_notice": True},
            "HIGH": {"max_impact": "financial_loss", "review_required": True},
            "CRITICAL": {"max_impact": "identity_risk", "immediate_action": True}
        })
        print(f"   ✅ Consumer risk thresholds configured")
        
        # GOVERN 3.2: Complaint escalation
        workflow = self.tracker.log_approval_workflow(
            risk_level="HIGH",
            approvers=["consumer_advocate", "privacy_officer", "legal_counsel"],
            conditions=["discrimination", "data_breach", "financial_harm"]
        )
        print(f"   ✅ Complaint escalation path defined")
        
        return governance
    
    def register_consumer(self, consumer_data: dict) -> str:
        """Register a new consumer with consent preferences."""
        
        # Hash PII for privacy
        consumer_id = f"CONS-{hashlib.sha256(consumer_data['email'].encode()).hexdigest()[:8]}"
        
        # Store consent preferences
        consent = {
            "consent_id": f"CONSENT-{int(time.time())}",
            "consumer_id": consumer_id,
            "purposes": consumer_data.get('consent_purposes', ['personalization', 'marketing']),
            "granted_at": time.time(),
            "expires_at": time.time() + 31536000,  # 1 year
            "status": "active",
            "channel": consumer_data.get('consent_channel', 'web'),
            "ip_address_hash": hashlib.sha256(consumer_data.get('ip', '').encode()).hexdigest()[:16] if 'ip' in consumer_data else None
        }
        
        self.consents.append(consent)
        
        # Store consumer profile
        self.consumers[consumer_id] = {
            "consumer_id": consumer_id,
            "age_range": consumer_data.get('age_range'),
            "location": consumer_data.get('location'),
            "preferences": consumer_data.get('preferences', {}),
            "consent_id": consent['consent_id'],
            "opt_out_status": False,
            "segment": consumer_data.get('segment', ConsumerSegment.GENERAL.value),
            "created_at": time.time(),
            "last_active": time.time()
        }
        
        print(f"   ✅ Consumer registered: {consumer_id}")
        print(f"      Consent ID: {consent['consent_id']}")
        print(f"      Purposes: {', '.join(consent['purposes'])}")
        
        return consumer_id
    
    def generate_recommendations(
        self,
        consumer_id: str,
        context: dict,
        recommendation_type: RecommendationType = RecommendationType.PRODUCT,
        limit: int = 10
    ) -> dict:
        """
        Generate personalized recommendations for consumer.
        
        Covers:
        - MAP 1.1-1.3: Consumer context
        - MAP 2.1-2.3: Consumer data governance
        - MAP 3.1-3.3: Personalization risks
        - MEASURE 1.1: Recommendation performance
        - MEASURE 2.1-2.4: Fairness metrics
        - MEASURE 3.1-3.3: Human oversight
        """
        print(f"\n🎯 Generating Recommendations for: {consumer_id}")
        print(f"   Type: {recommendation_type.value}")
        print(f"   Context: {context.get('page', 'homepage')}")
        
        consumer = self.consumers.get(consumer_id)
        if not consumer:
            raise ValueError(f"Consumer {consumer_id} not found")
        
        # Check consent
        consent = next((c for c in self.consents if c['consent_id'] == consumer['consent_id']), None)
        if not consent or 'personalization' not in consent['purposes']:
            print(f"   ⚠️ No consent for personalization - using default recommendations")
            return self._generate_default_recommendations(limit)
        
        # Check opt-out
        if consumer.get('opt_out_status'):
            print(f"   ⚠️ Consumer opted out - using default recommendations")
            return self._generate_default_recommendations(limit)
        
        # Generate AI recommendations
        recommendations = self._generate_ai_recommendations(consumer, context, recommendation_type, limit)
        
        # Analyze for fairness
        fairness_analysis = self._analyze_recommendation_fairness(recommendations, consumer)
        
        # Determine risk level
        risk_level = self._determine_recommendation_risk(recommendations, fairness_analysis)
        print(f"   Risk Level: {risk_level}")
        
        # Check if human review required
        human_reviewer = None
        if risk_level in ["HIGH", "CRITICAL"]:
            human_reviewer = "consumer_advocate-456"
            print(f"   ⚠️ Human review required: {human_reviewer}")
        
        # Log the recommendation decision
        receipt = self.tracker.log_decision(
            operation="GENERATE_RECOMMENDATIONS",
            resource=f"consumer/{consumer_id}/recommendations",
            actor_id="recommendation-engine-v2",
            risk_level=risk_level,
            human_approver=human_reviewer,
            reasoning=self._generate_recommendation_explanation(recommendations, fairness_analysis),
            
            # MAP 1: Consumer context
            purpose="personalization",
            stakeholders=[
                {"role": "consumer", "rights": ["opt_out", "explanation"]},
                {"role": "platform", "responsibility": "fair_recommendations"}
            ],
            deployment_context={
                "platform": self.platform_name,
                "page": context.get('page', 'unknown'),
                "device": context.get('device', 'web'),
                "timestamp": datetime.now().isoformat()
            },
            
            # MAP 2: Consumer data
            data_sources=[
                {
                    "source": "purchase_history",
                    "data_elements": ["product_ids", "categories", "amounts"]
                },
                {
                    "source": "browsing_history",
                    "data_elements": ["pages_viewed", "time_on_site"]
                },
                {
                    "source": "consumer_profile",
                    "data_elements": ["preferences", "segment"]
                }
            ],
            data_quality={
                "completeness": 0.95,
                "freshness": "real_time",
                "consent_verified": True
            },
            data_governance={
                "purpose_limited": True,
                "minimization_applied": True,
                "retention_policy": "2_years"
            },
            
            # MAP 3: Risks
            risk_factors=fairness_analysis.get('risk_factors', []),
            risk_likelihood=risk_level,
            risk_context={
                "consumer_segment": consumer['segment'],
                "recommendation_count": len(recommendations),
                "personalization_depth": context.get('personalization_depth', 'medium')
            },
            
            # MEASURE 1: Performance
            performance_metrics={
                "recommendation_count": len(recommendations),
                "generation_time_ms": 150,
                "model_version": "recommendation-v2.3",
                "confidence_scores": [r['confidence'] for r in recommendations]
            },
            
            # MEASURE 2: Trustworthiness
            fairness_metrics=fairness_analysis.get('fairness_metrics', {}),
            explanation={
                "recommendations": recommendations,
                "fairness_analysis": fairness_analysis
            },
            robustness={
                "fallback_available": True,
                "diversity_check": True,
                "novelty_check": True,
                "serendipity_score": 0.75
            },
            
            metadata={
                "consumer_id": consumer_id,
                "consumer_segment": consumer['segment'],
                "recommendation_type": recommendation_type.value,
                "recommendations": recommendations,
                "context": context
            }
        )
        
        # Store recommendations
        self.recommendations.append({
            "recommendation_id": receipt['decision_id'],
            "consumer_id": consumer_id,
            "timestamp": time.time(),
            "recommendations": recommendations,
            "receipt": receipt
        })
        
        return receipt
    
    def _generate_ai_recommendations(self, consumer: dict, context: dict, rec_type: RecommendationType, limit: int) -> list:
        """Generate AI-powered recommendations."""
        
        # Simulate AI recommendation engine
        recommendations = []
        
        # Sample product catalog
        products = [
            {"id": "P001", "name": "Wireless Headphones", "category": "electronics", "price": 99.99},
            {"id": "P002", "name": "Smart Watch", "category": "electronics", "price": 249.99},
            {"id": "P003", "name": "Yoga Mat", "category": "fitness", "price": 29.99},
            {"id": "P004", "name": "Coffee Maker", "category": "home", "price": 79.99},
            {"id": "P005", "name": "Running Shoes", "category": "apparel", "price": 89.99},
            {"id": "P006", "name": "Blender", "category": "home", "price": 129.99},
            {"id": "P007", "name": "Backpack", "category": "accessories", "price": 49.99},
            {"id": "P008", "name": "Fitness Tracker", "category": "electronics", "price": 59.99},
            {"id": "P009", "name": "Water Bottle", "category": "fitness", "price": 19.99},
            {"id": "P010", "name": "Desk Lamp", "category": "home", "price": 34.99}
        ]
        
        # Personalize based on consumer preferences
        for i in range(min(limit, len(products))):
            confidence = 0.95 - (i * 0.02)  # Decreasing confidence
            recommendations.append({
                "product": products[i],
                "score": confidence,
                "confidence": confidence,
                "reason": f"Based on your interest in {products[i]['category']}",
                "personalization_factors": [
                    {"factor": "purchase_history", "weight": 0.4},
                    {"factor": "browsing_history", "weight": 0.3},
                    {"factor": "similar_users", "weight": 0.2},
                    {"factor": "popular_items", "weight": 0.1}
                ]
            })
        
        return recommendations
    
    def _generate_default_recommendations(self, limit: int) -> dict:
        """Generate default (non-personalized) recommendations."""
        # Simplified for demo
        return {"recommendations": [], "type": "default", "personalized": False}
    
    def _analyze_recommendation_fairness(self, recommendations: list, consumer: dict) -> dict:
        """Analyze recommendations for fairness."""
        
        # Check for diversity
        categories = [r['product']['category'] for r in recommendations]
        unique_categories = len(set(categories))
        diversity_score = unique_categories / len(recommendations) if recommendations else 1.0
        
        # Check for price range distribution
        prices = [r['product']['price'] for r in recommendations]
        avg_price = sum(prices) / len(prices) if prices else 0
        price_diversity = max(prices) - min(prices) if prices else 0
        
        fairness_metrics = {
            "diversity_score": diversity_score,
            "category_coverage": unique_categories,
            "avg_price": avg_price,
            "price_range": price_diversity,
            "personalization_strength": 0.85
        }
        
        risk_factors = []
        if diversity_score < 0.5:
            risk_factors.append({"factor": "low_diversity", "score": diversity_score})
        if price_diversity > 100:
            risk_factors.append({"factor": "wide_price_range", "range": price_diversity})
        
        return {
            "fairness_metrics": fairness_metrics,
            "risk_factors": risk_factors,
            "overall_fairness": "ACCEPTABLE" if diversity_score >= 0.5 else "NEEDS_REVIEW"
        }
    
    def _determine_recommendation_risk(self, recommendations: list, fairness_analysis: dict) -> str:
        """Determine risk level of recommendations."""
        if not recommendations:
            return "LOW"
        
        if fairness_analysis.get('overall_fairness') == "NEEDS_REVIEW":
            return "MEDIUM"
        
        return "LOW"
    
    def _generate_recommendation_explanation(self, recommendations: list, fairness_analysis: dict) -> str:
        """Generate explanation for recommendations."""
        return f"Generated {len(recommendations)} recommendations with diversity score {fairness_analysis['fairness_metrics']['diversity_score']:.2f}"
    
    def log_consumer_interaction(
        self,
        consumer_id: str,
        interaction_type: ConsumerInteraction,
        interaction_data: dict
    ) -> dict:
        """Log consumer interaction for learning and audit."""
        
        interaction = {
            "interaction_id": f"INT-{int(time.time())}",
            "consumer_id": consumer_id,
            "type": interaction_type.value,
            "timestamp": time.time(),
            "data": interaction_data
        }
        
        receipt = self.tracker.log_decision(
            operation="CONSUMER_INTERACTION",
            resource=f"consumer/{consumer_id}/interaction",
            actor_id="tracking-service",
            risk_level="LOW",
            reasoning=f"Consumer {interaction_type.value} recorded",
            metadata=interaction
        )
        
        interaction['receipt_id'] = receipt['decision_id']
        self.interactions.append(interaction)
        
        # Update consumer last active
        if consumer_id in self.consumers:
            self.consumers[consumer_id]['last_active'] = time.time()
        
        return receipt
    
    def handle_opt_out(self, consumer_id: str, opt_out_data: dict) -> dict:
        """Handle consumer opt-out request."""
        
        consumer = self.consumers.get(consumer_id)
        if not consumer:
            raise ValueError(f"Consumer {consumer_id} not found")
        
        # Update consumer status
        consumer['opt_out_status'] = True
        consumer['opt_out_date'] = time.time()
        consumer['opt_out_reason'] = opt_out_data.get('reason', 'Not specified')
        
        # Update consent
        consent = next((c for c in self.consents if c['consent_id'] == consumer['consent_id']), None)
        if consent:
            consent['status'] = 'revoked'
            consent['revoked_at'] = time.time()
        
        opt_out_record = {
            "opt_out_id": f"OPT-{int(time.time())}",
            "consumer_id": consumer_id,
            "timestamp": time.time(),
            "reason": opt_out_data.get('reason'),
            "method": opt_out_data.get('method', 'web_form'),
            "channels": opt_out_data.get('channels', ['all'])
        }
        
        receipt = self.tracker.log_decision(
            operation="CONSUMER_OPT_OUT",
            resource=f"consumer/{consumer_id}/opt-out",
            actor_id="privacy-service",
            risk_level="MEDIUM",
            reasoning=f"Consumer opted out of personalization",
            metadata=opt_out_record
        )
        
        opt_out_record['receipt_id'] = receipt['decision_id']
        self.opt_outs.append(opt_out_record)
        
        print(f"\n🚫 Consumer Opt-Out Processed:")
        print(f"   Consumer: {consumer_id}")
        print(f"   Reason: {opt_out_record['reason']}")
        print(f"   Channels: {', '.join(opt_out_record['channels'])}")
        
        return receipt
    
    def handle_complaint(self, complaint_data: dict) -> dict:
        """Handle consumer complaint."""
        
        complaint = {
            "complaint_id": f"CMP-{int(time.time())}",
            "consumer_id": complaint_data['consumer_id'],
            "type": complaint_data['type'],
            "description": complaint_data['description'],
            "received_at": time.time(),
            "status": "OPEN",
            "priority": complaint_data.get('priority', 'MEDIUM'),
            "assigned_to": complaint_data.get('assigned_to', 'consumer_advocate'),
            "resolution_deadline": time.time() + 604800  # 7 days
        }
        
        # Determine risk level
        risk_level = "HIGH" if complaint['priority'] in ['HIGH', 'CRITICAL'] else "MEDIUM"
        
        receipt = self.tracker.log_decision(
            operation="CONSUMER_COMPLAINT",
            resource=f"consumer/{complaint['consumer_id']}/complaint",
            actor_id="complaint-service",
            risk_level=risk_level,
            human_approver=complaint['assigned_to'],
            reasoning=f"Consumer complaint: {complaint['type']}",
            metadata=complaint
        )
        
        complaint['receipt_id'] = receipt['decision_id']
        self.complaints.append(complaint)
        
        print(f"\n📝 Complaint Registered:")
        print(f"   Complaint ID: {complaint['complaint_id']}")
        print(f"   Type: {complaint['type']}")
        print(f"   Priority: {complaint['priority']}")
        print(f"   Assigned: {complaint['assigned_to']}")
        
        return receipt
    
    def generate_consumer_report(self) -> dict:
        """Generate consumer services compliance report."""
        
        print("\n" + "="*80)
        print("📊 Generating Consumer Services Report")
        print("="*80)
        
        report = self.tracker.generate_nist_report(
            start_date="2026-01-01",
            end_date="2026-03-31"
        )
        
        # Add consumer-specific metrics
        report["consumer_metrics"] = {
            "total_consumers": len(self.consumers),
            "active_consumers": len([c for c in self.consumers.values() if c['last_active'] > time.time() - 2592000]),  # 30 days
            "opt_out_rate": len(self.opt_outs) / len(self.consumers) if self.consumers else 0,
            "consent_rate": len([c for c in self.consents if c['status'] == 'active']) / len(self.consents) if self.consents else 0,
            "recommendations_generated": len(self.recommendations),
            "interactions_logged": len(self.interactions),
            "complaints_filed": len(self.complaints),
            "complaints_resolved": len([c for c in self.complaints if c.get('status') == 'RESOLVED']),
            "avg_response_time_hours": 24.5
        }
        
        # Save report
        filename = f"consumer_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Report saved: {filename}")
        
        return report


def run_consumer_demo():
    """Run complete consumer services demonstration."""
    
    # Initialize platform
    platform = ConsumerServicesPlatform(
        company_name="ShopEase",
        platform_name="Personalized Shopping Assistant"
    )
    
    # Set up governance
    platform.setup_consumer_governance()
    
    # Register consumers with different segments
    consumers = [
        {
            "email": "john.doe@example.com",
            "age_range": "35-50",
            "location": "California",
            "segment": ConsumerSegment.PREMIUM.value,
            "consent_purposes": ["personalization", "marketing", "analytics"],
            "preferences": {"categories": ["electronics", "fitness"]}
        },
        {
            "email": "jane.smith@example.com",
            "age_range": "25-34",
            "location": "New York",
            "segment": ConsumerSegment.LOYAL.value,
            "consent_purposes": ["personalization", "marketing"],
            "preferences": {"categories": ["home", "apparel"]}
        },
        {
            "email": "bob.wilson@example.com",
            "age_range": "51-65",
            "location": "Texas",
            "segment": ConsumerSegment.NEW.value,
            "consent_purposes": ["personalization"],
            "preferences": {"categories": ["electronics"]}
        },
        {
            "email": "alice.chen@example.com",
            "age_range": "18-24",
            "location": "Virginia",
            "segment": ConsumerSegment.GENERAL.value,
            "consent_purposes": ["personalization", "marketing", "analytics", "sharing"],
            "preferences": {"categories": ["fitness", "accessories"]}
        }
    ]
    
    consumer_ids = []
    for consumer in consumers:
        cid = platform.register_consumer(consumer)
        consumer_ids.append(cid)
    
    # Generate recommendations for different contexts
    contexts = [
        {"page": "homepage", "device": "mobile", "personalization_depth": "high"},
        {"page": "product_page", "device": "desktop", "personalization_depth": "medium"},
        {"page": "category_page", "device": "tablet", "personalization_depth": "low"}
    ]
    
    for i, cid in enumerate(consumer_ids[:3]):  # First 3 consumers
        platform.generate_recommendations(
            consumer_id=cid,
            context=contexts[i % len(contexts)],
            recommendation_type=RecommendationType.PRODUCT,
            limit=5
        )
    
    # Log consumer interactions
    interactions = [
        {"consumer_id": consumer_ids[0], "type": ConsumerInteraction.VIEW, "data": {"product_id": "P001", "time_seconds": 45}},
        {"consumer_id": consumer_ids[0], "type": ConsumerInteraction.CART_ADD, "data": {"product_id": "P001", "quantity": 1}},
        {"consumer_id": consumer_ids[1], "type": ConsumerInteraction.SEARCH, "data": {"query": "wireless headphones", "results": 15}},
        {"consumer_id": consumer_ids[2], "type": ConsumerInteraction.PURCHASE, "data": {"product_id": "P005", "amount": 89.99}}
    ]
    
    for interaction in interactions:
        platform.log_consumer_interaction(
            consumer_id=interaction['consumer_id'],
            interaction_type=interaction['type'],
            interaction_data=interaction['data']
        )
    
    # Handle opt-out
    platform.handle_opt_out(
        consumer_id=consumer_ids[2],
        opt_out_data={
            "reason": "Too many emails",
            "method": "preference_center",
            "channels": ["email", "push"]
        }
    )
    
    # Handle complaint
    platform.handle_complaint({
        "consumer_id": consumer_ids[3],
        "type": "inappropriate_recommendation",
        "description": "Received recommendations for adult products",
        "priority": "HIGH",
        "assigned_to": "consumer_advocate-456"
    })
    
    # Generate consumer report
    report = platform.generate_consumer_report()
    
    print("\n" + "="*80)
    print("✅ Consumer Services Demo Complete")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Consumers Registered: {len(consumer_ids)}")
    print(f"   Recommendations Generated: {len(platform.recommendations)}")
    print(f"   Interactions Logged: {len(platform.interactions)}")
    print(f"   Opt-Outs Processed: {len(platform.opt_outs)}")
    print(f"   Complaints Filed: {len(platform.complaints)}")


if __name__ == "__main__":
    run_consumer_demo()
```
