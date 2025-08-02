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
    .sweet-spot {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_quadratic_functions():

    # At the top:
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    with col2:
        st.title("📊 Quadratic Functions")
    # Main Title
    st.markdown('<h1 class="main-header">📊 Maya\'s Pricing Experiment - Quadratic Functions</h1>', unsafe_allow_html=True)
    
    # Introduction
    st.header("🔍 What is a Quadratic Function?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **A quadratic function creates a curved line (like a hill or valley).** 
        
        In business, this happens when there's a **"sweet spot"** - a perfect middle point 
        where your business performs best. Going too far in either direction hurts performance.
        
        Maya discovered this through her **7-week pricing experiment**!
        """)
    
    with col2:
        st.info("""
        **Key Insight:**
        
        Unlike linear functions (straight lines), 
        quadratic functions show that 
        **small changes near the optimum** = small effects
        **big changes from optimum** = big effects
        """)
    
    # Maya's Experiment Story
    st.header("🧪 Maya's 7-Week Pricing Experiment")
    
    st.markdown("""
    Maya wanted to find the **perfect price** for her tea. Instead of guessing, 
    she decided to test different prices systematically and track results.
    """)
    
    # Create Maya's original data
    maya_data = {
        'Week': [1, 2, 3, 4, 5, 6, 7],
        'Price (₹)': [12, 13, 14, 15, 16, 17, 18],
        'Cups Sold': [200, 230, 240, 250, 240, 230, 200],
        'Maya\'s Notes': [
            "People think it's too cheap",
            "Better, but still suspicious", 
            "Getting good response",
            "Perfect! Maximum customers",
            "Good, but fewer customers",
            "Getting expensive for some",
            "Too pricey for many"
        ]
    }
    
    df_maya = pd.DataFrame(maya_data)
    st.dataframe(df_maya, use_container_width=True)
    
    # Maya's Discovery
    st.markdown('<div class="discovery-highlight">', unsafe_allow_html=True)
    st.subheader("💡 Maya's Big Discovery")
    st.markdown("""
    **"This is strange! At ₹15, I get maximum sales. If I go higher OR lower, I sell fewer cups. 
    It's like there's a perfect middle point!"**
    
    Maya noticed that her sales formed a **curved pattern**, not a straight line!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Quadratic Function Explorer
    st.header("🎛️ Interactive Quadratic Function Explorer")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        optimal_price = st.slider("Optimal Price (₹)", 10, 20, 15, 1, 
                                 help="The price that gives maximum sales")
    
    with col2:
        max_sales = st.slider("Maximum Sales (cups)", 200, 300, 250, 10,
                             help="Peak daily sales at optimal price")
    
    with col3:
        sensitivity = st.slider("Customer Sensitivity", 1, 10, 5, 1,
                               help="How quickly sales drop when moving away from optimal price")
    
    # Generate quadratic function data
    price_range = np.linspace(8, 22, 100)
    sales = max_sales - sensitivity * (price_range - optimal_price)**2
    
    # Ensure sales don't go below 0
    sales = np.maximum(sales, 0)
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: The Quadratic Curve with Maya's Data Points
    ax1.plot(price_range, sales, 'b-', linewidth=3, label=f'Sales = {max_sales} - {sensitivity}×(P - {optimal_price})²')
    
    # Add Maya's original data points
    maya_prices = [12, 13, 14, 15, 16, 17, 18]
    maya_sales = [200, 230, 240, 250, 240, 230, 200]
    ax1.scatter(maya_prices, maya_sales, color='red', s=100, zorder=5, label="Maya's Experiment Data")
    
    # Highlight the optimal point
    ax1.plot(optimal_price, max_sales, 'go', markersize=12, label=f'Sweet Spot: ₹{optimal_price}')
    
    ax1.set_xlabel('Price per Cup (₹)')
    ax1.set_ylabel('Cups Sold per Day')
    ax1.set_title('Maya\'s Sales Curve: Finding the Sweet Spot')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(8, 22)
    
    # Plot 2: Revenue Analysis
    revenue = price_range * sales
    max_revenue_idx = np.argmax(revenue)
    max_revenue_price = price_range[max_revenue_idx]
    max_revenue_value = revenue[max_revenue_idx]
    
    ax2.plot(price_range, revenue, 'g-', linewidth=3, label='Daily Revenue')
    ax2.plot(max_revenue_price, max_revenue_value, 'ro', markersize=12, 
             label=f'Max Revenue: ₹{max_revenue_value:.0f} at ₹{max_revenue_price:.1f}')
    ax2.plot(optimal_price, optimal_price * max_sales, 'bo', markersize=10, 
             label=f'Max Sales Point: ₹{optimal_price * max_sales:.0f} at ₹{optimal_price}')
    
    ax2.set_xlabel('Price per Cup (₹)')
    ax2.set_ylabel('Daily Revenue (₹)')
    ax2.set_title('Revenue vs Price: Sales ≠ Revenue Maximization')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(8, 22)
    
    # Plot 3: Distance from Optimal Analysis
    distance_from_optimal = np.abs(price_range - optimal_price)
    sales_loss = max_sales - sales
    
    ax3.plot(distance_from_optimal, sales_loss, 'purple', linewidth=3, label='Sales Lost')
    ax3.set_xlabel('Distance from Optimal Price (₹)')
    ax3.set_ylabel('Cups Lost from Peak')
    ax3.set_title('Why It\'s Quadratic: Accelerating Losses')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Add annotation showing quadratic relationship
    ax3.annotate('Losses accelerate!\nFar from optimal = Big losses', 
                xy=(3, sensitivity * 9), xytext=(4, sensitivity * 15),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, ha='center')
    
    # Plot 4: Profit Analysis (assuming cost structure)
    cost_per_cup = 8  # Maya's cost from linear functions story
    profit_per_cup = price_range - cost_per_cup
    total_profit = profit_per_cup * sales
    
    # Only show positive profits
    positive_profit_mask = total_profit > 0
    if np.any(positive_profit_mask):
        ax4.plot(price_range[positive_profit_mask], total_profit[positive_profit_mask], 
                'orange', linewidth=3, label='Daily Profit')
        
        max_profit_idx = np.argmax(total_profit)
        if total_profit[max_profit_idx] > 0:
            ax4.plot(price_range[max_profit_idx], total_profit[max_profit_idx], 
                    'ro', markersize=12, 
                    label=f'Max Profit: ₹{total_profit[max_profit_idx]:.0f} at ₹{price_range[max_profit_idx]:.1f}')
    
    ax4.set_xlabel('Price per Cup (₹)')
    ax4.set_ylabel('Daily Profit (₹)')
    ax4.set_title('Profit Optimization: The Ultimate Goal')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(8, 22)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Mathematical Representation
    st.header("🧮 Maya's Mathematical Discovery")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Quadratic Equation:**
    
    **Sales = {max_sales} - {sensitivity} × (P - {optimal_price})²**
    
    **What each part means:**
    - **{max_sales}**: Maya's maximum possible daily sales (at perfect price)
    - **{sensitivity}**: Customer sensitivity factor (how quickly sales drop)
    - **(P - {optimal_price})²**: The "accelerating loss" factor
    - **P**: Price per cup
    
    **Why it's quadratic:** The **(P - {optimal_price})²** creates the curved shape!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Key Business Metrics Dashboard
    st.header("📊 Maya's Business Dashboard")
    
    # Calculate key metrics at different points
    sales_at_optimal = max_sales
    revenue_at_optimal = optimal_price * sales_at_optimal
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Optimal Price", f"₹{optimal_price}", "Maximum Sales")
    
    with col2:
        st.metric("Max Daily Sales", f"{sales_at_optimal} cups", "At optimal price")
    
    with col3:
        st.metric("Revenue at Max Sales", f"₹{revenue_at_optimal:.0f}", 
                 f"At ₹{optimal_price}")
    
    with col4:
        if 'max_revenue_price' in locals():
            st.metric("Max Revenue Price", f"₹{max_revenue_price:.1f}", 
                     f"₹{max_revenue_value:.0f}/day")
    
    # Pattern Analysis Table
    st.header("🔍 Maya's Pattern Analysis")
    
    st.markdown('<div class="sweet-spot">', unsafe_allow_html=True)
    st.subheader("Understanding the Curve")
    
    # Create pattern analysis table
    test_prices = [optimal_price - 3, optimal_price - 2, optimal_price - 1, 
                   optimal_price, optimal_price + 1, optimal_price + 2, optimal_price + 3]
    
    pattern_data = []
    for price in test_prices:
        if price >= 0:
            distance = abs(price - optimal_price)
            sales_val = max(0, max_sales - sensitivity * (price - optimal_price)**2)
            cups_lost = max_sales - sales_val
            
            pattern_data.append({
                'Price (₹)': f'{price:.0f}',
                'Distance from Optimal': f'{distance:.0f}',
                'Cups Sold': f'{sales_val:.0f}',
                'Cups Lost': f'{cups_lost:.0f}',
                'Revenue (₹)': f'{price * sales_val:.0f}'
            })
    
    df_pattern = pd.DataFrame(pattern_data)
    st.dataframe(df_pattern, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Business Calculator
    st.header("🤔 Maya's Business Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Price Tester")
        test_price = st.number_input("Test any price (₹):", 
                                    min_value=5.0, max_value=25.0, 
                                    value=float(optimal_price), step=0.5)
        
        test_sales = max(0, max_sales - sensitivity * (test_price - optimal_price)**2)
        test_revenue = test_price * test_sales
        
        if test_sales > 0:
            st.success(f"📈 Sales: {test_sales:.0f} cups")
            st.info(f"💰 Revenue: ₹{test_revenue:.0f}")
            
            # Compare to optimal
            sales_diff = test_sales - max_sales
            if sales_diff < 0:
                st.warning(f"📉 {abs(sales_diff):.0f} fewer cups than optimal")
            else:
                st.success("🎯 This is the optimal price!")
        else:
            st.error("💸 No sales at this price!")
    
    with col2:
        st.subheader("🔍 Sales Target Finder")
        target_sales = st.number_input("Target daily sales:", 
                                      min_value=50, max_value=int(max_sales), 
                                      value=200, step=10)
        
        # Solve quadratic equation: target_sales = max_sales - sensitivity * (P - optimal_price)²
        # Rearranging: (P - optimal_price)² = (max_sales - target_sales) / sensitivity
        
        if target_sales <= max_sales:
            discriminant = (max_sales - target_sales) / sensitivity
            if discriminant >= 0:
                distance = sqrt(discriminant)
                price1 = optimal_price - distance
                price2 = optimal_price + distance
                
                st.info(f"🎯 Two prices achieve {target_sales} cups:")
                if price1 > 0:
                    st.write(f"• **₹{price1:.1f}** (lower price)")
                if price2 > 0:
                    st.write(f"• **₹{price2:.1f}** (higher price)")
                    
                st.write("**Maya's insight:** Same sales, different revenues!")
                if price1 > 0 and price2 > 0:
                    rev1 = price1 * target_sales
                    rev2 = price2 * target_sales
                    st.write(f"Revenue at ₹{price1:.1f}: ₹{rev1:.0f}")
                    st.write(f"Revenue at ₹{price2:.1f}: ₹{rev2:.0f}")
        else:
            st.error("Target too high! Maximum possible is {max_sales} cups")
    
    # Business Insights
    st.header("💡 Key Business Insights")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 The Sweet Spot Principle")
        st.write("**Maximum Sales ≠ Maximum Revenue ≠ Maximum Profit**")
        st.write(f"• Max sales at ₹{optimal_price} = {max_sales} cups")
        if 'max_revenue_price' in locals():
            st.write(f"• Max revenue at ₹{max_revenue_price:.1f} = ₹{max_revenue_value:.0f}")
        st.write("• Each goal needs different pricing!")
        
        st.subheader("📈 Why It's Curved")
        st.write("**Customer psychology isn't linear:**")
        st.write("• Small price changes → small reactions")
        st.write("• Big price changes → big reactions that multiply")
        st.write("• The (P - optimal)² captures this acceleration")
    
    with col2:
        st.subheader("🔢 Mathematical Power")
        st.write("**Maya transformed from:**")
        st.write("❌ \"I'll try prices and see what happens\"")
        st.write("✅ \"I can predict exactly what happens at any price\"")
        
        st.subheader("🏢 Business Applications")
        st.write("**Quadratic patterns appear in:**")
        st.write("• Team productivity (sweet spot size)")
        st.write("• Marketing spend (optimal budget)")
        st.write("• Product features (not too few, not too many)")
        st.write("• Inventory levels (optimal stock)")
    
    st.markdown('</div>', unsafe_allow_html=True)

     # ADD THIS NAVIGATION SECTION AT THE END:
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])

    with nav_col1:

        if st.button("← Linear Functions"):
            st.session_state.page = 'algebra_linear'
            st.rerun()
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    with nav_col3:
        if st.button("Exponential Functions →"):
            st.session_state.page = 'algebra_exponential'
            st.rerun()
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Quadratic Story")
    
    with st.expander("📝 Exercise 1: Maya's Competition Analysis"):
        st.markdown(f"""
        A competitor near Maya charges ₹{optimal_price + 2} and sells 180 cups daily. 
        Maya's equation predicts she'd sell {max_sales - sensitivity * 4:.0f} cups at that price.
        
        **Questions:**
        1. Why is there a difference?
        2. What advantages might Maya have?
        3. Should Maya match the competitor's price?
        4. What price would give Maya the same revenue as her competitor?
        """)
        
        if st.button("Show Solutions", key="ex1_quad"):
            competitor_revenue = (optimal_price + 2) * 180
            maya_predicted = max_sales - sensitivity * 4
            maya_revenue_at_comp_price = (optimal_price + 2) * maya_predicted
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Why the difference?**
               - Different locations, customer bases, or quality perceptions
               - Maya's equation is specific to her customer behavior
               - Competitors may have different optimal prices
            
            2. **Maya's possible advantages:**
               - Better location or foot traffic
               - Higher perceived quality or service
               - Stronger customer loyalty
            
            3. **Should Maya match ₹{optimal_price + 2}?**
               - Maya's revenue at ₹{optimal_price + 2}: ₹{maya_revenue_at_comp_price:.0f}
               - Maya's revenue at optimal ₹{optimal_price}: ₹{optimal_price * max_sales:.0f}
               - **Decision: Stay at ₹{optimal_price}** (higher revenue)
            
            4. **Price for same revenue as competitor:**
               - Competitor revenue: ₹{competitor_revenue:.0f}
               - Maya needs to solve: P × sales(P) = {competitor_revenue:.0f}
               - This requires testing different prices in her equation
            """)
    
    with st.expander("📝 Exercise 2: Maya's Menu Expansion"):
        st.markdown("""
        Maya wants to add masala chai alongside regular tea. She estimates:
        - Regular tea follows her current equation
        - Masala chai: Sales = 150 - 3×(P - 18)² (higher optimal price, lower volume)
        
        **Questions:**
        1. What's the optimal price for masala chai?
        2. At optimal prices, what's Maya's total daily revenue?
        3. If Maya can only focus on one product, which should she choose?
        """)
        
        if st.button("Show Solutions", key="ex2_quad"):
            # Masala chai parameters
            masala_optimal = 18
            masala_max_sales = 150
            masala_sensitivity = 3
            
            # Regular tea revenue at optimal
            regular_revenue = optimal_price * max_sales
            
            # Masala chai revenue at optimal
            masala_revenue = masala_optimal * masala_max_sales
            
            # Total revenue
            total_revenue = regular_revenue + masala_revenue
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Masala chai optimal price:** ₹{masala_optimal} (gives {masala_max_sales} cups)
            
            2. **Total daily revenue at optimal prices:**
               - Regular tea: ₹{optimal_price} × {max_sales} = ₹{regular_revenue:.0f}
               - Masala chai: ₹{masala_optimal} × {masala_max_sales} = ₹{masala_revenue:.0f}
               - **Total: ₹{total_revenue:.0f} per day**
            
            3. **Single product choice:**
               - Regular tea revenue: ₹{regular_revenue:.0f}
               - Masala chai revenue: ₹{masala_revenue:.0f}
               - **Winner: {"Regular tea" if regular_revenue > masala_revenue else "Masala chai"}**
               
            **Business insight:** Diversification increases total revenue even if individual products earn less!
            """)
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Quadratic Functions in Maya's Business:**
    
    1. **Sweet Spot Principle:** There's often an optimal point - not too high, not too low
    2. **Accelerating Effects:** Small changes from optimal have small impacts, big changes have big impacts  
    3. **Multiple Objectives:** Maximum sales ≠ maximum revenue ≠ maximum profit
    4. **Predictive Power:** The equation lets Maya test any scenario without real experiments
    5. **Customer Psychology:** People's reactions aren't linear - they accelerate with bigger changes
    6. **Business Strategy:** Understanding the curve helps optimize pricing, features, team size, etc.
    
    **Maya's Transformation:** From trial-and-error to mathematical precision in business decisions!
    """)



    
            # At the end:
    
# This would be called from the main navigation system
# No st.set_page_config() needed here - handled by main.py