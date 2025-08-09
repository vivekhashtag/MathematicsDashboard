import streamlit as st

def show_calculus_overview():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("📈 Calculus - Financial Analysis Applications")
    
    # Breadcrumb
    st.markdown("**Home** > **Calculus**")
    
    # Introduction
    st.markdown("""
    Welcome to the Calculus module! Follow **Priya's transformation** from a confused financial 
    analyst to a calculus-powered decision maker. Discover how derivatives and integrals solve 
    real financial challenges through interactive examples and practical insights.
    """)
    
    st.markdown("---")
    
    # Progress tracker
    st.subheader("📊 Your Progress")
    progress_col1, progress_col2, progress_col3 = st.columns(3)
    
    with progress_col1:
        st.metric("Topics Available", "2")
    with progress_col2:
        st.metric("Completed", "0")  # This could be dynamic later
    with progress_col3:
        st.metric("Progress", "0%")  # This could be dynamic later
    
    st.markdown("---")
    
    # Priya's Story Arc
    st.header("📖 Priya's Financial Analysis Journey")
    st.markdown("""
    **Meet Priya!** She's a financial analyst at a Mumbai-based mutual fund company. Her boss 
    keeps asking complex questions about rates of change, total accumulated values, and optimal 
    decision points. Through calculus, she'll discover mathematical tools that transform 
    confusing financial data into clear, actionable insights.
    """)
    
    st.markdown("---")
    
    # The Central Challenge
    st.header("💼 Priya's Core Business Challenges")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("❓ The Rate Questions")
        st.markdown("""
        **Priya's Boss Asks:**
        - *"How FAST is our fund value changing?"*
        - *"When is our growth rate the HIGHEST?"*
        - *"At what point should we worry about decline?"*
        - *"What's the optimal investment level?"*
        
        **Priya's Confusion:**
        *"I can see the daily values, but how do I measure 
        the 'speed' of change? How do I find the best and 
        worst points mathematically?"*
        """)
        
        st.info("""
        **This is where DERIVATIVES come in!**
        Derivatives measure rates of change - they're like 
        speedometers for financial data.
        """)
    
    with col2:
        st.subheader("❓ The Accumulation Questions")
        st.markdown("""
        **Priya's Boss Also Asks:**
        - *"What's our TOTAL profit over the quarter?"*
        - *"If cash flow varies daily, what's our net position?"*
        - *"How do we calculate accumulated returns?"*
        - *"What's the area under our performance curve?"*
        
        **Priya's Challenge:**
        *"I know the daily rates, but how do I add them up 
        properly? How do I get total accumulated values 
        from changing rates?"*
        """)
        
        st.info("""
        **This is where INTEGRALS come in!**
        Integrals accumulate values over time - they're like 
        smart calculators for total financial impact.
        """)
    
    # Topic cards data
    calculus_topics = [
        {
            "title": "📈 Derivatives - Rate Analysis",
            "subtitle": "Priya's Fund Growth Rate Discovery",
            "description": "Priya learns to measure how fast her fund value changes, find peak performance points, and identify optimal investment levels. Master the mathematics of rates, trends, and optimization in finance.",
            "business_scenario": "Fund performance optimization and trend analysis",
            "key_concepts": ["Rate of change", "Tangent lines", "Maxima & minima", "Marginal analysis"],
            "priya_learns": "How to measure financial 'speed' and find optimal decision points",
            "page_key": "calculus_derivatives",
            "applications": ["Revenue optimization", "Cost minimization", "Risk analysis", "Performance peaks"]
        },
        {
            "title": "📊 Integrals - Accumulation Analysis", 
            "subtitle": "Priya's Total Value Calculation Mastery",
            "description": "Priya discovers how to calculate total accumulated profits from daily rates, understand area under curves, and handle real-world financial data. Master the mathematics of accumulation and total value analysis.",
            "business_scenario": "Cash flow analysis and total return calculation",
            "key_concepts": ["Definite integrals", "Indefinite integrals", "Area under curve", "Numerical integration"],
            "priya_learns": "How to calculate total accumulated financial values from rates",
            "page_key": "calculus_integrals",
            "applications": ["NPV calculation", "Total revenue", "Cash flow analysis", "Lifetime value"]
        }
    ]
    
    # Display topic cards
    st.markdown("---")
    st.subheader("🎯 Priya's Learning Path")
    st.markdown("**Follow Priya's journey - each topic solves a different type of financial challenge!**")
    
    for i, topic in enumerate(calculus_topics):
        with st.container():
            st.markdown("---")
            
            # Header with number and title
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {i+1}. {topic['title']}")
                st.markdown(f"**📖 Priya's Challenge:** {topic['subtitle']}")
                st.write(topic['description'])
                
                # What Priya learns
                st.markdown(f"**🎓 Priya Discovers:** {topic['priya_learns']}")
                
                # Business scenario
                st.write(f"**🏢 Business Focus:** {topic['business_scenario']}")
                
                # Key concepts
                concepts_text = " • ".join(topic['key_concepts'])
                st.write(f"**🔑 Key Concepts:** {concepts_text}")
                
                # Applications
                apps_text = " • ".join(topic['applications'])
                st.write(f"**💼 Applications:** {apps_text}")
            
            with col2:
                st.write("")  # Spacing
                st.write("")  # Spacing
                
                # Start button with topic number
                if st.button(f"Start Topic {i+1}", key=f"topic_{i}"):
                    st.session_state.page = topic['page_key']
                    st.rerun()
                
                # Estimated time and difficulty
                st.write("⏱️ ~25-30 min")
                st.write("📊 Interactive")
                
                # Difficulty indicator
                if i == 0:
                    st.write("🟡 Intermediate")
                else:
                    st.write("🔴 Advanced")
    
    # The Connection Between Topics
    st.markdown("---")
    st.header("🔗 How Derivatives and Integrals Connect")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        **📈 DERIVATIVES**
        *(The Rate Detectors)*
        
        **Question:** "How fast?"
        - Fund growth rate
        - Revenue change speed  
        - Cost increase rate
        - Performance trends
        
        **Symbol:** f'(x) or df/dx
        **Meaning:** Rate of change
        """)
    
    with col2:
        st.markdown("""
        **🔄 THE CONNECTION**
        *(Fundamental Theorem)*
        
        **Amazing Discovery:**
        Derivatives and integrals are 
        **mathematical opposites!**
        
        If you know the rate →  
        You can find the total
        
        If you know the total →  
        You can find the rate
        """)
    
    with col3:
        st.markdown("""
        **📊 INTEGRALS**
        *(The Accumulators)*
        
        **Question:** "How much total?"
        - Total profit accumulated
        - Net cash flow
        - Accumulated returns
        - Area under curve
        
        **Symbol:** ∫f(x)dx
        **Meaning:** Total accumulated
        """)
    
    # Priya's Journey Summary
    st.markdown("---")
    st.header("🚀 Priya's Complete Transformation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Priya's Mathematical Evolution:**
        
        📈 **Starts with:** Daily financial data confusion  
        🔍 **Discovers:** Rate analysis with derivatives  
        📊 **Masters:** Total value calculation with integrals  
        🎯 **Achieves:** Complete financial insight mastery
        
        **From Confused Analyst to Calculus Expert:**
        - Overwhelmed by changing financial data
        - Understanding rates, trends, and optimization  
        - Calculating accurate totals and accumulated values
        - Making data-driven financial decisions
        """)
    
    with col2:
        st.markdown("""
        **Calculus Superpowers Unlocked:**
        
        ✅ **Rate analysis** → Understanding how fast things change  
        ✅ **Trend prediction** → Finding peaks and valleys in data  
        ✅ **Optimization** → Discovering best and worst points  
        ✅ **Accumulation** → Calculating totals from rates  
        ✅ **Area analysis** → Understanding financial curves  
        ✅ **Decision making** → Mathematical basis for choices  
        """)
    
    # Real-World Impact
    st.markdown("---")
    st.header("💰 Real-World Financial Applications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Investment Analysis**
        - Portfolio growth rates
        - Risk assessment curves
        - Optimal allocation points
        - Performance derivatives
        """)
    
    with col2:
        st.markdown("""
        **📈 Business Operations**
        - Revenue optimization
        - Cost minimization points
        - Profit maximization
        - Marginal analysis
        """)
    
    with col3:
        st.markdown("""
        **💼 Financial Planning**
        - NPV calculations
        - Cash flow integration
        - Retirement planning
        - Loan amortization
        """)
    
    # Learning Tips
    st.markdown("---")
    st.markdown("""
    ### 💡 Learning Tips for Priya's Journey:
    
    **🎯 Recommended Path:**
    - **Start with Derivatives** - Learn to measure rates and find optimal points
    - **Progress to Integrals** - Master total value calculation and accumulation
    - **See the connection** - Understand how derivatives and integrals work together
    - **Use interactive examples** - Practice with real financial scenarios
    - **Focus on business meaning** - Always connect math to financial decisions
    
    **📚 Study Strategy:**
    - **Think in rates vs. totals** - Derivatives measure speed, integrals measure distance
    - **Visualize the concepts** - Use graphs to see rates and areas
    - **Practice with real data** - Apply concepts to actual financial scenarios
    - **Connect to daily life** - See calculus in investment decisions and business analysis
    """)
    
    # Quick Navigation
    st.markdown("### 🚀 Quick Topic Access:")
    nav_col1, nav_col2 = st.columns(2)
    
    with nav_col1:
        if st.button("📈 Start: Derivatives", key="quick_derivatives"):
            st.session_state.page = 'calculus_derivatives'
            st.rerun()
    
    with nav_col2:
        if st.button("📊 Topic 2: Integrals", key="quick_integrals"):
            st.session_state.page = 'calculus_integrals'
            st.rerun()
    
    # Success Message
    st.markdown("---")
    st.success("""
    🎉 **Ready to Begin Priya's Financial Calculus Journey?**
    
    Start with **Derivatives** to learn how Priya measures financial rates and finds optimal 
    decision points. Then progress to **Integrals** to master total value calculations and 
    accumulation analysis.
    
    By the end, you'll have followed Priya from a confused analyst to a calculus-powered 
    financial expert who uses mathematics to make confident, data-driven decisions!
    """)
    
    st.markdown("---")