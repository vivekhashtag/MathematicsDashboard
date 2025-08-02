import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
    .break-even-highlight {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_linear_functions():
   
    # ADD THIS HEADER SECTION:
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("📈 Linear Functions & Equations")
    
    # ADD THIS BREADCRUMB:
    st.markdown("**Home** > **Algebra** > **Linear Functions**")
   
    # Main Title
    st.markdown('<h1 class="main-header">☕ Maya\'s Tea Stall - Linear Functions</h1>', unsafe_allow_html=True)


    
    # Business Storyline
    st.header("📖 The Complete Business Story")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Meet Maya!** She runs a small tea stall near Mumbai railway station. 
        Every morning, Maya serves fresh, hot tea to commuters rushing to catch their trains.
        
        Like every business owner, Maya needs to understand:
        - How much does it cost to run her business?
        - How much money does she make from sales?
        - When does she start making profit?
        
        Let's help Maya understand her business through **Linear Functions**!
        """)
    
    with col2:
        st.info("""
        **What is a Linear Function?**
        
        A straight-line relationship between two variables. 
        In Maya's case: as tea sales increase, 
        costs and revenue change at constant rates.
        """)
    
    # Interactive Business Parameters
    st.header("🎛️ Maya's Business Parameters")
    st.markdown("Adjust the sliders to see how changes affect Maya's business:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fixed_costs = st.slider("Monthly Fixed Costs (₹)", 30000, 80000, 50000, 5000, 
                               help="Rent, gas connection, permits, basic setup")
    
    with col2:
        variable_cost = st.slider("Cost per Cup (₹)", 5, 15, 8, 1,
                                 help="Tea leaves, milk, sugar, disposable cup")
    
    with col3:
        selling_price = st.slider("Selling Price per Cup (₹)", 10, 25, 15, 1,
                                 help="What Maya charges customers")
    
    # Calculate key business metrics
    profit_per_cup = selling_price - variable_cost
    
    # Break-even calculation
    if profit_per_cup > 0:
        break_even_cups = fixed_costs / profit_per_cup
        break_even_daily = break_even_cups / 30
        break_even_hourly = break_even_daily / 12  # Assuming 12 hours operation
    else:
        break_even_cups = float('inf')
        break_even_daily = float('inf')
        break_even_hourly = float('inf')
    
    # Mathematical Representation
    st.header("🧮 The Mathematical Model")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Business Equations:**
    
    **Cost Function:** C = {fixed_costs:,} + {variable_cost}n
    - Fixed costs: ₹{fixed_costs:,} (rent, setup, permits)
    - Variable cost: ₹{variable_cost} per cup
    
    **Revenue Function:** R = {selling_price}n
    - Selling price: ₹{selling_price} per cup
    
    **Profit Function:** P = {selling_price}n - ({fixed_costs:,} + {variable_cost}n) = {profit_per_cup}n - {fixed_costs:,}
    - Profit per cup: ₹{profit_per_cup}
    
    Where **n** = Number of cups sold per month
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate data for visualization
    cups_range = np.arange(0, 15001, 500)
    total_cost = fixed_costs + variable_cost * cups_range
    total_revenue = selling_price * cups_range
    profit = total_revenue - total_cost
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Cost vs Revenue vs Profit
    ax1.plot(cups_range, total_cost, 'r-', linewidth=2, label=f'Total Cost (₹{fixed_costs:,} + ₹{variable_cost}n)')
    ax1.plot(cups_range, total_revenue, 'g-', linewidth=2, label=f'Total Revenue (₹{selling_price}n)')
    ax1.plot(cups_range, profit, 'b-', linewidth=2, label=f'Profit (₹{profit_per_cup}n - ₹{fixed_costs:,})')
    
    # Add break-even point
    if break_even_cups <= 15000:
        ax1.axvline(x=break_even_cups, color='orange', linestyle='--', linewidth=2, 
                   label=f'Break-even: {break_even_cups:.0f} cups')
        ax1.plot(break_even_cups, selling_price * break_even_cups, 'ro', markersize=8)
    
    ax1.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    ax1.set_xlabel('Cups Sold per Month')
    ax1.set_ylabel('Amount (₹)')
    ax1.set_title('Maya\'s Tea Stall: Complete Financial Overview')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.ticklabel_format(style='plain', axis='y')
    
    # Plot 2: Profit zones
    ax2.fill_between(cups_range, profit, 0, where=(profit >= 0), alpha=0.3, color='green', label='Profit Zone')
    ax2.fill_between(cups_range, profit, 0, where=(profit < 0), alpha=0.3, color='red', label='Loss Zone')
    ax2.plot(cups_range, profit, 'b-', linewidth=2, label='Profit Line')
    if break_even_cups <= 15000:
        ax2.axvline(x=break_even_cups, color='orange', linestyle='--', linewidth=2, label='Break-even')
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    ax2.set_xlabel('Cups Sold per Month')
    ax2.set_ylabel('Profit (₹)')
    ax2.set_title('Profit Analysis: When Does Maya Make Money?')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Daily breakdown
    daily_cups = cups_range / 30
    daily_profit = profit / 30
    ax3.plot(daily_cups, daily_profit, 'purple', linewidth=2)
    ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    if break_even_daily <= 500:
        ax3.axvline(x=break_even_daily, color='orange', linestyle='--', linewidth=2, 
                   label=f'Daily break-even: {break_even_daily:.0f} cups')
    ax3.set_xlabel('Cups Sold per Day')
    ax3.set_ylabel('Daily Profit (₹)')
    ax3.set_title('Daily Profit Target')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Hourly breakdown
    hourly_cups = daily_cups / 12
    ax4.plot(hourly_cups, daily_profit, 'brown', linewidth=2)
    ax4.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    if break_even_hourly <= 50:
        ax4.axvline(x=break_even_hourly, color='orange', linestyle='--', linewidth=2, 
                   label=f'Hourly break-even: {break_even_hourly:.1f} cups')
    ax4.set_xlabel('Cups Sold per Hour')
    ax4.set_ylabel('Daily Profit (₹)')
    ax4.set_title('Hourly Sales Target (12-hour operation)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Key Business Metrics
    st.header("📊 Maya's Business Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Profit per Cup", f"₹{profit_per_cup}", 
                 f"₹{profit_per_cup - 7} vs base" if profit_per_cup != 7 else None)
    
    with col2:
        if break_even_cups != float('inf'):
            st.metric("Break-even (Monthly)", f"{break_even_cups:.0f} cups")
        else:
            st.metric("Break-even", "Never", "Fix pricing!")
    
    with col3:
        if break_even_daily != float('inf'):
            st.metric("Break-even (Daily)", f"{break_even_daily:.0f} cups")
        else:
            st.metric("Break-even (Daily)", "Never")
    
    with col4:
        if break_even_hourly != float('inf'):
            st.metric("Break-even (Hourly)", f"{break_even_hourly:.1f} cups")
        else:
            st.metric("Break-even (Hourly)", "Never")
    
    # Break-even Analysis
    if break_even_cups != float('inf'):
        st.markdown('<div class="break-even-highlight">', unsafe_allow_html=True)
        st.subheader("🎯 Break-Even Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Maya's Break-Even Targets:**")
            st.write(f"• **Monthly:** {break_even_cups:.0f} cups")
            st.write(f"• **Daily:** {break_even_daily:.0f} cups (30 days)")
            st.write(f"• **Hourly:** {break_even_hourly:.1f} cups (12 hours/day)")
            
        with col2:
            st.write("**What this means:**")
            st.write(f"• Maya must sell at least {break_even_hourly:.1f} cups every hour")
            st.write(f"• Every cup beyond break-even adds ₹{profit_per_cup} profit")
            st.write(f"• If she sells less, she loses money")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Real Numbers Example Table
    st.header("📈 Real Numbers: Maya's Monthly Performance")
    
    # Create sample scenarios
    scenarios = [5000, 7000, int(break_even_cups) if break_even_cups != float('inf') else 8000, 10000, 12000]
    
    data = []
    for cups in scenarios:
        cost = fixed_costs + variable_cost * cups
        revenue = selling_price * cups
        profit_val = revenue - cost
        daily_cups = cups / 30
        
        status = "✅ Profit" if profit_val > 0 else "🔴 Loss" if profit_val < 0 else "⚖️ Break-even"
        
        data.append({
            'Cups Sold': f'{cups:,}',
            'Daily Average': f'{daily_cups:.0f}',
            'Total Cost': f'₹{cost:,}',
            'Total Revenue': f'₹{revenue:,}',
            'Profit/Loss': f'₹{profit_val:,}',
            'Status': status
        })
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    # Business Insights
    st.header("💡 Linear Function Insights for Maya")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📐 Slope Analysis")
        st.write(f"**Cost Slope ({variable_cost}):** Every additional cup increases cost by ₹{variable_cost}")
        st.write(f"**Revenue Slope ({selling_price}):** Every additional cup brings in ₹{selling_price}")
        st.write(f"**Profit Slope ({profit_per_cup}):** Every additional cup adds ₹{profit_per_cup} to profit")
        
        st.subheader("📍 Y-Intercept Insights")
        st.write(f"**Cost Y-intercept (₹{fixed_costs:,}):** Maya pays ₹{fixed_costs:,} even with zero sales")
        st.write("**Revenue Y-intercept (0):** No sales = no revenue")
        st.write(f"**Profit Y-intercept (-₹{fixed_costs:,}):** Maya starts ₹{fixed_costs:,} in the hole")
    
    with col2:
        st.subheader("🎯 Practical Business Decisions")
        
        if break_even_cups != float('inf'):
            monthly_for_30k = (30000 + fixed_costs) / profit_per_cup if profit_per_cup > 0 else float('inf')
            
            st.write("**Maya can instantly answer:**")
            st.write(f"• 'If I sell 300 cups tomorrow, my profit is ₹{300 * profit_per_cup - fixed_costs/30:.0f}'")
            if monthly_for_30k != float('inf'):
                st.write(f"• 'I need {monthly_for_30k:.0f} cups for ₹30,000 monthly profit'")
            st.write(f"• 'Each extra 1,000 cups = ₹{1000 * profit_per_cup:,} more profit'")
            
            st.subheader("🚨 Risk Assessment")
            st.write(f"• If sales drop below {break_even_cups:.0f} cups, Maya loses money")
            st.write(f"• Buffer needed: Aim for {break_even_cups * 1.2:.0f}+ cups for safety")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Business Questions
    st.header("🤔 Interactive Business Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Profit Calculator")
        target_cups = st.number_input("How many cups will Maya sell?", 
                                     min_value=0, max_value=20000, value=8000, step=100)
        
        target_profit = profit_per_cup * target_cups - fixed_costs
        target_daily = target_cups / 30
        
        if target_profit > 0:
            st.success(f"✅ Profit: ₹{target_profit:,} (₹{target_profit/30:.0f}/day)")
        elif target_profit < 0:
            st.error(f"🔴 Loss: ₹{abs(target_profit):,} (₹{abs(target_profit)/30:.0f}/day)")
        else:
            st.info("⚖️ Break-even: No profit, no loss")
            
        st.write(f"Daily average: {target_daily:.0f} cups")
    
    with col2:
        st.subheader("🎯 Target Calculator")
        profit_goal = st.number_input("Maya's monthly profit goal (₹):", 
                                     min_value=0, max_value=100000, value=25000, step=1000)
        
        if profit_per_cup > 0:
            cups_needed = (profit_goal + fixed_costs) / profit_per_cup
            daily_needed = cups_needed / 30
            hourly_needed = daily_needed / 12
            
            st.info(f"📈 Cups needed: {cups_needed:.0f}/month")
            st.info(f"📅 Daily target: {daily_needed:.0f} cups")
            st.info(f"⏰ Hourly target: {hourly_needed:.1f} cups")
        else:
            st.error("Cannot achieve profit with current pricing!")
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Linear Functions in Maya's Business:**
    
    1. **Constant Relationships:** Fixed costs stay the same, variable costs change proportionally
    2. **Break-even Analysis:** Where total revenue meets total cost - crucial for survival
    3. **Slope = Rate of Change:** How much profit changes per additional cup sold
    4. **Intercepts Tell Stories:** Starting points reveal fixed costs and baseline scenarios
    5. **Predictive Power:** Once you know the equation, you can predict any scenario
    6. **Business Planning:** Linear functions help make informed decisions about pricing, costs, and targets
    
    **The Power of Linear Thinking:** Every successful business owner uses these concepts, 
    even if they don't call it algebra!
    """)

     # ADD THIS NAVIGATION SECTION AT THE END:
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("← Previous Topic"):
            st.info("This is the first topic!")
    
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with nav_col3:
        if st.button("Next Topic →"):
            st.session_state.page = 'algebra_quadratic'
            st.rerun()

