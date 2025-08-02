import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

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
    .inverse-highlight {
        background-color: #f1f8e9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #689f38;
        margin: 1rem 0;
    }
    .reverse-thinking {
        background-color: #fce4ec;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #e91e63;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_inverse_functions():
    # Header with back navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("🔄 Inverse Functions")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra** > **Inverse Functions**")
    
    # Main Title
    st.markdown('<h1 class="main-header">🎯 Maya\'s Reverse Business Questions - Inverse Functions</h1>', unsafe_allow_html=True)
    
    # Business Storyline
    st.header("📖 Maya's New Challenge: Working Backwards")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Maya receives an interesting order:** *"We want exactly 200 cups for our office party. What will you charge us?"*
        
        **Maya's dilemma:** *"I know how to calculate sales from price, but now I need to calculate price from sales!"*
        
        This forces Maya to think in **reverse** - instead of asking "If I charge X, how many will I sell?" 
        she needs to ask "If I want to sell Y cups, what should I charge?"
        
        **Welcome to the world of inverse functions - flipping business questions around!**
        """)
    
    with col2:
        st.info("""
        **What is an Inverse Function?**
        
        **Flips the question around:**
        - Forward: "If I do X, what happens?"
        - Inverse: "If I want Y, what should I do?"
        
        Same relationship, opposite direction!
        """)
    
    # Forward vs Reverse Thinking
    st.header("🔄 Forward vs Reverse Business Thinking")
    
    st.markdown('<div class="discovery-highlight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("➡️ Forward Thinking (Original)")
        st.markdown("""
        **Input:** Price (₹)  
        **Output:** Sales (cups)  
        **Question:** "At ₹17, how many cups will I sell?"  
        **Formula:** Sales = 250 - 5 × (Price - 15)²  
        **Maya controls:** Price  
        **Customers decide:** Quantity
        """)
    
    with col2:
        st.subheader("⬅️ Reverse Thinking (Inverse)")
        st.markdown("""
        **Input:** Sales (cups)  
        **Output:** Price (₹)  
        **Question:** "To sell 200 cups, what should I charge?"  
        **Formula:** Price = 15 ± √[(250 - Sales) ÷ 5]  
        **Maya targets:** Quantity  
        **Maya calculates:** Required price
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Inverse Function Explorer
    st.header("🎛️ Interactive Forward vs Inverse Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        optimal_price = st.slider("Optimal Price (₹)", 10, 20, 15, 1,
                                 help="The price that gives maximum sales")
    
    with col2:
        max_sales = st.slider("Maximum Sales (cups)", 200, 300, 250, 10,
                             help="Peak daily sales at optimal price")
    
    with col3:
        sensitivity = st.slider("Price Sensitivity", 1, 10, 5, 1,
                               help="How sensitive customers are to price changes")
    
    # Define forward and inverse functions
    def forward_function(price):
        return max_sales - sensitivity * (price - optimal_price)**2
    
    def inverse_function(sales):
        if sales > max_sales:
            return None, None  # Impossible sales target
        discriminant = (max_sales - sales) / sensitivity
        if discriminant < 0:
            return None, None
        sqrt_val = sqrt(discriminant)
        price1 = optimal_price - sqrt_val
        price2 = optimal_price + sqrt_val
        return price1, price2
    
    # Generate data for visualization
    price_range = np.linspace(5, 25, 200)
    sales_from_price = np.array([max(0, forward_function(p)) for p in price_range])
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Original Function (Price → Sales)
    ax1.plot(price_range, sales_from_price, 'b-', linewidth=3, label=f'Sales = {max_sales} - {sensitivity}×(Price - {optimal_price})²')
    ax1.scatter([optimal_price], [max_sales], color='red', s=100, zorder=5, label=f'Peak: ₹{optimal_price} → {max_sales} cups')
    
    # Add example points
    example_prices = [12, 15, 18]
    for ep in example_prices:
        es = forward_function(ep)
        if es > 0:
            ax1.scatter([ep], [es], color='orange', s=60, zorder=4)
            ax1.annotate(f'₹{ep}→{es:.0f}cups', xy=(ep, es), xytext=(ep, es+10),
                        ha='center', fontsize=9)
    
    ax1.set_xlabel('Price (₹)')
    ax1.set_ylabel('Sales (cups)')
    ax1.set_title('Forward Function: Price → Sales')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Inverse Function (Sales → Price)
    # We need to flip the axes for the inverse
    ax2.plot(sales_from_price, price_range, 'g-', linewidth=3, label='Inverse: Sales → Price')
    ax2.scatter([max_sales], [optimal_price], color='red', s=100, zorder=5, label=f'Peak: {max_sales} cups → ₹{optimal_price}')
    
    # Add example points for inverse
    example_sales = [200, 225, 240]
    for es in example_sales:
        if es <= max_sales:
            p1, p2 = inverse_function(es)
            if p1 is not None and p2 is not None:
                ax2.scatter([es, es], [p1, p2], color='orange', s=60, zorder=4)
                ax2.annotate(f'{es}→₹{p1:.1f}', xy=(es, p1), xytext=(es-15, p1),
                           ha='center', fontsize=9)
                ax2.annotate(f'{es}→₹{p2:.1f}', xy=(es, p2), xytext=(es-15, p2),
                           ha='center', fontsize=9)
    
    ax2.set_xlabel('Sales (cups)')
    ax2.set_ylabel('Price (₹)')
    ax2.set_title('Inverse Function: Sales → Price')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Revenue Analysis
    revenue = price_range * sales_from_price
    ax3.plot(price_range, revenue, 'purple', linewidth=3, label='Revenue = Price × Sales')
    
    # Find maximum revenue point
    max_revenue_idx = np.argmax(revenue)
    max_revenue_price = price_range[max_revenue_idx]
    max_revenue_value = revenue[max_revenue_idx]
    
    ax3.scatter([max_revenue_price], [max_revenue_value], color='red', s=100, zorder=5,
               label=f'Max Revenue: ₹{max_revenue_value:.0f} at ₹{max_revenue_price:.1f}')
    
    ax3.set_xlabel('Price (₹)')
    ax3.set_ylabel('Revenue (₹)')
    ax3.set_title('Revenue Optimization Using Inverse Thinking')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Multiple Solutions Demonstration
    target_sales = 200
    if target_sales <= max_sales:
        p1, p2 = inverse_function(target_sales)
        if p1 is not None and p2 is not None:
            # Show both solutions
            ax4.plot(price_range, sales_from_price, 'b-', linewidth=2, alpha=0.7, label='Sales Function')
            ax4.axhline(y=target_sales, color='red', linestyle='--', alpha=0.7, label=f'Target: {target_sales} cups')
            ax4.scatter([p1, p2], [target_sales, target_sales], color='red', s=100, zorder=5)
            
            # Add annotations
            ax4.annotate(f'Solution 1:\n₹{p1:.2f}', xy=(p1, target_sales), 
                        xytext=(p1, target_sales+20), ha='center', fontsize=10,
                        arrowprops=dict(arrowstyle='->', color='red'))
            ax4.annotate(f'Solution 2:\n₹{p2:.2f}', xy=(p2, target_sales), 
                        xytext=(p2, target_sales+20), ha='center', fontsize=10,
                        arrowprops=dict(arrowstyle='->', color='red'))
            
            ax4.set_xlabel('Price (₹)')
            ax4.set_ylabel('Sales (cups)')
            ax4.set_title(f'Two Prices Give Same Sales: {target_sales} cups')
            ax4.legend()
            ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Mathematical Representation
    st.header("🧮 Maya's Forward and Inverse Equations")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Forward Function (Price → Sales):**
    
    **Sales = {max_sales} - {sensitivity} × (Price - {optimal_price})²**
    
    **Maya's Inverse Function (Sales → Price):**
    
    **Price = {optimal_price} ± √[({max_sales} - Sales) ÷ {sensitivity}]**
    
    **Key Insights:**
    - **Forward:** One price gives one sales amount
    - **Inverse:** One sales target can have TWO price solutions!
    - **±** symbol means Maya can choose higher or lower price for same sales
    - **Higher price** = Higher revenue per cup
    - **Lower price** = More accessible to customers
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Dashboard
    st.header("📊 Maya's Inverse Business Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Optimal Price", f"₹{optimal_price}", "Maximum sales point")
    
    with col2:
        st.metric("Max Possible Sales", f"{max_sales} cups", "At optimal price")
    
    with col3:
        max_revenue_price_calc = optimal_price + sqrt((max_sales/2)/sensitivity) if max_sales/(2*sensitivity) >= 0 else optimal_price
        max_revenue_calc = max_revenue_price_calc * forward_function(max_revenue_price_calc)
        st.metric("Max Revenue Price", f"₹{max_revenue_price_calc:.1f}", f"₹{max_revenue_calc:.0f} revenue")
    
    with col4:
        # Price range for 90% of max sales
        sales_90_percent = max_sales * 0.9
        p1_90, p2_90 = inverse_function(sales_90_percent)
        if p1_90 and p2_90:
            price_range_90 = abs(p2_90 - p1_90)
            st.metric("Price Range (90% sales)", f"₹{price_range_90:.1f}", "Flexibility")
    
    # Interactive Business Calculator
    st.header("🤔 Maya's Forward & Inverse Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("➡️ Forward Calculator")
        st.write("**Question:** *If I charge this price, how many cups will I sell?*")
        
        input_price = st.number_input("Set your price (₹):", 
                                     min_value=5.0, max_value=25.0, value=16.0, step=0.5)
        
        calculated_sales = forward_function(input_price)
        calculated_revenue = input_price * calculated_sales if calculated_sales > 0 else 0
        
        if calculated_sales > 0:
            st.success(f"📈 Price ₹{input_price} → **{calculated_sales:.1f} cups sold**")
            st.info(f"💰 Revenue: ₹{calculated_revenue:.0f}")
            
            # Compare to optimal
            sales_diff = calculated_sales - max_sales
            if abs(sales_diff) < 1:
                st.success("🎯 This is very close to optimal sales!")
            elif sales_diff < 0:
                st.warning(f"📉 {abs(sales_diff):.1f} fewer cups than maximum possible")
        else:
            st.error("💸 No sales at this price!")
    
    with col2:
        st.subheader("⬅️ Inverse Calculator")
        st.write("**Question:** *If I want to sell this many cups, what should I charge?*")
        
        target_sales_input = st.number_input("Target sales (cups):", 
                                           min_value=0, max_value=int(max_sales), 
                                           value=200, step=10)
        
        if target_sales_input <= max_sales:
            price1, price2 = inverse_function(target_sales_input)
            
            if price1 is not None and price2 is not None:
                revenue1 = price1 * target_sales_input
                revenue2 = price2 * target_sales_input
                
                st.success(f"🎯 To sell {target_sales_input} cups:")
                st.write(f"**Option 1:** ₹{price1:.2f} → Revenue: ₹{revenue1:.0f}")
                st.write(f"**Option 2:** ₹{price2:.2f} → Revenue: ₹{revenue2:.0f}")
                
                if revenue2 > revenue1:
                    st.info(f"💡 **Recommendation:** Choose ₹{price2:.2f} for ₹{revenue2-revenue1:.0f} more revenue!")
                else:
                    st.info(f"💡 **Recommendation:** Choose ₹{price1:.2f} for ₹{revenue1-revenue2:.0f} more revenue!")
            else:
                st.error("Cannot calculate - mathematical error")
        else:
            st.error(f"Target too high! Maximum possible sales: {max_sales} cups")
    
    # Business Applications
    st.header("💼 Maya's Real Business Applications")
    
    st.markdown('<div class="inverse-highlight">', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📋 Order Planning", "🎯 Revenue Target", "⚡ Capacity Planning"])
    
    with tab1:
        st.subheader("Customer Order Scenario")
        st.write("**Customer request:** *'We need exactly 240 cups for our corporate event.'*")
        
        if 240 <= max_sales:
            p1_240, p2_240 = inverse_function(240)
            if p1_240 and p2_240:
                rev1_240 = p1_240 * 240
                rev2_240 = p2_240 * 240
                
                st.write(f"**Maya's options:**")
                st.write(f"• **Lower price:** ₹{p1_240:.2f} → Revenue: ₹{rev1_240:.0f}")
                st.write(f"• **Higher price:** ₹{p2_240:.2f} → Revenue: ₹{rev2_240:.0f}")
                st.write(f"**Maya's decision:** *'I'll charge ₹{p2_240:.2f} for ₹{rev2_240-rev1_240:.0f} more revenue!'*")
    
    with tab2:
        st.subheader("Revenue Target Scenario")
        revenue_target = st.number_input("Maya's daily revenue goal (₹):", 
                                        min_value=1000, max_value=5000, value=3000, step=100)
        
        st.write(f"**Maya's goal:** *'I want exactly ₹{revenue_target} revenue today.'*")
        
        # Find combinations that achieve target revenue
        combinations = []
        for sales in range(50, int(max_sales), 10):
            price_needed = revenue_target / sales
            predicted_sales = forward_function(price_needed)
            if abs(predicted_sales - sales) < 5:  # Close enough
                combinations.append((sales, price_needed, revenue_target))
        
        if combinations:
            st.write("**Possible combinations:**")
            for sales, price, revenue in combinations[:3]:  # Show top 3
                st.write(f"• {sales} cups × ₹{price:.2f} = ₹{revenue}")
        else:
            st.write("**Maya's challenge:** This revenue target may not be achievable with current demand curve.")
    
    with tab3:
        st.subheader("Capacity Planning Scenario")
        max_capacity = st.number_input("Maya's maximum daily capacity (cups):", 
                                      min_value=100, max_value=int(max_sales), value=220, step=10)
        
        st.write(f"**Maya's constraint:** *'I can only make {max_capacity} cups maximum per day.'*")
        
        if max_capacity <= max_sales:
            p1_cap, p2_cap = inverse_function(max_capacity)
            if p1_cap and p2_cap:
                rev1_cap = p1_cap * max_capacity
                rev2_cap = p2_cap * max_capacity
                
                st.write(f"**Maya's pricing options for {max_capacity} cups:**")
                st.write(f"• **Lower price:** ₹{p1_cap:.2f} → Revenue: ₹{rev1_cap:.0f}")
                st.write(f"• **Higher price:** ₹{p2_cap:.2f} → Revenue: ₹{rev2_cap:.0f}")
                st.write(f"**Maya's strategy:** *'₹{p2_cap:.2f} maximizes my revenue at full capacity!'*")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Insights
    st.header("💡 Inverse Function Business Insights")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Goal-Oriented Planning")
        st.write("**Start with desired outcome, work backwards:**")
        st.write("• **Traditional:** 'If I do X, what happens?'")
        st.write("• **Inverse:** 'To achieve Y, what should I do?'")  
        st.write("• **Strategic advantage:** Clear path from goals to actions")
        st.write("• **Decision clarity:** Multiple solutions allow optimization")
        
        st.subheader("🔄 Multiple Solutions Power")
        st.write("**Why two prices give same sales:**")
        st.write("• **Lower price:** Attracts price-sensitive customers")
        st.write("• **Higher price:** Fewer customers but premium positioning")
        st.write("• **Maya's choice:** Depends on brand strategy and goals")
    
    with col2:
        st.subheader("🏢 Real-World Inverse Applications")
        st.write("**Common business scenarios:**")
        st.write("• **Target costing:** 'To sell at ₹100, what's max cost?'")
        st.write("• **Staffing:** 'To serve 1000 customers, how many staff?'")
        st.write("• **Production planning:** 'To meet deadline, when start?'")
        st.write("• **Marketing:** 'For 500 customers, what ad spend?'")
        
        st.subheader("🚨 Maya's Strategic Transformation")
        st.write("**Maya now thinks in both directions:**")
        st.write("• **Forward planning:** Cause → Effect")
        st.write("• **Backward planning:** Goal → Required Actions")
        st.write("• **Scenario analysis:** 'What if I want X?'")
        st.write("• **Customer-driven pricing:** Match customer needs")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Inverse Story")
    
    with st.expander("📝 Exercise 1: Maya's Competitor Analysis"):
        st.markdown(f"""
        Maya's competitor has the sales function: Sales = 200 - 3 × (Price - 12)²
        
        Maya wants to match her competitor's sales volume of 170 cups.
        
        **Questions:**
        1. What prices should the competitor charge for 170 cups?
        2. What prices should Maya charge for 170 cups using her function?
        3. Who has more pricing flexibility for the same sales target?
        """)
        
        if st.button("Show Solutions", key="ex1_inv"):
            # Competitor's inverse function
            def competitor_inverse(sales):
                if sales > 200:
                    return None, None
                discriminant = (200 - sales) / 3
                if discriminant < 0:
                    return None, None
                sqrt_val = sqrt(discriminant)
                return 12 - sqrt_val, 12 + sqrt_val
            
            # Maya's inverse for 170 cups
            maya_p1, maya_p2 = inverse_function(170)
            comp_p1, comp_p2 = competitor_inverse(170)
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Competitor's prices for 170 cups:**
               - Using Sales = 200 - 3×(Price - 12)²
               - 170 = 200 - 3×(Price - 12)²
               - Price = 12 ± √(30/3) = 12 ± {sqrt(10):.2f}
               - **Prices: ₹{comp_p1:.2f} or ₹{comp_p2:.2f}**
            
            2. **Maya's prices for 170 cups:**
               - Using Sales = {max_sales} - {sensitivity}×(Price - {optimal_price})²
               - **Prices: ₹{maya_p1:.2f} or ₹{maya_p2:.2f}**
            
            3. **Pricing flexibility comparison:**
               - **Competitor range:** ₹{comp_p2 - comp_p1:.2f} (₹{comp_p1:.2f} to ₹{comp_p2:.2f})
               - **Maya's range:** ₹{maya_p2 - maya_p1:.2f} (₹{maya_p1:.2f} to ₹{maya_p2:.2f})
               - **Winner:** {"Maya" if (maya_p2 - maya_p1) > (comp_p2 - comp_p1) else "Competitor"} has more pricing flexibility
            
            **Business insight:** Different demand curves give different strategic options!
            """)
    
    with st.expander("📝 Exercise 2: Maya's Event Planning Business"):
        st.markdown(f"""
        Maya is considering catering events. For events, her demand changes to:
        Event Sales = 100 - 2 × (Price - 20)²
        
        She gets three event requests:
        - **Wedding:** Needs exactly 80 cups
        - **Corporate:** Needs exactly 90 cups  
        - **Birthday:** Needs exactly 95 cups
        
        **Questions:**
        1. What should Maya charge for each event?
        2. Which event gives the highest revenue?
        3. Should Maya focus on events or regular daily sales?
        """)
        
        if st.button("Show Solutions", key="ex2_inv"):
            def event_inverse(sales):
                if sales > 100:
                    return None, None
                discriminant = (100 - sales) / 2
                if discriminant < 0:
                    return None, None
                sqrt_val = sqrt(discriminant)
                return 20 - sqrt_val, 20 + sqrt_val
            
            events = [
                ("Wedding", 80),
                ("Corporate", 90), 
                ("Birthday", 95)
            ]
            
            st.markdown("**Solutions:**")
            
            revenues = []
            for event_name, cups in events:
                p1, p2 = event_inverse(cups)
                rev1 = p1 * cups
                rev2 = p2 * cups
                revenues.append((event_name, p1, p2, rev1, rev2, max(rev1, rev2)))
                
                st.write(f"""
                **{event_name} ({cups} cups):**
                - Lower price: ₹{p1:.2f} → Revenue: ₹{rev1:.0f}
                - Higher price: ₹{p2:.2f} → Revenue: ₹{rev2:.0f}
                """)
            
            # Find highest revenue event
            max_revenue_event = max(revenues, key=lambda x: x[5])
            
            st.markdown(f"""
            2. **Highest revenue event:** {max_revenue_event[0]} with ₹{max_revenue_event[5]:.0f}
            
            3. **Events vs Regular Sales:**
               - **Best event revenue:** ₹{max_revenue_event[5]:.0f}
               - **Maya's regular max revenue:** ₹{max_revenue_calc:.0f}
               - **Recommendation:** {"Focus on events!" if max_revenue_event[5] > max_revenue_calc else "Stick with regular sales!"}
            
            **Business insight:** Inverse functions help compare different business models!
            """)
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Inverse Functions in Maya's Business:**
    
    1. **Reverse Thinking:** Work backward from goals to required actions - crucial for strategic planning
    2. **Multiple Solutions:** Same outcome can be achieved through different paths - choose based on strategy
    3. **Goal-Oriented Planning:** Start with desired results, calculate what needs to be done
    4. **Strategic Flexibility:** Inverse functions reveal all possible ways to achieve targets
    5. **Customer-Driven Pricing:** Match customer quantity needs with appropriate pricing
    6. **Scenario Analysis:** "What if I want X?" becomes mathematically answerable
    
    **Maya's Complete Transformation:** From reactive business owner to strategic planner who thinks both forward and backward!
    
    **The Ultimate Power:** Maya can now analyze any business situation from multiple angles - cause to effect AND effect to cause!
    """)
    
    # Maya's Journey Complete
    st.markdown('<div class="reverse-thinking">', unsafe_allow_html=True)
    st.header("🎉 Maya's Algebra Journey Complete!")
    
    st.markdown("""
    **Maya's Mathematical Evolution:**
    
    📈 **Linear Functions:** Understanding basic profit relationships  
    📊 **Quadratic Functions:** Finding optimal pricing sweet spots  
    🌱 **Exponential Functions:** Predicting explosive growth patterns  
    📉 **Logarithmic Functions:** Managing diminishing returns in learning  
    🔗 **Piecewise Functions:** Creating sophisticated business rules  
    🔄 **Inverse Functions:** Mastering goal-oriented strategic planning  
    
    **From Tea Stall Owner to Mathematical Business Strategist!**
    
    Maya now has the mathematical tools to analyze, predict, and optimize any business situation. 
    She can think forward (what will happen?) and backward (what should I do?), 
    handle complex scenarios with multiple rules, and make data-driven decisions with confidence.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("← Piecewise Functions"):
            st.session_state.page = 'algebra_piecewise'
            st.rerun()
    
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    