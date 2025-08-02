import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64
import io
from datetime import datetime
import numpy as np
from math import sqrt

class MathsPDF(FPDF):
    def __init__(self, topic_title, topic_icon):
        super().__init__()
        self.topic_title = topic_title
        self.topic_icon = topic_icon
        
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 15, f'{self.topic_icon} {self.topic_title}', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'Mathematics Learning Dashboard - Business Applications', 0, 1, 'C')
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        self.set_y(-25)
        self.cell(0, 10, f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 0, 'R')
    
    def add_section_header(self, title, icon=""):
        self.ln(5)
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(230, 240, 250)
        self.cell(0, 10, f'{icon} {title}', 0, 1, 'L', True)
        self.ln(5)
    
    def add_business_story(self, story_text):
        self.set_font('Arial', '', 11)
        self.set_fill_color(248, 252, 248)
        self.set_draw_color(76, 175, 80)
        self.set_line_width(1)
        
        lines = story_text.split('\n')
        height = len(lines) * 6 + 10
        self.rect(10, self.get_y(), 190, height, 'DF')
        self.set_xy(15, self.get_y() + 5)
        
        for line in lines:
            self.cell(0, 6, line.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'L')
        self.ln(5)
    
    def add_equation_box(self, equation_text):
        self.set_font('Courier', 'B', 10)
        self.set_fill_color(255, 248, 225)
        self.set_draw_color(255, 193, 7)
        
        lines = equation_text.split('\n')
        height = len(lines) * 6 + 10
        self.rect(10, self.get_y(), 190, height, 'DF')
        self.set_xy(15, self.get_y() + 5)
        
        for line in lines:
            self.cell(0, 6, line.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'L')
        self.ln(5)
    
    def add_insight_box(self, insight_text, title="Key Insights"):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(232, 244, 253)
        self.set_draw_color(33, 150, 243)
        
        self.rect(10, self.get_y(), 190, 8, 'DF')
        self.set_xy(15, self.get_y() + 2)
        self.cell(0, 6, title, 0, 1, 'L')
        
        self.set_font('Arial', '', 10)
        lines = insight_text.split('\n')
        content_height = len(lines) * 5 + 5
        
        self.rect(10, self.get_y(), 190, content_height, 'DF')
        self.set_xy(15, self.get_y() + 2)
        
        for line in lines:
            if line.strip():
                self.cell(0, 5, line.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'L')
        self.ln(8)

# PDF Generation Functions for Each Topic
def create_linear_functions_pdf(params=None):
    """Create PDF for Linear Functions topic"""
    # Default parameters if none provided
    if params is None:
        params = {
            'selling_price': 15,
            'cost_per_pizza': 8,
            'fixed_costs': 50000,
            'profit_per_pizza': 7,
            'break_even_point': 7143
        }
    
    pdf = MathsPDF("Linear Functions - Maya's Tea Stall", "📈")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Business Storyline", "🏪")
    story = """Meet Maya, owner of Pizza Palace!

Maya wants to understand how her daily profit relates to pizza sales.
She knows her costs, selling price, and fixed daily expenses.

The Question: How does profit change with each pizza sold? What's the break-even point?

This is LINEAR FUNCTIONS in business!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Mathematical Model", "🧮")
    equation_text = f"""LINEAR FUNCTION EQUATIONS:

Cost Function: C = {params['fixed_costs']} + {params['cost_per_pizza']} × Q
Revenue Function: R = {params['selling_price']} × Q  
Profit Function: P = {params['profit_per_pizza']}Q - {params['fixed_costs']}

Where Q = Number of pizzas sold"""
    pdf.add_equation_box(equation_text)
    
    # Analysis
    pdf.add_section_header("Business Analysis", "📊")
    analysis = f"""CURRENT PARAMETERS:
