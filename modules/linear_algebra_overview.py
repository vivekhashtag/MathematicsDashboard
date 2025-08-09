import streamlit as st

def show_linear_algebra_overview():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("📐 Linear Algebra - Data Analytics Applications")
    
    # Breadcrumb
    st.markdown("**Home** > **Linear Algebra**")
    
    # Introduction
    st.markdown("""
    Welcome to the Linear Algebra module! Follow **Arjun's transformation** from a struggling data consultant 
    to a powerful analytics expert. Discover how Linear Algebra unlocks the secrets hidden in multi-dimensional 
    business data through practical examples and interactive visualizations.
    """)
    
    st.markdown("---")
    
    # Progress tracker
    st.subheader("📊 Your Progress")
    progress_col1, progress_col2, progress_col3 = st.columns(3)
    
    with progress_col1:
        st.metric("Topics Available", "3")
    with progress_col2:
        st.metric("Completed", "0")  # This could be dynamic later
    with progress_col3:
        st.metric("Progress", "0%")  # This could be dynamic later
    
    st.markdown("---")
    
    # Arjun's Story Arc
    st.header("📖 Arjun's Data Analytics Journey")
    st.markdown("""
    **Meet Arjun!** He runs a small data analytics consultancy in Bangalore, helping local businesses 
    understand their data. But he's overwhelmed by complex multi-dimensional problems. Through Linear Algebra, 
    he'll discover mathematical tools that transform raw data into actionable business insights.
    """)
    
    st.markdown("---")
    
    # Topic cards data
    linear_algebra_topics = [
        {
            "title": "📊 Vectors, Matrices & Systems",
            "subtitle": "Arjun's Multi-Dimensional Customer Analysis",
            "description": "Arjun struggles to analyze customers with multiple attributes (age, income, spending). He discovers vectors and matrices - powerful ways to organize and manipulate multi-dimensional business data systematically.",
            "business_scenario": "Customer segmentation and multi-variable analysis",
            "key_concepts": ["Vectors (customer profiles)", "Matrices (data tables)", "Vector operations", "Systems of equations"],
            "arjun_learns": "How to represent and solve complex multi-variable business problems",
            "page_key": "linear_algebra_vectors"
        },
        {
            "title": "🎯 Eigenvalues & Eigenvectors",
            "subtitle": "Arjun Discovers Hidden Data Patterns",
            "description": "Arjun finds that some data directions remain stable even when business conditions change. He learns to identify these 'eigenpatterns' - the fundamental structures that persist in business data.",
            "business_scenario": "Finding stable patterns and core business drivers",
            "key_concepts": ["Eigenvectors (stable directions)", "Eigenvalues (pattern strength)", "Orthogonality (independence)", "Data structure analysis"],
            "arjun_learns": "How to find the underlying stable patterns in complex business data",
            "page_key": "linear_algebra_eigen"
        },
        {
            "title": "🔬 Principal Component Analysis (PCA)",
            "subtitle": "Arjun Masters Data Compression & Insights",
            "description": "Arjun learns to compress 50 customer features into 3 key dimensions while keeping the essential information. He transforms from drowning in data to surfacing powerful insights that drive business decisions.",
            "business_scenario": "Data simplification and insight extraction",
            "key_concepts": ["Dimensionality reduction", "Principal components", "Variance capture", "Data visualization"],
            "arjun_learns": "How to extract the most important insights from overwhelming amounts of data",
            "page_key": "linear_algebra_pca"
        }
    ]
    
    # Display topic cards
    st.subheader("🎯 Arjun's Learning Path")
    st.markdown("**Follow Arjun's journey in order - each mathematical tool builds on the previous ones!**")
    
    for i, topic in enumerate(linear_algebra_topics):
        with st.container():
            st.markdown("---")
            
            # Header with number and title
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {i+1}. {topic['title']}")
                st.markdown(f"**📖 Arjun's Challenge:** {topic['subtitle']}")
                st.write(topic['description'])
                
                # What Arjun learns
                st.markdown(f"**🎓 Arjun Discovers:** {topic['arjun_learns']}")
                
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
                st.write("⏱️ ~20-25 min")
                st.write("📊 Interactive")
                
                # Difficulty indicator
                if i == 0:
                    st.write("🟡 Intermediate")
                elif i == 1:
                    st.write("🔴 Advanced")
                else:
                    st.write("🔴 Expert")
    
    # Arjun's Journey Summary
    st.markdown("---")
    st.header("🚀 Arjun's Complete Transformation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Arjun's Mathematical Evolution:**
        
        📊 **Starts with:** Overwhelming multi-dimensional data  
        🎯 **Discovers:** Hidden stable patterns in chaos  
        🔬 **Masters:** Data compression and insight extraction  
        
        **From Overwhelmed to Expert:**
        - Struggling with customer spreadsheets
        - Finding core business drivers  
        - Extracting actionable insights from big data
        """)
    
    with col2:
        st.markdown("""
        **Linear Algebra Superpowers Unlocked:**
        
        ✅ **Vector thinking** → Organizing multi-dimensional problems  
        ✅ **Matrix operations** → Systematic data manipulation  
        ✅ **Pattern recognition** → Finding stability in chaos  
        ✅ **Dimensionality mastery** → Simplifying complexity  
        ✅ **Data compression** → Extracting essential insights  
        ✅ **Business intelligence** → Data-driven decisions  
        """)
    
    # Learning Tips
    st.markdown("---")
    st.markdown("""
    ### 💡 Learning Tips for Arjun's Journey:
    
    **🎯 Recommended Path:**
    - **Start with Vectors & Matrices** - Foundation of multi-dimensional thinking
    - **Progress to Eigenvalues** - Understanding data structure and stability
    - **Master PCA** - Practical application for real business insights
    - **Use interactive examples** - See how math transforms actual business data
    - **Focus on intuition** - Understand what the math means for business decisions
    
    **📚 Study Strategy:**
    - **Think in dimensions** - Move beyond 2D to multi-dimensional business problems
    - **Practice with real data** - Use the interactive examples with business scenarios
    - **Connect concepts** - See how each topic builds on the previous mathematical foundation
    - **Visualize transformations** - Watch how data changes through mathematical operations
    """)
    
    # Quick Navigation
    st.markdown("### 🚀 Quick Topic Access:")
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    
    with nav_col1:
        if st.button("📊 Start: Vectors & Matrices", key="quick_vectors"):
            st.session_state.page = 'linear_algebra_vectors'
            st.rerun()
    
    with nav_col2:
        if st.button("🎯 Topic 2: Eigenvalues", key="quick_eigen"):
            st.session_state.page = 'linear_algebra_eigen'
            st.rerun()
    
    with nav_col3:
        if st.button("🔬 Topic 3: PCA", key="quick_pca"):
            st.session_state.page = 'linear_algebra_pca'
            st.rerun()
    
    # Success Message
    st.markdown("---")
    st.success("""
    🎉 **Ready to Begin Arjun's Data Analytics Journey?**
    
    Start with **Vectors & Matrices** to understand how Arjun organizes multi-dimensional 
    business data. Each topic reveals new mathematical tools that transform his consulting 
    practice from overwhelming complexity to clear, actionable insights.
    
    By the end, you'll have followed Arjun from a struggling consultant to a data analytics 
    expert who uses Linear Algebra to solve real business intelligence challenges!
    """)
    
    st.markdown("---")