# =========================================================================
# === FASA 2: TRUE INTEGRATED MARKET AI - STREAMLIT VERSION ===
# =========================================================================

import time
import random
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# =========================================================================
# === KNOWLEDGE TRANSFORMATION ENGINE (SAMA SEPERTI SEBELUM) ===
# =========================================================================

class KnowledgeTransformation:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.vision_to_trading_map = {
            'HYPER_VISION_PATTERN': 'MARKET_MOMENTUM_STRATEGY',
            'QUANTUM_COMPLEX_PATTERN': 'ADVANCED_PATTERN_RECOGNITION',
            'SUPPORT_RESISTANCE_DETECTED': 'SUPPORT_RESISTANCE_STRATEGY',
            'TREND_LINE_DETECTED': 'TREND_FOLLOWING_STRATEGY',
            'CHANNEL_PATTERN': 'CHANNEL_TRADING_STRATEGY',
            'FIBONACCI_LEVELS_IDENTIFIED': 'FIBONACCI_TRADING_STRATEGY',
            'POTENTIAL_ENTRY_SIGNAL': 'PRECISION_ENTRY_STRATEGY',
            'STRONG_TREND_IDENTIFIED': 'TREND_MOMENTUM_STRATEGY',
            'LOW_RISK_SETUP': 'RISK_OPTIMIZED_STRATEGY',
            'META_LEARNING_OPTIMIZED': 'ADAPTIVE_LEARNING_STRATEGY',
            'ADVANCED_CHART_ANALYSIS': 'CHART_PATTERN_STRATEGY',
            'MARKET_STRUCTURE_CONFIRMED': 'STRUCTURE_BASED_STRATEGY'
        }

    def transform_vision_rules(self):
        """Transform semua vision rules dari FASA 1 menjadi trading strategies"""
        trading_strategies = []

        st.info("🔄 TRANSFORMING FASA 1 KNOWLEDGE TO TRADING STRATEGIES...")

        for rule in self.memory.learned_knowledge['sop_rules']:
            strategy = self._create_trading_strategy(rule)
            if strategy:
                trading_strategies.append(strategy)
                st.success(f"✅ {rule.get('rule', 'Unknown')} → {strategy['strategy']}")

        st.success(f"🎯 TOTAL STRATEGIES CREATED: {len(trading_strategies)}")
        return trading_strategies

    def _create_trading_strategy(self, vision_rule):
        """Create trading strategy dari vision rule"""
        rule_type = vision_rule.get('rule', '')
        confidence = vision_rule.get('confidence', 0.5)
        learned_by = vision_rule.get('learned_by', 'unknown_ai')

        # Mapping berdasarkan rule type
        if 'SUPPORT' in rule_type or 'RESISTANCE' in rule_type:
            return {
                'strategy': 'SUPPORT_RESISTANCE_STRATEGY',
                'conditions': ['price_near_key_level', 'rejection_signals'],
                'action': 'BUY_AT_SUPPORT_SELL_AT_RESISTANCE',
                'confidence': confidence,
                'source_rule': rule_type,
                'learned_from': learned_by,
                'risk_level': 'LOW',
                'performance': {'wins': 0, 'losses': 0, 'total': 0}
            }

        elif 'TREND' in rule_type:
            return {
                'strategy': 'TREND_FOLLOWING_STRATEGY',
                'conditions': ['confirmed_trend_direction', 'momentum_alignment'],
                'action': 'FOLLOW_TREND_WITH_MOMENTUM',
                'confidence': confidence,
                'source_rule': rule_type,
                'learned_from': learned_by,
                'risk_level': 'MEDIUM',
                'performance': {'wins': 0, 'losses': 0, 'total': 0}
            }

        elif 'FIBONACCI' in rule_type:
            return {
                'strategy': 'FIBONACCI_RETRACEMENT_STRATEGY',
                'conditions': ['price_at_fibo_level', 'confluence_signals'],
                'action': 'TRADE_FIBO_LEVELS',
                'confidence': confidence,
                'source_rule': rule_type,
                'learned_from': learned_by,
                'risk_level': 'MEDIUM',
                'performance': {'wins': 0, 'losses': 0, 'total': 0}
            }

        elif 'ENTRY' in rule_type or 'BUY' in rule_type or 'SELL' in rule_type:
            return {
                'strategy': 'PRECISION_ENTRY_STRATEGY',
                'conditions': ['multiple_confluence', 'low_risk_setup'],
                'action': 'PRECISION_ENTRY_EXECUTION',
                'confidence': confidence,
                'source_rule': rule_type,
                'learned_from': learned_by,
                'risk_level': 'MEDIUM_HIGH',
                'performance': {'wins': 0, 'losses': 0, 'total': 0}
            }

        elif 'PATTERN' in rule_type:
            return {
                'strategy': 'PATTERN_RECOGNITION_STRATEGY',
                'conditions': ['chart_pattern_confirmed', 'volume_confirmation'],
                'action': 'TRADE_PATTERN_BREAKOUT',
                'confidence': confidence,
                'source_rule': rule_type,
                'learned_from': learned_by,
                'risk_level': 'MEDIUM',
                'performance': {'wins': 0, 'losses': 0, 'total': 0}
            }

        # Default strategy untuk rules yang tidak specific
        return {
            'strategy': 'ADAPTIVE_LEARNING_STRATEGY',
            'conditions': ['market_analysis', 'risk_assessment'],
            'action': 'ADAPTIVE_POSITION_SIZING',
            'confidence': confidence,
            'source_rule': rule_type,
            'learned_from': learned_by,
            'risk_level': 'VARIABLE',
            'performance': {'wins': 0, 'losses': 0, 'total': 0}
        }

