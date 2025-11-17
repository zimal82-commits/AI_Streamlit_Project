# =========================================================================
# === FASA 2: TRUE INTEGRATED MARKET AI - BELAJAR DARI FASA 1 ===
# =========================================================================

import threading, time, random
import numpy as np
import pandas as pd
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import warnings
warnings.filterwarnings('ignore')

# =========================================================================
# === KNOWLEDGE TRANSFORMATION ENGINE ===
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

        print("🔄 TRANSFORMING FASA 1 KNOWLEDGE TO TRADING STRATEGIES...")

        for rule in self.memory.learned_knowledge['sop_rules']:
            strategy = self._create_trading_strategy(rule)
            if strategy:
                trading_strategies.append(strategy)
                print(f"   ✅ {rule.get('rule', 'Unknown')} → {strategy['strategy']}")

        print(f"🎯 TOTAL STRATEGIES CREATED: {len(trading_strategies)}")
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
# === ADAPTIVE LEARNING SYSTEM ===
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
# === TRUE INTEGRATED MARKET AI ===
# =========================================================================

class TrueIntegratedMarketAI:
    def __init__(self, memory_system):
        print("🚀 INITIALIZING TRUE INTEGRATED MARKET AI...")

        self.memory = memory_system
        self.knowledge_transformer = KnowledgeTransformation(memory_system)
        self.adaptive_learner = AdaptiveLearningSystem(memory_system)

        # Transform FASA 1 knowledge ke trading strategies
        self.trading_strategies = self.knowledge_transformer.transform_vision_rules()

        # Trading statistics
        self.trading_stats = {
            'total_signals': 0,
            'profitable_signals': 0,
            'total_profit': 0.0,
            'win_rate': 0.0,
            'learning_cycles': 0,
            'strategies_developed': len(self.trading_strategies),
            'ai_intelligence_growth': 0
        }

        self.is_running = False
        self.analysis_thread = None
        self.market_data_history = []

        print(f"✅ INTEGRATED AI READY: {len(self.trading_strategies)} strategies from FASA 1")
        self.setup_integrated_ui()

    def setup_integrated_ui(self):
        """Setup UI untuk integrated system"""

        self.btn_start_learning = widgets.Button(
            description="🧠 START LEARNING AI",
            button_style='success',
            layout=widgets.Layout(width='220px', height='60px')
        )

        self.btn_stop_learning = widgets.Button(
            description="⏹️ STOP LEARNING",
            button_style='danger',
            layout=widgets.Layout(width='200px', height='60px')
        )

        self.btn_strategy_analysis = widgets.Button(
            description="📊 STRATEGY ANALYSIS",
            button_style='info',
            layout=widgets.Layout(width='200px', height='60px')
        )

        self.btn_learning_progress = widgets.Button(
            description="📈 LEARNING PROGRESS",
            button_style='warning',
            layout=widgets.Layout(width='200px', height='60px')
        )

        self.btn_ai_intelligence = widgets.Button(
            description="🤖 AI INTELLIGENCE",
            button_style='primary',
            layout=widgets.Layout(width='200px', height='60px')
        )

        self.integrated_output = widgets.Output(layout=widgets.Layout(
            height='600px',
            border='3px solid #4CAF50',
            padding='20px',
            margin='15px 0',
            background_color='#f1f8e9'
        ))

        # Event handlers
        self.btn_start_learning.on_click(self.start_integrated_learning)
        self.btn_stop_learning.on_click(self.stop_integrated_learning)
        self.btn_strategy_analysis.on_click(self.show_strategy_analysis)
        self.btn_learning_progress.on_click(self.show_learning_progress)
        self.btn_ai_intelligence.on_click(self.show_ai_intelligence)

    def start_integrated_learning(self, b):
        """Start integrated learning loop"""
        if not self.is_running:
            self.is_running = True
            self.analysis_thread = threading.Thread(target=self.integrated_learning_loop, daemon=True)
            self.analysis_thread.start()

            with self.integrated_output:
                clear_output()
                print("🧠 TRUE INTEGRATED LEARNING AI ACTIVATED!")
                print("=" * 65)
                print("🔗 FULLY CONNECTED TO FASA 1 KNOWLEDGE BASE")
                print("📈 CONTINUOUS LEARNING FROM MARKET EXPERIENCE")
                print("🚀 ADAPTIVE STRATEGY DEVELOPMENT ENABLED")
                print("=" * 65)
                print(f"📚 USING {len(self.trading_strategies)} LEARNED STRATEGIES")
                print(f"🎯 AI INTELLIGENCE: {self.memory.performance_stats['ai_intelligence']}%")

    def stop_integrated_learning(self, b):
        """Stop integrated learning"""
        self.is_running = False
        with self.integrated_output:
            print("\n🛑 INTEGRATED LEARNING STOPPED")
            print(f"📊 Final Performance:")
            print(f"   • Win Rate: {self.trading_stats['win_rate']:.1%}")
            print(f"   • Total Profit: ${self.trading_stats['total_profit']:.2f}")
            print(f"   • Learning Cycles: {self.trading_stats['learning_cycles']}")
            print(f"   • Strategies Developed: {self.trading_stats['strategies_developed']}")

    def integrated_learning_loop(self):
        """Main integrated learning loop"""
        cycle_count = 0

        while self.is_running:
            cycle_count += 1
            self.trading_stats['learning_cycles'] = cycle_count

            # Get market data
            market_data = self.get_advanced_market_data()
            self.market_data_history.append(market_data)

            # Analyze dengan learned strategies
            analysis = self.analyze_with_learned_strategies(market_data)

            # Execute trade jika ada signal kuat
            if analysis['signal_strength'] > 0.7:
                trade_result = self.execute_learning_trade(analysis, market_data)
                self.update_learning_stats(trade_result)

                # Adaptive learning - update strategies berdasarkan results
                self.adaptive_learning_update(analysis, trade_result)

            # Update display
            with self.integrated_output:
                clear_output()
                self.display_integrated_dashboard(cycle_count, market_data, analysis)

            time.sleep(3)  # Learning cycle interval

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
                self.trading_stats['strategies_developed'] += 1

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
        self.trading_stats['total_signals'] += 1

        if trade_result['profitable']:
            self.trading_stats['profitable_signals'] += 1
            self.trading_stats['total_profit'] += trade_result['profit_dollars']

        # Update win rate
        if self.trading_stats['total_signals'] > 0:
            self.trading_stats['win_rate'] = (
                self.trading_stats['profitable_signals'] / self.trading_stats['total_signals']
            )

        # Update AI intelligence growth
        self.trading_stats['ai_intelligence_growth'] = min(
            self.trading_stats['learning_cycles'] * 0.5 +
            self.trading_stats['win_rate'] * 50,
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
            'market_conditions': self.get_market_conditions(self.market_data_history[-1] if self.market_data_history else {}),
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

    # Market condition evaluation methods
    def is_price_near_key_level(self, market_data):
        return abs(market_data['price'] - market_data['support_level']) < 0.001 or \
               abs(market_data['price'] - market_data['resistance_level']) < 0.001

    def has_confirmed_trend(self, market_data):
        return market_data['trend_strength'] > 60

    def is_price_at_fibo_level(self, market_data):
        # Simulate Fibonacci level detection
        fibo_levels = [1.0820, 1.0840, 1.0860, 1.0880]
        return any(abs(market_data['price'] - level) < 0.0005 for level in fibo_levels)

    def has_multiple_confluence(self, market_data):
        # Multiple technical factors aligning
        return (market_data['trend_strength'] > 50 and
                market_data['volatility'] > 0.8 and
                self.is_price_near_key_level(market_data))

    def is_chart_pattern_confirmed(self, market_data):
        # Simulate chart pattern confirmation
        return market_data['volatility'] > 1.0 and market_data['trend_strength'] > 40

    def is_consolidation_breakout(self, market_data):
        # Simulate consolidation breakout detection
        if len(self.market_data_history) < 5:
            return False
        recent_volatility = np.mean([d['volatility'] for d in self.market_data_history[-5:]])
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

    def display_integrated_dashboard(self, cycle_count, market_data, analysis):
        """Display integrated learning dashboard"""
        print(f"🧠 TRUE INTEGRATED AI LEARNING - CYCLE #{cycle_count}")
        print("=" * 70)
        print(f"⏰ {time.strftime('%H:%M:%S')} | EUR/USD | CONTINUOUS LEARNING")
        print(f"💰 Price: {market_data['price']:.4f} | Volatility: {market_data['volatility']:.2f}")
        print(f"📈 Trend Strength: {market_data['trend_strength']:.1f}%")

        print(f"\n🎯 TRADING SIGNAL: {analysis['signal']}")
        print(f"💪 Signal Strength: {analysis['signal_strength']:.1%}")
        print(f"🔍 Confidence: {analysis['confidence']:.1%}")
        print(f"📚 Strategies Used: {analysis['strategy_count']} from FASA 1")

        print(f"\n🤖 STRATEGIES ACTIVATED:")
        for strategy in analysis['strategies_used'][:4]:  # Show first 4
            print(f"   • {strategy}")
        if len(analysis['strategies_used']) > 4:
            print(f"   • ... and {len(analysis['strategies_used']) - 4} more")

        print(f"\n📊 LEARNING PERFORMANCE:")
        print(f"   Win Rate: {self.trading_stats['win_rate']:.1%} | "
              f"Total Trades: {self.trading_stats['total_signals']}")
        print(f"   Total Profit: ${self.trading_stats['total_profit']:.2f} | "
              f"Learning Cycles: {self.trading_stats['learning_cycles']}")
        print(f"   AI Intelligence Growth: {self.trading_stats['ai_intelligence_growth']:.1f}%")

        print(f"\n💡 LEARNING INSIGHT:")
        print(f"   {analysis['reason']}")

    def show_strategy_analysis(self, b):
        """Show detailed strategy analysis"""
        with self.integrated_output:
            clear_output()
            print("📊 STRATEGY ANALYSIS - FASA 1 INTEGRATION")
            print("=" * 70)

            print(f"🧠 TOTAL STRATEGIES: {len(self.trading_strategies)}")
            print(f"📈 FROM FASA 1 RULES: {len([s for s in self.trading_strategies if s['source_rule'] != 'MARKET_EXPERIENCE'])}")
            print(f"🚀 LEARNED FROM MARKET: {len([s for s in self.trading_strategies if s['source_rule'] == 'MARKET_EXPERIENCE'])}")

            print(f"\n🎯 STRATEGY PERFORMANCE:")
            for strategy in self.trading_strategies[:8]:  # Show top 8
                perf = self.adaptive_learner.strategy_performance.get(strategy['strategy'], {})
                win_rate = perf.get('win_rate', 0)
                trades = perf.get('total_trades', 0)

                print(f"   • {strategy['strategy']}:")
                print(f"     Source: {strategy['source_rule']}")
                print(f"     Confidence: {strategy['confidence']:.1%} → {strategy.get('current_confidence', strategy['confidence']):.1%}")
                print(f"     Performance: {win_rate:.1%} win rate ({trades} trades)")

    def show_learning_progress(self, b):
        """Show learning progress and experiences"""
        with self.integrated_output:
            clear_output()
            print("📈 LEARNING PROGRESS & EXPERIENCES")
            print("=" * 70)

            learning_experiences = self.memory.learned_knowledge.get('learning_experiences', [])

            print(f"📚 TOTAL LEARNING EXPERIENCES: {len(learning_experiences)}")
            print(f"🧠 AI INTELLIGENCE: {self.memory.performance_stats['ai_intelligence']}%")
            print(f"📈 LEARNING GROWTH: {self.trading_stats['ai_intelligence_growth']:.1f}%")

            if learning_experiences:
                print(f"\n🎯 RECENT LEARNING EXPERIENCES:")
                for exp in learning_experiences[-5:]:  # Last 5 experiences
                    print(f"   • {exp['lesson_learned']}")
                    print(f"     Strategies: {', '.join(exp['strategies_used'][:2])}...")
                    print(f"     Result: {'PROFIT' if exp['trade_result']['profitable'] else 'LOSS'} "
                          f"${exp['trade_result']['profit_dollars']:.2f}")

    def show_ai_intelligence(self, b):
        """Show AI intelligence metrics"""
        with self.integrated_output:
            clear_output()
            print("🤖 AI INTELLIGENCE METRICS")
            print("=" * 70)

            fasa1_intelligence = self.memory.performance_stats['ai_intelligence']
            fasa2_growth = self.trading_stats['ai_intelligence_growth']
            total_intelligence = min(fasa1_intelligence + fasa2_growth, 100)

            print(f"🧠 OVERALL AI INTELLIGENCE: {total_intelligence:.1f}%")
            print(f"📚 FASA 1 KNOWLEDGE: {fasa1_intelligence}%")
            print(f"📈 FASA 2 GROWTH: {fasa2_growth:.1f}%")

            print(f"\n📊 KNOWLEDGE BREAKDOWN:")
            print(f"   • SOP Rules from FASA 1: {len(self.memory.learned_knowledge['sop_rules'])}")
            print(f"   • Trading Strategies: {len(self.trading_strategies)}")
            print(f"   • Learning Experiences: {len(self.memory.learned_knowledge.get('learning_experiences', []))}")
            print(f"   • Market Analysis Cycles: {self.trading_stats['learning_cycles']}")

            print(f"\n🎯 PERFORMANCE METRICS:")
            print(f"   • Win Rate: {self.trading_stats['win_rate']:.1%}")
            print(f"   • Learning Efficiency: {min(self.trading_stats['learning_cycles'] / 10, 100):.1f}%")
            print(f"   • Strategy Diversity: {min(len(self.trading_strategies) * 5, 100):.1f}%")

    def display_integrated_system(self):
        """Display the complete integrated system"""
        display(HTML("""
        <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
                   padding: 30px; border-radius: 20px; color: white; text-align: center;">
        <h1>🧠 FASA 2: TRUE INTEGRATED MARKET AI</h1>
        <h3>Continuous Learning from FASA 1 | Adaptive Strategy Development | Real-time Market Intelligence</h3>
        </div>
        """))

        # Integration status
        total_rules = len(self.memory.learned_knowledge['sop_rules'])
        integration_html = f"""
        <div style="background: #e8f5e8; padding: 25px; border-radius: 15px; margin: 20px 0;">
        <h3>🔗 FULL INTEGRATION WITH FASA 1</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
            <div style="text-align: center;">
                <h4>📚 SOP Rules</h4>
                <p style="font-size: 24px; font-weight: bold; color: #4CAF50;">{total_rules}</p>
            </div>
            <div style="text-align: center;">
                <h4>🎯 Strategies</h4>
                <p style="font-size: 24px; font-weight: bold; color: #2196F3;">{len(self.trading_strategies)}</p>
            </div>
            <div style="text-align: center;">
                <h4>🧠 AI Intelligence</h4>
                <p style="font-size: 24px; font-weight: bold; color: #FF9800;">{self.memory.performance_stats['ai_intelligence']}%</p>
            </div>
        </div>
        <p style="text-align: center; margin-top: 15px;">
            <strong>🚀 Continuous Learning Active</strong> | <strong>📈 Adaptive Development Enabled</strong>
        </p>
        </div>
        """
        display(HTML(integration_html))

        # Display control buttons
        display(HTML("<h3>🎯 INTEGRATED AI CONTROLS:</h3>"))
        display(widgets.HBox([self.btn_start_learning, self.btn_stop_learning]))
        display(widgets.HBox([self.btn_strategy_analysis, self.btn_learning_progress, self.btn_ai_intelligence]))
        display(self.integrated_output)

# =========================================================================
# === FASA 2 MAIN INTEGRATED SYSTEM ===
# =========================================================================

class Fasa2IntegratedSystem:
    def __init__(self, superior_memory):
        print("INITIALIZING FASA 2 INTEGRATED SYSTEM...")

        self.memory = superior_memory
        self.integrated_ai = TrueIntegratedMarketAI(superior_memory)

        print("\n" + "="*70)
        print("🧠 FASA 2 TRUE INTEGRATED AI READY!")
        print("🔗 FULLY CONNECTED TO FASA 1 KNOWLEDGE BASE")
        print("📈 CONTINUOUS LEARNING & ADAPTIVE DEVELOPMENT ENABLED")
        print("🚀 AI WILL LEARN AND GROW FROM MARKET EXPERIENCE")
        print("="*70)

    def display_fasa2_system(self):
        """Display complete FASA 2 integrated system"""
        self.integrated_ai.display_integrated_system()

# =========================================================================
# === RUN FASA 2 INTEGRATED SYSTEM ===
# =========================================================================

print("\n" + "="*70)
print("FASA 2 TRUE INTEGRATED AI SYSTEM READY")
print("To use: fasa2_integrated = Fasa2IntegratedSystem(superior_ai.memory)")
print("Then: fasa2_integrated.display_fasa2_system()")
print("="*70)
