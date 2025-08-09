import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

def show_series_sequences():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("📊 Series & Sequences - Financial Applications")
    
    # Breadcrumb
    st.markdown("**Home** > **Series & Sequences**")
    
    st.markdown("---")
    
    # Overview Section
    st.header("📖 Rajesh's Portfolio Management Challenge")
    
    st.markdown("""
    **Meet Rajesh!** He's an investment portfolio manager in Mumbai, handling high-net-worth clients. 
    Three clients have asked him complex questions that require understanding different types of 
    mathematical series. Through their challenges, Rajesh will discover the power of Arithmetic, 
    Geometric, and Harmonic Progressions in finance.
    """)
    
    # Client Challenges Overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("👩‍💼 Mrs. Sharma")
        st.markdown("""
        **SIP Investment Query:**
        *"I want to invest ₹10,000 monthly, 
        increasing by ₹500 each year. 
        How much total after 20 years?"*
        
        **Mathematical Tool Needed:**
        📈 **Arithmetic Progression (AP)**
        """)
    
    with col2:
        st.subheader("👨‍💼 Mr. Patel")
        st.markdown("""
        **Home Loan EMI Question:**
        *"₹50 lakh loan at 8% interest. 
        What's my EMI and total interest 
        over 20 years?"*
        
        **Mathematical Tool Needed:**
        🚀 **Geometric Progression (GP)**
        """)
    
    with col3:
        st.subheader("👩‍💼 Ms. Reddy")
        st.markdown("""
        **Portfolio P/E Averaging:**
        *"My 5 stocks have different P/E ratios. 
        What's the proper 'average' P/E 
        of my portfolio?"*
        
        **Mathematical Tool Needed:**
        ⚖️ **Harmonic Progression (HP)**
        """)
    
    st.info("""
    **Rajesh's Mission:** Master three types of series to solve these real financial challenges!
    Each type of progression serves a different purpose in portfolio management and financial planning.
    """)
    
    # Section 1: Arithmetic Progression (AP)
    st.markdown("---")
    st.header("📈 Arithmetic Progression (AP) - The Steady Investor")
    
    st.markdown("""
    **Mrs. Sharma's Detailed Challenge:** *"Rajesh, I want to start with ₹10,000/month SIP, 
    but increase it by ₹500 every year to beat inflation. How much will I invest in total?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔢 The AP Pattern Discovery")
        
        st.markdown("""
        **Mrs. Sharma's Investment Pattern:**
        ```
        Year 1: ₹10,000/month = ₹1,20,000/year
        Year 2: ₹10,500/month = ₹1,26,000/year
        Year 3: ₹11,000/month = ₹1,32,000/year
        Year 4: ₹11,500/month = ₹1,38,000/year
        ...
        Year 20: ₹19,500/month = ₹2,34,000/year
        ```
        
        **Rajesh's Discovery:**
        *"This is an Arithmetic Progression! Each year increases by the same amount (₹6,000)."*
        """)
        
        # Interactive AP Calculator
        st.markdown("**🧮 Interactive SIP Calculator:**")
        
        initial_sip = st.slider("Initial Monthly SIP (₹)", 5000, 50000, 10000, 1000)
        annual_increase = st.slider("Annual Increase (₹)", 0, 2000, 500, 100)
        years = st.slider("Investment Period (years)", 5, 30, 20, 1)
        
        # Calculate AP values
        first_year_investment = initial_sip * 12
        annual_increase_total = annual_increase * 12
        
        # AP Formula: Sum = n/2 * [2a + (n-1)d]
        total_invested = years/2 * (2*first_year_investment + (years-1)*annual_increase_total)
        
        st.code(f"""
AP Formula Application:
First term (a) = ₹{first_year_investment:,}
Common difference (d) = ₹{annual_increase_total:,}
Number of terms (n) = {years} years

Sum = n/2 × [2a + (n-1)d]
    = {years}/2 × [2×{first_year_investment:,} + {years-1}×{annual_increase_total:,}]
    = ₹{total_invested:,.0f}
        """)
        
        st.success(f"**Total Investment over {years} years: ₹{total_invested:,.0f}**")
    
    with col2:
        st.subheader("📊 SIP Growth Visualization")
        
        # Create year-wise investment data
        years_list = list(range(1, years + 1))
        yearly_investments = [first_year_investment + (i-1)*annual_increase_total for i in years_list]
        cumulative_investments = [sum(yearly_investments[:i]) for i in range(1, len(yearly_investments)+1)]
        
        # Create visualization
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Annual Investment Amount', 'Cumulative Investment'),
            vertical_spacing=0.1
        )
        
        # Annual investments
        fig.add_trace(go.Bar(
            x=years_list, y=yearly_investments,
            name='Annual Investment',
            marker_color='lightblue'
        ), row=1, col=1)
        
        # Cumulative investments
        fig.add_trace(go.Scatter(
            x=years_list, y=cumulative_investments,
            mode='lines+markers',
            name='Cumulative Investment',
            line=dict(color='green', width=3),
            marker=dict(size=6)
        ), row=2, col=1)
        
        fig.update_layout(height=500, showlegend=False)
        fig.update_xaxes(title_text="Year", row=2, col=1)
        fig.update_yaxes(title_text="Amount (₹)", row=1, col=1)
        fig.update_yaxes(title_text="Cumulative (₹)", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **AP Characteristics:**
        - **Linear Growth:** Each year adds exactly ₹{annual_increase_total:,}
        - **Predictable:** Easy to plan and budget
        - **Final Year Investment:** ₹{yearly_investments[-1]:,}
        - **Average Annual Investment:** ₹{total_invested/years:,.0f}
        """)
    
    # AP Applications in Finance
    st.subheader("💼 AP Applications in Finance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📈 Investment Planning**
        - SIP with annual increases
        - Salary-based investments
        - Fixed increment savings
        - Budget progressions
        """)
    
    with col2:
        st.markdown("""
        **💰 Loan & EMI Planning**
        - Step-up EMI loans
        - Graduated payment mortgages  
        - Progressive savings plans
        - Linear depreciation
        """)
    
    with col3:
        st.markdown("""
        **📊 Business Applications**
        - Revenue projections (linear)
        - Cost planning with fixed increases
        - Inventory management
        - Capacity expansion planning
        """)
    
    # Section 2: Geometric Progression (GP)
    st.markdown("---")
    st.header("🚀 Geometric Progression (GP) - The Compound Growth Master")
    
    st.markdown("""
    **Mr. Patel's EMI Challenge:** *"Rajesh, I'm taking a ₹50 lakh home loan at 8% annual interest 
    for 20 years. Calculate my EMI and explain how compound interest works mathematically."*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 The GP Discovery - Compound Interest")
        
        st.markdown("""
        **How Loan Amount Grows (Without EMI):**
        ```
        Principal = ₹50,00,000
        Monthly Rate = 8%/12 = 0.6667%
        Growth Factor = 1.006667
        
        Month 1: ₹50,00,000 × 1.006667¹ = ₹50,33,333
        Month 2: ₹50,00,000 × 1.006667² = ₹50,66,889
        Month 3: ₹50,00,000 × 1.006667³ = ₹51,00,667
        ...
        Month 240: ₹50,00,000 × 1.006667²⁴⁰ = ₹2,46,69,196
        ```
        
        **Rajesh's Insight:**
        *"The loan grows geometrically! This is GP with ratio r = 1.006667"*
        """)
        
        # Interactive EMI Calculator
        st.markdown("**🧮 Interactive EMI Calculator:**")
        
        loan_amount = st.slider("Loan Amount (₹ lakhs)", 10, 100, 50, 5) * 100000
        annual_rate = st.slider("Annual Interest Rate (%)", 5.0, 15.0, 8.0, 0.5)
        loan_tenure = st.slider("Loan Tenure (years)", 5, 30, 20, 1)
        
        # Calculate EMI using GP formula
        monthly_rate = annual_rate / (12 * 100)
        total_months = loan_tenure * 12
        
        # EMI Formula: P * r * (1+r)^n / ((1+r)^n - 1)
        emi = loan_amount * monthly_rate * (1 + monthly_rate)**total_months / ((1 + monthly_rate)**total_months - 1)
        total_payment = emi * total_months
        total_interest = total_payment - loan_amount
        
        st.code(f"""
GP Formula for EMI:
EMI = P × r × (1+r)ⁿ / ((1+r)ⁿ - 1)

Where:
P = ₹{loan_amount:,} (Principal)
r = {monthly_rate:.6f} (Monthly rate)
n = {total_months} months

EMI = ₹{emi:,.0f} per month
Total Payment = ₹{total_payment:,.0f}
Total Interest = ₹{total_interest:,.0f}
        """)
        
        st.success(f"""
        **EMI Breakdown:**
        - **Monthly EMI:** ₹{emi:,.0f}
        - **Total Interest:** ₹{total_interest:,.0f}
        - **Interest %:** {(total_interest/loan_amount)*100:.1f}% of principal
        """)
    
    with col2:
        st.subheader("📊 EMI & Interest Breakdown")
        
        # Calculate month-wise breakdown for first few years
        months = list(range(1, min(61, total_months + 1)))  # First 5 years or total tenure
        outstanding_balance = []
        principal_component = []
        interest_component = []
        
        remaining_principal = loan_amount
        
        for month in months:
            interest_part = remaining_principal * monthly_rate
            principal_part = emi - interest_part
            remaining_principal -= principal_part
            
            outstanding_balance.append(remaining_principal)
            principal_component.append(principal_part)
            interest_component.append(interest_part)
        
        # Create EMI breakdown visualization
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('EMI Composition (Principal vs Interest)', 'Outstanding Loan Balance'),
            vertical_spacing=0.1
        )
        
        # EMI composition
        fig.add_trace(go.Bar(
            x=months, y=principal_component,
            name='Principal Component',
            marker_color='green'
        ), row=1, col=1)
        
        fig.add_trace(go.Bar(
            x=months, y=interest_component,
            name='Interest Component',
            marker_color='red'
        ), row=1, col=1)
        
        # Outstanding balance
        fig.add_trace(go.Scatter(
            x=months, y=outstanding_balance,
            mode='lines',
            name='Outstanding Balance',
            line=dict(color='blue', width=3)
        ), row=2, col=1)
        
        fig.update_layout(height=500, showlegend=True)
        fig.update_xaxes(title_text="Month", row=2, col=1)
        fig.update_yaxes(title_text="Amount (₹)", row=1, col=1)
        fig.update_yaxes(title_text="Balance (₹)", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **GP Pattern Insights:**
        - **Initial Interest:** ₹{interest_component[0]:,.0f}/month
        - **Initial Principal:** ₹{principal_component[0]:,.0f}/month
        - **Ratio shifts over time** due to reducing balance
        """)
    
    # Investment Growth with GP
    st.subheader("📈 Investment Growth Using GP")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**💰 SIP with Market Returns (GP Application):**")
        
        sip_amount = st.slider("Monthly SIP Amount (₹)", 5000, 50000, 15000, 1000, key="gp_sip")
        expected_return = st.slider("Expected Annual Return (%)", 8.0, 18.0, 12.0, 0.5)
        investment_years = st.slider("Investment Period (years)", 5, 30, 15, 1, key="gp_years")
        
        # Calculate future value using GP
        monthly_return = expected_return / (12 * 100)
        total_sip_months = investment_years * 12
        
        # Future Value of SIP = SIP × [((1+r)^n - 1) / r]
        future_value = sip_amount * (((1 + monthly_return)**total_sip_months - 1) / monthly_return)
        total_invested = sip_amount * total_sip_months
        wealth_created = future_value - total_invested
        
        st.code(f"""
GP Formula for SIP Future Value:
FV = SIP × [((1+r)ⁿ - 1) / r]

Where:
SIP = ₹{sip_amount:,}/month
r = {monthly_return:.6f} (Monthly return)
n = {total_sip_months} months

Future Value = ₹{future_value:,.0f}
Amount Invested = ₹{total_invested:,.0f}
Wealth Created = ₹{wealth_created:,.0f}
        """)
        
        st.success(f"""
        **Investment Results:**
        - **Total Corpus:** ₹{future_value:,.0f}
        - **Wealth Multiplier:** {future_value/total_invested:.1f}x
        - **Return:** {((future_value/total_invested - 1)*100):.1f}%
        """)
    
    with col2:
        st.subheader("📊 SIP Growth Trajectory")
        
        # Calculate year-wise SIP growth
        years_range = list(range(1, investment_years + 1))
        corpus_progression = []
        
        for year in years_range:
            months_completed = year * 12
            year_fv = sip_amount * (((1 + monthly_return)**months_completed - 1) / monthly_return)
            corpus_progression.append(year_fv)
        
        # Create growth visualization
        fig = go.Figure()
        
        # Future value progression
        fig.add_trace(go.Scatter(
            x=years_range, y=corpus_progression,
            mode='lines+markers',
            name='SIP Corpus Growth',
            line=dict(color='green', width=4),
            marker=dict(size=8)
        ))
        
        # Add exponential trend line
        fig.add_trace(go.Scatter(
            x=years_range, 
            y=[total_invested * year / investment_years for year in years_range],
            mode='lines',
            name='Linear Growth (No Returns)',
            line=dict(color='red', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="SIP Growth: Compound vs Linear",
            xaxis_title="Year",
            yaxis_title="Corpus Value (₹)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **The Power of Compounding (GP):**
        Green line shows exponential growth due to compounding.
        Red dashed line shows what linear growth would look like.
        """)
    
    # GP Applications in Finance
    st.subheader("💼 GP Applications in Finance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🏦 Loan Calculations**
        - EMI computations
        - Compound interest
        - Loan amortization
        - Present value calculations
        """)
    
    with col2:
        st.markdown("""
        **📈 Investment Growth**
        - SIP future value
        - Compound annual growth
        - Retirement planning
        - Wealth creation projections
        """)
    
    with col3:
        st.markdown("""
        **📊 Business Modeling**
        - Revenue growth projections
        - Population/market expansion
        - Viral marketing reach
        - Inflation adjustments
        """)
    
    # Section 3: Harmonic Progression (HP)
    st.markdown("---")
    st.header("⚖️ Harmonic Progression (HP) - The Proper Averaging Master")
    
    st.markdown("""
    **Ms. Reddy's P/E Averaging Challenge:** *"Rajesh, I have 5 stocks with P/E ratios: 15, 20, 25, 30, 40. 
    What's the proper 'average' P/E of my portfolio? Simple average gives 26, but that doesn't seem right for financial ratios."*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("⚖️ The HP Discovery - Proper Ratio Averaging")
        
        st.markdown("""
        **Ms. Reddy's Portfolio:**
        ```
        Stock A: P/E = 15 (₹10 lakh investment)
        Stock B: P/E = 20 (₹10 lakh investment)  
        Stock C: P/E = 25 (₹10 lakh investment)
        Stock D: P/E = 30 (₹10 lakh investment)
        Stock E: P/E = 40 (₹10 lakh investment)
        ```
        
        **The Problem with Simple Average:**
        ```
        Simple Average = (15+20+25+30+40)/5 = 26
        ```
        
        **But P/E is a ratio! For rates and ratios, we need Harmonic Mean.**
        """)
        
        # Interactive HP Calculator
        st.markdown("**🧮 Interactive P/E Calculator:**")
        
        pe_ratios = []
        investments = []
        
        for i in range(5):
            col1_inner, col2_inner = st.columns(2)
            with col1_inner:
                pe = st.number_input(f"Stock {chr(65+i)} P/E", 5.0, 50.0, [15.0, 20.0, 25.0, 30.0, 40.0][i], 0.5, key=f"pe_{i}")
                pe_ratios.append(pe)
            with col2_inner:
                inv = st.number_input(f"Investment (₹L)", 1, 50, 10, 1, key=f"inv_{i}")
                investments.append(inv)
        
        # Calculate different averages
        arithmetic_mean = sum(pe_ratios) / len(pe_ratios)
        harmonic_mean = len(pe_ratios) / sum(1/pe for pe in pe_ratios)
        
        # Weighted harmonic mean (proper for portfolio)
        total_investment = sum(investments)
        weighted_harmonic = total_investment / sum(inv/pe for inv, pe in zip(investments, pe_ratios))
        
        st.code(f"""
Portfolio P/E Analysis:

Arithmetic Mean = (15+20+25+30+40)/5 = {arithmetic_mean:.2f}

Harmonic Mean = 5 / (1/15 + 1/20 + 1/25 + 1/30 + 1/40)
              = 5 / ({sum(1/pe for pe in pe_ratios):.4f})
              = {harmonic_mean:.2f}

Weighted Harmonic Mean = {weighted_harmonic:.2f}
(Most accurate for portfolio analysis)
        """)
        
        st.success(f"""
        **Portfolio P/E Comparison:**
        - **Simple Average:** {arithmetic_mean:.2f} (Overstates)
        - **Harmonic Mean:** {harmonic_mean:.2f} (Conservative)
        - **Weighted H.M.:** {weighted_harmonic:.2f} (Most Accurate)
        """)
    
    with col2:
        st.subheader("📊 Averaging Methods Comparison")
        
        # Create comparison visualization
        categories = ['Arithmetic Mean', 'Harmonic Mean', 'Weighted Harmonic']
        values = [arithmetic_mean, harmonic_mean, weighted_harmonic]
        colors = ['red', 'orange', 'green']
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=categories, y=values,
            marker_color=colors,
            text=[f'{v:.2f}' for v in values],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="P/E Ratio: Different Averaging Methods",
            yaxis_title="P/E Ratio",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Why Harmonic Mean for P/E?**
        - P/E is price-to-earnings ratio
        - For ratios, harmonic mean gives proper average
        - Prevents high-ratio stocks from dominating
        - More conservative and realistic for risk assessment
        """)
        
        # Speed averaging example
        st.markdown("**🚗 Speed Averaging Example:**")
        st.markdown("""
        **Why HP works for rates:**
        Car travels 60 km: first 30km at 30 km/h, next 30km at 60 km/h
        
        **Wrong:** Arithmetic mean = (30+60)/2 = 45 km/h
        **Right:** Harmonic mean = 2/(1/30 + 1/60) = 40 km/h
        
        **Verification:** Total time = 1h + 0.5h = 1.5h
        Average speed = 60km/1.5h = 40 km/h ✓
        """)
    
    # HP Applications in Finance
    st.subheader("💼 HP Applications in Finance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Ratio Analysis**
        - P/E ratio averaging
        - P/B ratio calculations
        - Debt-to-equity ratios
        - Efficiency ratios
        """)
    
    with col2:
        st.markdown("""
        **⚡ Rate Calculations**
        - Average return rates
        - Interest rate averaging
        - Growth rate analysis
        - Performance metrics
        """)
    
    with col3:
        st.markdown("""
        **💰 Cost Analysis**
        - Cost per unit averaging
        - Efficiency measurements
        - Resource utilization
        - Productivity ratios
        """)
    
    # Section 4: Integration - Advanced Applications
    st.markdown("---")
    st.header("🔗 Integration: IRR and NPV Using Series")
    
    st.markdown("""
    **Rajesh's Ultimate Challenge:** *"A client wants to evaluate a project with varying cash flows. 
    I need to calculate IRR (Internal Rate of Return) using geometric series principles!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💡 IRR Calculation Using GP")
        
        st.markdown("""
        **Project Cash Flows:**
        ```
        Year 0: -₹100 lakhs (Investment)
        Year 1: +₹30 lakhs
        Year 2: +₹40 lakhs  
        Year 3: +₹50 lakhs
        Year 4: +₹60 lakhs
        ```
        
        **IRR Calculation:**
        Find rate 'r' where NPV = 0
        ```
        NPV = -100 + 30/(1+r) + 40/(1+r)² + 50/(1+r)³ + 60/(1+r)⁴ = 0
        ```
        
        **This is a GP where each term is discounted by (1+r)ⁿ**
        """)
        
        # IRR Calculator
        st.markdown("**🧮 IRR Calculator:**")
        
        initial_investment = st.slider("Initial Investment (₹ lakhs)", 50, 200, 100, 10)
        
        cash_flows = []
        for i in range(4):
            cf = st.slider(f"Year {i+1} Cash Flow (₹ lakhs)", 10, 100, [30, 40, 50, 60][i], 5, key=f"cf_{i}")
            cash_flows.append(cf)
        
        # Simple IRR approximation using iteration
        def calculate_npv(rate, investment, flows):
            npv = -investment
            for i, cf in enumerate(flows):
                npv += cf / (1 + rate)**(i+1)
            return npv
        
        # Find IRR using binary search approximation
        low_rate, high_rate = 0.0, 1.0
        for _ in range(50):  # 50 iterations for approximation
            mid_rate = (low_rate + high_rate) / 2
            npv = calculate_npv(mid_rate, initial_investment, cash_flows)
            if abs(npv) < 0.01:
                break
            elif npv > 0:
                low_rate = mid_rate
            else:
                high_rate = mid_rate
        
        irr = mid_rate
        
        st.code(f"""
IRR Calculation Result:
Internal Rate of Return = {irr*100:.2f}%

Verification:
NPV at {irr*100:.2f}% = ₹{calculate_npv(irr, initial_investment, cash_flows):.2f} lakhs
(Should be approximately 0)
        """)
        
        if irr > 0.15:
            st.success(f"✅ **Excellent Project** - IRR = {irr*100:.1f}%")
        elif irr > 0.10:
            st.info(f"✅ **Good Project** - IRR = {irr*100:.1f}%")
        else:
            st.warning(f"⚠️ **Marginal Project** - IRR = {irr*100:.1f}%")
    
    with col2:
        st.subheader("📊 NPV Profile Analysis")
        
        # Create NPV profile
        discount_rates = np.linspace(0, 0.5, 50)
        npv_values = [calculate_npv(rate, initial_investment, cash_flows) for rate in discount_rates]
        
        fig = go.Figure()
        
        # NPV curve
        fig.add_trace(go.Scatter(
            x=discount_rates*100, y=npv_values,
            mode='lines',
            name='NPV Profile',
            line=dict(color='blue', width=3)
        ))
        
        # Zero line
        fig.add_hline(y=0, line_dash="dash", line_color="gray")
        
        # IRR point
        fig.add_trace(go.Scatter(
            x=[irr*100], y=[0],
            mode='markers',
            name=f'IRR = {irr*100:.1f}%',
            marker=dict(color='red', size=12, symbol='star')
        ))
        
        fig.update_layout(
            title="NPV Profile - Finding IRR",
            xaxis_title="Discount Rate (%)",
            yaxis_title="NPV (₹ lakhs)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **IRR Insights:**
        - **IRR:** {irr*100:.1f}% (where NPV = 0)
        - **At 10% discount:** NPV = ₹{calculate_npv(0.10, initial_investment, cash_flows):.1f} lakhs
        - **At 20% discount:** NPV = ₹{calculate_npv(0.20, initial_investment, cash_flows):.1f} lakhs
        """)
    
    # Practice Exercises
    st.markdown("---")
    st.header("💪 Practice: Master All Three Progressions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📝 Exercise 1: Retirement Planning (AP + GP)"):
            st.markdown("""
            **Scenario:** Retirement planning with increasing SIP
            
            **Challenge:** 
            - Start with ₹20,000/month SIP
            - Increase by ₹2,000 every year (AP pattern)
            - Market returns 11% annually (GP growth)
            - Calculate corpus after 25 years
            
            **Tasks:**
            1. Total amount invested using AP
            2. Future value using GP principles
            3. Wealth creation analysis
            """)
            
            if st.button("Show Solution", key="ex1"):
                st.success("""
                **Solution Approach:**
                1. **AP for investments:** Sum = 25/2 × [2×240000 + 24×24000] = ₹1,44,00,000
                2. **GP for each year's growth:** Calculate FV of each year's SIP separately
                3. **Total corpus:** Sum of all yearly contributions' future values
                4. **Result:** Approximately ₹4.2 crores with ₹2.76 crores as wealth creation
                """)
    
    with col2:
        with st.expander("📝 Exercise 2: Portfolio Analysis (HP)"):
            st.markdown("""
            **Scenario:** Multi-asset portfolio optimization
            
            **Challenge:**
            Portfolio with different asset classes:
            - Equity: P/E = 18, Weight = 60%
            - Debt: Yield = 7%, Weight = 30% 
            - Gold: P/E = N/A, Weight = 10%
            
            **Tasks:**
            1. Calculate weighted average P/E (use HP)
            2. Compare with arithmetic mean
            3. Explain why HP is better for ratios
            """)
            
            if st.button("Show Solution", key="ex2"):
                st.success("""
                **Solution:**
                1. **For P/E ratios:** Use harmonic mean weighted by market value
                2. **Weighted HM:** More conservative than arithmetic mean
                3. **Why HP:** P/E is price/earnings ratio - rates need harmonic averaging
                4. **Result:** HP gives more realistic portfolio valuation
                """)
    
    # Key Takeaways
    st.markdown("---")
    st.header("🎓 Rajesh's Series Mastery Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📈 Arithmetic Progression**
        
        **When to Use:**
        - Fixed incremental changes
        - Linear growth patterns
        - SIP with annual increases
        - Salary progressions
        
        **Key Formula:**
        Sum = n/2 × [2a + (n-1)d]
        
        **Business Power:**
        Predictable planning & budgeting
        """)
    
    with col2:
        st.markdown("""
        **🚀 Geometric Progression**
        
        **When to Use:**
        - Compound growth/interest
        - EMI calculations
        - Investment projections
        - Exponential patterns
        
        **Key Formula:**
        Sum = a × (rⁿ - 1)/(r - 1)
        
        **Business Power:**
        Wealth creation & loan analysis
        """)
    
    with col3:
        st.markdown("""
        **⚖️ Harmonic Progression**
        
        **When to Use:**
        - Ratio averaging
        - Rate calculations
        - Efficiency metrics
        - Performance analysis
        
        **Key Formula:**
        HM = n / (1/a₁ + 1/a₂ + ... + 1/aₙ)
        
        **Business Power:**
        Accurate ratio & rate analysis
        """)
    
    st.success("""
    🎉 **Rajesh's Complete Transformation Achieved!**
    
    From three confused client questions to mastering all financial series applications:
    ✅ **AP Mastery** - SIP planning and linear growth analysis
    ✅ **GP Expertise** - EMI calculations and compound growth projections  
    ✅ **HP Precision** - Proper ratio averaging and performance metrics
    ✅ **Integration Skills** - IRR and NPV calculations using series principles
    
    **The Power of Series:** Rajesh can now handle any financial calculation involving 
    patterns, growth, or proper averaging - making him the go-to expert for complex 
    portfolio management challenges!
    """)
    
    st.markdown("---")