# =========================================================================
# === ADAPTIVE LEARNING SYSTEM (SAMA) ===
# =========================================================================

class AdaptiveLearningSystem:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.strategy_performance = {}
        self.learning_history = []

    def update_strategy_performance(self, strategy_name, trade_result):
        """Update performance tracking untuk setiap strategy"""
        if strategy_name not in self.strategy_performance:
            self.strategy_performance[strategy_name] = {
                'total_trades': 0,
                'winning_trades': 0,
                'total_profit': 0.0,
                'win_rate': 0.0,
                'average_profit': 0.0,
                'last_updated': time.time()
            }

        perf = self.strategy_performance[strategy_name]
        perf['total_trades'] += 1

        if trade_result['profitable']:
            perf['winning_trades'] += 1
            perf['total_profit'] += trade_result['profit_dollars']

        perf['win_rate'] = perf['winning_trades'] / perf['total_trades']
        perf['average_profit'] = perf['total_profit'] / perf['total_trades']
        perf['last_updated'] = time.time()

        # Record learning experience
        self.learning_history.append({
            'timestamp': time.time(),
            'strategy': strategy_name,
            'result': 'WIN' if trade_result['profitable'] else 'LOSS',
            'profit': trade_result['profit_dollars'],
            'lesson': self._extract_lesson(strategy_name, trade_result)
        })

    def _extract_lesson(self, strategy_name, trade_result):
        """Extract specific lesson dari trade result"""
        if trade_result['profitable']:
            return f"{strategy_name} performed well in current market conditions"
        else:
            return f"{strategy_name} needs adjustment for current market conditions"

    def get_strategy_confidence_boost(self, strategy_name):
        """Calculate confidence boost berdasarkan performance"""
        if strategy_name not in self.strategy_performance:
            return 1.0  # Default multiplier

        perf = self.strategy_performance[strategy_name]
        win_rate = perf['win_rate']

        if win_rate > 0.7:
            return 1.3  # 30% confidence boost
        elif win_rate > 0.6:
            return 1.15  # 15% confidence boost
        elif win_rate < 0.4:
            return 0.8   # 20% confidence reduction
        else:
            return 1.0   # No change

    def create_new_strategy(self, market_conditions, successful_patterns):
        """Create new strategy berdasarkan market experience"""
        strategy_id = f"LEARNED_STRATEGY_{int(time.time())}"

        # Analyze successful patterns untuk buat strategy baru
        if 'high_volatility' in market_conditions and 'breakout' in successful_patterns:
            return {
                'strategy': 'VOLATILITY_BREAKOUT_STRATEGY',
                'conditions': ['high_volatility', 'consolidation_breakout'],
                'action': 'TRADE_BREAKOUT_WITH_VOLATILITY',
                'confidence': 0.75,
                'source_rule': 'MARKET_EXPERIENCE',
                'learned_from': 'adaptive_learning_system',
                'risk_level': 'HIGH',
                'performance': {'wins': 0, 'losses': 0, 'total': 0},
                'created_at': time.time()
            }
        elif 'low_volatility' in market_conditions and 'range' in successful_patterns:
            return {
                'strategy': 'RANGE_BOUND_STRATEGY',
                'conditions': ['low_volatility', 'clear_support_resistance'],
                'action': 'BUY_LOW_SELL_HIGH_RANGE',
                'confidence': 0.70,
                'source_rule': 'MARKET_EXPERIENCE',
                'learned_from': 'adaptive_learning_system',
                'risk_level': 'LOW',
                'performance': {'wins': 0, 'losses': 0, 'total': 0},
                'created_at': time.time()
            }

        return None

