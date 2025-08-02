import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64
from datetime import datetime

def create_pdf_report(selling_price, cost_per_pizza, fixed_costs, profit_per_pizza, break_even_point):
    """Create a PDF report with the current analysis"""
    
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'Pizza Palace - Linear Functions Analysis Report', 0, 1, 'C')
            self.ln(10)
        
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 0, 'C')
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    
    # Business Scenario
    pdf.cell(0, 10, 'Business Scenario: Pizza Palace Profit Analysis', 0, 1, 'L')
    pdf.ln(5)
    
    scenario_text = """Sarah owns Pizza Palace and wants to understand how her daily profit relates to pizza sales.
This analysis uses linear functions to model the relationship between sales volume and profitability."""
    
    pdf.multi_cell(0, 10, scenario_text)
    pdf.ln(5)
    
    # Parameters
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Current Business Parameters:', 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    
    pdf.cell(0, 8, f'• Selling Price per Pizza: ${selling_price}', 0, 1, 'L')
    pdf.cell(0, 8, f'• Cost per Pizza: ${cost_per_pizza}', 0, 1, 'L')
    pdf.cell(0, 8, f'• Daily Fixed Costs: ${fixed_costs}', 0, 1, 'L')
    pdf.cell(0, 8, f'• Profit per Pizza: ${profit_per_pizza}', 0, 1, 'L')
    pdf.ln(5)
    
    # Mathematical Model
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Linear Function Model:', 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    
    equation = f'Profit = {profit_per_pizza} × Pizzas Sold - {fixed_costs}'
    pdf.cell(0, 8, f'Equation: {equation}', 0, 1, 'L')
    
    if break_even_point != float('inf'):
        pdf.cell(0, 8, f'Break-even Point: {break_even_point:.1f} pizzas', 0, 1, 'L')
    else:
        pdf.cell(0, 8, 'Break-even Point: Not achievable with current pricing', 0, 1, 'L')
    
    pdf.ln(5)
    
    # Business Insights
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Key Business Insights:', 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    
    insights = [
        f'Each pizza sold contributes ${profit_per_pizza} to covering fixed costs and profit',
        f'Daily fixed costs of ${fixed_costs} must be covered before generating profit',
        'The linear relationship shows constant marginal profit per pizza',
        'Break-even analysis helps determine minimum daily sales targets'
    ]
    
    for insight in insights:
        pdf.multi_cell(0, 8, f'• {insight}')
    
    return pdf.output(dest='S').encode('latin-1')