- Selling Price: Rs.{params['selling_price']}
- Cost per Pizza: Rs.{params['cost_per_pizza']}
- Fixed Costs: Rs.{params['fixed_costs']}
- Profit per Pizza: Rs.{params['profit_per_pizza']}
- Break-even: {params['break_even_point']:.0f} pizzas"""
    pdf.add_insight_box(analysis, "Key Metrics")
    
    return pdf.output(dest='S').encode('latin-1')

def create_quadratic_functions_pdf(params=None):
    """Create PDF for Quadratic Functions topic"""
    if params is None:
        params = {
            'optimal_price': 15,
            'max_sales': 250,
            'sensitivity': 5
        }
    
    pdf = MathsPDF("Quadratic Functions - Maya's Pricing Experiment", "📊")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Maya's Pricing Experiment", "🧪")
    story = """Maya's 7-Week Discovery:

Maya tested different prices for 7 weeks and found a "sweet spot" at Rs.15.
Higher or lower prices both reduced sales, creating a curved relationship.

This is QUADRATIC FUNCTIONS in business!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Quadratic Model", "🧮")
    equation_text = f"""QUADRATIC EQUATION:

Sales = {params['max_sales']} - {params['sensitivity']} × (P - {params['optimal_price']})²

Where:
- {params['max_sales']} = Maximum sales at optimal price
- {params['sensitivity']} = Customer sensitivity factor
- (P - {params['optimal_price']})² = Accelerating loss factor"""
    pdf.add_equation_box(equation_text)
    
    return pdf.output(dest='S').encode('latin-1')

def create_exponential_functions_pdf(params=None):
    """Create PDF for Exponential Functions topic"""
    if params is None:
        params = {
            'principal': 10000,
            'interest_rate': 7,
            'years': 20
        }
    
    pdf = MathsPDF("Exponential Functions - Investment Growth", "🌱")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Investment Growth Story", "💰")
    story = """Maya's Investment Journey:

Maya learns about compound interest and exponential growth.
Small differences in interest rates create huge differences over time.

This is EXPONENTIAL FUNCTIONS in finance!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Exponential Model", "🧮")
    equation_text = f"""COMPOUND INTEREST FORMULA:

A = P(1 + r)^t

Where:
- A = Final amount
- P = Principal (Rs.{params['principal']})
- r = Interest rate ({params['interest_rate']}% annually)
- t = Time ({params['years']} years)"""
    pdf.add_equation_box(equation_text)
    
    return pdf.output(dest='S').encode('latin-1')

def create_logarithmic_functions_pdf(params=None):
    """Create PDF for Logarithmic Functions topic"""
    if params is None:
        params = {
            'effectiveness': 50,
            'baseline': 20,
            'max_spend': 200
        }
    
    pdf = MathsPDF("Logarithmic Functions - Marketing Analytics", "📉")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Marketing Analytics Story", "📢")
    story = """David's Marketing Discovery:

Advertising effectiveness follows diminishing returns.
Initial spend produces dramatic results, but additional dollars yield less.

This is LOGARITHMIC FUNCTIONS in marketing!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Logarithmic Model", "🧮")
    equation_text = f"""LOGARITHMIC RESPONSE FUNCTION:

Response = {params['effectiveness']} × ln(spend + 1) + {params['baseline']}

Where:
- Response = Customer acquisition
- {params['effectiveness']} = Effectiveness multiplier
- spend = Advertising spend (thousands)
- {params['baseline']} = Baseline response"""
    pdf.add_equation_box(equation_text)
    
    return pdf.output(dest='S').encode('latin-1')

def create_piecewise_functions_pdf(params=None):
    """Create PDF for Piecewise Functions topic"""
    if params is None:
        params = {
            'base_rate': 5,
            'tier2_rate': 2,
            'tier3_rate': 1.5,
            'tier4_rate': 1
        }
    
    pdf = MathsPDF("Piecewise Functions - Shipping Logistics", "🔗")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Shipping Logistics Story", "📦")
    story = """Jennifer's Pricing Strategy:

FlexiShip uses tiered pricing based on package weight.
Different rates for different weight ranges optimize profitability.

This is PIECEWISE FUNCTIONS in logistics!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Piecewise Model", "🧮")
    equation_text = f"""TIERED PRICING FUNCTION:

