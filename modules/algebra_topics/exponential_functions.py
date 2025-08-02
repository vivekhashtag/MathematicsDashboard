import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import log

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #8B4513;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .business-insight {
        background-color: #f0f8e8;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    .equation-box {
        background-color: #fff8e1;
        padding: 1rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border: 1px solid #ffc107;
        margin: 1rem 0;
    }
    .discovery-highlight {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
    .exponential-highlight {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_exponential_functions():
    # Header with back navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("🌱 Exponential Functions")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra** > **Exponential Functions**")
    
    # Main Title
    st.markdown('<h1 class="main-header">🚀 Maya\'s Customer Growth Mystery - Exponential Functions</h1>', unsafe_allow_html=True)
    
    # Business Storyline
    st.header("📖 Maya's Amazing Discovery")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Maya's tea stall is thriving!** After finding her optimal price of ₹15, something incredible starts happening. 
        Her customer base begins growing through **word-of-mouth**, and the pattern she discovers amazes her.
        
        **"This is weird!"** Maya notices. **"I'm not doing any advertising, but every month I'm getting 
        way more new customers than the month before. It's like the growth is growing!"**
        
        Let's help Maya understand the mathematics behind **exponential growth**!
        """)
    
    with col2:
        st.info("""
        **What is Exponential Growth?**
        
        Unlike linear growth (adding the same amount each time), 
        exponential growth means growing by the same **percentage** each time.
        
        This creates acceleration!
        """)
    
    # Maya's Original Data
    st.header("📊 Maya's 6-Month Customer Journey")
    
    maya_original_data = {
        'Month': [1, 2, 3, 4, 5, 6],
        'Regular Customers': [50, 75, 112, 168, 252, 378],
        'Growth from Previous': ['-', '+25 (50%)', '+37 (50%)', '+56 (50%)', '+84 (50%)', '+126 (50%)'],
        'Maya\'s Observation': [
            "Starting small",
            "Some people tried and liked it", 
            "More people talking about it",
            "Wow! Growth is speeding up",
            "This is getting crazy fast!",
            "I can barely handle this!"
        ]
    }
    
    df_maya = pd.DataFrame(maya_original_data)
    st.dataframe(df_maya, use_container_width=True)
    
    # Maya's Discovery
    st.markdown('<div class="discovery-highlight">', unsafe_allow_html=True)
    st.subheader("💡 Maya's Big Discovery")
    st.markdown("""
    **"I see the pattern now! Every month, my customers grow by 50%. It's not growing by the same NUMBER, 
    it's growing by the same PERCENTAGE!"**
    
    - Month 1: 50 customers
    - Month 2: 50 + (50% of 50) = 50 + 25 = 75 customers  
    - Month 3: 75 + (50% of 75) = 75 + 37.5 ≈ 112 customers
    
    **This creates an exponential pattern because each month's growth builds on the previous total!**
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Exponential Function Explorer
    st.header("🎛️ Interactive Customer Growth Simulator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        initial_customers = st.slider("Starting Customers", 20, 100, 50, 5,
                                     help="Maya's initial customer base")
    
    with col2:
        growth_rate = st.slider("Monthly Growth Rate (%)", 10, 100, 50, 5,
                               help="Percentage growth each month through word-of-mouth")
    
    with col3:
        months_to_show = st.slider("Months to Predict", 6, 24, 12, 1,
                                  help="How far into the future to project")
    
    # Calculate exponential growth
    growth_multiplier = 1 + (growth_rate / 100)
    months = np.arange(1, months_to_show + 1)
    customers = initial_customers * (growth_multiplier ** (months - 1))
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Exponential Growth Curve
    ax1.plot(months, customers, 'b-', linewidth=3, label=f'Customers = {initial_customers} × {growth_multiplier:.2f}^(Month-1)')
    ax1.scatter(months[:6], customers[:6], color='red', s=100, zorder=5, label='First 6 Months')
    
    # Highlight key points
    month_6_customers = initial_customers * (growth_multiplier ** 5)
    month_12_customers = initial_customers * (growth_multiplier ** 11)
    
    ax1.plot(6, month_6_customers, 'go', markersize=12, label=f'Month 6: {month_6_customers:.0f} customers')
    if months_to_show >= 12:
        ax1.plot(12, month_12_customers, 'ro', markersize=12, label=f'Month 12: {month_12_customers:.0f} customers')
    
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Regular Customers')
    ax1.set_title('Maya\'s Customer Growth: The Exponential Curve')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Linear vs Exponential Comparison
    linear_growth = initial_customers + (months - 1) * (growth_rate * initial_customers / 100)
    
    ax2.plot(months, customers, 'b-', linewidth=3, label=f'Exponential ({growth_rate}% monthly)')
    ax2.plot(months, linear_growth, 'r--', linewidth=3, label=f'Linear (+{growth_rate * initial_customers / 100:.0f} customers/month)')
    
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Customers')
    ax2.set_title('Why Exponential Growth is Powerful')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Add annotation showing the difference
    if months_to_show >= 8:
        month_8_exp = initial_customers * (growth_multiplier ** 7)
        month_8_lin = initial_customers + 7 * (growth_rate * initial_customers / 100)
        difference = month_8_exp - month_8_lin
        ax2.annotate(f'Month 8 difference:\n{difference:.0f} customers!', 
                    xy=(8, month_8_exp), xytext=(10, month_8_exp * 0.7),
                    arrowprops=dict(arrowstyle='->', color='green'),
                    fontsize=10, ha='center')
    
    # Plot 3: Monthly Growth Analysis
    monthly_growth = np.diff(customers)
    monthly_growth = np.insert(monthly_growth, 0, 0)  # Add 0 for month 1
    
    ax3.bar(months, monthly_growth, alpha=0.7, color='orange', label='New Customers Each Month')
    ax3.set_xlabel('Month')
    ax3.set_ylabel('New Customers Added')
    ax3.set_title('Accelerating Monthly Growth')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Doubling Time Analysis
    # Calculate when customer base doubles, triples, etc.
    multiples = [2, 3, 4, 5]
    doubling_times = []
    
    for multiple in multiples:
        target = initial_customers * multiple
        # Solve: target = initial_customers * (growth_multiplier)^(t-1)
        # t = log(target/initial_customers) / log(growth_multiplier) + 1
        if growth_multiplier > 1:
            time_to_reach = log(multiple) / log(growth_multiplier) + 1
            doubling_times.append(time_to_reach)
        else:
            doubling_times.append(float('inf'))
    
    ax4.bar(range(len(multiples)), doubling_times, color=['green', 'blue', 'orange', 'red'])
    ax4.set_xlabel('Multiple of Initial Customers')
    ax4.set_ylabel('Months to Reach')
    ax4.set_title('Time to Reach Customer Milestones')
    ax4.set_xticks(range(len(multiples)))
    ax4.set_xticklabels([f'{m}x\n({initial_customers * m:.0f})' for m in multiples])
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Mathematical Representation
    st.header("🧮 Maya's Exponential Equation")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Exponential Growth Formula:**
    
    **Customers = {initial_customers} × ({growth_multiplier:.2f})^(Month-1)**
    
    **Breaking it down:**
    - **{initial_customers}**: Maya's starting customer base (Month 1)
    - **{growth_multiplier:.2f}**: Growth multiplier ({growth_rate}% growth = multiply by {growth_multiplier:.2f})
    - **(Month-1)**: The exponent - how many times growth compounds
    - **Month**: The time period we're calculating for
    
    **Why Month-1?** Because in Month 1, there's been zero growth periods yet!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Dashboard
    st.header("📊 Maya's Growth Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Growth Rate", f"{growth_rate}%", "per month")
    
    with col2:
        month_6_value = initial_customers * (growth_multiplier ** 5)
        st.metric("Month 6 Customers", f"{month_6_value:.0f}", 
                 f"{((month_6_value/initial_customers - 1) * 100):.0f}% total growth")
    
    with col3:
        if months_to_show >= 12:
            month_12_value = initial_customers * (growth_multiplier ** 11)
            st.metric("Month 12 Customers", f"{month_12_value:.0f}")
        else:
            st.metric("Projected Growth", "Exponential", "📈")
    
    with col4:
        if growth_multiplier > 1:
            doubling_time = log(2) / log(growth_multiplier) + 1
            st.metric("Doubling Time", f"{doubling_time:.1f} months")
        else:
            st.metric("Doubling Time", "Never", "📉")
    
    # Pattern Analysis Table
    st.header("🔍 Maya's Growth Pattern Analysis")
    
    st.markdown('<div class="exponential-highlight">', unsafe_allow_html=True)
    st.subheader("Understanding the Acceleration")
    
    # Create detailed analysis table
    analysis_months = months[:min(8, len(months))]
    analysis_data = []
    
    for i, month in enumerate(analysis_months):
        customers_val = initial_customers * (growth_multiplier ** (month - 1))
        if i == 0:
            new_customers = 0
            growth_factor = 1.0
        else:
            prev_customers = initial_customers * (growth_multiplier ** (month - 2))
            new_customers = customers_val - prev_customers
            growth_factor = customers_val / initial_customers
        
        analysis_data.append({
            'Month': int(month),
            'Total Customers': f'{customers_val:.0f}',
            'New This Month': f'{new_customers:.0f}' if new_customers > 0 else '-',
            'Growth Factor': f'{growth_factor:.1f}x',
            'Status': '🚀 Exponential' if month > 3 else '📈 Building'
        })
    
    df_analysis = pd.DataFrame(analysis_data)
    st.dataframe(df_analysis, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Business Calculator
    st.header("🤔 Maya's Growth Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Future Predictor")
        target_month = st.number_input("Predict customers for month:", 
                                      min_value=1, max_value=36, value=8, step=1)
        
        predicted_customers = initial_customers * (growth_multiplier ** (target_month - 1))
        
        st.success(f"📈 Month {target_month}: {predicted_customers:.0f} customers")
        
        # Show the calculation
        st.info(f"Calculation: {initial_customers} × {growth_multiplier:.2f}^{target_month-1} = {predicted_customers:.0f}")
        
        # Compare to linear growth
        linear_equivalent = initial_customers + (target_month - 1) * (growth_rate * initial_customers / 100)
        difference = predicted_customers - linear_equivalent
        
        if difference > 0:
            st.warning(f"📊 {difference:.0f} more customers than linear growth!")
    
    with col2:
        st.subheader("🔍 Target Finder")
        target_customers = st.number_input("When will Maya reach:", 
                                          min_value=initial_customers, max_value=10000, 
                                          value=500, step=50)
        
        if target_customers > initial_customers and growth_multiplier > 1:
            # Solve: target = initial * (multiplier)^(month-1)
            # month = log(target/initial) / log(multiplier) + 1
            months_needed = log(target_customers / initial_customers) / log(growth_multiplier) + 1
            
            st.info(f"🗓️ Maya will reach {target_customers} customers in **{months_needed:.1f} months**")
            
            # Show what this means in practical terms
            years = months_needed / 12
            if years < 1:
                st.write(f"That's about **{months_needed:.0f} months** from now")
            else:
                st.write(f"That's about **{years:.1f} years** from now")
        else:
            st.error("Target too low or negative growth!")
    
    # Business Insights
    st.header("💡 Exponential Growth Insights")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Why It's Exponential")
        st.write("**Word-of-mouth creates compound effects:**")
        st.write("• 1 happy customer tells 2 friends")
        st.write("• Now 3 customers each tell 2 friends")  
        st.write("• Now 9 customers each tell 2 friends")
        st.write("• The spreading accelerates!")
        
        st.subheader("📈 The Power of Percentage Growth")
        st.write(f"**{growth_rate}% monthly sounds small, but:**")
        if growth_multiplier > 1:
            year_multiplier = growth_multiplier ** 12
            st.write(f"• In 1 year: {year_multiplier:.1f}x growth")
            st.write(f"• {initial_customers} becomes {initial_customers * year_multiplier:.0f} customers!")
        st.write("• Small percentages + time = massive results")
    
    with col2:
        st.subheader("🏢 Business Applications")
        st.write("**Exponential patterns appear in:**")
        st.write("• **Viral marketing** - posts spread exponentially")
        st.write("• **Compound interest** - money grows on money")
        st.write("• **Network effects** - more users attract more users")
        st.write("• **Disease spread** - each person infects multiple others")
        
        st.subheader("🚨 Maya's Planning Insights")
        st.write("**Maya can now predict:**")
        st.write("• When she'll need more staff")
        st.write("• When she'll need a bigger location")
        st.write("• How much tea to order months ahead")
        st.write("• When to plan her second stall")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Growth Story")
    
    with st.expander("📝 Exercise 1: Maya's Competition Analysis"):
        st.markdown(f"""
        Maya's competitor starts with 100 customers but only grows at 20% per month.
        Maya starts with {initial_customers} customers and grows at {growth_rate}% per month.
        
        **Questions:**
        1. Who has more customers after 6 months?
        2. When (if ever) does Maya overtake her competitor?
        3. What's the difference after 12 months?
        """)
        
        if st.button("Show Solutions", key="ex1_exp"):
            # Competitor calculations
            comp_initial = 100
            comp_growth = 1.20
            
            maya_6_months = initial_customers * (growth_multiplier ** 5)
            comp_6_months = comp_initial * (comp_growth ** 5)
            
            maya_12_months = initial_customers * (growth_multiplier ** 11) 
            comp_12_months = comp_initial * (comp_growth ** 11)
            
            # Find when Maya overtakes (if she does)
            overtake_month = None
            if growth_multiplier > comp_growth:
                # Solve: initial_customers * growth_multiplier^(t-1) = 100 * 1.2^(t-1)
                # This requires numerical solving, but we can approximate
                for month in range(1, 25):
                    maya_val = initial_customers * (growth_multiplier ** (month - 1))
                    comp_val = comp_initial * (comp_growth ** (month - 1))
                    if maya_val > comp_val and overtake_month is None:
                        overtake_month = month
                        break
            
            st.markdown(f"""
            **Solutions:**
            
            1. **After 6 months:**
               - Maya: {maya_6_months:.0f} customers
               - Competitor: {comp_6_months:.0f} customers
               - **Winner: {"Maya" if maya_6_months > comp_6_months else "Competitor"}**
            
            2. **When Maya overtakes:**
               - {"Maya overtakes in Month " + str(overtake_month) if overtake_month else "Maya never overtakes with current growth rates"}
            
            3. **After 12 months:**
               - Maya: {maya_12_months:.0f} customers  
               - Competitor: {comp_12_months:.0f} customers
               - **Difference: {abs(maya_12_months - comp_12_months):.0f} customers**
            
            **Business insight:** Higher growth rates compound dramatically over time!
            """)
    
    with st.expander("📝 Exercise 2: Maya's Growth Rate Experiment"):
        st.markdown(f"""
        Maya wonders: "What if I could improve my word-of-mouth growth rate?"
        
        Current: {growth_rate}% monthly growth
        Scenarios: 30%, 40%, 60%, 70% monthly growth
        
        **Questions:**
        1. How many customers would each scenario give after 8 months?
        2. Which growth rate doubles her customer base fastest?
        3. What's the practical difference between 60% and 70% growth?
        """)
        
        if st.button("Show Solutions", key="ex2_exp"):
            scenarios = [30, 40, 50, 60, 70]
            results_8_months = []
            doubling_times = []
            
            for rate in scenarios:
                multiplier = 1 + (rate / 100)
                customers_8 = initial_customers * (multiplier ** 7)
                results_8_months.append(customers_8)
                
                doubling_time = log(2) / log(multiplier) + 1
                doubling_times.append(doubling_time)
            
            # Calculate difference between 60% and 70%
            growth_60 = initial_customers * (1.60 ** 7)
            growth_70 = initial_customers * (1.70 ** 7)
            difference_60_70 = growth_70 - growth_60
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Customers after 8 months:**""")
            
            for i, rate in enumerate(scenarios):
                st.write(f"   - {rate}% growth: {results_8_months[i]:.0f} customers")
            
            st.markdown(f"""
            2. **Doubling times:**""")
            
            for i, rate in enumerate(scenarios):
                st.write(f"   - {rate}% growth: {doubling_times[i]:.1f} months to double")
            
            st.markdown(f"""
            3. **60% vs 70% difference after 8 months:**
               - 60% growth: {growth_60:.0f} customers
               - 70% growth: {growth_70:.0f} customers  
               - **Difference: {difference_60_70:.0f} customers**
            
            **Business insight:** Small improvements in growth rate create massive long-term differences!
            """)
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Exponential Functions in Maya's Business:**
    
    1. **Compound Effect:** Growth builds on previous growth - accelerating results
    2. **Percentage vs Absolute:** Same percentage growth creates larger absolute numbers over time
    3. **Time is Powerful:** Small growth rates become massive with enough time
    4. **Prediction Power:** Maya can forecast any future month with her equation
    5. **Planning Tool:** Understanding exponential growth helps prepare for rapid scaling
    6. **Network Effects:** Word-of-mouth naturally creates exponential patterns
    
    **Maya's Transformation:** From wondering "why is this happening?" to "I can predict exactly what will happen!"
    
    **The Magic:** Exponential functions help you see the future of any growing business!
    """)
    
    # Navigation
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("← Quadratic Functions"):
            st.session_state.page = 'algebra_quadratic'
            st.rerun()
    
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with nav_col3:
        if st.button("Logarithmic Functions →"):
            st.session_state.page = 'algebra_logarithmic'
            st.rerun()