import streamlit as st

def show_homepage():
    # Main Title
    st.title("📊 Mathematics Learning Dashboard")
    st.subheader("Learn Mathematics through Real Business Applications")
    st.markdown("Have a great learning experience - [Vivek Dhandapani](https://www.linkedin.com/in/vivekdhandapani)")
    
    # Introduction
    st.info("""
    🎯 **Our Approach:** Transform abstract mathematical concepts into practical business scenarios 
    that make sense in the real world. Each topic includes interactive examples, visual representations, 
    and actionable business insights.
    """)
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Learning Modules", "5")
    
    with col2:
        st.metric("Business Scenarios", "25+")
    
    with col3:
        st.metric("Interactive Examples", "∞")
    
    with col4:
        st.metric("Practical Focus", "100%")
    
    st.markdown("---")
    
    # Main Content Area
    st.header("🚀 Choose Your Learning Path")
    
    # Division data
    divisions_data = [
        {
            "title": "🔢 Algebra",
            "description": "Master linear equations, quadratic functions, and systems through business profit analysis, cost optimization, and investment planning scenarios.",
            "topics": ["Linear Functions", "Quadratic Functions", "Exponential Growth", "Logarithmic Functions", "Piecewise Functions", "Inverse Functions", "Systems of Equations"],
            "status": "available",
            "business_applications": "Profit Analysis, Cost Optimization, Revenue Planning"
        },
        {
            
    "title": "📐 Linear Algebra", 
    "description": "Explore matrices and vectors through portfolio management, supply chain optimization, and data transformation business cases.",
    "topics": ["Vectors & Matrices", "Eigenvalues & Eigenvectors", "Principal Component Analysis"],  # Updated topics
    "status": "available",  # CHANGED FROM "coming_soon"
    "business_applications": "Customer Analytics, Data Patterns, Dimensionality Reduction"  # Updated applications

        },
        {
            "title": "📈 Calculus",
            "description": "Understand derivatives and integrals through marginal analysis, optimization problems, and growth rate calculations in business contexts.",
            "topics": ["Limits", "Derivatives", "Integrals", "Optimization", "Applications"],
            "status": "available", 
            "business_applications": "Marginal Analysis, Rate Optimization, Growth Modeling"
        },
        {
            "title": "🔄 Series & Sequences",
            "description": "Learn arithmetic and geometric progressions through compound interest, loan calculations, and recurring business pattern analysis.",
            "topics": ["Arithmetic Series", "Geometric Series", "Power Series", "Convergence"],
            "status": "available",
            "business_applications": "Financial Planning, Loan Analysis, Growth Projections"
        },
        {
            "title": "⚡ Optimization",
            "description": "Apply mathematical optimization to resource allocation, production planning, and strategic decision-making scenarios.",
            "topics": ["Linear Programming", "Nonlinear Optimization", "Constraint Problems", "Game Theory"],
            "status": "available",
            "business_applications": "Resource Allocation, Production Planning, Strategy"
        }
    ]
    
    # Display division cards using Streamlit's built-in components
    for division in divisions_data:
        with st.container():
            # Create a bordered container for each division
            st.markdown("---")
            
            # Title and description
            st.subheader(division['title'])
            st.write(division['description'])
            
            # Topics in columns
            st.write("**📚 Topics Covered:**")
            topic_text = " | ".join(division['topics'])
            st.write(topic_text)
            
            # Business applications
            st.write("**🏢 Business Applications:**")
            st.write(f"*{division['business_applications']}*")
            
            # Status and button
            col1, col2 = st.columns([1, 3])
            
            with col1:
                if division["status"] == "available":
                    st.success("✅ Available Now")
                    if st.button(f"Start Learning", key=f"btn_{division['title']}"):
                            # ADD THIS CONDITION:
                        if "Linear Algebra" in division['title']:
                            st.session_state.page = "linear_algebra"
                        elif "Calculus" in division['title']:
                            st.session_state.page = "calculus"  # Route to calculus overview
                        # Add elif condition in button handler:
                        elif "Series" in division['title']:
                            st.session_state.page = "series_sequences"
                        elif "Optimization" in division['title']:
                            st.session_state.page = "optimization"
                        else:
                            st.session_state.page = "algebra"  # Existing algebra route
                            st.rerun()
                else:
                    st.warning("🚧 Coming Soon")
            
            with col2:
                if division["status"] == "available":
                    st.write("Click 'Start Learning' to begin with interactive business scenarios!")
                else:
                    st.write("This module is under development. Stay tuned!")
    
    # Footer section
    st.markdown("---")
    st.markdown("""
    ### 🎓 Learning Philosophy
    
    *"Mathematics is not about numbers, equations, computations, or algorithms: 
    it is about understanding business problems and making informed decisions."*
    
    **Start with Algebra to build your foundation, then progress through advanced topics!**
    """)

    # After your existing divisions_data loop, add this special section:

    st.markdown("---")
    st.header("🚀 Complete Your Journey")

    # Special capstone section
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("🌟 The Mathematical Evolution - From Formulas to AI")
        st.write("""
        Discover how your mathematical foundation leads naturally to Statistics and Machine Learning. 
        See the complete journey from pure mathematics to intelligent systems and AI applications.
        """)
        
        st.write("**🎯 What You'll Discover:**")
        st.write("Mathematics → Statistics → Machine Learning → Artificial Intelligence")
        
        st.info("Perfect capstone to complete your mathematical learning journey!")

    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        
        if st.button("🚀 Explore the Evolution", key="evolution_btn"):
            st.session_state.page = 'mathematical_evolution'
            st.rerun()
        
        st.write("⏱️ ~15-20 min")
        st.write("🎓 Inspirational")
        st.write("🌟 Vision & Roadmap")