# =========================================================================
# === TRUE INTEGRATED MARKET AI - STREAMLIT VERSION ===
# =========================================================================

class TrueIntegratedMarketAIStreamlit:
    def __init__(self, memory_system):
        st.header("🧠 FASA 2: TRUE INTEGRATED MARKET AI")
        st.info("🔗 CONTINUOUS LEARNING FROM FASA 1 | ADAPTIVE STRATEGY DEVELOPMENT")

        self.memory = memory_system
        self.knowledge_transformer = KnowledgeTransformation(memory_system)
        self.adaptive_learner = AdaptiveLearningSystem(memory_system)

        # Initialize session state untuk FASA 2
        if 'fasa2_initialized' not in st.session_state:
            st.session_state.fasa2_initialized = True
            st.session_state.is_learning_running = False
            st.session_state.learning_cycles = 0
            st.session_state.trading_stats = {
                'total_signals': 0,
                'profitable_signals': 0,
                'total_profit': 0.0,
                'win_rate': 0.0,
                'learning_cycles': 0,
                'strategies_developed': 0,
                'ai_intelligence_growth': 0
            }
            st.session_state.market_data_history = []
            st.session_state.current_analysis = {}
            st.session_state.last_update = time.time()

        # Transform FASA 1 knowledge ke trading strategies
        with st.spinner("🔄 Transforming FASA 1 knowledge to trading strategies..."):
            self.trading_strategies = self.knowledge_transformer.transform_vision_rules()
            st.session_state.trading_stats['strategies_developed'] = len(self.trading_strategies)

        st.success(f"✅ INTEGRATED AI READY: {len(self.trading_strategies)} strategies from FASA 1")

    def show_integrated_dashboard(self):
        """Show main integrated dashboard"""
        
        # Display integration status
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📚 SOP Rules", len(self.memory.learned_knowledge['sop_rules']))
        with col2:
            st.metric("🎯 Strategies", len(self.trading_strategies))
        with col3:
            st.metric("🧠 AI Intelligence", f"{self.memory.performance_stats['ai_intelligence']}%")
        with col4:
            st.metric("📈 Learning Cycles", st.session_state.learning_cycles)

        st.markdown("---")

        # Control panel
        st.subheader("🎯 INTEGRATED AI CONTROLS")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🚀 START INTEGRATED LEARNING", type="primary", use_container_width=True):
                self.start_integrated_learning()
        
        with col2:
            if st.button("⏹️ STOP LEARNING", use_container_width=True):
                self.stop_integrated_learning()
        
        with col3:
            if st.button("🔄 SINGLE LEARNING CYCLE", use_container_width=True):
                self.single_learning_cycle()

        # Real-time dashboard
        self.show_realtime_dashboard()

        # Additional analysis sections
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Strategy Analysis", "📈 Learning Progress", "🤖 AI Intelligence", "🔍 Market Analysis"])

        with tab1:
            self.show_strategy_analysis()
        
        with tab2:
            self.show_learning_progress()
        
        with tab3:
            self.show_ai_intelligence()
        
        with tab4:
            self.show_market_analysis()

    def start_integrated_learning(self):
        """Start continuous learning"""
        st.session_state.is_learning_running = True
        st.success("🧠 INTEGRATED LEARNING STARTED - AI is learning from market experience!")
        
        # Simulate continuous learning dengan automatic refresh
        st.rerun()

    def stop_integrated_learning(self):
        """Stop continuous learning"""
        st.session_state.is_learning_running = False
        st.warning("🛑 INTEGRATED LEARNING STOPPED")
        
        # Show final performance
        stats = st.session_state.trading_stats
        st.info(f"""
        📊 **Final Performance:**
        - Win Rate: {stats['win_rate']:.1%}
        - Total Profit: ${stats['total_profit']:.2f}
        - Learning Cycles: {stats['learning_cycles']}
        - Strategies Developed: {stats['strategies_developed']}
        """)

    def single_learning_cycle(self):
        """Execute single learning cycle"""
        market_data = self.get_advanced_market_data()
        st.session_state.market_data_history.append(market_data)
        
        analysis = self.analyze_with_learned_strategies(market_data)
        st.session_state.current_analysis = analysis
        
        # Execute trade jika ada signal kuat
        if analysis['signal_strength'] > 0.7:
            trade_result = self.execute_learning_trade(analysis, market_data)
            self.update_learning_stats(trade_result)
            self.adaptive_learning_update(analysis, trade_result)
        
        st.session_state.learning_cycles += 1
        st.session_state.trading_stats['learning_cycles'] = st.session_state.learning_cycles
        st.session_state.last_update = time.time()
        
        st.success(f"🔁 Learning Cycle #{st.session_state.learning_cycles} Completed!")

    def show_realtime_dashboard(self):
        """Show real-time learning dashboard"""
        st.subheader("📊 REAL-TIME LEARNING DASHBOARD")
        
        if st.session_state.current_analysis:
            analysis = st.session_state.current_analysis
            market_data = self.get_advanced_market_data() if not st.session_state.market_data_history else st.session_state.market_data_history[-1]
            
            # Current market info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💰 EUR/USD Price", f"{market_data['price']:.4f}")
            with col2:
                st.metric("📈 Volatility", f"{market_data['volatility']:.2f}")
            with col3:
                st.metric("🎯 Trend Strength", f"{market_data['trend_strength']:.1f}%")
            
            # Trading signal
            signal_color = "green" if analysis['signal'] == 'BUY' else "red" if analysis['signal'] == 'SELL' else "gray"
            st.markdown(f"### 🎯 TRADING SIGNAL: :{signal_color}[{analysis['signal']}]")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💪 Signal Strength", f"{analysis['signal_strength']:.1%}")
            with col2:
                st.metric("🔍 Confidence", f"{analysis['confidence']:.1%}")
            with col3:
                st.metric("📚 Strategies Used", analysis['strategy_count'])
            
            # Performance metrics
            stats = st.session_state.trading_stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📈 Win Rate", f"{stats['win_rate']:.1%}")
            with col2:
                st.metric("💰 Total Profit", f"${stats['total_profit']:.2f}")
            with col3:
                st.metric("🧠 AI Growth", f"{stats['ai_intelligence_growth']:.1f}%")
            
            # Active strategies
            if analysis['strategies_used']:
                st.write("**🤖 STRATEGIES ACTIVATED:**")
                for strategy in analysis['strategies_used'][:4]:
                    st.write(f"• {strategy}")
        else:
            st.info("🔄 No learning data yet. Start learning to see real-time analysis.")

    def analyze_with_learned_strategies(self, market_data):
        """Analyze market dengan strategies yang dipelajari dari FASA 1"""
        applicable_strategies = []

        # Check setiap strategy terhadap market conditions
        for strategy in self.trading_strategies:
            if self.evaluate_strategy_conditions(strategy, market_data):
                # Apply confidence boost berdasarkan performance
                confidence_boost = self.adaptive_learner.get_strategy_confidence_boost(strategy['strategy'])
                strategy['current_confidence'] = strategy['confidence'] * confidence_boost
                applicable_strategies.append(strategy)

        # Jika tidak ada strategy yang applicable, buat strategy baru
        if not applicable_strategies:
            new_strategy = self.adaptive_learner.create_new_strategy(
                self.get_market_conditions(market_data),
                ['adaptive_learning']  # Default pattern
            )
            if new_strategy:
                applicable_strategies.append(new_strategy)
                self.trading_strategies.append(new_strategy)
                st.session_state.trading_stats['strategies_developed'] += 1

        return self.calculate_integrated_signal(applicable_strategies, market_data)

    def evaluate_strategy_conditions(self, strategy, market_data):
        """Evaluate jika strategy conditions match market data"""
        conditions = strategy.get('conditions', [])

        for condition in conditions:
            if condition == 'price_near_key_level':
                if not self.is_price_near_key_level(market_data):
                    return False
            elif condition == 'confirmed_trend_direction':
                if not self.has_confirmed_trend(market_data):
                    return False
            elif condition == 'price_at_fibo_level':
                if not self.is_price_at_fibo_level(market_data):
                    return False
            elif condition == 'multiple_confluence':
                if not self.has_multiple_confluence(market_data):
                    return False
            elif condition == 'chart_pattern_confirmed':
                if not self.is_chart_pattern_confirmed(market_data):
                    return False
            elif condition == 'high_volatility':
                if market_data['volatility'] < 1.2:
                    return False
            elif condition == 'low_volatility':
                if market_data['volatility'] > 0.8:
                    return False
            elif condition == 'consolidation_breakout':
                if not self.is_consolidation_breakout(market_data):
                    return False

        return True

    def calculate_integrated_signal(self, strategies, market_data):
        """Calculate signal berdasarkan strategies yang applicable"""
        if not strategies:
            return {
                'signal': 'HOLD',
                'signal_strength': 0.0,
                'confidence': 0.5,
                'strategies_used': [],
                'reason': 'No strategies match current market conditions'
            }

        # Calculate signal strength berdasarkan strategy confidence
        total_confidence = sum(s.get('current_confidence', s['confidence']) for s in strategies)
        avg_confidence = total_confidence / len(strategies)

        # Determine signal direction
        buy_strategies = [s for s in strategies if 'BUY' in s.get('action', '')]
        sell_strategies = [s for s in strategies if 'SELL' in s.get('action', '')]

        if len(buy_strategies) > len(sell_strategies):
            signal = 'BUY'
            direction_strength = len(buy_strategies) / len(strategies)
        elif len(sell_strategies) > len(buy_strategies):
            signal = 'SELL'
            direction_strength = len(sell_strategies) / len(strategies)
        else:
            signal = 'HOLD'
            direction_strength = 0.5

        signal_strength = avg_confidence * direction_strength

        return {
            'signal': signal,
            'signal_strength': signal_strength,
            'confidence': avg_confidence,
            'strategies_used': [s['strategy'] for s in strategies],
            'source_rules': [s['source_rule'] for s in strategies],
            'strategy_count': len(strategies),
            'reason': f"Based on {len(strategies)} learned strategies from FASA 1"
        }

    def execute_learning_trade(self, analysis, market_data):
        """Execute trade dan update learning"""
        # Simulate trade execution
        entry_price = market_data['price']

        if analysis['signal'] == 'BUY':
            # Simulate buy trade dengan probability berdasarkan confidence
            if random.random() < analysis['confidence']:
                exit_price = entry_price + np.random.uniform(0.0008, 0.0020)  # Profit
                profitable = True
            else:
                exit_price = entry_price - np.random.uniform(0.0005, 0.0012)  # Loss
                profitable = False
        else:  # SELL
            if random.random() < analysis['confidence']:
                exit_price = entry_price - np.random.uniform(0.0008, 0.0020)  # Profit
                profitable = True
            else:
                exit_price = entry_price + np.random.uniform(0.0005, 0.0012)  # Loss
                profitable = False

        profit_pips = abs(exit_price - entry_price) * 10000
        profit_dollars = profit_pips * 10  # $10 per pip

        if not profitable:
            profit_dollars = -profit_dollars

        trade_result = {
            'signal': analysis['signal'],
            'entry_price': entry_price,
            'exit_price': exit_price,
            'profit_pips': profit_pips if profitable else -profit_pips,
            'profit_dollars': profit_dollars,
            'profitable': profitable,
            'confidence': analysis['confidence']
        }

        return trade_result

    def update_learning_stats(self, trade_result):
        """Update learning statistics"""
        st.session_state.trading_stats['total_signals'] += 1

        if trade_result['profitable']:
            st.session_state.trading_stats['profitable_signals'] += 1
            st.session_state.trading_stats['total_profit'] += trade_result['profit_dollars']

        # Update win rate
        if st.session_state.trading_stats['total_signals'] > 0:
            st.session_state.trading_stats['win_rate'] = (
                st.session_state.trading_stats['profitable_signals'] / st.session_state.trading_stats['total_signals']
            )

        # Update AI intelligence growth
        st.session_state.trading_stats['ai_intelligence_growth'] = min(
            st.session_state.trading_stats['learning_cycles'] * 0.5 +
            st.session_state.trading_stats['win_rate'] * 50,
            100
        )

    def adaptive_learning_update(self, analysis, trade_result):
        """Update strategies berdasarkan trade results"""
        for strategy_name in analysis['strategies_used']:
            self.adaptive_learner.update_strategy_performance(strategy_name, trade_result)

        # Update memory dengan learning experience
        learning_record = {
            'timestamp': time.time(),
            'analysis': analysis,
            'trade_result': trade_result,
            'strategies_used': analysis['strategies_used'],
            'market_conditions': self.get_market_conditions(self.market_data_history[-1] if st.session_state.market_data_history else {}),
            'lesson_learned': self.extract_learning_lesson(analysis, trade_result)
        }

        if 'learning_experiences' not in self.memory.learned_knowledge:
            self.memory.learned_knowledge['learning_experiences'] = []

        self.memory.learned_knowledge['learning_experiences'].append(learning_record)
        self.memory.save_memory_guaranteed()

    def extract_learning_lesson(self, analysis, trade_result):
        """Extract specific lesson dari trading experience"""
        if trade_result['profitable']:
            return f"Strategies {analysis['strategies_used']} worked well with {analysis['confidence']:.1%} confidence"
        else:
            return f"Strategies {analysis['strategies_used']} need adjustment despite {analysis['confidence']:.1%} confidence"

    # Market condition evaluation methods (sama seperti sebelumnya)
    def is_price_near_key_level(self, market_data):
        return abs(market_data['price'] - market_data['support_level']) < 0.001 or \
               abs(market_data['price'] - market_data['resistance_level']) < 0.001

    def has_confirmed_trend(self, market_data):
        return market_data['trend_strength'] > 60

    def is_price_at_fibo_level(self, market_data):
        fibo_levels = [1.0820, 1.0840, 1.0860, 1.0880]
        return any(abs(market_data['price'] - level) < 0.0005 for level in fibo_levels)

    def has_multiple_confluence(self, market_data):
        return (market_data['trend_strength'] > 50 and
                market_data['volatility'] > 0.8 and
                self.is_price_near_key_level(market_data))

    def is_chart_pattern_confirmed(self, market_data):
        return market_data['volatility'] > 1.0 and market_data['trend_strength'] > 40

    def is_consolidation_breakout(self, market_data):
        if len(st.session_state.market_data_history) < 5:
            return False
        recent_volatility = np.mean([d['volatility'] for d in st.session_state.market_data_history[-5:]])
        return market_data['volatility'] > recent_volatility * 1.5

    def get_market_conditions(self, market_data):
        conditions = []
        if market_data['volatility'] > 1.2:
            conditions.append('high_volatility')
        elif market_data['volatility'] < 0.8:
            conditions.append('low_volatility')
        if market_data['trend_strength'] > 60:
            conditions.append('strong_trend')
        if self.is_consolidation_breakout(market_data):
            conditions.append('breakout')
        return conditions

    def get_advanced_market_data(self):
        """Get realistic market data simulation"""
        base_price = 1.0850
        trend_component = np.sin(time.time() / 100) * 0.003
        noise_component = np.random.normal(0, 0.0005)
        news_impact = np.random.choice([0, 0.001, -0.001], p=[0.8, 0.1, 0.1])

        current_price = base_price + trend_component + noise_component + news_impact

        return {
            'price': current_price,
            'volume': np.random.uniform(1000, 8000),
            'volatility': np.random.uniform(0.3, 1.8),
            'trend_strength': abs(trend_component) * 100,
            'momentum': trend_component * 1000,
            'support_level': 1.0820 + np.random.uniform(-0.0005, 0.0005),
            'resistance_level': 1.0880 + np.random.uniform(-0.0005, 0.0005),
            'spread': np.random.uniform(0.6, 1.2),
            'timestamp': time.time()
        }

    def show_strategy_analysis(self):
        """Show detailed strategy analysis"""
        st.subheader("📊 STRATEGY ANALYSIS - FASA 1 INTEGRATION")
        
        st.write(f"🧠 **TOTAL STRATEGIES:** {len(self.trading_strategies)}")
        st.write(f"📈 **FROM FASA 1 RULES:** {len([s for s in self.trading_strategies if s['source_rule'] != 'MARKET_EXPERIENCE'])}")
        st.write(f"🚀 **LEARNED FROM MARKET:** {len([s for s in self.trading_strategies if s['source_rule'] == 'MARKET_EXPERIENCE'])}")

        st.subheader("🎯 STRATEGY PERFORMANCE")
        
        for strategy in self.trading_strategies[:8]:  # Show top 8
            perf = self.adaptive_learner.strategy_performance.get(strategy['strategy'], {})
            win_rate = perf.get('win_rate', 0)
            trades = perf.get('total_trades', 0)

            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{strategy['strategy']}**")
                st.write(f"Source: {strategy['source_rule']}")
            with col2:
                st.metric("Win Rate", f"{win_rate:.1%}")
            
            st.progress(win_rate, text=f"Confidence: {strategy['confidence']:.1%} → {strategy.get('current_confidence', strategy['confidence']):.1%}")
            st.divider()

    def show_learning_progress(self):
        """Show learning progress and experiences"""
        st.subheader("📈 LEARNING PROGRESS & EXPERIENCES")
        
        learning_experiences = self.memory.learned_knowledge.get('learning_experiences', [])
        
        st.write(f"📚 **TOTAL LEARNING EXPERIENCES:** {len(learning_experiences)}")
        st.write(f"🧠 **AI INTELLIGENCE:** {self.memory.performance_stats['ai_intelligence']}%")
        st.write(f"📈 **LEARNING GROWTH:** {st.session_state.trading_stats['ai_intelligence_growth']:.1f}%")

        if learning_experiences:
            st.subheader("🎯 RECENT LEARNING EXPERIENCES")
            for exp in learning_experiences[-5:]:  # Last 5 experiences
                result_color = "green" if exp['trade_result']['profitable'] else "red"
                st.write(f"**{exp['lesson_learned']}**")
                st.write(f"Strategies: {', '.join(exp['strategies_used'][:2])}...")
                st.write(f"Result: :{result_color}[{'PROFIT' if exp['trade_result']['profitable'] else 'LOSS'} ${exp['trade_result']['profit_dollars']:.2f}]")
                st.divider()

    def show_ai_intelligence(self):
        """Show AI intelligence metrics"""
        st.subheader("🤖 AI INTELLIGENCE METRICS")
        
        fasa1_intelligence = self.memory.performance_stats['ai_intelligence']
        fasa2_growth = st.session_state.trading_stats['ai_intelligence_growth']
        total_intelligence = min(fasa1_intelligence + fasa2_growth, 100)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🧠 OVERALL AI INTELLIGENCE", f"{total_intelligence:.1f}%")
        with col2:
            st.metric("📚 FASA 1 KNOWLEDGE", f"{fasa1_intelligence}%")
        with col3:
            st.metric("📈 FASA 2 GROWTH", f"{fasa2_growth:.1f}%")

        st.subheader("📊 KNOWLEDGE BREAKDOWN")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"• SOP Rules from FASA 1: {len(self.memory.learned_knowledge['sop_rules'])}")
            st.write(f"• Trading Strategies: {len(self.trading_strategies)}")
        with col2:
            st.write(f"• Learning Experiences: {len(self.memory.learned_knowledge.get('learning_experiences', []))}")
            st.write(f"• Market Analysis Cycles: {st.session_state.trading_stats['learning_cycles']}")

        st.subheader("🎯 PERFORMANCE METRICS")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Win Rate", f"{st.session_state.trading_stats['win_rate']:.1%}")
        with col2:
            st.metric("Learning Efficiency", f"{min(st.session_state.trading_stats['learning_cycles'] / 10, 100):.1f}%")
        with col3:
            st.metric("Strategy Diversity", f"{min(len(self.trading_strategies) * 5, 100):.1f}%")

    def show_market_analysis(self):
        """Show detailed market analysis"""
        st.subheader("🔍 MARKET ANALYSIS")
        
        if st.session_state.market_data_history:
            market_data = st.session_state.market_data_history[-1]
            
            # Market metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Current Price", f"{market_data['price']:.4f}")
            with col2:
                st.metric("Volatility", f"{market_data['volatility']:.2f}")
            with col3:
                st.metric("Trend Strength", f"{market_data['trend_strength']:.1f}%")
            with col4:
                st.metric("Momentum", f"{market_data['momentum']:.1f}")

            # Support/Resistance levels
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Support Level", f"{market_data['support_level']:.4f}")
            with col2:
                st.metric("Resistance Level", f"{market_data['resistance_level']:.4f}")

            # Market conditions
            conditions = self.get_market_conditions(market_data)
            st.write("**📊 CURRENT MARKET CONDITIONS:**")
            for condition in conditions:
                st.write(f"• {condition.replace('_', ' ').title()}")

