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
    .discovery-highlight {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
    .piecewise-highlight {
        background-color: #f3e5f5;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #9c27b0;
        margin: 1rem 0;
    }
    .threshold-highlight {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_piecewise_functions():
    # Header with back navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("🔗 Piecewise Functions")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra** > **Piecewise Functions**")
    
    # Main Title
    st.markdown('<h1 class="main-header">🚚 Maya\'s Business Rules - Piecewise Functions</h1>', unsafe_allow_html=True)
    
    # Business Storyline
    st.header("📖 Maya's Delivery Pricing Challenge")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Maya's tea stall is booming!** Customer demand is so high that people want home delivery. 
        But Maya faces a new challenge: **how to price deliveries fairly based on distance?**
        
        After thinking about her costs, Maya realizes she can't use one simple rule for all distances. 
        Different distances require different transportation methods and time investments.
        
        **"I use different pricing rules depending on the distance. It's not one single rule for everyone!"**
        
        Let's help Maya understand **piecewise functions** - the mathematics of different rules for different situations!
        """)
    
    with col2:
        st.info("""
        **What is a Piecewise Function?**
        
        Uses **different rules for different situations**.
        
        Like having different prices for different customer types, or "IF this, THEN that" in business.
        """)
    
    # Maya's Delivery Logic
    st.header("🧠 Maya's Delivery Logic")
    
    st.markdown('<div class="discovery-highlight">', unsafe_allow_html=True)
    st.subheader("Maya's Reasoning Process")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🚶 Short Distance (0-2 km)**
        - "I can walk there easily"
        - Low time investment
        - **Charge: ₹10**
        """)
    
    with col2:
        st.markdown("""
        **🛺 Medium Distance (2-5 km)**
        - "Need to take auto-rickshaw"
        - Medium cost and time
        - **Charge: ₹25**
        """)
    
    with col3:
        st.markdown("""
        **🚌 Long Distance (5+ km)**
        - "Takes too much time and money"
        - High cost investment
        - **Charge: ₹50**
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Maya's First Week Data
    st.header("📊 Maya's First Week of Deliveries")
    
    delivery_data = {
        'Customer': ['Ravi', 'Priya', 'Arjun', 'Meera', 'Suresh', 'Kavya', 'Rohit'],
        'Distance (km)': [1.0, 3.0, 6.0, 2.0, 4.5, 1.5, 7.2],
        'Delivery Charge (₹)': [10, 25, 50, 10, 25, 10, 50],
        'Rule Used': [
            'Short distance rule',
            'Medium distance rule', 
            'Long distance rule',
            'Short distance rule',
            'Medium distance rule',
            'Short distance rule',
            'Long distance rule'
        ]
    }
    
    df_delivery = pd.DataFrame(delivery_data)
    st.dataframe(df_delivery, use_container_width=True)
    
    # Interactive Piecewise Function Explorer
    st.header("🎛️ Interactive Delivery Pricing Simulator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        short_charge = st.slider("Short Distance Charge (₹)", 5, 20, 10, 1,
                                help="Charge for 0-2 km deliveries")
    
    with col2:
        medium_charge = st.slider("Medium Distance Charge (₹)", 15, 40, 25, 1,
                                 help="Charge for 2-5 km deliveries")
    
    with col3:
        long_charge = st.slider("Long Distance Charge (₹)", 30, 80, 50, 5,
                               help="Charge for 5+ km deliveries")
    
    # Additional parameters
    col1, col2 = st.columns(2)
    with col1:
        short_threshold = st.slider("Short/Medium Boundary (km)", 1.0, 3.0, 2.0, 0.1,
                                   help="Distance where pricing changes to medium")
    with col2:
        medium_threshold = st.slider("Medium/Long Boundary (km)", 4.0, 8.0, 5.0, 0.1,
                                    help="Distance where pricing changes to long")
    
    # Define piecewise function
    def delivery_charge(distance):
        if distance <= short_threshold:
            return short_charge
        elif distance <= medium_threshold:
            return medium_charge
        else:
            return long_charge
    
    # Generate data for visualization
    distances = np.linspace(0, 10, 1000)
    charges = np.array([delivery_charge(d) for d in distances])
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Piecewise Function Graph
    ax1.plot(distances, charges, 'b-', linewidth=3, label='Maya\'s Delivery Pricing')
    
    # Add vertical lines at thresholds
    ax1.axvline(x=short_threshold, color='red', linestyle='--', alpha=0.7, label=f'Threshold 1: {short_threshold} km')
    ax1.axvline(x=medium_threshold, color='orange', linestyle='--', alpha=0.7, label=f'Threshold 2: {medium_threshold} km')
    
    # Add annotations for each piece
    ax1.annotate(f'₹{short_charge}', xy=(short_threshold/2, short_charge), xytext=(short_threshold/2, short_charge + 5),
                ha='center', fontsize=12, fontweight='bold')
    ax1.annotate(f'₹{medium_charge}', xy=((short_threshold + medium_threshold)/2, medium_charge), 
                xytext=((short_threshold + medium_threshold)/2, medium_charge + 5),
                ha='center', fontsize=12, fontweight='bold')
    ax1.annotate(f'₹{long_charge}', xy=(medium_threshold + 1, long_charge), xytext=(medium_threshold + 1, long_charge + 5),
                ha='center', fontsize=12, fontweight='bold')
    
    ax1.set_xlabel('Distance (km)')
    ax1.set_ylabel('Delivery Charge (₹)')
    ax1.set_title('Maya\'s Piecewise Delivery Pricing')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 10)
    
    # Plot 2: Customer Distribution Analysis
    # Simulate customer distribution across distances
    np.random.seed(42)
    customer_distances = np.random.exponential(2.5, 100)  # Most customers are nearby
    customer_distances = customer_distances[customer_distances <= 10]  # Limit to 10km
    
    customer_charges = np.array([delivery_charge(d) for d in customer_distances])
    
    ax2.scatter(customer_distances, customer_charges, alpha=0.6, s=50, c='purple')
    ax2.set_xlabel('Customer Distance (km)')
    ax2.set_ylabel('Charge Paid (₹)')
    ax2.set_title('Customer Charge Distribution')
    ax2.grid(True, alpha=0.3)
    
    # Add average charge per zone
    short_customers = customer_distances[customer_distances <= short_threshold]
    medium_customers = customer_distances[(customer_distances > short_threshold) & (customer_distances <= medium_threshold)]
    long_customers = customer_distances[customer_distances > medium_threshold]
    
    ax2.axhline(y=short_charge, xmax=short_threshold/10, color='blue', linewidth=3, alpha=0.7)
    ax2.axhline(y=medium_charge, xmin=short_threshold/10, xmax=medium_threshold/10, color='green', linewidth=3, alpha=0.7)
    ax2.axhline(y=long_charge, xmin=medium_threshold/10, color='red', linewidth=3, alpha=0.7)
    
    # Plot 3: Revenue Analysis by Distance Zone
    zone_names = ['Short\n(0-2km)', 'Medium\n(2-5km)', 'Long\n(5+km)']
    zone_customers = [len(short_customers), len(medium_customers), len(long_customers)]
    zone_revenues = [len(short_customers) * short_charge, 
                    len(medium_customers) * medium_charge,
                    len(long_customers) * long_charge]
    
    ax3.bar(zone_names, zone_revenues, color=['lightblue', 'lightgreen', 'lightcoral'], alpha=0.8)
    ax3.set_ylabel('Total Revenue (₹)')
    ax3.set_title('Revenue by Distance Zone')
    ax3.grid(True, alpha=0.3)
    
    # Add customer count labels on bars
    for i, (customers, revenue) in enumerate(zip(zone_customers, zone_revenues)):
        ax3.text(i, revenue + max(zone_revenues) * 0.02, f'{customers} customers\n₹{revenue:.0f}', 
                ha='center', va='bottom', fontweight='bold')
    
    # Plot 4: Production Cost Analysis (Maya's second piecewise example)
    # Production costs with different tiers
    production_volumes = np.arange(0, 600, 1)
    
    def production_cost_per_cup(volume):
        if volume <= 200:
            return 5
        elif volume <= 400:
            return 7
        else:
            return 10
    
    production_costs = np.array([production_cost_per_cup(v) for v in production_volumes])
    
    ax4.plot(production_volumes, production_costs, 'g-', linewidth=3, label='Cost per Cup')
    ax4.axvline(x=200, color='red', linestyle='--', alpha=0.7, label='200 cup threshold')
    ax4.axvline(x=400, color='orange', linestyle='--', alpha=0.7, label='400 cup threshold')
    
    ax4.set_xlabel('Daily Production (cups)')
    ax4.set_ylabel('Cost per Cup (₹)')
    ax4.set_title('Maya\'s Production Cost Structure')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Mathematical Representation
    st.header("🧮 Maya's Piecewise Equations")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Delivery Pricing Function:**
    
    Delivery Charge = {{
        ₹{short_charge}, if 0 ≤ distance ≤ {short_threshold} km
        ₹{medium_charge}, if {short_threshold} < distance ≤ {medium_threshold} km  
        ₹{long_charge}, if distance > {medium_threshold} km
    }}
    
    **Maya's Production Cost Function:**
    
    Cost per Cup = {{
        ₹5, if cups ≤ 200
        ₹7, if 200 < cups ≤ 400
        ₹10, if cups > 400
    }}
    
    **Key Features:**
    - **Different rules** for different ranges (pieces)
    - **Clear boundaries** at threshold points
    - **Step changes** rather than smooth curves
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Dashboard
    st.header("📊 Maya's Piecewise Business Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_delivery_revenue = np.mean([delivery_charge(d) for d in customer_distances])
        st.metric("Avg Delivery Revenue", f"₹{avg_delivery_revenue:.1f}", "per delivery")
    
    with col2:
        total_customers = len(customer_distances)
        st.metric("Sample Customers", f"{total_customers}", "this week")
    
    with col3:
        total_delivery_revenue = sum([delivery_charge(d) for d in customer_distances])
        st.metric("Total Delivery Revenue", f"₹{total_delivery_revenue:.0f}", "this week")
    
    with col4:
        most_common_zone = max(zone_names, key=lambda x: zone_customers[zone_names.index(x)])
        st.metric("Most Common Zone", most_common_zone, "highest volume")
    
    # Threshold Analysis Table
    st.header("🔍 Maya's Threshold Analysis")
    
    st.markdown('<div class="threshold-highlight">', unsafe_allow_html=True)
    st.subheader("Understanding Business Boundaries")
    
    # Create threshold analysis table
    threshold_data = []
    
    # Analyze different distance scenarios
    test_distances = [0.5, 1.5, 2.0, 2.1, 3.5, 5.0, 5.1, 7.5]
    
    for distance in test_distances:
        charge = delivery_charge(distance)
        
        if distance <= short_threshold:
            zone = "Short"
            reason = "Walking distance"
        elif distance <= medium_threshold:
            zone = "Medium" 
            reason = "Auto-rickshaw needed"
        else:
            zone = "Long"
            reason = "Significant travel time"
        
        threshold_data.append({
            'Distance (km)': distance,
            'Zone': zone,
            'Charge (₹)': charge,
            'Business Reason': reason,
            'At Boundary?': 'Yes' if distance in [short_threshold, medium_threshold] else 'No'
        })
    
    df_threshold = pd.DataFrame(threshold_data)
    st.dataframe(df_threshold, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Business Calculator
    st.header("🤔 Maya's Piecewise Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Delivery Charge Calculator")
        test_distance = st.number_input("Customer distance (km):", 
                                       min_value=0.0, max_value=15.0, value=3.5, step=0.1)
        
        calculated_charge = delivery_charge(test_distance)
        
        st.success(f"📍 Distance: {test_distance} km → **₹{calculated_charge} delivery charge**")
        
        # Show which rule was used
        if test_distance <= short_threshold:
            st.info(f"✅ Used **Short Distance Rule** (0 to {short_threshold} km)")
            st.write("🚶 Maya can walk this distance easily")
        elif test_distance <= medium_threshold:
            st.info(f"✅ Used **Medium Distance Rule** ({short_threshold} to {medium_threshold} km)")
            st.write("🛺 Maya needs auto-rickshaw for this distance")
        else:
            st.info(f"✅ Used **Long Distance Rule** (over {medium_threshold} km)")
            st.write("🚌 Significant time and transport cost required")
    
    with col2:
        st.subheader("🏭 Production Cost Calculator")
        production_volume = st.number_input("Daily production (cups):", 
                                           min_value=0, max_value=600, value=350, step=10)
        
        cost_per_cup = production_cost_per_cup(production_volume)
        
        # Calculate total cost using piecewise logic
        total_cost = 0
        if production_volume <= 200:
            total_cost = production_volume * 5
        elif production_volume <= 400:
            total_cost = 200 * 5 + (production_volume - 200) * 7
        else:
            total_cost = 200 * 5 + 200 * 7 + (production_volume - 400) * 10
        
        st.success(f"🏭 {production_volume} cups → **₹{cost_per_cup}/cup, ₹{total_cost} total**")
        
        # Show the breakdown
        if production_volume <= 200:
            st.info("✅ **Low Volume Tier** - All cups at ₹5 each")
        elif production_volume <= 400:
            st.info("✅ **Medium Volume Tier** - First 200 at ₹5, rest at ₹7")
            st.write(f"Breakdown: 200×₹5 + {production_volume-200}×₹7 = ₹{total_cost}")
        else:
            st.info("✅ **High Volume Tier** - Three different rates")
            st.write(f"Breakdown: 200×₹5 + 200×₹7 + {production_volume-400}×₹10 = ₹{total_cost}")
    
    # Business Insights
    st.header("💡 Piecewise Function Insights")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Why Piecewise Makes Sense")
        st.write("**Business reality isn't smooth:**")
        st.write("• Transportation costs jump at certain distances")
        st.write("• Production efficiency changes at volume thresholds")  
        st.write("• Different situations require different strategies")
        st.write("• Clear rules help consistent decision-making")
        
        st.subheader("📈 Threshold Effects")
        st.write("**Business behavior changes at specific points:**")
        st.write(f"• At {short_threshold} km: Walking → Auto-rickshaw")
        st.write(f"• At {medium_threshold} km: Auto → Long-distance transport")
        st.write("• At 200 cups: Normal work → Overtime needed")
        st.write("• At 400 cups: Overtime → Extra staff needed")
    
    with col2:
        st.subheader("🏢 Real-World Piecewise Examples")
        st.write("**Common business applications:**")
        st.write("• **Tax brackets** - different rates for income ranges")
        st.write("• **Shipping costs** - different rates for weight ranges")
        st.write("• **Bulk discounts** - different prices for quantity ranges")
        st.write("• **Salary structures** - different bonus rates for performance")
        st.write("• **Utility bills** - different rates for usage levels")
        
        st.subheader("🚨 Maya's Strategic Insights")
        st.write("**Maya now understands:**")
        st.write("• How to set clear, fair pricing boundaries")
        st.write("• When business rules need to change")
        st.write("• How to plan for different volume scenarios")
        st.write("• Why one-size-fits-all doesn't work")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Piecewise Story")
    
    with st.expander("📝 Exercise 1: Maya's Expanded Delivery Zones"):
        st.markdown(f"""
        Maya wants to expand her delivery service. She's considering adding two new zones:
        - **Extra Short (0-1 km):** ₹5 (premium nearby service)
        - **Extra Long (8+ km):** ₹75 (far suburbs)
        
        Current system: 0-{short_threshold}km→₹{short_charge}, {short_threshold}-{medium_threshold}km→₹{medium_charge}, {medium_threshold}+km→₹{long_charge}
        
        **Questions:**
        1. Write the new 5-zone piecewise function
        2. How would revenue change for a customer 9km away?
        3. What's the charge for customers at exactly 1km, 2km, 5km, and 8km?
        """)
        
        if st.button("Show Solutions", key="ex1_piece"):
            st.markdown(f"""
            **Solutions:**
            
            1. **New 5-zone piecewise function:**
            
            Delivery Charge = {{
                ₹5, if 0 ≤ distance ≤ 1 km
                ₹{short_charge}, if 1 < distance ≤ {short_threshold} km
                ₹{medium_charge}, if {short_threshold} < distance ≤ {medium_threshold} km
                ₹{long_charge}, if {medium_threshold} < distance ≤ 8 km
                ₹75, if distance > 8 km
            }}
            
            2. **Revenue change for 9km customer:**
               - Old system: ₹{long_charge} (long distance rule)
               - New system: ₹75 (extra long rule)
               - **Increase: ₹{75 - long_charge}** per delivery
            
            3. **Charges at boundary points:**
               - **1 km exactly:** ₹5 (extra short zone)
               - **2 km exactly:** ₹{short_charge} (short zone) 
               - **5 km exactly:** ₹{medium_charge} (medium zone)
               - **8 km exactly:** ₹{long_charge} (long zone)
            
            **Business insight:** Boundary definitions matter! Maya needs to decide if "exactly at boundary" goes in lower or higher tier.
            """)
    
    with st.expander("📝 Exercise 2: Maya's Volume Discount Strategy"):
        st.markdown("""
        Maya wants to offer bulk discounts for large tea orders. She's considering:
        
        **Current pricing:** ₹15 per cup for any quantity
        **Proposed piecewise pricing:**
        - 1-50 cups: ₹15 per cup (regular price)
        - 51-100 cups: ₹13 per cup (small bulk discount)  
        - 101+ cups: ₹11 per cup (large bulk discount)
        
        **Questions:**
        1. Calculate total cost for orders of 30, 75, and 150 cups
        2. At what order size does the customer save ₹100+ compared to regular pricing?
        3. How much revenue does Maya lose on a 200-cup order vs regular pricing?
        """)
        
        if st.button("Show Solutions", key="ex2_piece"):
            def bulk_price_total(cups):
                if cups <= 50:
                    return cups * 15
                elif cups <= 100:
                    return 50 * 15 + (cups - 50) * 13
                else:
                    return 50 * 15 + 50 * 13 + (cups - 100) * 11
            
            regular_price_total = lambda cups: cups * 15
            
            # Calculate for different quantities
            orders = [30, 75, 150, 200]
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Total costs with bulk pricing:**""")
            
            for order in orders[:3]:
                bulk_total = bulk_price_total(order)
                regular_total = regular_price_total(order)
                savings = regular_total - bulk_total
                
                if order <= 50:
                    breakdown = f"{order} × ₹15"
                elif order <= 100:
                    breakdown = f"50×₹15 + {order-50}×₹13"
                else:
                    breakdown = f"50×₹15 + 50×₹13 + {order-100}×₹11"
                
                st.write(f"   - **{order} cups:** {breakdown} = **₹{bulk_total}** (saves ₹{savings})")
            
            # Find when savings reach ₹100
            target_savings = 100
            cups_for_100_savings = None
            
            for cups in range(51, 200):
                savings = regular_price_total(cups) - bulk_price_total(cups)
                if savings >= target_savings and cups_for_100_savings is None:
                    cups_for_100_savings = cups
                    break
            
            # Revenue loss on 200-cup order
            bulk_200 = bulk_price_total(200)
            regular_200 = regular_price_total(200)
            revenue_loss = regular_200 - bulk_200
            
            st.markdown(f"""
            2. **₹100+ savings threshold:**
               - Customer saves ₹100+ starting at **{cups_for_100_savings} cups**
               - At this point: Regular = ₹{regular_price_total(cups_for_100_savings)}, Bulk = ₹{bulk_price_total(cups_for_100_savings)}, Savings = ₹{regular_price_total(cups_for_100_savings) - bulk_price_total(cups_for_100_savings)}
            
            3. **Maya's revenue loss on 200-cup order:**
               - Regular pricing: ₹{regular_200}
               - Bulk pricing: ₹{bulk_200}
               - **Revenue loss: ₹{revenue_loss}** (but potentially gains customer loyalty!)
            
            **Business insight:** Piecewise discounts can drive larger orders but reduce per-unit margins!
            """)
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Piecewise Functions in Maya's Business:**
    
    1. **Different Rules for Different Situations:** Real business problems often require multiple approaches, not one simple rule
    2. **Threshold Effects:** Business behavior changes at specific boundary points (distance, volume, time)
    3. **Step Changes:** Some costs and prices jump in steps rather than changing smoothly
    4. **Clear Decision Making:** Well-defined ranges help make consistent, fair business decisions
    5. **Range-Based Strategy:** Different customer segments or volume levels may need different treatment
    6. **Boundary Management:** Careful definition of "exactly at threshold" cases prevents confusion
    
    **Maya's Transformation:** From one-size-fits-all thinking to sophisticated, situation-appropriate business rules!
    
    **The Power:** Piecewise functions help businesses handle complexity by breaking it into clear, manageable pieces!
    """)
    
    # Navigation
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("← Logarithmic Functions"):
            st.session_state.page = 'algebra_logarithmic'
            st.rerun()
    
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with nav_col3:
        if st.button("Inverse Functions →"):
            st.session_state.page = 'algebra_inverse'
            st.rerun()