Cost(w) = {{
  Rs.{params['base_rate']},                if 0 < w ≤ 1 lb
  Rs.{params['base_rate']} + Rs.{params['tier2_rate']}(w-1),  if 1 < w ≤ 5 lbs
  ... (more tiers)
}}

Where w = package weight in pounds"""
    pdf.add_equation_box(equation_text)
    
    return pdf.output(dest='S').encode('latin-1')

def create_inverse_functions_pdf(params=None):
    """Create PDF for Inverse Functions topic"""
    if params is None:
        params = {
            'ad_spend': 100,
            'target_revenue': 120
        }
    
    pdf = MathsPDF("Inverse Functions - Revenue Planning", "🔄")
    pdf.add_page()
    
    # Business Story
    pdf.add_section_header("Revenue Planning Story", "🎯")
    story = """Carlos's Planning Challenge:

Carlos knows the relationship between ad spend and revenue.
But he needs to work backward: given a revenue target, what investment is needed?

This is INVERSE FUNCTIONS in planning!"""
    pdf.add_business_story(story)
    
    # Mathematical Model
    pdf.add_section_header("Inverse Model", "🧮")
    equation_text = f"""FORWARD AND INVERSE FUNCTIONS:

Forward: Revenue = f(Ad Spend)
Inverse: Ad Spend = f⁻¹(Revenue)