# =========================================================================
# === INTEGRATION DENGAN FASA 1 ===
# =========================================================================

def setup_fasa2_integration(superior_ai):
    """Setup FASA 2 integration dengan FASA 1 system"""
    
    # Add FASA 2 to navigation
    st.sidebar.markdown("---")
    st.sidebar.subheader("🚀 FASA 2 INTEGRATION")
    
    if st.sidebar.button("🧠 LAUNCH FASA 2 INTEGRATED AI"):
        # Initialize FASA 2 system
        if 'fasa2_ai' not in st.session_state:
            with st.spinner("🔗 INITIALIZING FASA 2 INTEGRATED AI..."):
                st.session_state.fasa2_ai = TrueIntegratedMarketAIStreamlit(superior_ai.memory)
        
        # Show FASA 2 dashboard
        st.session_state.fasa2_ai.show_integrated_dashboard()
        return True
    
    return False

# =========================================================================
# === UPDATE FASA 1 UNTUK INTEGRASI FASA 2 ===
# =========================================================================

# Dalam class SuperiorAILearning (FASA 1), tambahkan ini:

def run_streamlit_interface_updated(self):
    """Run AI system in Streamlit interface dengan FASA 2 integration"""
    
    # Sidebar untuk navigation
    st.sidebar.title("🎯 SUPERIOR AI NAVIGATION")
    app_mode = st.sidebar.selectbox(
        "Choose Action",
        ["🏠 Dashboard", "🎬 Upload Video", "🖼️ Upload Image", "📊 AI Status", 
         "🧠 Knowledge Master", "🔍 Pattern Analyzer", "💾 Memory Explorer",
         "🚀 FASA 2 Integrated AI"]  # ← TAMBAH INI
    )

    # Main content based on selection
    if app_mode == "🏠 Dashboard":
        self.show_dashboard()
    elif app_mode == "🎬 Upload Video":
        self.upload_video_interface()
    elif app_mode == "🖼️ Upload Image":
        self.upload_image_interface()
    elif app_mode == "📊 AI Status":
        self.show_super_status()
    elif app_mode == "🧠 Knowledge Master":
        self.show_knowledge_master()
    elif app_mode == "🔍 Pattern Analyzer":
        self.show_pattern_analyzer()
    elif app_mode == "💾 Memory Explorer":
        self.show_memory_explorer()
    elif app_mode == "🚀 FASA 2 Integrated AI":  # ← TAMBAH INI
        setup_fasa2_integration(self)
