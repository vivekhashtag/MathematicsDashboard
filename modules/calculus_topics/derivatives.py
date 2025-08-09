import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import sympy as sp
from sympy import symbols, diff, solve, lambdify

def show_derivatives():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Calculus"):
            st.session_state.page = 'calculus'
            st.rerun()
    
    with col2:
        st.title("📈 Derivatives - Rate Analysis")
    
    # Breadcrumb
    st.markdown("**Home** > **Calculus** > **Derivatives**")
    
    st.markdown("---")
    
    # Story Introduction
    st.header("📖 Priya's Rate Analysis Challenge")
    
    st.markdown("""
    **The Boss's Question:** *"Priya, I don't just want to know our fund value each day. 
    I want to know HOW FAST it's changing, WHEN it's growing fastest, and WHEN we should 
    worry about decline. Can you give me the 'speedometer' for our fund?"*
    
    **Priya's Mission:** Learn to measure rates of change and find optimal decision points in financial data.
    """)
    
    # Section 1: The Problem - Understanding Rates
    st.markdown("---")
    st.header("1️⃣ The Speed Problem: What Are Rates of Change?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Daily Fund Values")
        
        # Sample fund data
        days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        fund_values = np.array([100, 103, 107, 110, 112, 113, 113, 112, 110, 107])
        
        # Create DataFrame
        fund_df = pd.DataFrame({
            'Day': days,
            'Fund Value (₹ Crores)': fund_values
        })
        
        st.dataframe(fund_df, use_container_width=True)
        
        st.markdown("""
        **Priya's Confusion:**
        - *"I can see the values changing..."*
        - *"But how do I measure the SPEED of change?"*
        - *"When is growth fastest? When does it slow down?"*
        - *"How do I find the exact moment things turn bad?"*
        """)
    
    with col2:
        st.subheader("📈 Fund Value Over Time")
        
        # Plot fund values
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=days,
            y=fund_values,
            mode='lines+markers',
            name='Fund Value',
            line=dict(color='blue', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Fund Value Growth Curve",
            xaxis_title="Day",
            yaxis_title="Fund Value (₹ Crores)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Priya's Observation:**
        *"The curve goes up, then levels off, then goes down... 
        but I need to measure the exact RATE of this change!"*
        """)
    
    # Section 2: Discovering Derivatives
    st.markdown("---")
    st.header("2️⃣ Priya's Discovery: Derivatives as Rate Detectors")
    
    st.markdown("""
    **Priya's Breakthrough:** *"A derivative is like a speedometer for my fund! 
    It tells me not just where I am, but how fast I'm moving at each moment."*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🧮 The Mathematical Method")
        
        st.markdown("""
        **Simple Example: Fund Growth Function**
        ```
        Fund Value: f(t) = 100 + 8t - 0.5t²
        (where t = days, f = value in crores)
        ```
        
        **The Derivative (Rate of Change):**
        ```
        f'(t) = 8 - t
        (Speed of fund growth per day)
        ```
        
        **Business Translation:**
        - **f(t)** = Fund value on day t
        - **f'(t)** = How fast fund is growing on day t
        - **f'(t) > 0** = Fund is growing
        - **f'(t) < 0** = Fund is declining
        - **f'(t) = 0** = Growth has stopped (critical moment!)
        """)
        
        # Interactive derivative calculator
        st.markdown("**🧪 Try Different Fund Functions:**")
        
        a = st.slider("Growth coefficient (a)", -2.0, 15.0, 8.0, 0.5)
        b = st.slider("Deceleration factor (b)", 0.0, 2.0, 0.5, 0.1)
        c = st.slider("Starting value (c)", 50, 150, 100, 5)
        
        # Define symbolic variable
        t = symbols('t')
        fund_function = c + a*t - b*t**2
        derivative_function = diff(fund_function, t)
        
        st.code(f"""
Fund Function: f(t) = {fund_function}
Derivative: f'(t) = {derivative_function}
        """)
    
    with col2:
        st.subheader("📊 Visualizing Rate of Change")
        
        # Create time array for plotting
        t_vals = np.linspace(0, 12, 100)
        
        # Convert symbolic expressions to numerical functions
        f_numeric = lambdify(t, fund_function, 'numpy')
        f_prime_numeric = lambdify(t, derivative_function, 'numpy')
        
        # Calculate values
        fund_vals = f_numeric(t_vals)
        rate_vals = f_prime_numeric(t_vals)
        
        # Create subplot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Fund Value', 'Rate of Change (Derivative)'),
            vertical_spacing=0.1
        )
        
        # Fund value plot
        fig.add_trace(go.Scatter(
            x=t_vals, y=fund_vals,
            mode='lines',
            name='f(t) - Fund Value',
            line=dict(color='blue', width=3)
        ), row=1, col=1)
        
        # Derivative plot
        fig.add_trace(go.Scatter(
            x=t_vals, y=rate_vals,
            mode='lines',
            name="f'(t) - Rate of Change",
            line=dict(color='red', width=3)
        ), row=2, col=1)
        
        # Add zero line for derivative
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)
        
        fig.update_layout(height=500, showlegend=False)
        fig.update_xaxes(title_text="Day", row=2, col=1)
        fig.update_yaxes(title_text="₹ Crores", row=1, col=1)
        fig.update_yaxes(title_text="₹ Crores/Day", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Find critical point
        critical_points = solve(derivative_function, t)
        if critical_points:
            critical_day = float(critical_points[0])
            critical_value = float(f_numeric(critical_day))
            
            st.success(f"""
            **Critical Point Found!**
            - **Day {critical_day:.1f}:** Rate = 0 (growth stops)
            - **Fund Value:** ₹{critical_value:.1f} crores
            - **Business Meaning:** Peak performance day!
            """)
    
    # Section 3: Finding Maxima and Minima
    st.markdown("---")
    st.header("3️⃣ Finding Peak Performance: Maxima & Minima")
    
    st.markdown("""
    **The Critical Business Question:** *"When exactly does our fund reach its peak? 
    When should we be most worried about decline?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔍 The Optimization Process")
        
        st.markdown("""
        **Step 1: Find Critical Points**
        Set derivative = 0 to find where rate of change stops
        
        **Step 2: Test the Nature**
        Use second derivative to determine if it's max or min
        
        **Step 3: Business Interpretation**
        Translate mathematical results to financial decisions
        """)
        
        # Interactive optimization example
        st.markdown("**📈 Revenue Optimization Example:**")
        
        price = st.slider("Base Price (₹)", 10, 100, 50, 5)
        demand_sensitivity = st.slider("Price Sensitivity", 0.1, 2.0, 0.8, 0.1)
        
        # Revenue function R(p) = p * demand(p) = p * (base_demand - sensitivity * p)
        p = symbols('p')
        base_demand = 1000
        revenue_func = p * (base_demand - demand_sensitivity * 100 * p)
        revenue_derivative = diff(revenue_func, p)
        revenue_second_derivative = diff(revenue_derivative, p)
        
        st.code(f"""
Revenue Function: R(p) = {revenue_func}
First Derivative: R'(p) = {revenue_derivative}
Second Derivative: R''(p) = {revenue_second_derivative}
        """)
        
        # Find optimal price
        optimal_price = solve(revenue_derivative, p)
        if optimal_price:
            opt_price = float(optimal_price[0])
            opt_revenue = float(revenue_func.subs(p, opt_price))
            second_deriv_value = float(revenue_second_derivative.subs(p, opt_price))
            
            st.success(f"""
            **Optimization Result:**
            - **Optimal Price:** ₹{opt_price:.2f}
            - **Maximum Revenue:** ₹{opt_revenue:.0f}
            - **Second Derivative:** {second_deriv_value:.1f} (negative = maximum)
            """)
    
    with col2:
        st.subheader("📊 Revenue Optimization Visualization")
        
        # Create price range for plotting
        p_vals = np.linspace(1, 15, 100)
        
        # Convert to numerical function
        revenue_numeric = lambdify(p, revenue_func, 'numpy')
        revenue_vals = revenue_numeric(p_vals)
        
        # Plot revenue curve
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=p_vals, y=revenue_vals,
            mode='lines',
            name='Revenue Function',
            line=dict(color='green', width=3)
        ))
        
        # Mark optimal point
        if optimal_price:
            fig.add_trace(go.Scatter(
                x=[opt_price], y=[opt_revenue],
                mode='markers',
                name='Maximum Revenue',
                marker=dict(color='red', size=15, symbol='star')
            ))
            
            # Add annotation
            fig.add_annotation(
                x=opt_price, y=opt_revenue,
                text=f"Max Revenue<br>₹{opt_revenue:.0f}",
                showarrow=True,
                arrowhead=2
            )
        
        fig.update_layout(
            title="Revenue vs Price - Finding the Optimal Point",
            xaxis_title="Price (₹)",
            yaxis_title="Revenue (₹)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Priya's Insight:**
        *"The derivative tells me the slope at each point. 
        When slope = 0, I've found the peak! The second 
        derivative tells me if it's a mountain top (max) 
        or valley bottom (min)."*
        """)
    
    # Section 4: Tangent Lines and Local Behavior
    st.markdown("---")
    st.header("4️⃣ Understanding Local Behavior: Tangent Lines")
    
    st.markdown("""
    **Priya's Question:** *"I understand derivatives give me rates, but how do I visualize 
    this? How can I see the 'speed' at any specific point?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📐 Tangent Line Explorer")
        
        st.markdown("""
        **What is a Tangent Line?**
        The tangent line at any point shows the instantaneous rate of change - 
        it's the "direction" the function is heading at that exact moment.
        
        **Slope of Tangent = Derivative Value**
        """)
        
        # Interactive tangent line
        selected_day = st.slider("Select Day for Tangent Analysis", 1.0, 10.0, 4.0, 0.5)
        
        # Use the fund function from earlier
        fund_func_tangent = c + a*selected_day - b*selected_day**2
        derivative_at_point = a - 2*b*selected_day
        
        st.code(f"""
At Day {selected_day}:
Fund Value: f({selected_day}) = {fund_func_tangent:.2f} crores
Derivative: f'({selected_day}) = {derivative_at_point:.2f} crores/day

Tangent Line Equation:
y = {derivative_at_point:.2f}(t - {selected_day}) + {fund_func_tangent:.2f}
        """)
        
        if derivative_at_point > 0:
            st.success(f"📈 Growing at {derivative_at_point:.2f} crores/day")
        elif derivative_at_point < 0:
            st.warning(f"📉 Declining at {abs(derivative_at_point):.2f} crores/day")
        else:
            st.info("⚖️ Rate of change is zero - critical point!")
    
    with col2:
        st.subheader("📊 Tangent Line Visualization")
        
        # Create detailed plot around selected point
        t_detailed = np.linspace(max(0, selected_day-3), selected_day+3, 100)
        f_detailed = c + a*t_detailed - b*t_detailed**2
        
        # Tangent line calculation
        tangent_slope = a - 2*b*selected_day
        tangent_intercept = fund_func_tangent - tangent_slope*selected_day
        tangent_line = tangent_slope * t_detailed + tangent_intercept
        
        fig = go.Figure()
        
        # Original function
        fig.add_trace(go.Scatter(
            x=t_detailed, y=f_detailed,
            mode='lines',
            name='Fund Value Function',
            line=dict(color='blue', width=3)
        ))
        
        # Tangent line
        fig.add_trace(go.Scatter(
            x=t_detailed, y=tangent_line,
            mode='lines',
            name=f'Tangent at Day {selected_day}',
            line=dict(color='red', width=2, dash='dash')
        ))
        
        # Point of tangency
        fig.add_trace(go.Scatter(
            x=[selected_day], y=[fund_func_tangent],
            mode='markers',
            name='Point of Analysis',
            marker=dict(color='red', size=12)
        ))
        
        fig.update_layout(
            title=f"Tangent Line Analysis at Day {selected_day}",
            xaxis_title="Day",
            yaxis_title="Fund Value (₹ Crores)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 5: Marginal Analysis in Business
    st.markdown("---")
    st.header("5️⃣ Marginal Analysis: Business Decision Making")
    
    st.markdown("""
    **Priya's Advanced Application:** *"Now I understand rates! But how do I use this 
    for business decisions like pricing, production, and investment levels?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💰 Marginal Revenue vs Marginal Cost")
        
        st.markdown("""
        **Key Business Insight:**
        - **Marginal Revenue** = Derivative of Revenue function
        - **Marginal Cost** = Derivative of Cost function  
        - **Optimal Production** = Where Marginal Revenue = Marginal Cost
        """)
        
        # Interactive marginal analysis
        fixed_cost = st.slider("Fixed Cost (₹ thousands)", 100, 500, 200, 50)
        variable_cost_rate = st.slider("Variable Cost Rate", 2.0, 10.0, 5.0, 0.5)
        max_price = st.slider("Maximum Price (₹)", 20, 50, 35, 5)
        
        # Define cost and revenue functions
        q = symbols('q')  # quantity
        cost_func = fixed_cost + variable_cost_rate * q + 0.1 * q**2
        revenue_func = max_price * q - 0.2 * q**2
        profit_func = revenue_func - cost_func
        
        # Calculate marginals
        marginal_cost = diff(cost_func, q)
        marginal_revenue = diff(revenue_func, q)
        marginal_profit = diff(profit_func, q)
        
        # Find optimal quantity
        optimal_q = solve(marginal_revenue - marginal_cost, q)
        
        if optimal_q and len(optimal_q) > 0:
            opt_q = float(optimal_q[0])
            if opt_q > 0:
                opt_profit = float(profit_func.subs(q, opt_q))
                opt_mc = float(marginal_cost.subs(q, opt_q))
                opt_mr = float(marginal_revenue.subs(q, opt_q))
                
                st.success(f"""
                **Optimal Business Decision:**
                - **Optimal Quantity:** {opt_q:.1f} units
                - **Maximum Profit:** ₹{opt_profit:.0f} thousands
                - **Marginal Cost at optimum:** ₹{opt_mc:.2f}
                - **Marginal Revenue at optimum:** ₹{opt_mr:.2f}
                """)
    
    with col2:
        st.subheader("📊 Marginal Analysis Visualization")
        
        # Create quantity range
        q_vals = np.linspace(1, 20, 100)
        
        # Convert to numerical functions
        mc_numeric = lambdify(q, marginal_cost, 'numpy')
        mr_numeric = lambdify(q, marginal_revenue, 'numpy')
        
        mc_vals = mc_numeric(q_vals)
        mr_vals = mr_numeric(q_vals)
        
        fig = go.Figure()
        
        # Marginal cost
        fig.add_trace(go.Scatter(
            x=q_vals, y=mc_vals,
            mode='lines',
            name='Marginal Cost',
            line=dict(color='red', width=3)
        ))
        
        # Marginal revenue
        fig.add_trace(go.Scatter(
            x=q_vals, y=mr_vals,
            mode='lines',
            name='Marginal Revenue',
            line=dict(color='green', width=3)
        ))
        
        # Mark optimal point
        if optimal_q and len(optimal_q) > 0 and opt_q > 0:
            fig.add_trace(go.Scatter(
                x=[opt_q], y=[opt_mc],
                mode='markers',
                name='Optimal Point',
                marker=dict(color='blue', size=15, symbol='star')
            ))
            
            fig.add_annotation(
                x=opt_q, y=opt_mc,
                text=f"Optimal Production<br>{opt_q:.1f} units",
                showarrow=True,
                arrowhead=2
            )
        
        fig.update_layout(
            title="Marginal Analysis - Finding Optimal Production",
            xaxis_title="Quantity (units)",
            yaxis_title="Marginal Value (₹)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 6: Key Business Applications
    st.markdown("---")
    st.header("6️⃣ Priya's Business Applications Mastery")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Investment Analysis**
        - Portfolio growth rates
        - Risk-return optimization  
        - Performance trend analysis
        - Optimal allocation timing
        """)
    
    with col2:
        st.markdown("""
        **📈 Revenue Optimization**
        - Price sensitivity analysis
        - Demand curve analysis
        - Profit maximization points
        - Market timing decisions
        """)
    
    with col3:
        st.markdown("""
        **💼 Cost Management**
        - Marginal cost analysis
        - Production optimization
        - Efficiency improvements
        - Break-even analysis
        """)
    
    # Practice Exercise
    st.markdown("---")
    st.subheader("💪 Practice: Apply Derivative Analysis")
    
    with st.expander("📝 Exercise: Bond Price Sensitivity"):
        st.markdown("""
        **Scenario:** A bond's price varies with interest rate changes.
        Price function: P(r) = 1000 × e^(-0.1r) where r is interest rate %
        
        **Tasks:**
        1. Find the derivative P'(r) - this is called "duration" in finance
        2. What's the price sensitivity when interest rate is 5%?
        3. If rates increase by 0.1%, how much does bond price change?
        4. At what rate is the price declining fastest?
        """)
        
        if st.button("Show Solution", key="derivatives_exercise"):
            st.markdown("---")
            st.markdown("### 🔍 **Solution:**")
            
            # Bond price analysis
            r = symbols('r')
            bond_price = 1000 * sp.exp(-0.1 * r)
            duration = diff(bond_price, r)
            
            st.code(f"""
Bond Price Function: P(r) = {bond_price}
Duration (Price Sensitivity): P'(r) = {duration}

At r = 5%:
Price: P(5) = {float(bond_price.subs(r, 5)):.2f}
Duration: P'(5) = {float(duration.subs(r, 5)):.2f}

For 0.1% rate increase:
Price change ≈ P'(5) × 0.1 = {float(duration.subs(r, 5)) * 0.1:.2f}
            """)
            
            st.success("""
            **Business Interpretation:**
            - Duration measures bond price sensitivity to interest rate changes
            - Negative duration means prices fall when rates rise
            - This helps in portfolio risk management and hedging decisions
            """)
    
    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Previous: Calculus Overview"):
            st.session_state.page = 'calculus'
            st.rerun()
    
    with col2:
        if st.button("Next: Integrals →"):
            st.session_state.page = 'calculus_integrals'
            st.rerun()
    
    st.markdown("---")
    st.success("""
    🎓 **Priya's Derivative Mastery Achieved!**
    
    Priya now understands how to:
    ✅ **Measure rates of change** in financial data
    ✅ **Find optimal points** for maximum profit and minimum cost  
    ✅ **Analyze trends** and predict turning points
    ✅ **Use marginal analysis** for business decisions
    ✅ **Apply tangent lines** to understand local behavior
    
    **Next:** Learn how Priya uses integrals to calculate total accumulated values 
    from these rates of change!
    """)