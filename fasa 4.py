# =========================================================================
# === PEMBETULAN MEMORY SYSTEM - FASA 1 ===
# =========================================================================

class SuperiorMemory:
    def __init__(self, base_dir="./ai_memory"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        
        self.memory_file = self.base_dir / "ai_superior_memory.pkl"
        self.learned_knowledge, self.performance_stats = self.load_memory_verified()
        
        # TUNJUKKAN STATISTIK LEARNING DENGAN JELAS
        st.sidebar.markdown("---")
        st.sidebar.subheader("🧠 AI LEARNING STATS")
        st.sidebar.write(f"**Rules:** {len(self.learned_knowledge['sop_rules'])}")
        st.sidebar.write(f"**Learning Sessions:** {self.performance_stats['learning_sessions']}")
        st.sidebar.write(f"**Intelligence:** {self.performance_stats['ai_intelligence']}%")

    def add_sop_rule(self, rule):
        """Tambah rule dan pastikan disimpan dengan betul"""
        try:
            self.learned_knowledge['sop_rules'].append(rule)
            self.performance_stats['patterns_mastered'] += 1
            self.performance_stats['learning_sessions'] += 1
            
            # UPDATE AI INTELLIGENCE
            self.performance_stats['ai_intelligence'] = self.calculate_ai_intelligence()
            
            # SIMPAN DENGAN SEGERA
            success = self.save_memory_guaranteed()
            
            if success:
                st.sidebar.success(f"✅ Learned: {rule.get('rule', 'Unknown')}")
                return True
                
        except Exception as e:
            st.error(f"❌ Rule add failed: {e}")
        return False

# =========================================================================
# === PEMBETULAN INTERFACE - TAMBAH BUTANG FASA 3 ===
# =========================================================================

class SuperiorAILearning:
    def run_streamlit_interface(self):
        """Run AI system dengan FASA 3 integration"""
        
        # SIDEBAR NAVIGATION - TAMBAH FASA 3
        st.sidebar.title("🎯 SUPERIOR AI NAVIGATION")
        app_mode = st.sidebar.selectbox(
            "Choose Action",
            ["🏠 Dashboard", "🎬 Upload Video", "🖼️ Upload Image", "📊 AI Status", 
             "🧠 Knowledge Master", "🔍 Pattern Analyzer", "💾 Memory Explorer",
             "🚀 FASA 2 Integrated AI", "📸 FASA 3 Screenshot Analysis"]  # ← TAMBAH FASA 3
        )

        # MAIN CONTENT
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
        elif app_mode == "🚀 FASA 2 Integrated AI":
            self.launch_fasa2()
        elif app_mode == "📸 FASA 3 Screenshot Analysis":  # ← FASA 3
            self.launch_fasa3()

    def launch_fasa2(self):
        """Launch FASA 2 Integrated AI"""
        if 'fasa2_ai' not in st.session_state:
            with st.spinner("🚀 INITIALIZING FASA 2 INTEGRATED AI..."):
                st.session_state.fasa2_ai = TrueIntegratedMarketAIStreamlit(self.memory)
        
        st.session_state.fasa2_ai.show_integrated_dashboard()

    def launch_fasa3(self):
        """Launch FASA 3 Screenshot Analysis"""
        if 'fasa2_ai' not in st.session_state:
            st.warning("⚠️ Please initialize FASA 2 first!")
            if st.button("Initialize FASA 2 Now"):
                st.session_state.fasa2_ai = TrueIntegratedMarketAIStreamlit(self.memory)
                st.rerun()
            return
            
        if 'fasa3_ai' not in st.session_state:
            with st.spinner("📸 INITIALIZING FASA 3 SCREENSHOT ANALYSIS..."):
                st.session_state.fasa3_ai = Fasa3MultitimeframeAnalysis(
                    self.memory, 
                    st.session_state.fasa2_ai.trading_strategies
                )
        
        # PANGGIL INTERFACE FASA 3 - INI YANG ANDA NAK LIHAT
        st.session_state.fasa3_ai.show_screenshot_analysis_interface()

    def show_knowledge_master(self):
        """Tunjukkan knowledge dengan lebih jelas"""
        st.header("🧠 KNOWLEDGE MASTER - DETAILED ANALYSIS")
        
        stats = self.memory.get_detailed_stats()
        rules = self.memory.learned_knowledge['sop_rules']

        if not rules:
            st.warning("❌ No knowledge accumulated yet. Upload images/videos to start learning!")
            return

        # STATISTIK UTAMA
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rules", len(rules))
        with col2:
            st.metric("Learning Sessions", stats['learning_sessions'])
        with col3:
            st.metric("AI Intelligence", f"{stats['ai_intelligence']}%")
        with col4:
            st.metric("Unique Patterns", stats['unique_patterns'])

        # DETAILED RULES LIST
        st.subheader("📝 DETAILED RULES DATABASE")
        
        for i, rule in enumerate(rules[-20:]):  # Show last 20 rules
            with st.expander(f"Rule #{i+1}: {rule.get('rule', 'Unknown')} (Confidence: {rule.get('confidence', 0):.2f})"):
                st.write(f"**Learned by:** {rule.get('learned_by', 'Unknown')}")
                st.write(f"**Session Type:** {rule.get('session_type', 'Unknown')}")
                st.write(f"**Timestamp:** {time.ctime(rule.get('timestamp', time.time()))}")
                st.write(f"**Condition:** {rule.get('condition', 'N/A')}")
                st.write(f"**Action:** {rule.get('action', 'N/A')}")

# =========================================================================
# === PEMBETULAN FASA 3 - PASTIKAN UPLOAD BUTANG ADA ===
# =========================================================================

class Fasa3MultitimeframeAnalysis:
    def show_screenshot_analysis_interface(self):
        """Tunjukkan interface untuk upload screenshot - INI YANG ANDA CARI"""
        
        st.header("📸 FASA 3: MT5 SCREENSHOT ANALYSIS")
        st.info("Upload screenshot MT5 dengan multiple timeframe (D1, H4, H1, M30, M15, M5, M1)")
        
        # INI BUTANG UPLOAD YANG ANDA NAK LIHAT
        uploaded_file = st.file_uploader(
            "📁 UPLOAD MT5 SCREENSHOT",
            type=['png', 'jpg', 'jpeg'],
            key="fasa3_screenshot_uploader"
        )
        
        if uploaded_file is not None:
            # Tunjukkan preview screenshot
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded MT5 Screenshot", use_column_width=True)
            
            # BUTANG ANALYZE - INI YANG AKAN PROSES
            if st.button("🔍 ANALYZE SCREENSHOT WITH AI", type="primary", use_container_width=True):
                self.analyze_multitimeframe_screenshot(image)
                
        # Tunjukkan results jika ada
        if st.session_state.fasa3_analysis_result:
            self.display_analysis_results()

# =========================================================================
# === PEMBETULAN UTAMA - PASTIKAN SEMUA BERFUNGSI ===
# =========================================================================

def main():
    st.set_page_config(
        page_title="SUPERIOR AI SYSTEM",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize system
    if 'superior_ai' not in st.session_state:
        with st.spinner("🔧 INITIALIZING SUPERIOR AI SYSTEM..."):
            st.session_state.superior_ai = SuperiorAILearning()
    
    # Run interface
    st.session_state.superior_ai.run_streamlit_interface()

if __name__ == "__main__":
    main()
