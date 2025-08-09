import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import scipy.optimize as opt
from scipy.optimize import linprog

def show_optimization():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("🎯 Optimization - Smart Resource Allocation")
    
    # Breadcrumb
    st.markdown("**Home** > **Optimization**")
    
    st.markdown("---")
    
    # Introduction - Anand's Confusion
    st.header("📖 Anand's Overwhelming Choice Problem")
    
    st.markdown("""
    **Meet Anand!** He manages an electronics manufacturing unit in Pune that produces smartphones and tablets. 
    Every day, he faces a confusing question that affects his company's profit:
    
    *"With limited workers, materials, and money - what's the BEST production mix to maximize profit?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("😰 Anand's Daily Dilemma")
        st.markdown("""
        **Product Options:**
        - **Smartphones:** ₹8,000 profit each
        - **Tablets:** ₹12,000 profit each
        
        **Available Resources:**
        - 40 workers (8 hours/day each) = 320 total labor hours
        - ₹50 lakh material budget  
        - 1,000 sq ft storage space
        
        **Resource Requirements per Unit:**
        - **Smartphone:** 1 hour labor, ₹3,000 materials, 2 sq ft storage
        - **Tablet:** 2 hours labor, ₹6,000 materials, 4 sq ft storage
        
        **Anand's Confusion:**
        *"Should I make only tablets (higher profit)? 
        Only phones (easier to make)? Some mix? 
        How do I find the BEST combination?"*
        """)
    
    with col2:
        st.subheader("🤔 The Choice Overwhelm")
        
        # Show some possible combinations
        combinations_df = pd.DataFrame({
            'Option': ['All Phones', 'All Tablets', 'Mix 1', 'Mix 2', 'Mix 3', '???'],
            'Phones': [160, 0, 100, 120, 80, '?'],
            'Tablets': [0, 160, 50, 40, 60, '?'],
            'Daily Profit (₹)': ['12,80,000', '19,20,000', '14,00,000', '14,40,000', '13,60,000', '???']
        })
        
        st.dataframe(combinations_df, use_container_width=True)
        
        st.warning("""
        **Anand's Problem:**
        - Hundreds of possible combinations!
        - Which one gives maximum profit?
        - How to check all constraints?
        - Trial and error takes forever!
        
        **Need:** A systematic mathematical approach!
        """)
    
    # Section 1: What is Optimization?
    st.markdown("---")
    st.header("1️⃣ What is Optimization? (Finding the Best)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 Simple Definition")
        st.markdown("""
        **Optimization = Finding the BEST solution from ALL possible choices**
        
        **Real-Life Examples:**
        - **Route Planning:** Fastest path to office among many roads
        - **Shopping:** Best value for money among products
        - **Diet Planning:** Healthiest meal within budget
        - **Investment:** Best return with acceptable risk
        
        **Anand's Case:**
        Find the production mix that gives **maximum profit** 
        from all possible phone-tablet combinations.
        """)
        
        st.info("""
        **Key Insight:** 
        Optimization isn't guessing - it's **mathematical certainty** 
        that you found the absolute best solution!
        """)
    
    with col2:
        st.subheader("📊 The Optimization Mindset")
        
        # Simple optimization example
        x_simple = np.linspace(0, 10, 100)
        y_simple = -(x_simple - 5)**2 + 25  # Parabola with maximum at x=5
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x_simple, y=y_simple,
            mode='lines',
            name='Profit Function',
            line=dict(color='blue', width=3)
        ))
        
        # Mark the maximum
        fig.add_trace(go.Scatter(
            x=[5], y=[25],
            mode='markers',
            name='Optimal Point',
            marker=dict(color='red', size=15, symbol='star')
        ))
        
        fig.update_layout(
            title="Simple Optimization: Finding the Peak",
            xaxis_title="Production Level",
            yaxis_title="Profit",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("""
        **Optimization Goal:** 
        Find the 🌟 **star point** - the peak profit 
        among ALL possible production levels.
        """)
    
    # Section 2: Why Do We Need Optimization?
    st.markdown("---")
    st.header("2️⃣ Why Do We Need Optimization? (The Business Reality)")
    
    st.markdown("""
    **Anand's Realization:** *"I can't just produce infinite tablets for infinite profit. 
    Real business has LIMITATIONS that constrain my choices!"*
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("⏰ Limited Resources")
        st.markdown("""
        **The Reality:**
        - Workers: 40 people only
        - Money: ₹50 lakh budget
        - Space: 1,000 sq ft storage
        - Time: 8 hours/day max
        
        **Cannot:**
        - Hire infinite workers
        - Spend unlimited money
        - Use unlimited space
        """)
    
    with col2:
        st.subheader("🎯 Multiple Objectives")
        st.markdown("""
        **Want to:**
        - Maximize profit
        - Minimize waste
        - Satisfy all customers
        - Keep workers happy
        - Meet deadlines
        
        **Challenge:**
        Often conflicting goals!
        """)
    
    with col3:
        st.subheader("🔄 Complex Relationships")
        st.markdown("""
        **Dependencies:**
        - More phones = Less tablets
        - More profit = More resources
        - Higher quality = Higher cost
        - Faster production = More errors
        
        **Need:**
        Mathematical balance!
        """)
    
    st.info("""
    **Why Optimization is Essential:**
    Real business = Limited resources + Multiple choices + Complex trade-offs
    
    **Without optimization:** Guesswork, suboptimal decisions, lost profits
    **With optimization:** Mathematical certainty of best possible outcome
    """)
    
    # Section 3: Linear Programming (LP) Basics
    st.markdown("---")
    st.header("3️⃣ Linear Programming: The Mathematical Solution")
    
    st.markdown("""
    **Anand's Discovery:** *"I need a systematic way to find the best production mix. 
    This is where Linear Programming comes in!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🧮 What is Linear Programming?")
        st.markdown("""
        **Simple Explanation:**
        Mathematical method to find the best solution when:
        - **Relationships are "linear"** (straight lines)
        - **Multiple variables** (phones, tablets)
        - **One objective** (maximize profit)
        - **Several constraints** (limited resources)
        
        **Why "Linear"?**
        - 1 phone = ₹8k profit
        - 2 phones = ₹16k profit  
        - 3 phones = ₹24k profit
        - (Straight line relationship!)
        
        **Why "Programming"?**
        Not computer programming - means "planning" or "scheduling"
        """)
        
        # LP formulation for Anand's problem
        st.markdown("**🎯 Anand's LP Formulation:**")
        st.code("""
Variables:
x₁ = Number of phones to produce
x₂ = Number of tablets to produce

Objective (Maximize):
Profit = 8000×x₁ + 12000×x₂

Subject to constraints:
(We'll add these in the next section!)
        """)
    
    with col2:
        st.subheader("📊 Linear Relationships Visualization")
        
        # Show linear profit relationship
        phones = np.linspace(0, 200, 50)
        tablets = np.linspace(0, 200, 50)
        
        # Create profit surface (linear)
        profit_phones = 8000 * phones
        profit_tablets = 12000 * tablets
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Phone Profit (Linear)', 'Tablet Profit (Linear)'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Phone profit line
        fig.add_trace(go.Scatter(
            x=phones, y=profit_phones,
            mode='lines',
            name='Phone Profit',
            line=dict(color='blue', width=3)
        ), row=1, col=1)
        
        # Tablet profit line
        fig.add_trace(go.Scatter(
            x=tablets, y=profit_tablets,
            mode='lines',
            name='Tablet Profit',
            line=dict(color='green', width=3)
        ), row=1, col=2)
        
        fig.update_layout(height=350, showlegend=False)
        fig.update_xaxes(title_text="Units Produced")
        fig.update_yaxes(title_text="Profit (₹)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("""
        **Linear Programming Power:**
        - **Systematic approach** to complex decisions
        - **Guaranteed optimal solution** (not guesswork)
        - **Handles multiple variables** simultaneously
        - **Mathematical certainty** of best outcome
        """)
    
    # Section 4: Understanding Constraints
    st.markdown("---")
    st.header("4️⃣ Understanding Constraints: Real Business Limitations")
    
    st.markdown("""
    **Anand's Reality Check:** *"I can't produce infinite tablets! I have real limitations 
    that constrain my production choices."*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("⚖️ What are Constraints?")
        st.markdown("""
        **Definition:** Real-world limitations that restrict your choices
        
        **Types of Business Constraints:**
        - **Resource Constraints:** Limited workers, materials, money
        - **Capacity Constraints:** Machine hours, storage space
        - **Demand Constraints:** Market size, customer requirements
        - **Regulatory Constraints:** Safety rules, legal limits
        - **Physical Constraints:** Cannot produce negative quantities!
        """)
        
        # Interactive constraint builder
        st.markdown("**🧮 Anand's Constraint Builder:**")
        
        # Let users modify constraints
        workers = st.slider("Available Workers", 20, 60, 40, 5)
        worker_hours = 8
        phone_time = st.slider("Hours per Phone", 0.5, 3.0, 1.0, 0.1)
        tablet_time = st.slider("Hours per Tablet", 1.0, 4.0, 2.0, 0.1)
        
        material_budget = st.slider("Material Budget (₹ lakhs)", 30, 100, 50, 5)
        phone_material = st.slider("Material Cost per Phone (₹)", 2000, 5000, 3000, 100)
        tablet_material = st.slider("Material Cost per Tablet (₹)", 4000, 8000, 6000, 200)
        
        storage_space = st.slider("Storage Space (sq ft)", 500, 2000, 1000, 100)
        phone_space = st.slider("Space per Phone (sq ft)", 1, 5, 2, 1)
        tablet_space = st.slider("Space per Tablet (sq ft)", 2, 8, 4, 1)
        
        st.code(f"""
Anand's Constraints:

1. Labor Constraint:
   {phone_time}×x₁ + {tablet_time}×x₂ ≤ {workers * worker_hours} hours/day
   
2. Material Budget Constraint:
   {phone_material}×x₁ + {tablet_material}×x₂ ≤ {material_budget * 100000}
   
3. Storage Constraint:
   {phone_space}×x₁ + {tablet_space}×x₂ ≤ {storage_space} sq ft
   
4. Non-negativity:
   x₁ ≥ 0, x₂ ≥ 0 (Cannot produce negative units!)
        """)
    
    with col2:
        st.subheader("📊 Constraint Visualization")
        
        # Create feasible region visualization
        x1_max = min(workers * worker_hours / phone_time, 
                    material_budget * 100000 / phone_material, 
                    storage_space / phone_space)
        x2_max = min(workers * worker_hours / tablet_time, 
                    material_budget * 100000 / tablet_material, 
                    storage_space / tablet_space)
        
        x1_range = np.linspace(0, x1_max * 1.2, 100)
        
        # Calculate constraint lines
        labor_line = (workers * worker_hours - phone_time * x1_range) / tablet_time
        material_line = (material_budget * 100000 - phone_material * x1_range) / tablet_material
        storage_line = (storage_space - phone_space * x1_range) / tablet_space
        
        fig = go.Figure()
        
        # Constraint lines
        fig.add_trace(go.Scatter(
            x=x1_range, y=np.maximum(0, labor_line),
            mode='lines',
            name=f'Labor Constraint',
            line=dict(color='red', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=x1_range, y=np.maximum(0, material_line),
            mode='lines',
            name=f'Material Constraint',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=x1_range, y=np.maximum(0, storage_line),
            mode='lines',
            name=f'Storage Constraint',
            line=dict(color='green', width=2)
        ))
        
        # Feasible region (approximate)
        feasible_x = []
        feasible_y = []
        for x in x1_range[::5]:  # Sample points
            max_y = min(
                max(0, (workers * worker_hours - phone_time * x) / tablet_time),
                max(0, (material_budget * 100000 - phone_material * x) / tablet_material),
                max(0, (storage_space - phone_space * x) / tablet_space)
            )
            if max_y >= 0:
                feasible_x.extend([x, x])
                feasible_y.extend([0, max_y])
        
        # Shade feasible region
        if feasible_x:
            fig.add_trace(go.Scatter(
                x=feasible_x, y=feasible_y,
                fill='tonext',
                mode='none',
                name='Feasible Region',
                fillcolor='rgba(128,128,128,0.3)'
            ))
        
        fig.update_layout(
            title="Feasible Production Region",
            xaxis_title="Phones (x₁)",
            yaxis_title="Tablets (x₂)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Feasible Region Insights:**
        - **Gray area:** All possible production combinations
        - **Boundaries:** Constraint limits
        - **Outside gray:** Impossible (violates constraints)
        - **Optimal point:** Somewhere on the boundary!
        """)
    
    # Section 5: Solving the LP Problem
    st.markdown("---")
    st.header("5️⃣ Finding the Optimal Solution")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 LP Solution Method")
        st.markdown("""
        **The Mathematical Approach:**
        
        **Step 1:** Set up the problem mathematically
        **Step 2:** Find the feasible region  
        **Step 3:** Check corner points of feasible region
        **Step 4:** The corner with highest profit = Optimal solution!
        
        **Why Corner Points?**
        In linear programming, the optimal solution always lies 
        at a corner (vertex) of the feasible region.
        """)
        
        # Solve the LP problem
        try:
            # Coefficients for objective function (we want to maximize, so negate)
            c = [-8000, -12000]  # Negative because linprog minimizes
            
            # Inequality constraint matrix (Ax <= b)
            A = [
                [phone_time, tablet_time],  # Labor constraint
                [phone_material, tablet_material],  # Material constraint  
                [phone_space, tablet_space]  # Storage constraint
            ]
            
            b = [
                workers * worker_hours,  # Labor limit
                material_budget * 100000,  # Material limit
                storage_space  # Storage limit
            ]
            
            # Bounds for variables (non-negative)
            x1_bounds = (0, None)
            x2_bounds = (0, None)
            
            # Solve the LP problem
            result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')
            
            if result.success:
                optimal_phones = result.x[0]
                optimal_tablets = result.x[1]
                max_profit = -result.fun  # Negate back since we minimized
                
                st.code(f"""
OPTIMAL SOLUTION FOUND! 🎉

Optimal Production Mix:
📱 Phones: {optimal_phones:.1f} units/day
📟 Tablets: {optimal_tablets:.1f} units/day

Maximum Daily Profit: ₹{max_profit:,.0f}

Resource Utilization:
Labor: {phone_time * optimal_phones + tablet_time * optimal_tablets:.1f}/{workers * worker_hours} hours
Material: ₹{phone_material * optimal_phones + tablet_material * optimal_tablets:,.0f}/{material_budget * 100000:,}
Storage: {phone_space * optimal_phones + tablet_space * optimal_tablets:.1f}/{storage_space} sq ft
                """)
                
                st.success(f"""
                **Anand's Breakthrough:**
                Mathematical optimization found the BEST production mix!
                Daily profit of ₹{max_profit:,.0f} is guaranteed optimal.
                """)
            else:
                st.error("No feasible solution found with current constraints!")
                
        except Exception as e:
            st.error(f"Optimization error: {str(e)}")
    
    with col2:
        st.subheader("📊 Optimal Solution Visualization")
        
        if 'optimal_phones' in locals() and result.success:
            # Enhanced feasible region with optimal point
            fig = go.Figure()
            
            # Constraint lines (same as before)
            fig.add_trace(go.Scatter(
                x=x1_range, y=np.maximum(0, labor_line),
                mode='lines',
                name=f'Labor Constraint',
                line=dict(color='red', width=2)
            ))
            
            fig.add_trace(go.Scatter(
                x=x1_range, y=np.maximum(0, material_line),
                mode='lines',
                name=f'Material Constraint',
                line=dict(color='blue', width=2)
            ))
            
            fig.add_trace(go.Scatter(
                x=x1_range, y=np.maximum(0, storage_line),
                mode='lines',
                name=f'Storage Constraint',
                line=dict(color='green', width=2)
            ))
            
            # Optimal point
            fig.add_trace(go.Scatter(
                x=[optimal_phones], y=[optimal_tablets],
                mode='markers',
                name=f'Optimal Solution',
                marker=dict(color='gold', size=20, symbol='star',
                           line=dict(color='black', width=2))
            ))
            
            # Profit contour lines
            for profit_level in [max_profit * 0.5, max_profit * 0.75, max_profit]:
                iso_profit_y = (profit_level - 8000 * x1_range) / 12000
                fig.add_trace(go.Scatter(
                    x=x1_range, y=iso_profit_y,
                    mode='lines',
                    name=f'Profit ₹{profit_level:,.0f}',
                    line=dict(color='orange', width=1, dash='dash'),
                    showlegend=False
                ))
            
            fig.update_layout(
                title="Optimal Production Plan",
                xaxis_title="Phones (x₁)",
                yaxis_title="Tablets (x₂)",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            **Solution Insights:**
            🌟 **Gold star** = Optimal production point
            📈 **Dashed lines** = Equal profit curves
            ✅ **Optimal point** lies where highest profit line touches feasible region
            """)
    
    # Section 6: Integer Programming
    st.markdown("---")
    st.header("6️⃣ Integer Programming: The Reality Check")
    
    st.markdown("""
    **Anand's Reality Check:** *"Wait! The optimal solution says make 156.7 phones and 89.3 tablets. 
    But I can't make 0.7 of a phone! I need WHOLE units only!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔢 Why Integer Programming?")
        st.markdown("""
        **The Problem with LP:**
        - LP gives exact mathematical solution
        - But often suggests fractional units
        - **Real world:** Can't make 2.5 phones!
        
        **Business Examples Needing Integers:**
        - Number of employees to hire
        - Number of machines to buy
        - Number of projects to select
        - Number of facilities to open
        
        **Solution:** Integer Programming (IP)
        - Same as LP but forces whole number solutions
        - Slightly lower profit but practically implementable
        """)
        
        # Compare LP vs IP solutions
        if 'optimal_phones' in locals() and result.success:
            # Integer solution (simple rounding for demo)
            int_phones = round(optimal_phones)
            int_tablets = round(optimal_tablets)
            
            # Check if rounded solution is feasible
            labor_used = phone_time * int_phones + tablet_time * int_tablets
            material_used = phone_material * int_phones + tablet_material * int_tablets
            storage_used = phone_space * int_phones + tablet_space * int_tablets
            
            if (labor_used <= workers * worker_hours and 
                material_used <= material_budget * 100000 and 
                storage_used <= storage_space):
                int_profit = 8000 * int_phones + 12000 * int_tablets
                profit_loss = max_profit - int_profit
                
                st.code(f"""
LP vs INTEGER PROGRAMMING COMPARISON:

LP Solution (Fractional):
📱 Phones: {optimal_phones:.1f} units
📟 Tablets: {optimal_tablets:.1f} units
💰 Profit: ₹{max_profit:,.0f}

IP Solution (Whole Units):
📱 Phones: {int_phones} units
📟 Tablets: {int_tablets} units  
💰 Profit: ₹{int_profit:,.0f}

Profit Loss: ₹{profit_loss:,.0f} ({profit_loss/max_profit*100:.1f}%)
But solution is IMPLEMENTABLE! ✅
                """)
            else:
                st.warning("Simple rounding doesn't work - need sophisticated IP algorithms!")
    
    with col2:
        st.subheader("📊 Integer vs Continuous Solutions")
        
        if 'optimal_phones' in locals() and result.success:
            # Create comparison chart
            categories = ['LP Solution\n(Fractional)', 'IP Solution\n(Integer)']
            profits = [max_profit, int_profit if 'int_profit' in locals() else max_profit * 0.95]
            colors = ['lightblue', 'darkblue']
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=categories, y=profits,
                marker_color=colors,
                text=[f'₹{p:,.0f}' for p in profits],
                textposition='auto'
            ))
            
            fig.update_layout(
                title="Profit Comparison: LP vs IP",
                yaxis_title="Daily Profit (₹)",
                height=350
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("""
            **Integer Programming Trade-off:**
            📉 **Slightly lower profit** (mathematical cost of integer requirement)
            ✅ **Practical implementation** (can actually produce these quantities)
            🎯 **Real-world applicability** (feasible business solution)
            """)
        
        st.markdown("""
        **When to Use Integer Programming:**
        - **Binary decisions:** Yes/No, On/Off, Select/Reject
        - **Discrete quantities:** Whole units, people, machines
        - **Project selection:** Can't do half a project
        - **Facility location:** Either build or don't build
        """)
    
    # Section 7: Dual Problem and Shadow Prices
    st.markdown("---")
    st.header("7️⃣ Dual Problem: What's My Bottleneck Worth?")
    
    st.markdown("""
    **Anand's Strategic Question:** *"I found the optimal solution, but now I want to know: 
    What's the value of getting one more worker? One more hour? One more rupee of budget?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🔄 Understanding the Dual Problem")
        st.markdown("""
        **What is the Dual?**
        For every LP problem (called "Primal"), there's a corresponding "Dual" problem
        
        **Primal Question:** 
        "What's the maximum profit I can make?"
        
        **Dual Question:** 
        "What's the minimum value of my resources that justifies this profit?"
        
        **Shadow Prices = Resource Values**
        How much would profit increase if I had:
        - One more worker hour?
        - One more rupee of material budget?
        - One more sq ft of storage?
        """)
        
        # Calculate shadow prices from the LP solution
        if 'result' in locals() and result.success and hasattr(result, 'slack'):
            # Extract shadow prices (dual values)
            try:
                # Shadow prices are the negative of dual values in minimization
                shadow_prices = []
                
                # Check which constraints are binding (active)
                tolerance = 1e-6
                
                labor_used = phone_time * optimal_phones + tablet_time * optimal_tablets
                material_used = phone_material * optimal_phones + tablet_material * optimal_tablets
                storage_used = phone_space * optimal_phones + tablet_space * optimal_tablets
                
                labor_slack = workers * worker_hours - labor_used
                material_slack = material_budget * 100000 - material_used
                storage_slack = storage_space - storage_used
                
                st.code(f"""
RESOURCE UTILIZATION ANALYSIS:

Labor Constraint:
Used: {labor_used:.1f} / {workers * worker_hours} hours
Slack: {labor_slack:.1f} hours
Status: {"BINDING (Fully Used)" if labor_slack < tolerance else "Not Binding"}

Material Constraint:
Used: ₹{material_used:,.0f} / ₹{material_budget * 100000:,}
Slack: ₹{material_slack:,.0f}
Status: {"BINDING (Fully Used)" if material_slack < tolerance else "Not Binding"}

Storage Constraint:
Used: {storage_used:.1f} / {storage_space} sq ft
Slack: {storage_slack:.1f} sq ft
Status: {"BINDING (Fully Used)" if storage_slack < tolerance else "Not Binding"}
                """)
                
                st.success("""
                **Shadow Price Insight:**
                Resources with zero slack (fully used) have positive shadow prices.
                Resources with slack (unused) have zero shadow prices.
                """)
                
            except Exception as e:
                st.info("Shadow prices calculation requires advanced optimization libraries.")
    
    with col2:
        st.subheader("💰 Shadow Price Business Applications")
        
        st.markdown("""
        **What Shadow Prices Tell Anand:**
        
        **High Shadow Price Resource:**
        - This is the bottleneck!
        - Getting more of this resource increases profit significantly
        - Should focus expansion efforts here
        
        **Zero Shadow Price Resource:**
        - Already have enough of this resource
        - Getting more won't increase profit
        - Don't invest in expanding this
        
        **Business Decisions Using Shadow Prices:**
        """)
        
        # Example shadow price analysis
        example_shadow = pd.DataFrame({
            'Resource': ['Labor Hours', 'Material Budget', 'Storage Space'],
            'Shadow Price (₹)': ['₹450/hour', '₹0.8/rupee', '₹0/sq ft'],
            'Business Meaning': [
                'Each extra hour increases profit by ₹450',
                'Each extra rupee budget increases profit by ₹0.80',
                'Extra storage space has no value (excess available)'
            ],
            'Action': [
                '🎯 Hire more workers or overtime',
                '💰 Negotiate better material prices',
                '❌ Don\'t expand storage yet'
            ]
        })
        
        st.dataframe(example_shadow, use_container_width=True)
        
        st.info("""
        **Shadow Price Strategy:**
        1. **Identify bottlenecks** (high shadow prices)
        2. **Invest in bottleneck resources** first
        3. **Ignore non-binding constraints** for now
        4. **Re-solve after changes** (shadow prices change!)
        """)
    
    # Section 8: Sensitivity Analysis
    st.markdown("---")
    st.header("8️⃣ Sensitivity Analysis: What-If Planning")
    
    st.markdown("""
    **Anand's Strategic Planning:** *"I have the optimal solution for today, but business conditions change. 
    What happens if material costs increase? If I hire more workers? How sensitive is my optimal plan to changes?"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Interactive Sensitivity Analysis")
        st.markdown("""
        **What-If Scenarios:**
        Change key parameters and see how the optimal solution shifts.
        """)
        
        # Sensitivity analysis controls
        st.markdown("**🎛️ Change Parameters:**")
        
        material_change = st.slider("Material Cost Change (%)", -30, 30, 0, 5)
        worker_change = st.slider("Number of Workers Change", -10, 20, 0, 1)
        profit_phone_change = st.slider("Phone Profit Change (%)", -20, 20, 0, 5)
        profit_tablet_change = st.slider("Tablet Profit Change (%)", -20, 20, 0, 5)
        
        # Recalculate with changes
        new_phone_material = phone_material * (1 + material_change/100)
        new_tablet_material = tablet_material * (1 + material_change/100)
        new_workers = workers + worker_change
        new_phone_profit = 8000 * (1 + profit_phone_change/100)
        new_tablet_profit = 12000 * (1 + profit_tablet_change/100)
        
        # Solve with new parameters
        try:
            c_new = [-new_phone_profit, -new_tablet_profit]
            A_new = [
                [phone_time, tablet_time],
                [new_phone_material, new_tablet_material],
                [phone_space, tablet_space]
            ]
            b_new = [
                new_workers * worker_hours,
                material_budget * 100000,
                storage_space
            ]
            
            result_new = linprog(c_new, A_ub=A_new, b_ub=b_new, bounds=[x1_bounds, x2_bounds], method='highs')
            
            if result_new.success:
                new_optimal_phones = result_new.x[0]
                new_optimal_tablets = result_new.x[1]
                new_max_profit = -result_new.fun
                
                # Compare solutions
                phone_change_abs = new_optimal_phones - optimal_phones
                tablet_change_abs = new_optimal_tablets - optimal_tablets
                profit_change_abs = new_max_profit - max_profit
                
                st.code(f"""
SENSITIVITY ANALYSIS RESULTS:

Original Solution:
📱 Phones: {optimal_phones:.1f} → {new_optimal_phones:.1f} ({phone_change_abs:+.1f})
📟 Tablets: {optimal_tablets:.1f} → {new_optimal_tablets:.1f} ({tablet_change_abs:+.1f})
💰 Profit: ₹{max_profit:,.0f} → ₹{new_max_profit:,.0f} ({profit_change_abs:+,.0f})

Parameter Changes:
Material Cost: {material_change:+}%
Workers: {worker_change:+} people
Phone Profit: {profit_phone_change:+}%
Tablet Profit: {profit_tablet_change:+}%
                """)
                
                if abs(profit_change_abs) > 1000:
                    if profit_change_abs > 0:
                        st.success(f"✅ Profit increased by ₹{profit_change_abs:,.0f}!")
                    else:
                        st.warning(f"⚠️ Profit decreased by ₹{abs(profit_change_abs):,.0f}")
                else:
                    st.info("📊 Minimal impact on optimal solution")
        
        except Exception as e:
            st.error("Could not solve with new parameters")
    
    with col2:
        st.subheader("📈 Sensitivity Visualization")
        
        if 'new_max_profit' in locals():
            # Create sensitivity comparison chart
            scenarios = ['Original', 'Modified']
            profits = [max_profit, new_max_profit]
            colors = ['lightgreen', 'darkgreen' if new_max_profit > max_profit else 'orange']
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=scenarios, y=profits,
                marker_color=colors,
                text=[f'₹{p:,.0f}' for p in profits],
                textposition='auto'
            ))
            
            fig.update_layout(
                title="Sensitivity Analysis: Profit Impact",
                yaxis_title="Daily Profit (₹)",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Sensitivity Analysis Benefits:**
        
        **🎯 Risk Management:**
        - Understand impact of parameter changes
        - Prepare for market fluctuations
        - Identify critical variables
        
        **📊 Strategic Planning:**
        - Test "what-if" scenarios
        - Evaluate investment options
        - Make robust decisions
        
        **⚡ Quick Responses:**
        - Rapid re-optimization
        - Adapt to changing conditions
        - Maintain competitiveness
        """)
        
        st.info("""
        **Key Insight:**
        Solutions that are highly sensitive to small changes might be risky.
        Robust solutions maintain good performance across scenarios.
        """)
    
    # Section 9: Portfolio Application Example
    st.markdown("---")
    st.header("9️⃣ Portfolio Optimization: Beyond Manufacturing")
    
    st.markdown("""
    **Anand's Expanded Learning:** *"Now I understand optimization for production. 
    But these same principles apply to investment portfolios too!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💼 Portfolio Optimization Problem")
        st.markdown("""
        **Scenario:** Company has ₹1 crore surplus funds to invest
        
        **Investment Options:**
        - **Equity:** 12% expected return, High risk
        - **Bonds:** 7% expected return, Low risk
        - **Fixed Deposits:** 5% expected return, No risk
        
        **Constraints:**
        - Maximum 60% in equity (risk management)
        - Minimum 20% in bonds (stability)
        - Minimum 10% in FDs (liquidity)
        - Total investment = 100% (fully invested)
        
        **Objective:** Maximize expected return
        """)
        
        # Portfolio optimization setup
        portfolio_amount = 10000000  # ₹1 crore
        
        equity_return = st.slider("Equity Return (%)", 8, 20, 12, 1)
        bond_return = st.slider("Bond Return (%)", 4, 12, 7, 1)
        fd_return = st.slider("FD Return (%)", 3, 8, 5, 1)
        
        max_equity = st.slider("Max Equity (%)", 40, 80, 60, 5)
        min_bonds = st.slider("Min Bonds (%)", 10, 40, 20, 5)
        min_fd = st.slider("Min FD (%)", 5, 30, 10, 5)
        
        st.code(f"""
PORTFOLIO OPTIMIZATION FORMULATION:

Variables:
x₁ = Proportion in Equity (0 to 1)
x₂ = Proportion in Bonds (0 to 1)
x₃ = Proportion in FDs (0 to 1)

Objective (Maximize):
Return = {equity_return}%×x₁ + {bond_return}%×x₂ + {fd_return}%×x₃

Constraints:
x₁ + x₂ + x₃ = 1 (Fully invested)
x₁ ≤ {max_equity/100} (Max equity)
x₂ ≥ {min_bonds/100} (Min bonds)
x₃ ≥ {min_fd/100} (Min FD)
x₁, x₂, x₃ ≥ 0 (Non-negative)
        """)
    
    with col2:
        st.subheader("📊 Optimal Portfolio Solution")
        
        # Solve portfolio optimization
        try:
            # Objective coefficients (negative for maximization)
            c_portfolio = [-equity_return/100, -bond_return/100, -fd_return/100]
            
            # Equality constraint: x1 + x2 + x3 = 1
            A_eq = [[1, 1, 1]]
            b_eq = [1]
            
            # Inequality constraints
            A_ub = [
                [1, 0, 0],  # x1 <= max_equity
                [-1, 0, 0],  # -x1 <= 0 (x1 >= 0)
                [0, -1, 0],  # -x2 <= -min_bonds (x2 >= min_bonds)
                [0, 0, -1]   # -x3 <= -min_fd (x3 >= min_fd)
            ]
            b_ub = [max_equity/100, 0, -min_bonds/100, -min_fd/100]
            
            # Bounds
            bounds = [(0, 1), (0, 1), (0, 1)]
            
            result_portfolio = linprog(c_portfolio, A_ub=A_ub, b_ub=b_ub, 
                                     A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
            
            if result_portfolio.success:
                opt_equity = result_portfolio.x[0]
                opt_bonds = result_portfolio.x[1]
                opt_fd = result_portfolio.x[2]
                portfolio_return = -result_portfolio.fun * 100
                
                # Create portfolio pie chart
                fig = go.Figure(data=[go.Pie(
                    labels=['Equity', 'Bonds', 'Fixed Deposits'],
                    values=[opt_equity*100, opt_bonds*100, opt_fd*100],
                    hole=.3,
                    marker_colors=['red', 'blue', 'green']
                )])
                
                fig.update_layout(
                    title="Optimal Portfolio Allocation",
                    height=350
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                st.code(f"""
OPTIMAL PORTFOLIO:

Allocation:
🔴 Equity: {opt_equity*100:.1f}% (₹{opt_equity*portfolio_amount:,.0f})
🔵 Bonds: {opt_bonds*100:.1f}% (₹{opt_bonds*portfolio_amount:,.0f})
🟢 FDs: {opt_fd*100:.1f}% (₹{opt_fd*portfolio_amount:,.0f})

Expected Annual Return: {portfolio_return:.2f}%
Expected Annual Income: ₹{portfolio_return/100*portfolio_amount:,.0f}
                """)
                
                st.success(f"✅ Optimal portfolio return: {portfolio_return:.2f}% annually")
        
        except Exception as e:
            st.error(f"Portfolio optimization error: {str(e)}")
    
    # Key Takeaways and Summary
    st.markdown("---")
    st.header("🎓 Anand's Optimization Mastery Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Core Concepts Mastered**
        
        ✅ **Optimization Basics**
        - Finding best from all choices
        - Mathematical certainty vs guesswork
        
        ✅ **Linear Programming**
        - Systematic approach to complex decisions
        - Handles multiple variables & constraints
        
        ✅ **Constraints Understanding**
        - Real business limitations
        - Feasible region concept
        """)
    
    with col2:
        st.markdown("""
        **🔢 Advanced Techniques**
        
        ✅ **Integer Programming**
        - Whole unit requirements
        - Practical implementability
        
        ✅ **Dual Problem Analysis**
        - Resource shadow prices
        - Bottleneck identification
        
        ✅ **Sensitivity Analysis**
        - What-if scenario planning
        - Risk management
        """)
    
    with col3:
        st.markdown("""
        **💼 Business Applications**
        
        ✅ **Production Planning**
        - Optimal product mix
        - Resource allocation
        
        ✅ **Investment Decisions**
        - Portfolio optimization
        - Capital budgeting
        
        ✅ **Strategic Planning**
        - Data-driven decisions
        - Competitive advantage
        """)
    
    # Final Success Message
    st.success("""
    🎉 **Anand's Complete Optimization Transformation!**
    
    **From:** Overwhelming choices and guesswork decisions
    **To:** Mathematical certainty and optimal resource allocation
    
    **Optimization Superpowers Unlocked:**
    ✅ **Systematic Decision Making** - No more guesswork, mathematical certainty
    ✅ **Resource Optimization** - Maximum output from limited inputs  
    ✅ **Constraint Management** - Turn limitations into strategic advantages
    ✅ **Sensitivity Planning** - Robust decisions that handle uncertainty
    ✅ **Multi-domain Application** - From production to portfolios to strategic planning
    
    **The Power of Optimization:** Anand can now tackle any resource allocation challenge
    with mathematical confidence, ensuring his company always makes the most profitable
    and efficient decisions possible!
    """)
    
    st.markdown("---")