import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

def show_eigenvalues_eigenvectors():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Linear Algebra"):
            st.session_state.page = 'linear_algebra'
            st.rerun()
    
    with col2:
        st.title("🎯 Eigenvalues & Eigenvectors")
    
    # Breadcrumb
    st.markdown("**Home** > **Linear Algebra** > **Eigenvalues & Eigenvectors**")
    
    st.markdown("---")
    
    # Story Introduction
    st.header("📖 Arjun's Investment Portfolio Challenge")
    
    st.markdown("""
    **Meet Mr. Sharma:** A local businessman comes to Arjun with ₹10 lakhs to invest. 
    He's overwhelmed by chaotic market data and asks:
    
    *"Arjun, is there any STABLE direction I can invest in that won't keep changing every month?"*
    """)
    
    # Section 1: The Business Problem
    st.markdown("---")
    st.header("1️⃣ The Overwhelming Market Data")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Monthly Market Chaos")
        
        # Sample market data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        stock_returns = [5, -3, 7, -2, 4, -1]
        bond_returns = [2, 1, 3, -1, 1, 2]
        
        # Create chaos visualization
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=stock_returns, mode='lines+markers', 
                                name='Stocks', line=dict(color='red', width=3)))
        fig.add_trace(go.Scatter(x=months, y=bond_returns, mode='lines+markers', 
                                name='Bonds', line=dict(color='blue', width=3)))
        
        fig.update_layout(
            title="Mr. Sharma's Confusion: Monthly Returns (%)",
            xaxis_title="Month",
            yaxis_title="Return %",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("😰 Mr. Sharma's Frustration")
        st.markdown("""
        **What Mr. Sharma sees:**
        - Month 1: Stocks +5%, Bonds +2%
        - Month 2: Stocks -3%, Bonds +1%  
        - Month 3: Stocks +7%, Bonds +3%
        - Month 4: Stocks -2%, Bonds -1%
        
        **His Questions:**
        - *"Which direction should I invest?"*
        - *"Is there any pattern in this chaos?"*
        - *"Will my portfolio keep changing every month?"*
        - *"What's the optimal long-term strategy?"*
        """)
        
        st.warning("""
        **Mr. Sharma's Challenge:** 
        *"I need a STABLE investment direction that won't drift every month!"*
        """)
    
    # Section 2: Arjun's Discovery Process
    st.markdown("---")
    st.header("2️⃣ Arjun's Mathematical Approach")
    
    st.markdown("""
    **Arjun's Insight:** *"Let me organize this chaos mathematically and find hidden patterns..."*
    """)
    
    st.subheader("🔢 The Market Transformation Matrix")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Arjun's Method:** Instead of looking at random monthly data, he creates a 
        "Market Behavior Matrix" that captures how portfolios typically transform:
        """)
        
        # Market matrix
        A = np.array([[1.05, 0.02], [0.01, 1.03]])
        
        st.code("""
Market Matrix A = [[1.05, 0.02],
                   [0.01, 1.03]]
        """)
        
        st.markdown("""
        **What this means:**
        - **Row 1:** Next month's stock % = 1.05 × current stock % + 0.02 × current bond %
        - **Row 2:** Next month's bond % = 0.01 × current stock % + 1.03 × current bond %
        """)
    
    with col2:
        st.subheader("🧪 Portfolio Evolution Simulator")
        
        # Interactive portfolio transformation
        initial_stocks = st.slider("Initial Stock %", 0, 100, 60, key="initial_stocks")
        initial_bonds = 100 - initial_stocks
        
        # Simulate portfolio evolution
        portfolio = np.array([initial_stocks/100, initial_bonds/100])
        evolution = [portfolio.copy()]
        
        for month in range(12):
            portfolio = A @ portfolio
            # Normalize to ensure percentages add to 1
            portfolio = portfolio / np.sum(portfolio)
            evolution.append(portfolio.copy())
        
        # Display evolution
        months_sim = list(range(13))
        stock_evolution = [p[0]*100 for p in evolution]
        bond_evolution = [p[1]*100 for p in evolution]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months_sim, y=stock_evolution, mode='lines+markers',
                                name='Stocks %', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=months_sim, y=bond_evolution, mode='lines+markers',
                                name='Bonds %', line=dict(color='blue')))
        
        fig.update_layout(
            title="Portfolio Evolution Over 12 Months",
            xaxis_title="Month",
            yaxis_title="Allocation %",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Final Portfolio:** {stock_evolution[-1]:.1f}% stocks, {bond_evolution[-1]:.1f}% bonds
        
        **Arjun's Observation:** *"No matter where we start, portfolios drift toward similar ratios!"*
        """)
    
    # Section 3: The Mathematical Discovery
    st.markdown("---")
    st.header("3️⃣ Finding the Stable Patterns (Eigenvectors)")
    
    st.markdown("""
    **The Key Question:** *"Is there a portfolio mix that stays exactly the same after transformation?"*
    
    **Mathematical Setup:** Find vectors **v** where **A × v = λ × v**
    - **A** = Market transformation matrix
    - **v** = Special stable direction (eigenvector)  
    - **λ** = Growth strength (eigenvalue)
    """)
    
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # Sort by eigenvalue magnitude
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Ensure positive eigenvectors for portfolio interpretation
    for i in range(len(eigenvectors[0])):
        if eigenvectors[0, i] < 0:
            eigenvectors[:, i] = -eigenvectors[:, i]
    
    # Normalize eigenvectors to sum to 1 (portfolio weights)
    eigenvectors_norm = np.abs(eigenvectors)
    for i in range(eigenvectors_norm.shape[1]):
        eigenvectors_norm[:, i] = eigenvectors_norm[:, i] / np.sum(eigenvectors_norm[:, i])
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔍 Step-by-Step Calculation")
        
        st.markdown("**Step 1: Characteristic Equation**")
        st.latex(r"det(A - \lambda I) = 0")
        
        st.markdown("**Step 2: Solve for λ (eigenvalues)**")
        st.code(f"""
(1.05-λ)(1.03-λ) - (0.02)(0.01) = 0
λ² - 2.08λ + 1.0813 = 0

Solutions:
λ₁ = {eigenvalues[0]:.3f} (Stronger pattern)
λ₂ = {eigenvalues[1]:.3f} (Weaker pattern)
        """)
        
        st.markdown("**Step 3: Find eigenvectors**")
        st.code(f"""
Eigenvector 1: [{eigenvectors_norm[0,0]:.2f}, {eigenvectors_norm[1,0]:.2f}]
→ {eigenvectors_norm[0,0]*100:.0f}% stocks, {eigenvectors_norm[1,0]*100:.0f}% bonds

Eigenvector 2: [{eigenvectors_norm[0,1]:.2f}, {eigenvectors_norm[1,1]:.2f}]  
→ {eigenvectors_norm[0,1]*100:.0f}% stocks, {eigenvectors_norm[1,1]*100:.0f}% bonds
        """)
    
    with col2:
        st.subheader("📈 Visualization of Stable Directions")
        
        # Create portfolio space visualization
        fig = go.Figure()
        
        # Plot eigenvectors as arrows
        fig.add_trace(go.Scatter(
            x=[0, eigenvectors_norm[0,0]], 
            y=[0, eigenvectors_norm[1,0]],
            mode='lines+markers',
            name=f'Pattern 1 (λ={eigenvalues[0]:.3f})',
            line=dict(color='green', width=4),
            marker=dict(size=10)
        ))
        
        fig.add_trace(go.Scatter(
            x=[0, eigenvectors_norm[0,1]], 
            y=[0, eigenvectors_norm[1,1]],
            mode='lines+markers',
            name=f'Pattern 2 (λ={eigenvalues[1]:.3f})',
            line=dict(color='orange', width=4),
            marker=dict(size=10)
        ))
        
        # Add some sample portfolio trajectories
        for start in [[0.8, 0.2], [0.4, 0.6], [0.6, 0.4]]:
            portfolio = np.array(start)
            trajectory_x, trajectory_y = [portfolio[0]], [portfolio[1]]
            
            for _ in range(20):
                portfolio = A @ portfolio
                portfolio = portfolio / np.sum(portfolio)
                trajectory_x.append(portfolio[0])
                trajectory_y.append(portfolio[1])
            
            fig.add_trace(go.Scatter(
                x=trajectory_x, y=trajectory_y,
                mode='lines',
                line=dict(color='lightblue', width=2, dash='dash'),
                showlegend=False
            ))
        
        fig.update_layout(
            title="Portfolio Paths Toward Stable Directions",
            xaxis_title="Stock Allocation",
            yaxis_title="Bond Allocation",
            height=400,
            xaxis=dict(range=[0, 1]),
            yaxis=dict(range=[0, 1])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 4: Business Interpretation
    st.markdown("---")
    st.header("4️⃣ Arjun's Business Translation")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🏆 Pattern 1: 'The Wealth Builder'")
        st.success(f"""
        **Portfolio Mix:** {eigenvectors_norm[0,0]*100:.0f}% stocks, {eigenvectors_norm[1,0]*100:.0f}% bonds
        
        **Growth Rate:** {(eigenvalues[0]-1)*100:.1f}% annually
        
        **Business Meaning:** 
        - Optimal long-term growth strategy
        - Naturally stable - no rebalancing needed
        - Aligned with market's dominant trend
        - Works in both bull and bear markets
        """)
        
        st.markdown(f"""
        **For Mr. Sharma's ₹10 lakhs:**
        - **Stocks:** ₹{eigenvectors_norm[0,0]*10:.1f} lakhs
        - **Bonds:** ₹{eigenvectors_norm[1,0]*10:.1f} lakhs
        """)
    
    with col2:
        st.subheader("📊 Pattern 2: 'The Conservative Path'")
        st.info(f"""
        **Portfolio Mix:** {eigenvectors_norm[0,1]*100:.0f}% stocks, {eigenvectors_norm[1,1]*100:.0f}% bonds
        
        **Growth Rate:** {(eigenvalues[1]-1)*100:.1f}% annually
        
        **Business Meaning:**
        - Conservative, stable approach  
        - Lower growth but higher security
        - Good for risk-averse investors
        - Very predictable returns
        """)
        
        st.markdown(f"""
        **For Mr. Sharma's ₹10 lakhs:**
        - **Stocks:** ₹{eigenvectors_norm[0,1]*10:.1f} lakhs  
        - **Bonds:** ₹{eigenvectors_norm[1,1]*10:.1f} lakhs
        """)
    
    # Section 5: Interactive Portfolio Tester
    st.markdown("---")
    st.header("5️⃣ Test Your Own Portfolio Strategy")
    
    st.subheader("🧪 Portfolio Stability Tester")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Try Different Starting Portfolios:**")
        
        test_stocks = st.slider("Test Portfolio - Stock %", 0, 100, 70, key="test_stocks")
        test_bonds = 100 - test_stocks
        
        # Test portfolio evolution
        test_portfolio = np.array([test_stocks/100, test_bonds/100])
        test_evolution = [test_portfolio.copy()]
        
        for month in range(60):  # 5 years
            test_portfolio = A @ test_portfolio
            test_portfolio = test_portfolio / np.sum(test_portfolio)
            test_evolution.append(test_portfolio.copy())
        
        final_stocks = test_evolution[-1][0] * 100
        final_bonds = test_evolution[-1][1] * 100
        
        st.write(f"**Starting:** {test_stocks}% stocks, {test_bonds}% bonds")
        st.write(f"**After 5 years:** {final_stocks:.1f}% stocks, {final_bonds:.1f}% bonds")
        
        # Check which eigenvector it's closest to
        final_portfolio = np.array([final_stocks/100, final_bonds/100])
        
        dist1 = np.linalg.norm(final_portfolio - eigenvectors_norm[:, 0])
        dist2 = np.linalg.norm(final_portfolio - eigenvectors_norm[:, 1])
        
        if dist1 < dist2:
            st.success("✅ Converged to **Wealth Builder** pattern!")
        else:
            st.info("✅ Converged to **Conservative** pattern!")
    
    with col2:
        # Plot evolution
        months_test = list(range(61))
        stock_test_evolution = [p[0]*100 for p in test_evolution]
        bond_test_evolution = [p[1]*100 for p in test_evolution]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months_test, y=stock_test_evolution, 
                                mode='lines', name='Stocks %', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=months_test, y=bond_test_evolution, 
                                mode='lines', name='Bonds %', line=dict(color='blue')))
        
        # Add target lines
        fig.add_hline(y=eigenvectors_norm[0,0]*100, line_dash="dash", line_color="green",
                     annotation_text="Wealth Builder Target")
        fig.add_hline(y=eigenvectors_norm[0,1]*100, line_dash="dash", line_color="orange",
                     annotation_text="Conservative Target")
        
        fig.update_layout(
            title="Your Portfolio Evolution (5 Years)",
            xaxis_title="Month",
            yaxis_title="Allocation %",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 6: Key Insights
    st.markdown("---")
    st.header("6️⃣ Arjun's Final Recommendation to Mr. Sharma")
    
    st.success(f"""
    ## 🎯 **The Mathematical Solution**
    
    **Mr. Sharma, here's what the mathematics reveals:**
    
    ✅ **Hidden in market chaos are exactly TWO stable investment patterns**
    
    ✅ **Pattern 1 (Recommended):** {eigenvectors_norm[0,0]*100:.0f}% stocks, {eigenvectors_norm[1,0]*100:.0f}% bonds
    - Annual growth: {(eigenvalues[0]-1)*100:.1f}%
    - Naturally stable across all market conditions
    - No rebalancing needed - maintains itself
    
    ✅ **Pattern 2 (Conservative):** {eigenvectors_norm[0,1]*100:.0f}% stocks, {eigenvectors_norm[1,1]*100:.0f}% bonds  
    - Annual growth: {(eigenvalues[1]-1)*100:.1f}%
    - Very safe but lower returns
    
    **The Guarantee:** These aren't random recommendations - they're mathematically proven stable points where market forces naturally balance out.
    
    **My Recommendation for your ₹10 lakhs:**
    - **₹{eigenvectors_norm[0,0]*10:.1f} lakhs in stocks**
    - **₹{eigenvectors_norm[1,0]*10:.1f} lakhs in bonds**
    
    This portfolio will ride the market's strongest natural trend while remaining stable over time!
    """)
    
    # Key Concepts Summary
    st.markdown("---")
    st.header("🎓 Key Mathematical Concepts Learned")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **🔑 Eigenvector** 
        - "Special stable direction"
        - Portfolio mix that doesn't drift over time
        - Optimal allocation ratio
        
        **🔢 Eigenvalue**
        - "Growth strength of stable direction"  
        - Annual return rate
        - Pattern dominance measure
        
        **⚖️ Market Transformation**
        - How portfolios evolve monthly
        - Mathematical description of market forces
        - Predictable long-term behavior
        """)
    
    with col2:
        st.markdown("""
        **💡 Business Applications:**
        
        ✅ **Portfolio Optimization** - Find mathematically optimal allocations
        
        ✅ **Risk Management** - Align with stable market patterns
        
        ✅ **Long-term Strategy** - Focus on fundamental stability, not daily chaos
        
        ✅ **Investment Discipline** - Trust mathematics over emotions
        """)
    
    # Practice Exercise
    st.markdown("---")
    st.subheader("💪 Practice: Apply Eigenvalue Analysis")
    
    with st.expander("📝 Exercise: Corporate Investment Strategy"):
        st.markdown("""
        **Scenario:** A company has ₹1 crore to allocate between R&D and Marketing.
        Historical data shows the transformation matrix:
        
        ```
        A = [[1.08, 0.05],
             [0.02, 1.06]]
        ```
        
        **Tasks:**
        1. Find the eigenvalues and eigenvectors
        2. Determine the optimal allocation strategy  
        3. Calculate expected annual growth
        4. Recommend the investment split
        """)
        
        if st.button("Show Solution", key="eigen_exercise"):
            st.markdown("---")
            st.markdown("### 🔍 **Solution:**")
            
            # Corporate matrix
            A_corp = np.array([[1.08, 0.05], [0.02, 1.06]])
            eigenvals, eigenvecs = np.linalg.eig(A_corp)
            
            # Sort and normalize
            idx = np.argsort(eigenvals)[::-1]
            eigenvals = eigenvals[idx]
            eigenvecs = eigenvecs[:, idx]
            
            # Ensure positive and normalize
            for i in range(len(eigenvecs[0])):
                if eigenvecs[0, i] < 0:
                    eigenvecs[:, i] = -eigenvecs[:, i]
            
            eigenvecs_norm = np.abs(eigenvecs)
            for i in range(eigenvecs_norm.shape[1]):
                eigenvecs_norm[:, i] = eigenvecs_norm[:, i] / np.sum(eigenvecs_norm[:, i])
            
            st.code(f"""
Eigenvalues: λ₁ = {eigenvals[0]:.3f}, λ₂ = {eigenvals[1]:.3f}

Optimal Strategy:
- R&D: {eigenvecs_norm[0,0]*100:.0f}%
- Marketing: {eigenvecs_norm[1,0]*100:.0f}%

Expected Growth: {(eigenvals[0]-1)*100:.1f}% annually

Recommendation for ₹1 crore:
- R&D: ₹{eigenvecs_norm[0,0]*100:.0f} lakhs
- Marketing: ₹{eigenvecs_norm[1,0]*100:.0f} lakhs
            """)
            
            st.success("This allocation will provide maximum stable growth!")
    
    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Previous: Vectors & Matrices"):
            st.session_state.page = 'linear_algebra_vectors'
            st.rerun()
    
    with col2:
        if st.button("Next: Principal Component Analysis →"):
            st.session_state.page = 'linear_algebra_pca'
            st.rerun()
    
    st.markdown("---")
    st.info("""
    🎯 **Next in Arjun's Journey:** 
    Now that Arjun can find stable patterns in data, he'll learn to compress complex 
    multi-dimensional information into simple, powerful insights using 
    **Principal Component Analysis (PCA)**!
    """)