import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import sympy as sp
from sympy import symbols, integrate, diff, lambdify
from scipy import integrate as scipy_integrate

def show_integrals():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Calculus"):
            st.session_state.page = 'calculus'
            st.rerun()
    
    with col2:
        st.title("📊 Integrals - Accumulation Analysis")
    
    # Breadcrumb
    st.markdown("**Home** > **Calculus** > **Integrals**")
    
    st.markdown("---")
    
    # Story Introduction
    st.header("📖 Priya's Accumulation Challenge")
    
    st.markdown("""
    **The Boss's New Question:** *"Priya, now that you can measure rates, I need you to solve 
    the opposite problem. I know our daily profit RATE, but I need the TOTAL accumulated profit 
    over the quarter. If cash flow varies every day, what's our net position over time?"*
    
    **Priya's Mission:** Learn to calculate total accumulated values from rates of change.
    """)
    
    # Section 1: The Accumulation Problem
    st.markdown("---")
    st.header("1️⃣ The Total Value Problem: From Rates to Totals")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📈 Daily Profit Rate Data")
        
        # Sample daily profit rate
        days = np.arange(1, 31)  # 30 days
        daily_rates = 50 + 2*days - 0.05*days**2 + 5*np.sin(days*0.2)  # Variable daily profit rate
        
        # Create DataFrame
        profit_df = pd.DataFrame({
            'Day': days[:10],  # Show first 10 days
            'Daily Profit Rate (₹k/day)': daily_rates[:10].round(1)
        })
        
        st.dataframe(profit_df, use_container_width=True)
        
        st.markdown("""
        **Priya's Challenge:**
        - *"I know how much profit we make each day..."*
        - *"But how do I add up all these varying rates?"*
        - *"What's the TOTAL accumulated profit over 30 days?"*
        - *"How do I calculate the area under this rate curve?"*
        """)
        
        st.warning("""
        **The Problem:**
        Simple addition won't work because the rates change continuously!
        We need a mathematical "smart adder" - that's what integrals do.
        """)
    
    with col2:
        st.subheader("📊 Daily Profit Rate Curve")
        
        # Plot daily profit rates
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=days,
            y=daily_rates,
            mode='lines+markers',
            name='Daily Profit Rate',
            line=dict(color='green', width=3),
            marker=dict(size=6)
        ))
        
        fig.update_layout(
            title="Daily Profit Rate Over Time",
            xaxis_title="Day",
            yaxis_title="Profit Rate (₹k/day)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Priya's Insight:**
        *"The area under this curve should give me the total profit! 
        But how do I calculate the area of this irregular shape?"*
        """)
    
    # Section 2: Discovering Integrals
    st.markdown("---")
    st.header("2️⃣ Priya's Discovery: Integrals as Smart Accumulators")
    
    st.markdown("""
    **Priya's Breakthrough:** *"An integral is like a smart calculator that perfectly adds up 
    all the rates to give me the exact total accumulated value!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🧮 The Mathematical Connection")
        
        st.markdown("""
        **The Fundamental Relationship:**
        ```
        If Profit Rate = P'(t) = 50 + 2t - 0.1t²
        Then Total Profit = P(t) = ∫(50 + 2t - 0.1t²)dt
                                  = 50t + t² - 0.033t³ + C
        ```
        
        **Business Translation:**
        - **P'(t)** = Daily profit rate (speed of earning)
        - **P(t)** = Total accumulated profit (distance traveled)
        - **∫** = Integration symbol (the "smart adder")
        - **C** = Starting value (initial cash position)
        """)
        
        # Interactive integral calculator
        st.markdown("**🧪 Try Different Profit Rate Functions:**")
        
        base_rate = st.slider("Base Daily Rate (₹k)", 20, 100, 50, 5)
        growth_rate = st.slider("Growth Factor", 0.0, 5.0, 2.0, 0.5)
        decay_rate = st.slider("Decay Factor", 0.0, 0.2, 0.1, 0.02)
        
        # Define symbolic variable
        t = symbols('t')
        rate_function = base_rate + growth_rate*t - decay_rate*t**2
        total_function = integrate(rate_function, t)
        
        st.code(f"""
Profit Rate: P'(t) = {rate_function}
Total Profit: P(t) = ∫P'(t)dt = {total_function} + C
        """)
        
        # Verification
        verification = diff(total_function, t)
        st.success(f"""
        **Verification:** 
        d/dt[{total_function}] = {verification} ✓
        (Taking derivative of integral gives back original function!)
        """)
    
    with col2:
        st.subheader("📊 Visualizing Integration")
        
        # Create time array for plotting
        t_vals = np.linspace(0, 20, 100)
        
        # Convert symbolic expressions to numerical functions
        rate_numeric = lambdify(t, rate_function, 'numpy')
        total_numeric = lambdify(t, total_function, 'numpy')
        
        # Calculate values
        rate_vals = rate_numeric(t_vals)
        total_vals = total_numeric(t_vals) - total_numeric(0)  # Start from zero
        
        # Create subplot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Profit Rate (What we know)', 'Total Accumulated Profit (What we calculate)'),
            vertical_spacing=0.1
        )
        
        # Rate plot with area shading
        fig.add_trace(go.Scatter(
            x=t_vals, y=rate_vals,
            mode='lines',
            name="P'(t) - Profit Rate",
            line=dict(color='green', width=3),
            fill='tonexty'
        ), row=1, col=1)
        
        # Total plot
        fig.add_trace(go.Scatter(
            x=t_vals, y=total_vals,
            mode='lines',
            name='P(t) - Total Profit',
            line=dict(color='blue', width=3)
        ), row=2, col=1)
        
        fig.update_layout(height=500, showlegend=False)
        fig.update_xaxes(title_text="Day", row=2, col=1)
        fig.update_yaxes(title_text="Rate (₹k/day)", row=1, col=1)
        fig.update_yaxes(title_text="Total (₹k)", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("""
        **Key Insight:** The shaded area under the rate curve 
        equals the height of the total profit curve at each point!
        """)
    
    # Section 3: Definite vs Indefinite Integrals
    st.markdown("---")
    st.header("3️⃣ Definite vs Indefinite Integrals: General vs Specific")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔄 Indefinite Integrals (General Formula)")
        
        st.markdown("""
        **What it gives:** General formula for accumulated value
        
        **Example:**
        ```
        ∫(50 + 2t - 0.1t²)dt = 50t + t² - 0.033t³ + C
        ```
        
        **Business Meaning:**
        - Formula to calculate total profit up to any day t
        - C = starting cash position (constant of integration)
        - Gives infinite family of solutions
        """)
        
        # Interactive indefinite integral
        st.markdown("**📊 Indefinite Integral Explorer:**")
        
        starting_cash = st.slider("Starting Cash Position (₹k)", 0, 200, 100, 10)
        
        # Calculate total profit with constant
        total_with_constant = total_function + starting_cash
        total_with_constant_numeric = lambdify(t, total_with_constant, 'numpy')
        
        st.code(f"""
Complete Solution: P(t) = {total_with_constant}

At t=10 days: P(10) = {float(total_with_constant_numeric(10)):.1f}k
At t=20 days: P(20) = {float(total_with_constant_numeric(20)):.1f}k
        """)
    
    with col2:
        st.subheader("🎯 Definite Integrals (Specific Period)")
        
        st.markdown("""
        **What it gives:** Exact accumulated value over specific period
        
        **Example:**
        ```
        ∫₁₀²⁰(50 + 2t - 0.1t²)dt = P(20) - P(10)
        ```
        
        **Business Meaning:**
        - Exact profit accumulated from day 10 to day 20
        - No constant needed - it cancels out
        - Gives specific numerical answer
        """)
        
        # Interactive definite integral
        st.markdown("**📊 Definite Integral Calculator:**")
        
        start_day = st.slider("Start Day", 1, 25, 5, 1)
        end_day = st.slider("End Day", start_day+1, 30, 15, 1)
        
        # Calculate definite integral
        definite_result = integrate(rate_function, (t, start_day, end_day))
        
        st.code(f"""
Definite Integral: ∫_{start_day}^{end_day} P'(t)dt = {float(definite_result):.1f}k

Business Translation:
Total profit from day {start_day} to day {end_day} = ₹{float(definite_result):.1f}k
        """)
        
        # Visualize definite integral as area
        t_definite = np.linspace(start_day, end_day, 100)
        rate_definite = rate_numeric(t_definite)
        
        fig = go.Figure()
        
        # Full curve
        fig.add_trace(go.Scatter(
            x=t_vals, y=rate_vals,
            mode='lines',
            name='Profit Rate',
            line=dict(color='green', width=2)
        ))
        
        # Highlighted area
        fig.add_trace(go.Scatter(
            x=t_definite, y=rate_definite,
            mode='lines',
            name=f'Integration Area (Days {start_day}-{end_day})',
            line=dict(color='red', width=3),
            fill='tonexty'
        ))
        
        fig.update_layout(
            title=f"Definite Integral = Shaded Area = ₹{float(definite_result):.1f}k",
            xaxis_title="Day",
            yaxis_title="Profit Rate (₹k/day)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 4: Area Under the Curve
    st.markdown("---")
    st.header("4️⃣ Area Under the Curve: Visual Understanding")
    
    st.markdown("""
    **Priya's Visualization Breakthrough:** *"I finally see it! The area under any rate curve 
    IS the total accumulated value. Integration is just a precise way to calculate irregular areas!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎨 Interactive Area Calculator")
        
        st.markdown("""
        **Different Scenarios:**
        Explore how different rate patterns affect total accumulated values.
        """)
        
        # Scenario selector
        scenario = st.selectbox("Choose Business Scenario:", [
            "Steady Growth",
            "Accelerating Growth", 
            "Peak and Decline",
            "Seasonal Fluctuation"
        ])
        
        # Define different rate functions based on scenario
        t_scenario = np.linspace(0, 12, 100)
        
        if scenario == "Steady Growth":
            rate_scenario = 40 + 2*t_scenario
            scenario_desc = "Consistent 2k/day increase in profit rate"
        elif scenario == "Accelerating Growth":
            rate_scenario = 30 + 1.5*t_scenario + 0.2*t_scenario**2
            scenario_desc = "Profit rate increases at accelerating pace"
        elif scenario == "Peak and Decline":
            rate_scenario = 30 + 8*t_scenario - 0.5*t_scenario**2
            scenario_desc = "Profit rate peaks then declines"
        else:  # Seasonal
            rate_scenario = 45 + 15*np.sin(t_scenario*0.8) + 2*t_scenario
            scenario_desc = "Seasonal fluctuations with underlying growth"
        
        st.info(f"**{scenario}:** {scenario_desc}")
        
        # Calculate area up to selected point
        end_point = st.slider("Calculate Area Up To Day:", 1, 12, 8, 1)
        
        # Numerical integration for area
        area_result = np.trapz(rate_scenario[:int(end_point*100/12)], 
                              t_scenario[:int(end_point*100/12)])
        
        st.metric("Total Accumulated Value", f"₹{area_result:.0f}k")
    
    with col2:
        st.subheader("📊 Area Visualization")
        
        # Create area visualization
        fig = go.Figure()
        
        # Full curve
        fig.add_trace(go.Scatter(
            x=t_scenario, y=rate_scenario,
            mode='lines',
            name='Rate Function',
            line=dict(color='blue', width=3)
        ))
        
        # Shaded area up to selected point
        t_shaded = t_scenario[t_scenario <= end_point]
        rate_shaded = rate_scenario[t_scenario <= end_point]
        
        fig.add_trace(go.Scatter(
            x=t_shaded, y=rate_shaded,
            mode='lines',
            name=f'Area = ₹{area_result:.0f}k',
            line=dict(color='green', width=2),
            fill='tonexty',
            fillcolor='rgba(0,255,0,0.3)'
        ))
        
        # Add vertical line at end point
        max_rate = np.max(rate_scenario)
        fig.add_shape(
            type="line",
            x0=end_point, y0=0, x1=end_point, y1=max_rate,
            line=dict(color="red", width=2, dash="dash")
        )
        
        fig.update_layout(
            title=f"{scenario}: Area Under Curve",
            xaxis_title="Time",
            yaxis_title="Rate",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"""
        **Area Interpretation:**
        The green shaded area represents the total accumulated 
        value (₹{area_result:.0f}k) from the varying rate over time.
        """)
    
    # Section 5: Numerical Integration
    st.markdown("---")
    st.header("5️⃣ Numerical Integration: Real-World Data Analysis")
    
    st.markdown("""
    **Priya's Real-World Challenge:** *"Sometimes I don't have a nice mathematical formula - 
    just daily data points from our accounting system. How do I still calculate total values?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Real Data Integration")
        
        st.markdown("""
        **The Trapezoidal Rule:**
        When you only have data points, approximate the area using trapezoids.
        """)
        
        # Generate realistic irregular data
        np.random.seed(42)
        data_days = np.arange(1, 16)  # 15 days of data
        base_trend = 40 + 2*data_days - 0.1*data_days**2
        noise = np.random.normal(0, 3, len(data_days))
        actual_data = base_trend + noise
        
        # Create data table
        data_df = pd.DataFrame({
            'Day': data_days,
            'Daily Cash Flow (₹k)': actual_data.round(1)
        })
        
        st.dataframe(data_df, use_container_width=True)
        
        # Numerical integration methods comparison
        st.markdown("**Integration Methods Comparison:**")
        
        # Trapezoidal rule
        trapz_result = np.trapz(actual_data, data_days)
        
        # Simpson's rule (if scipy available)
        try:
            simpson_result = scipy_integrate.simpson(actual_data, data_days)
        except:
            simpson_result = trapz_result
        
        # Simple rectangle rule (for comparison)
        rectangle_result = np.sum(actual_data) * (data_days[1] - data_days[0])
        
        col1_inner, col2_inner = st.columns(2)
        
        with col1_inner:
            st.metric("Rectangle Rule", f"₹{rectangle_result:.0f}k")
            st.metric("Trapezoidal Rule", f"₹{trapz_result:.0f}k")
        
        with col2_inner:
            st.metric("Simpson's Rule", f"₹{simpson_result:.0f}k")
            st.write("**Most Accurate** ⭐")
    
    with col2:
        st.subheader("📈 Numerical Integration Visualization")
        
        # Visualize different numerical methods
        fig = go.Figure()
        
        # Original data points
        fig.add_trace(go.Scatter(
            x=data_days, y=actual_data,
            mode='markers+lines',
            name='Actual Data',
            line=dict(color='blue', width=2),
            marker=dict(size=8)
        ))
        
        # Trapezoidal approximation
        for i in range(len(data_days)-1):
            fig.add_shape(
                type="line",
                x0=data_days[i], y0=0, x1=data_days[i], y1=actual_data[i],
                line=dict(color="red", width=1, dash="dot")
            )
            fig.add_shape(
                type="line", 
                x0=data_days[i+1], y0=0, x1=data_days[i+1], y1=actual_data[i+1],
                line=dict(color="red", width=1, dash="dot")
            )
            fig.add_shape(
                type="line",
                x0=data_days[i], y0=actual_data[i], 
                x1=data_days[i+1], y1=actual_data[i+1],
                line=dict(color="red", width=1, dash="dot")
            )
        
        fig.update_layout(
            title="Trapezoidal Rule Approximation",
            xaxis_title="Day",
            yaxis_title="Cash Flow (₹k)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Trapezoidal Rule Result:** ₹{trapz_result:.0f}k
        
        This method connects data points with straight lines 
        and calculates the area of resulting trapezoids.
        """)
    
    # Section 6: NPV and Financial Applications
    st.markdown("---")
    st.header("6️⃣ Advanced Application: NPV and Cash Flow Analysis")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💰 Net Present Value (NPV) Calculation")
        
        st.markdown("""
        **Real Business Application:**
        Calculate the present value of future cash flows using integration.
        """)
        
        # NPV parameters
        discount_rate = st.slider("Discount Rate (%)", 1.0, 15.0, 8.0, 0.5) / 100
        project_duration = st.slider("Project Duration (years)", 1, 10, 5, 1)
        initial_investment = st.slider("Initial Investment (₹ lakhs)", 100, 1000, 500, 50)
        
        # Define cash flow function (increasing over time)
        t_npv = symbols('t')
        annual_cash_flow = 100 + 20*t_npv  # Increasing cash flows
        
        # Present value function
        present_value_function = annual_cash_flow * sp.exp(-discount_rate * t_npv)
        
        # Calculate NPV using integration
        pv_of_cash_flows = integrate(present_value_function, (t_npv, 0, project_duration))
        npv = float(pv_of_cash_flows) - initial_investment
        
        st.code(f"""
Cash Flow Function: CF(t) = {annual_cash_flow} lakhs/year
Discount Rate: {discount_rate*100:.1f}%

Present Value of Cash Flows:
PV = ∫₀^{project_duration} CF(t) × e^(-{discount_rate:.3f}t) dt
   = {float(pv_of_cash_flows):.0f} lakhs

NPV = PV - Initial Investment
    = {float(pv_of_cash_flows):.0f} - {initial_investment}
    = ₹{npv:.0f} lakhs
        """)
        
        if npv > 0:
            st.success(f"✅ **Project Acceptable** - NPV = ₹{npv:.0f} lakhs")
        else:
            st.error(f"❌ **Project Rejected** - NPV = ₹{npv:.0f} lakhs")
    
    with col2:
        st.subheader("📊 NPV Analysis Visualization")
        
        # Create time series for NPV visualization
        t_values = np.linspace(0, project_duration, 100)
        cf_values = 100 + 20*t_values
        pv_values = cf_values * np.exp(-discount_rate * t_values)
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Future Cash Flows', 'Present Value of Cash Flows'),
            vertical_spacing=0.1
        )
        
        # Future cash flows
        fig.add_trace(go.Scatter(
            x=t_values, y=cf_values,
            mode='lines',
            name='Future Cash Flows',
            line=dict(color='green', width=3),
            fill='tonexty'
        ), row=1, col=1)
        
        # Present value
        fig.add_trace(go.Scatter(
            x=t_values, y=pv_values,
            mode='lines',
            name='Present Value',
            line=dict(color='blue', width=3),
            fill='tonexty'
        ), row=2, col=1)
        
        fig.update_layout(height=500, showlegend=False)
        fig.update_xaxes(title_text="Year", row=2, col=1)
        fig.update_yaxes(title_text="₹ Lakhs", row=1, col=1)
        fig.update_yaxes(title_text="₹ Lakhs", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Key Insight:** 
        The area under the present value curve (₹{float(pv_of_cash_flows):.0f} lakhs) 
        represents the total value of all future cash flows in today's money.
        """)
    
    # Section 7: Key Business Applications
    st.markdown("---")
    st.header("7️⃣ Priya's Integration Mastery Applications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **💼 Financial Planning**
        - NPV calculations
        - Cash flow analysis
        - Investment evaluation
        - Retirement planning
        """)
    
    with col2:
        st.markdown("""
        **📊 Business Analysis**
        - Total revenue calculation
        - Accumulated cost analysis
        - Customer lifetime value
        - Market size estimation
        """)
    
    with col3:
        st.markdown("""
        **🎯 Risk Management**
        - Portfolio value integration
        - Risk exposure calculation
        - Probability distributions
        - Expected value analysis
        """)
    
    # Practice Exercise
    st.markdown("---")
    st.subheader("💪 Practice: Apply Integration Analysis")
    
    with st.expander("📝 Exercise: Customer Lifetime Value"):
        st.markdown("""
        **Scenario:** A subscription business has monthly revenue rate from each customer:
        R(t) = 100 × e^(-0.02t) (revenue decreases due to churn over time)
        
        **Tasks:**
        1. Calculate total revenue from one customer over 24 months
        2. What's the customer lifetime value (CLV)?
        3. If acquisition cost is ₹1,200, is it profitable?
        4. What's the payback period?
        """)
        
        if st.button("Show Solution", key="integrals_exercise"):
            st.markdown("---")
            st.markdown("### 🔍 **Solution:**")
            
            # Customer lifetime value analysis
            t_clv = symbols('t')
            revenue_rate = 100 * sp.exp(-0.02 * t_clv)
            
            # Integrate over 24 months
            clv_24_months = integrate(revenue_rate, (t_clv, 0, 24))
            
            # Find when cumulative revenue = acquisition cost
            cumulative_revenue = integrate(revenue_rate, (t_clv, 0, t_clv))
            
            st.code(f"""
Revenue Rate: R(t) = {revenue_rate}

Customer Lifetime Value (24 months):
CLV = ∫₀²⁴ R(t) dt = {float(clv_24_months):.0f}

Cumulative Revenue Function:
CR(t) = ∫₀ᵗ R(s) ds = {cumulative_revenue}

Acquisition Cost: ₹1,200
Profit = ₹{float(clv_24_months) - 1200:.0f}
            """)
            
            if float(clv_24_months) > 1200:
                st.success(f"""
                ✅ **Customer Acquisition is Profitable!**
                - CLV: ₹{float(clv_24_months):.0f}
                - Profit: ₹{float(clv_24_months) - 1200:.0f}
                - ROI: {((float(clv_24_months) - 1200)/1200)*100:.1f}%
                """)
            else:
                st.error("❌ Customer acquisition is not profitable over 24 months")
    
    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Previous: Derivatives"):
            st.session_state.page = 'calculus_derivatives'
            st.rerun()
    
    with col2:
        if st.button("🏠 Back to Calculus Overview"):
            st.session_state.page = 'calculus'
            st.rerun()
    
    st.markdown("---")
    st.success("""
    🎉 **Congratulations! Priya's Complete Calculus Journey is Complete!**
    
    Priya has mastered both sides of calculus:
    ✅ **Derivatives** - Measuring rates and finding optimal points
    ✅ **Integrals** - Calculating totals and accumulated values
    ✅ **Business Applications** - NPV, optimization, and financial analysis
    ✅ **Real-World Skills** - From theory to practical decision-making
    
    **The Power of Calculus:** Priya can now analyze any changing business data, 
    find optimal decision points, and calculate accurate total values from rates!
    """)
    
    st.markdown("---")