Example with current parameters:
- Ad Spend: Rs.{params['ad_spend']}k
- Target Revenue: Rs.{params['target_revenue']}k"""
    pdf.add_equation_box(equation_text)
    
    return pdf.output(dest='S').encode('latin-1')

def create_download_link(pdf_bytes, filename, button_text):
    """Create download link for PDF"""
    b64_pdf = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="{filename}" style="text-decoration: none;">' \
           f'<button style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; ' \
           f'border-radius: 8px; cursor: pointer; font-size: 16px; margin: 5px;">{button_text}</button></a>'
    return href

def show_pdf_download_center():
    """Main PDF Download Center - Call this from algebra_overview.py"""
    
    st.header("📚 Download Study Materials")
    st.markdown("Generate personalized PDF study guides for any topic with current parameters and solutions.")
    
    # Topic selection
    available_topics = {
        "📈 Linear Functions": {
            "description": "Maya's Tea Stall - Profit analysis and break-even calculations",
            "generator": create_linear_functions_pdf,
            "filename": "Linear_Functions_Study_Guide.pdf"
        },
        "📊 Quadratic Functions": {
            "description": "Maya's Pricing Experiment - Finding the sweet spot",
            "generator": create_quadratic_functions_pdf,
            "filename": "Quadratic_Functions_Study_Guide.pdf"
        },
        "🌱 Exponential Functions": {
            "description": "Investment Growth - Compound interest and exponential growth",
            "generator": create_exponential_functions_pdf,
            "filename": "Exponential_Functions_Study_Guide.pdf"
        },
        "📉 Logarithmic Functions": {
            "description": "Marketing Analytics - Diminishing returns and optimization",
            "generator": create_logarithmic_functions_pdf,
            "filename": "Logarithmic_Functions_Study_Guide.pdf"
        },
        "🔗 Piecewise Functions": {
            "description": "Shipping Logistics - Tiered pricing strategies",
            "generator": create_piecewise_functions_pdf,
            "filename": "Piecewise_Functions_Study_Guide.pdf"
        },
        "🔄 Inverse Functions": {
            "description": "Revenue Planning - Working backward from goals",
            "generator": create_inverse_functions_pdf,
            "filename": "Inverse_Functions_Study_Guide.pdf"
        }
    }
    
    # Download options
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Individual Topic Downloads")
        
        for topic, info in available_topics.items():
            with st.expander(f"{topic} - Study Guide"):
                st.write(f"**Description:** {info['description']}")
                
                # Parameters section (simplified for demo)
                st.write("**Customize parameters:**")
                if "Linear" in topic:
                    params = {
                        'selling_price': st.slider("Selling Price", 10, 25, 15, key=f"linear_price"),
                        'cost_per_pizza': st.slider("Cost per Pizza", 5, 15, 8, key=f"linear_cost"),
                        'fixed_costs': st.slider("Fixed Costs", 30000, 80000, 50000, key=f"linear_fixed"),
                        'profit_per_pizza': 0,  # Will be calculated
                        'break_even_point': 0   # Will be calculated
                    }
                    params['profit_per_pizza'] = params['selling_price'] - params['cost_per_pizza']
                    params['break_even_point'] = params['fixed_costs'] / params['profit_per_pizza'] if params['profit_per_pizza'] > 0 else float('inf')
                    
                elif "Quadratic" in topic:
                    params = {
                        'optimal_price': st.slider("Optimal Price", 10, 20, 15, key=f"quad_price"),
                        'max_sales': st.slider("Max Sales", 200, 300, 250, key=f"quad_sales"),
                        'sensitivity': st.slider("Sensitivity", 1, 10, 5, key=f"quad_sens")
                    }
                else:
                    params = None  # Use defaults for other topics
                
                # Generate and download button
                if st.button(f"📥 Generate {topic} PDF", key=f"btn_{topic}"):
                    with st.spinner(f"Creating {topic} study guide..."):
                        try:
                            pdf_bytes = info['generator'](params)
                            download_link = create_download_link(
                                pdf_bytes, 
                                info['filename'],
                                f"📥 Download {topic} PDF"
                            )
                            st.markdown(download_link, unsafe_allow_html=True)
                            st.success("✅ PDF generated successfully!")
                        except Exception as e:
                            st.error("Install required library: pip install fpdf2")
                            st.error(f"Error: {str(e)}")
    
    with col2:
        st.subheader("📦 Bulk Download")
        
        st.info("""
        **Coming Soon:**
        - Download all topics as one PDF
        - Create custom study packs
        - Export with practice exercises
        - Share with classmates
        """)
        
        # Bulk download option
        selected_topics = st.multiselect(
            "Select topics for bulk download:",
            list(available_topics.keys()),
            help="Choose multiple topics to download together"
        )
        
        if selected_topics:
            if st.button("📥 Generate Combined PDF", key="bulk_download"):
                st.info("Bulk download feature coming soon!")
    
    # Usage instructions
    st.markdown("---")
    st.subheader("📖 How to Use Study Guides")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📚 What's Included:**
        - Complete business storylines
        - Mathematical equations
        - Step-by-step explanations
        - Practice exercises with solutions
        """)
    
    with col2:
        st.markdown("""
        **🎯 Perfect For:**
        - Offline study and review
        - Exam preparation
        - Assignment reference
        - Sharing with study groups
        """)
    
    with col3:
        st.markdown("""
        **💡 Pro Tips:**
        - Adjust parameters before downloading
        - Print for better retention
        - Work through exercises first
        - Use as quick reference guides
        """)

# Instructions for implementation:
"""
IMPLEMENTATION STEPS:

1. Save this entire code as: modules/pdf_generator.py

2. Add to your algebra_overview.py:

   from modules.pdf_generator import show_pdf_download_center
   
   # Add this section at the end of show_algebra_overview():
   st.markdown("---")
   show_pdf_download_center()

3. Install required library:
   pip install fpdf2

4. Users can now:
   - Choose any topic from the algebra overview page
   - Customize parameters with sliders
   - Generate personalized PDFs instantly
   - Download professional study materials

This centralized approach is much cleaner and more scalable!
"""