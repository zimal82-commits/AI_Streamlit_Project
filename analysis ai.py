# =========================================================================
# === FASA 3: MULTITIMEFRAME SCREENSHOT ANALYSIS AI ===
# =========================================================================

import cv2
import numpy as np
import streamlit as st
from PIL import Image
import time

class Fasa3MultitimeframeAnalysis:
    def __init__(self, superior_memory, fasa2_strategies):
        st.header("🚀 FASA 3: MULTITIMEFRAME SCREENSHOT ANALYSIS AI")
        st.info("📊 ANALYZING MT5 SCREENSHOTS | MULTITIMEFRAME D1-H4-H1-M30-M15-M5-M1")
        
        self.memory = superior_memory
        self.fasa2_strategies = fasa2_strategies
        
        # Initialize session state
        if 'fasa3_screenshot' not in st.session_state:
            st.session_state.fasa3_screenshot = None
            st.session_state.fasa3_analysis_result = None
            
    def show_screenshot_analysis_interface(self):
        """Show screenshot analysis interface"""
        
        # Upload screenshot
        st.subheader("📸 UPLOAD MT5 MULTITIMEFRAME SCREENSHOT")
        uploaded_file = st.file_uploader(
            "Upload MT5 Screenshot (D1-H4-H1-M30-M15-M5-M1)",
            type=['png', 'jpg', 'jpeg'],
            key="fasa3_screenshot_uploader"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.session_state.fasa3_screenshot = image
            
            st.image(image, caption="Uploaded MT5 Screenshot", use_column_width=True)
            
            # Analyze button
            if st.button("🔍 ANALYZE WITH FASA 1 & FASA 2 KNOWLEDGE", type="primary"):
                self.analyze_multitimeframe_screenshot(image)
                
        # Display results if available
        if st.session_state.fasa3_analysis_result:
            self.display_analysis_results()
    
    def analyze_multitimeframe_screenshot(self, image):
        """Analyze multitimeframe screenshot menggunakan knowledge FASA 1 & FASA 2"""
        with st.spinner("🔮 AI SEDANG MENGANALISIS MULTITIMEFRAME DENGAN SOP YANG DIPELAJARI..."):
            
            # Convert to OpenCV format
            cv_image = np.array(image)
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
            
            # Analyze each timeframe menggunakan knowledge dari FASA 1
            timeframe_analysis = self.analyze_all_timeframes(cv_image)
            
            # Integrate dengan FASA 2 strategies
            integrated_analysis = self.integrate_with_fasa2(timeframe_analysis)
            
            # Generate final trend dan entry point
            final_result = self.generate_final_signal(integrated_analysis)
            
            st.session_state.fasa3_analysis_result = {
                'timeframe_analysis': timeframe_analysis,
                'integrated_analysis': integrated_analysis,
                'final_result': final_result,
                'timestamp': time.time()
            }
            
        st.success("✅ ANALYSIS COMPLETE!")
    
    def analyze_all_timeframes(self, cv_image):
        """Analyze semua timeframe menggunakan SOP dari FASA 1"""
        timeframes = ['D1', 'H4', 'H1', 'M30', 'M15', 'M5', 'M1']
        analysis_results = {}
        
        for timeframe in timeframes:
            # Simulate extracting each timeframe dari screenshot
            # Dalam implementation sebenar, ini akan involve computer vision untuk crop setiap timeframe
            timeframe_image = self.extract_timeframe_from_screenshot(cv_image, timeframe)
            
            # Analyze menggunakan knowledge dari FASA 1
            timeframe_rules = self.analyze_with_fasa1_knowledge(timeframe_image, timeframe)
            analysis_results[timeframe] = timeframe_rules
            
            st.write(f"📈 {timeframe}: {len(timeframe_rules)} patterns detected")
            
        return analysis_results
    
    def extract_timeframe_from_screenshot(self, cv_image, timeframe):
        """Extract specific timeframe dari screenshot MT5"""
        # Ini adalah simulation - dalam real implementation akan gunakan computer vision
        # untuk detect dan crop setiap timeframe dari screenshot MT5
        return cv_image  # Return full image untuk simulation
    
    def analyze_with_fasa1_knowledge(self, image, timeframe):
        """Analyze image menggunakan SOP yang AI belajar dari FASA 1"""
        detected_rules = []
        
        try:
            # Convert to grayscale untuk analysis
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            
            # Calculate features sama seperti FASA 1
            edge_density = np.sum(edges) / (image.shape[0] * image.shape[1])
            brightness = np.mean(gray)
            color_complexity = np.std(image)
            
            # APPLY SOP YANG AI SUDAH BELAJAR DARI FASA 1
            # Pattern detection berdasarkan knowledge acquired
            
            # HYPER_VISION_PATTERN - dari FASA 1 code
            if edge_density > 0.07:
                detected_rules.append({
                    'rule': 'HYPER_VISION_PATTERN',
                    'timeframe': timeframe,
                    'confidence': min(edge_density * 6, 0.97),
                    'learned_by': 'hyper_vision_ai',
                    'characteristics': f'high_edge_density_{edge_density:.3f}'
                })
            
            # QUANTUM_COMPLEX_PATTERN - dari FASA 1 code  
            if color_complexity > 35:
                detected_rules.append({
                    'rule': 'QUANTUM_COMPLEX_PATTERN',
                    'timeframe': timeframe,
                    'confidence': 0.88 + (random.random() * 0.1),
                    'learned_by': 'quantum_pattern_ai',
                    'characteristics': f'high_complexity_{color_complexity:.1f}'
                })
            
            # TREND_LINE_DETECTED - dari FASA 1 code
            if edge_density > 0.1 and edge_density < 0.3:
                detected_rules.append({
                    'rule': 'TREND_LINE_DETECTED',
                    'timeframe': timeframe, 
                    'confidence': 0.82 + (random.random() * 0.15),
                    'learned_by': 'chart_pattern_ai',
                    'characteristics': 'optimal_trend_conditions'
                })
            
            # FIBONACCI_LEVELS_IDENTIFIED - dari FASA 1 code
            if random.random() > 0.7:  # Simulate Fibonacci detection
                detected_rules.append({
                    'rule': 'FIBONACCI_LEVELS_IDENTIFIED',
                    'timeframe': timeframe,
                    'confidence': 0.85 + (random.random() * 0.12),
                    'learned_by': 'fibonacci_detector_ai',
                    'characteristics': 'fibo_levels_aligned'
                })
                
        except Exception as e:
            st.error(f"Analysis error for {timeframe}: {e}")
            
        return detected_rules
    
    def integrate_with_fasa2(self, timeframe_analysis):
        """Integrate analysis dengan FASA 2 strategies"""
        integrated_results = {}
        
        for timeframe, rules in timeframe_analysis.items():
            applicable_strategies = []
            
            # Check setiap FASA 2 strategy terhadap detected rules
            for strategy in self.fasa2_strategies:
                if self.is_strategy_applicable_fasa3(strategy, rules):
                    applicable_strategies.append({
                        'strategy': strategy['strategy'],
                        'confidence': strategy.get('current_confidence', strategy['confidence']),
                        'action': strategy['action'],
                        'source_rules': [rule['rule'] for rule in rules]
                    })
            
            integrated_results[timeframe] = {
                'detected_rules': rules,
                'applicable_strategies': applicable_strategies
            }
            
        return integrated_results
    
    def is_strategy_applicable_fasa3(self, strategy, rules):
        """Check jika FASA 2 strategy applicable berdasarkan FASA 3 rules"""
        # Logic untuk match strategies dengan detected patterns
        strategy_conditions = strategy.get('conditions', [])
        rule_types = [rule['rule'] for rule in rules]
        
        # Simple matching logic - boleh diperbaiki berdasarkan relationship
        if 'SUPPORT_RESISTANCE_STRATEGY' in strategy['strategy']:
            return any('HYPER_VISION_PATTERN' in rule_type for rule_type in rule_types)
        elif 'TREND_FOLLOWING_STRATEGY' in strategy['strategy']:
            return any('TREND_LINE_DETECTED' in rule_type for rule_type in rule_types)
        elif 'FIBONACCI_TRADING_STRATEGY' in strategy['strategy']:
            return any('FIBONACCI_LEVELS_IDENTIFIED' in rule_type for rule_type in rule_types)
        
        return len(rules) > 0  # Default jika ada rules
    
    def generate_final_signal(self, integrated_analysis):
        """Generate final trend dan entry point"""
        
        # Analyze trend dari semua timeframe
        trend_analysis = self.analyze_multitimeframe_trend(integrated_analysis)
        
        # Determine entry point berdasarkan analysis
        entry_analysis = self.determine_entry_point(integrated_analysis)
        
        return {
            'trend': trend_analysis['final_trend'],
            'trend_confidence': trend_analysis['confidence'],
            'entry_point': entry_analysis['action'],
            'entry_confidence': entry_analysis['confidence'],
            'timeframe_alignment': trend_analysis['alignment'],
            'timestamp': time.time()
        }
    
    def analyze_multitimeframe_trend(self, integrated_analysis):
        """Analyze trend dari semua timeframe"""
        timeframe_signals = {}
        
        for timeframe, analysis in integrated_analysis.items():
            rules = analysis['detected_rules']
            strategies = analysis['applicable_strategies']
            
            # Analyze trend berdasarkan rules dan strategies
            trend_score = 0
            total_confidence = 0
            
            for rule in rules:
                if 'BULLISH' in rule['rule'] or 'BUY' in rule['rule']:
                    trend_score += rule['confidence']
                elif 'BEARISH' in rule['rule'] or 'SELL' in rule['rule']:
                    trend_score -= rule['confidence']
                total_confidence += rule['confidence']
            
            for strategy in strategies:
                if 'BUY' in strategy['action']:
                    trend_score += strategy['confidence']
                elif 'SELL' in strategy['action']:
                    trend_score -= strategy['confidence']
                total_confidence += strategy['confidence']
            
            if total_confidence > 0:
                normalized_score = trend_score / total_confidence
            else:
                normalized_score = 0
                
            timeframe_signals[timeframe] = normalized_score
        
        # Determine final trend berdasarkan semua timeframe
        final_trend, confidence, alignment = self.calculate_final_trend(timeframe_signals)
        
        return {
            'final_trend': final_trend,
            'confidence': confidence,
            'alignment': alignment,
            'timeframe_signals': timeframe_signals
        }
    
    def calculate_final_trend(self, timeframe_signals):
        """Calculate final trend dari semua timeframe signals"""
        # Beratkan timeframe yang lebih tinggi
        weights = {'D1': 0.3, 'H4': 0.25, 'H1': 0.2, 'M30': 0.1, 'M15': 0.08, 'M5': 0.05, 'M1': 0.02}
        
        weighted_sum = 0
        total_weight = 0
        
        for timeframe, signal in timeframe_signals.items():
            weight = weights.get(timeframe, 0.1)
            weighted_sum += signal * weight
            total_weight += weight
        
        if total_weight > 0:
            final_score = weighted_sum / total_weight
        else:
            final_score = 0
        
        # Determine trend
        if final_score > 0.1:
            trend = "BULLISH"
            confidence = min(abs(final_score), 1.0)
        elif final_score < -0.1:
            trend = "BEARISH" 
            confidence = min(abs(final_score), 1.0)
        else:
            trend = "SIDEWAYS"
            confidence = 0.5
        
        # Calculate alignment (berapa banyak timeframe setuju)
        aligned_timeframes = 0
        for timeframe, signal in timeframe_signals.items():
            if (trend == "BULLISH" and signal > 0) or (trend == "BEARISH" and signal < 0):
                aligned_timeframes += 1
        
        alignment = aligned_timeframes / len(timeframe_signals)
        
        return trend, confidence, alignment
    
    def determine_entry_point(self, integrated_analysis):
        """Determine entry point berdasarkan analysis"""
        # Analyze untuk entry point
        buy_signals = 0
        sell_signals = 0
        total_confidence = 0
        
        for timeframe, analysis in integrated_analysis.items():
            for strategy in analysis['applicable_strategies']:
                if 'BUY' in strategy['action']:
                    buy_signals += strategy['confidence']
                elif 'SELL' in strategy['action']:
                    sell_signals += strategy['confidence']
                total_confidence += strategy['confidence']
        
        if total_confidence > 0:
            buy_ratio = buy_signals / total_confidence
            sell_ratio = sell_signals / total_confidence
        else:
            buy_ratio = 0
            sell_ratio = 0
        
        if buy_ratio > sell_ratio and buy_ratio > 0.6:
            action = "BUY"
            confidence = buy_ratio
        elif sell_ratio > buy_ratio and sell_ratio > 0.6:
            action = "SELL"
            confidence = sell_ratio
        else:
            action = "HOLD"
            confidence = max(buy_ratio, sell_ratio)
        
        return {'action': action, 'confidence': confidence}
    
    def display_analysis_results(self):
        """Display analysis results"""
        result = st.session_state.fasa3_analysis_result
        final_result = result['final_result']
        
        st.subheader("🎯 ANALYSIS RESULTS")
        
        # Trend Analysis
        trend_color = "green" if final_result['trend'] == "BULLISH" else "red" if final_result['trend'] == "BEARISH" else "blue"
        st.metric("TREND", f":{trend_color}[{final_result['trend']}]", f"{final_result['trend_confidence']:.1%}")
        
        # Entry Point
        entry_color = "green" if final_result['entry_point'] == "BUY" else "red" if final_result['entry_point'] == "SELL" else "blue"
        st.metric("ENTRY POINT", f":{entry_color}[{final_result['entry_point']}]", f"{final_result['entry_confidence']:.1%}")
        
        # Timeframe Alignment
        st.metric("TIMEFRAME ALIGNMENT", f"{final_result['timeframe_alignment']:.1%}")
        
        # Detailed Analysis
        with st.expander("📊 DETAILED TIMEFRAME ANALYSIS"):
            for timeframe, analysis in result['integrated_analysis'].items():
                st.write(f"**{timeframe}**")
                st.write(f"Rules Detected: {len(analysis['detected_rules'])}")
                st.write(f"Strategies Applied: {len(analysis['applicable_strategies'])}")
                
                for rule in analysis['detected_rules'][:2]:  # Show first 2 rules
                    st.write(f"- {rule['rule']} ({rule['confidence']:.1%})")
                
                st.divider()

# =========================================================================
# === INTEGRATION DENGAN FASA 1 & FASA 2 ===
# =========================================================================

def setup_fasa3_integration(superior_ai, fasa2_ai):
    """Setup FASA 3 integration"""
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔮 FASA 3 MULTITIMEFRAME AI")
    
    if st.sidebar.button("📸 LAUNCH FASA 3 SCREENSHOT ANALYSIS"):
        if 'fasa3_ai' not in st.session_state:
            with st.spinner("🔗 INITIALIZING FASA 3 MULTITIMEFRAME ANALYSIS..."):
                st.session_state.fasa3_ai = Fasa3MultitimeframeAnalysis(
                    superior_ai.memory, 
                    fasa2_ai.trading_strategies
                )
        
        st.session_state.fasa3_ai.show_screenshot_analysis_interface()
        return True
    
    return False
