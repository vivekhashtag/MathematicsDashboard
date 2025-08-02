import streamlit as st
# Add import at the top
#from modules.pdf_generator import show_pdf_download_center


def show_algebra_overview():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("🔢 Algebra - Business Applications")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra**")
    
    # Introduction
    st.markdown("""
    Welcome to the Algebra module! Follow **Maya's complete business journey** from a small tea stall owner 
    to a sophisticated business strategist. Each topic builds on the previous one, showing how mathematical 
    concepts solve real business challenges through interactive examples and practical insights.
    """)
    
    st.markdown("---")
    
    # Progress tracker
    st.subheader("📊 Your Progress")
    progress_col1, progress_col2, progress_col3 = st.columns(3)
    
    with progress_col1:
        st.metric("Topics Available", "6")
    with progress_col2:
        st.metric("Completed", "0")  # This could be dynamic later
    with progress_col3:
        st.metric("Progress", "0%")  # This could be dynamic later
    
    st.markdown("---")
    
    # Maya's Story Arc
    st.header("📖 Maya's Complete Business Journey")
    st.markdown("""
    **Meet Maya!** She runs a small tea stall near Mumbai railway station. Through her business challenges, 
    you'll discover how algebra powers real-world decision making. Each mathematical concept emerges naturally 
    from her evolving business needs.
    """)
    
    st.markdown("---")
    
    # Topic cards data - Updated with actual content
    algebra_topics = [
        {
            "title": "📈 Linear Functions & Equations",
            "subtitle": "Maya's Tea Stall Profit Analysis",
            "description": "Maya discovers how her profit changes with sales volume. Learn about fixed costs, variable costs, break-even analysis, and why every additional cup matters for her bottom line.",
            "business_scenario": "Basic profit analysis and break-even planning",
            "key_concepts": ["Slope (profit per cup)", "Y-intercept (fixed costs)", "Break-even point", "Linear relationships"],
            "maya_learns": "How to predict profit for any sales volume and find her break-even point",
            "page_key": "algebra_linear"
        },
        {
            "title": "📊 Quadratic Functions",
            "subtitle": "Maya's 7-Week Pricing Experiment",
            "description": "Maya runs a pricing experiment and discovers the 'sweet spot' - why there's an optimal price that maximizes sales, and how moving too far in either direction hurts business.",
            "business_scenario": "Pricing optimization and finding the perfect balance",
            "key_concepts": ["Parabolas and curves", "Vertex (optimal point)", "Sweet spot pricing", "Two prices, same sales"],
            "maya_learns": "Why pricing isn't linear and how to find her optimal price point",
            "page_key": "algebra_quadratic"
        },
        {
            "title": "🌱 Exponential Functions",
            "subtitle": "Maya's Customer Growth Through Word-of-Mouth",
            "description": "Maya's customer base grows exponentially through word-of-mouth. Discover why 50% monthly growth creates explosive results and how to predict future growth patterns.",
            "business_scenario": "Understanding and predicting explosive business growth",
            "key_concepts": ["Compound growth", "Growth multipliers", "Doubling time", "Exponential acceleration"],
            "maya_learns": "How small growth rates become massive results over time",
            "page_key": "algebra_exponential"
        },
        {
            "title": "📉 Logarithmic Functions",
            "subtitle": "Maya's Tea-Making Skill Development",
            "description": "Maya practices to make tea faster but discovers diminishing returns - early improvements come easily, but mastery requires exponentially more effort. The mathematics of learning curves.",
            "business_scenario": "Skill development and understanding diminishing returns",
            "key_concepts": ["Diminishing returns", "Learning curves", "Logarithmic improvement", "Mastery costs"],
            "maya_learns": "Why getting better gets harder and how to set realistic improvement goals",
            "page_key": "algebra_logarithmic"
        },
        {
            "title": "🔗 Piecewise Functions",
            "subtitle": "Maya's Delivery Pricing and Production Rules",
            "description": "Maya creates different pricing rules for different delivery distances and discovers that real business often requires multiple strategies, not one-size-fits-all approaches.",
            "business_scenario": "Creating sophisticated, situation-appropriate business rules",
            "key_concepts": ["Different rules for different ranges", "Threshold effects", "Step changes", "Boundary definitions"],
            "maya_learns": "How to handle complexity by breaking it into clear, manageable pieces",
            "page_key": "algebra_piecewise"
        },
        {
            "title": "🔄 Inverse Functions",
            "subtitle": "Maya's Goal-Oriented Strategic Planning",
            "description": "Maya learns to think backwards - instead of 'If I charge X, what happens?' she asks 'If I want Y to happen, what should I charge?' The mathematics of reverse planning.",
            "business_scenario": "Working backward from goals to required actions",
            "key_concepts": ["Reverse thinking", "Goal-oriented planning", "Multiple solutions", "Strategic flexibility"],
            "maya_learns": "How to work backward from desired outcomes to required inputs",
            "page_key": "algebra_inverse"
        }
    ]
    
    # Display topic cards
    st.subheader("🎯 Maya's Learning Path")
    st.markdown("**Follow Maya's journey in order - each topic builds on the previous ones!**")
    
    for i, topic in enumerate(algebra_topics):
        with st.container():
            # Topic card with enhanced styling
            st.markdown("---")
            
            # Header with number and title
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {i+1}. {topic['title']}")
                st.markdown(f"**📖 Maya's Story:** {topic['subtitle']}")
                st.write(topic['description'])
                
                # What Maya learns
                st.markdown(f"**🎓 Maya Learns:** {topic['maya_learns']}")
                
                # Business scenario
                st.write(f"**🏢 Business Focus:** {topic['business_scenario']}")
                
                # Key concepts
                concepts_text = " • ".join(topic['key_concepts'])
                st.write(f"**🔑 Key Concepts:** {concepts_text}")
            
            with col2:
                st.write("")  # Spacing
                st.write("")  # Spacing
                
                # Start button with topic number
                if st.button(f"Start Topic {i+1}", key=f"topic_{i}"):
                    st.session_state.page = topic['page_key']
                    st.rerun()
                
                # Estimated time and difficulty
                st.write("⏱️ ~15-20 min")
                st.write("📊 Interactive")
                
                # Difficulty indicator
                if i == 0:
                    st.write("🟢 Beginner")
                elif i <= 2:
                    st.write("🟡 Intermediate")
                else:
                    st.write("🔴 Advanced")
    
    # Maya's Journey Summary
    st.markdown("---")
    st.header("🚀 Maya's Complete Transformation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Maya's Mathematical Evolution:**
        
        📈 **Starts with:** Basic profit questions  
        📊 **Discovers:** Optimal pricing strategies  
        🌱 **Experiences:** Explosive growth patterns  
        📉 **Learns:** Skill development reality  
        🔗 **Masters:** Complex business rules  
        🔄 **Achieves:** Strategic reverse planning  
        """)
    
    with col2:
        st.markdown("""
        **From Tea Stall Owner to Business Strategist:**
        
        ✅ **Linear thinking** → Understanding basic relationships  
        ✅ **Optimization** → Finding sweet spots and maximums  
        ✅ **Growth prediction** → Forecasting exponential patterns  
        ✅ **Learning management** → Realistic improvement planning  
        ✅ **Complex rules** → Sophisticated decision frameworks  
        ✅ **Goal achievement** → Working backward from targets  
        """)
    
    # Learning Tips
    st.markdown("---")
    st.markdown("""
    ### 💡 Learning Tips for Maya's Journey:
    
    **🎯 Recommended Path:**
    - **Start with Linear Functions** - Maya's foundation story that introduces her business
    - **Follow the sequence** - Each topic builds on previous mathematical concepts
    - **Use the interactive sliders** - See how changing parameters affects Maya's business
    - **Focus on Maya's insights** - Understand what the math means for her decisions
    - **Complete the practice exercises** - Apply the concepts to new scenarios
    
    **📚 Study Strategy:**
    - **Take notes** on Maya's key discoveries and business applications
    - **Pause between topics** to let concepts sink in
    - **Try different slider values** to see how Maya's business changes
    - **Think about your own business** - How could these concepts apply?
    """)
    
    # Quick Navigation
    st.markdown("### 🚀 Quick Topic Access:")
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    
    with nav_col1:
        if st.button("📈 Start: Linear Functions", key="quick_linear"):
            st.session_state.page = 'algebra_linear'
            st.rerun()
        
        if st.button("🌱 Topic 3: Exponential", key="quick_exp"):
            st.session_state.page = 'algebra_exponential'
            st.rerun()
    
    with nav_col2:
        if st.button("📊 Topic 2: Quadratic", key="quick_quad"):
            st.session_state.page = 'algebra_quadratic'
            st.rerun()
            
        if st.button("📉 Topic 4: Logarithmic", key="quick_log"):
            st.session_state.page = 'algebra_logarithmic'
            st.rerun()
    
    with nav_col3:
        if st.button("🔗 Topic 5: Piecewise", key="quick_piece"):
            st.session_state.page = 'algebra_piecewise'
            st.rerun()
            
        if st.button("🔄 Topic 6: Inverse", key="quick_inv"):
            st.session_state.page = 'algebra_inverse'
            st.rerun()
    
    # Success Message
    st.markdown("---")
    st.success("""
    🎉 **Ready to Begin Maya's Journey?**
    
    Start with **Linear Functions** to meet Maya and understand her basic business challenges. 
    Each topic will reveal new mathematical tools that help Maya make better business decisions. 
    
    By the end, you'll have followed Maya from a simple tea stall owner to a sophisticated 
    business strategist who uses algebra to solve complex real-world problems!
    """)
    
    st.markdown("---")