def show_linear_functions():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("📈 Linear Functions & Equations")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra** > **Linear Functions**")
    
    # Business Storyline
    st.header("🏪 Business Storyline: Pizza Palace")
    
    with st.container():
        st.markdown("""
        **Meet Sarah, owner of Pizza Palace!** 
        
        Sarah wants to understand how her daily profit relates to the number of pizzas she sells. 
        She knows that each pizza costs her $4 to make (ingredients, labor), she sells each pizza for $12, 
        and she has fixed daily costs (rent, utilities, staff) of $200.
        
        **The Question:** How does her profit change with each pizza sold? What's her break-even point?
        """)
    
    # Mathematical Representation
    st.header("🧮 Mathematical Representation")
    
    with st.expander("📝 Click to see the mathematical breakdown"):
        st.markdown("""
        **Business Logic:**
        - Revenue per pizza = Selling Price
        - Cost per pizza = Ingredient & Labor Cost  
        - Profit per pizza = Revenue per pizza - Cost per pizza
        - Total Profit = (Profit per pizza × Number of pizzas) - Fixed Costs
        
        **Linear Equation:**
        ```
        Profit = (Selling Price - Cost per pizza) × Quantity - Fixed Costs
        P = (S - C) × Q - F
        ```
        
        This is a **linear function** because:
        - The relationship between pizzas sold (Q) and profit (P) is a straight line
        - The slope represents profit per additional pizza
        - The y-intercept represents the loss when no pizzas are sold (negative fixed costs)
        """)
    
    # Interactive Controls
    st.header("🎛️ Interactive Pizza Palace Simulator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selling_price = st.slider("Selling Price per Pizza ($)", 8, 20, 12, 1)
    
    with col2:
        cost_per_pizza = st.slider("Cost per Pizza ($)", 3, 10, 4, 1)
    
    with col3:
        fixed_costs = st.slider("Daily Fixed Costs ($)", 100, 500, 200, 50)
    
    # Calculate profit per pizza
    profit_per_pizza = selling_price - cost_per_pizza
    
    # Generate data for graph
    pizzas_sold = np.arange(0, 101, 1)
    total_profit = profit_per_pizza * pizzas_sold - fixed_costs
    
    # Break-even calculation
    if profit_per_pizza > 0:
        break_even_point = fixed_costs / profit_per_pizza
    else:
        break_even_point = float('inf')
    
    # Create the graph
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot profit line
    ax.plot(pizzas_sold, total_profit, 'b-', linewidth=3, label=f'Profit Line (${profit_per_pizza}/pizza)')
    
    # Add break-even point
    if break_even_point <= 100:
        ax.axvline(x=break_even_point, color='red', linestyle='--', linewidth=2, 
                  label=f'Break-even: {break_even_point:.1f} pizzas')
        ax.plot(break_even_point, 0, 'ro', markersize=10)
        ax.annotate(f'Break-even\n{break_even_point:.1f} pizzas', 
                   xy=(break_even_point, 0), xytext=(break_even_point + 15, 100),
                   arrowprops=dict(arrowstyle='->', color='red'),
                   fontsize=10, ha='center')
    
    # Add zero line
    ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    
    # Color areas
    ax.fill_between(pizzas_sold, total_profit, 0, where=(total_profit >= 0), 
                   alpha=0.3, color='green', label='Profit Zone')
    ax.fill_between(pizzas_sold, total_profit, 0, where=(total_profit < 0), 
                   alpha=0.3, color='red', label='Loss Zone')
    
    # Formatting
    ax.set_xlabel('Number of Pizzas Sold', fontsize=12)
    ax.set_ylabel('Daily Profit ($)', fontsize=12)
    ax.set_title('Pizza Palace: Daily Profit Analysis', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    
    # Set reasonable axis limits
    ax.set_xlim(0, 100)
    ax.set_ylim(-300, 500)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Download Report Button
    st.subheader("📄 Download Analysis Report")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("📥 Generate PDF Report"):
            try:
                pdf_bytes = create_pdf_report(selling_price, cost_per_pizza, fixed_costs, 
                                            profit_per_pizza, break_even_point)
                
                b64_pdf = base64.b64encode(pdf_bytes).decode()
                href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="pizza_palace_analysis.pdf">Click here to download PDF</a>'
                st.markdown(href, unsafe_allow_html=True)
                st.success("✅ PDF report generated! Click the link above to download.")
                
            except Exception as e:
                st.error("PDF generation requires fpdf2 library. Install with: pip install fpdf2")
    
    with col2:
        st.info("📊 The PDF report includes your current analysis, equations, and business insights for offline study.")
    
    # Business Insights
    st.header("💡 Business Insights & Key Metrics")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Profit per Pizza", f"${profit_per_pizza}", 
                 f"${profit_per_pizza - 8} vs base" if profit_per_pizza != 8 else None)
    
    with col2:
        if break_even_point != float('inf') and break_even_point > 0:
            st.metric("Break-even Point", f"{break_even_point:.1f} pizzas",
                     f"{break_even_point - 25:.1f}" if break_even_point < 50 else "High")
        else:
            st.metric("Break-even Point", "Never", "Fix pricing!")
    
    with col3:
        daily_50_pizzas = profit_per_pizza * 50 - fixed_costs
        st.metric("Profit at 50 pizzas/day", f"${daily_50_pizzas}")
    
    with col4:
        daily_100_pizzas = profit_per_pizza * 100 - fixed_costs
        st.metric("Profit at 100 pizzas/day", f"${daily_100_pizzas}")
    
    # Practice Exercises Section
    st.header("🎯 Practice Exercises")
    
    st.markdown("Test your understanding with these real-world scenarios:")
    
    # Exercise 1
    with st.expander("📝 Exercise 1: Break-even Analysis"):
        st.markdown("""
        **Scenario:** A coffee shop sells coffee at $5 per cup, with variable costs of $2 per cup and fixed costs of $180 per day.
        
        **Questions:**
        1. What is the profit per cup?
        2. What is the break-even point in cups per day?
        3. What would be the daily profit if they sell 80 cups?
        4. How many cups must they sell to make $300 profit per day?
        """)
        
        if st.button("Show Solutions", key="ex1_solution"):
            st.markdown("""
            **Solutions:**
            
            1. **Profit per cup:** $5 - $2 = $3 per cup
            
            2. **Break-even point:** Fixed costs ÷ Profit per cup = $180 ÷ $3 = 60 cups per day
            
            3. **Daily profit at 80 cups:** (80 × $3) - $180 = $240 - $180 = $60 profit
            
            4. **Cups needed for $300 profit:** 
               - Total needed revenue = $300 + $180 = $480
               - Cups needed = $480 ÷ $3 = 160 cups per day
            
            **Linear equation:** Profit = 3Q - 180 (where Q = cups sold)
            """)
    
    # Exercise 2
    with st.expander("📝 Exercise 2: Price Optimization"):
        st.markdown("""
        **Scenario:** A bakery currently sells bread at $4 per loaf, with costs of $1.50 per loaf and fixed costs of $120 per day. They're considering raising the price to $4.50.
        
        **Questions:**
        1. Calculate the current break-even point
        2. Calculate the new break-even point after price increase
        3. If they currently sell 60 loaves per day, what's the profit difference?
        4. What would happen if they reduced costs to $1.20 per loaf instead of raising prices?
        """)
        
        if st.button("Show Solutions", key="ex2_solution"):
            st.markdown("""
            **Solutions:**
            
            **Current Situation:**
            - Profit per loaf = $4.00 - $1.50 = $2.50
            - Break-even = $120 ÷ $2.50 = 48 loaves
            
            **After Price Increase to $4.50:**
            - New profit per loaf = $4.50 - $1.50 = $3.00
            - New break-even = $120 ÷ $3.00 = 40 loaves
            
            **Profit difference at 60 loaves:**
            - Current profit: (60 × $2.50) - $120 = $30
            - New profit: (60 × $3.00) - $120 = $60
            - Difference: $30 more profit per day
            
            **Cost reduction alternative:**
            - Profit per loaf = $4.00 - $1.20 = $2.80
            - Break-even = $120 ÷ $2.80 = 43 loaves
            - Profit at 60 loaves: (60 × $2.80) - $120 = $48
            
            **Conclusion:** Price increase gives better profit than cost reduction in this case.
            """)
    
    # Exercise 3
    with st.expander("📝 Exercise 3: Multi-Product Analysis"):
        st.markdown("""
        **Scenario:** A restaurant sells two items:
        - Burgers: $8 selling price, $3 cost, expecting to sell 40 per day
        - Fries: $3 selling price, $1 cost, expecting to sell 60 per day
        - Combined fixed costs: $200 per day
        
        **Questions:**
        1. What's the combined daily profit?
        2. What's the overall break-even point in total items?
        3. If burger sales drop to 30, how many fries must they sell to maintain the same profit?
        """)
        
        if st.button("Show Solutions", key="ex3_solution"):
            st.markdown("""
            **Solutions:**
            
            1. **Combined daily profit:**
               - Burger profit: (40 × ($8-$3)) = 40 × $5 = $200
               - Fries profit: (60 × ($3-$1)) = 60 × $2 = $120
               - Total profit: $200 + $120 - $200 (fixed) = $120 per day
            
            2. **Overall break-even analysis:**
               - Total items expected: 40 + 60 = 100 items
               - Average profit per item: ($200 + $120) ÷ 100 = $3.20
               - Break-even: $200 ÷ $3.20 = 62.5 items total
            
            3. **Maintaining profit with reduced burger sales:**
               - Lost burger profit: (40-30) × $5 = $50
               - Additional fries needed: $50 ÷ $2 = 25 more fries
               - Total fries needed: 60 + 25 = 85 fries per day
            
            **Key insight:** Different products have different profit margins - focus on high-margin items!
            """)
    
    # Key takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Linear Functions in Business:**
    1. **Slope = Marginal Impact** - How much profit changes per additional unit
    2. **Y-intercept = Fixed Component** - What happens at zero activity level  
    3. **X-intercept = Break-even** - Where total profit equals zero
    4. **Linear relationships** are common in cost analysis, pricing, and profit planning
    5. **Practice exercises** help apply concepts to real business decisions
    """)
    
    # Navigation buttons
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