# Function ends here
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Story")
    
    with st.expander("📝 Exercise 1: Maya's Expansion Plan"):
        st.markdown(f"""
        Maya is considering expanding. She found a new location with:
        - Higher rent: ₹{fixed_costs + 15000:,}/month  
        - Same costs per cup: ₹{variable_cost}
        - Can charge more: ₹{selling_price + 2}/cup
        
        **Questions:**
        1. What would be the new break-even point?
        2. How does this compare to her current break-even?
        3. If she expects to sell 10,000 cups/month, which location is better?
        """)
        
        if st.button("Show Solution", key="ex1"):
            new_fixed = fixed_costs + 15000
            new_price = selling_price + 2
            new_profit_per_cup = new_price - variable_cost
            new_breakeven = new_fixed / new_profit_per_cup
            
            old_profit_10k = profit_per_cup * 10000 - fixed_costs
            new_profit_10k = new_profit_per_cup * 10000 - new_fixed
            
            st.markdown(f"""
            **Solutions:**
            1. **New break-even:** {new_breakeven:.0f} cups ({new_breakeven/30:.0f} per day)
            2. **Comparison:** Current = {break_even_cups:.0f} cups, New = {new_breakeven:.0f} cups  
               New location needs {new_breakeven - break_even_cups:.0f} more cups to break even
            3. **At 10,000 cups/month:**
               - Current location profit: ₹{old_profit_10k:,}
               - New location profit: ₹{new_profit_10k:,}
               - **Better choice:** {"New location" if new_profit_10k > old_profit_10k else "Current location"}
            """)

