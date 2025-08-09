import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def show_mathematical_evolution():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("🚀 The Mathematical Evolution - From Formulas to AI")
    
    # Breadcrumb
    st.markdown("**Home** > **Mathematical Evolution**")
    
    st.markdown("---")
    
    # Introduction - The Big Picture
    st.header("🌟 The Complete Journey: Mathematics → Statistics → Machine Learning")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Meet Dr. Kavya!** She's a brilliant analyst who discovered that mastering business problems 
        requires a beautiful evolution through three interconnected domains:
        
        🔢 **Mathematics** → Perfect formulas and precise relationships  
        📊 **Statistics** → Real-world uncertainty and data variability  
        🤖 **Machine Learning** → Intelligent systems that learn and predict  
        
        *"I started with clean equations, encountered messy reality, and ended up building intelligent systems!"*
        """)
        
        st.info("""
        **The Evolution Story:**
        Each domain builds naturally on the previous one, solving problems the earlier couldn't handle alone.
        This is your pathway from foundational mathematics to cutting-edge AI applications!
        """)
    
    with col2:
        # Create evolution flow diagram
        fig = go.Figure(data=go.Sankey(
            node = dict(
                pad = 15,
                thickness = 20,
                line = dict(color = "black", width = 0.5),
                label = ["Pure\nMathematics", "Statistics", "Machine\nLearning", "Business\nIntelligence"],
                color = ["lightblue", "lightgreen", "orange", "gold"]
            ),
            link = dict(
                source = [0, 1, 2],
                target = [1, 2, 3],
                value = [1, 1, 1],
                color = ["rgba(0,100,200,0.3)", "rgba(0,200,100,0.3)", "rgba(200,100,0,0.3)"]
            )
        ))
        
        fig.update_layout(
            title_text="Dr. Kavya's Evolution Path",
            font_size=10,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 1: Mathematics Foundation
    st.markdown("---")
    st.header("🔢 Stage 1: Mathematics - The Perfect Foundation")
    
    st.markdown("""
    **Dr. Kavya's Starting Point:** *"I love creating perfect mathematical models that describe 
    business relationships with precision and elegance!"*
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("✅ What You've Mastered")
        st.markdown("""
        **🎯 Your Mathematical Toolkit:**
        
        **📈 Algebra**
        - Linear relationships  
        - Optimization models
        - Systems of equations
        - Growth patterns
        
        **📐 Linear Algebra**
        - Multi-dimensional analysis
        - Matrix operations
        - Eigenvalue decomposition
        - Data transformation
        
        **📊 Calculus**
        - Rate analysis
        - Optimization (maxima/minima)
        - Accumulation calculations
        - Marginal analysis
        """)
    
    with col2:
        st.subheader("🎯 Business Power")
        st.markdown("""
        **💼 What Mathematics Gives You:**
        
        **Precise Models:**
        - Revenue = Price × Quantity
        - ROI = (Gain - Cost) / Cost
        - NPV calculations
        - Growth projections
        
        **Optimization:**
        - Resource allocation
        - Cost minimization
        - Profit maximization
        - Portfolio balancing
        
        **Certainty:**
        - Exact answers
        - Predictable outcomes
        - Clear relationships
        - Logical consistency
        """)
    
    with col3:
        st.subheader("⚠️ The Limitation")
        st.markdown("""
        **🤔 Dr. Kavya's Realization:**
        
        *"My beautiful formulas assume:*
        - *Perfect information*
        - *No randomness*
        - *Exact relationships*
        - *Predictable behavior"*
        
        **But Real Business Has:**
        - Market volatility
        - Customer unpredictability  
        - Economic uncertainties
        - Random external factors
        - Measurement errors
        - Incomplete data
        
        **💡 Need:** Tools to handle uncertainty!
        """)
    
    # Interactive Mathematics Recap
    st.subheader("🧮 Your Mathematical Journey Recap")
    
    # Create a summary of what was learned
    domains_data = {
        'Domain': ['Algebra', 'Linear Algebra', 'Calculus', 'Series & Sequences', 'Optimization'],
        'Character': ['Maya', 'Arjun', 'Priya', 'Rajesh', 'Anand'],
        'Key Business Application': [
            'Business strategy & growth',
            'Data insights & patterns', 
            'Financial rate analysis',
            'Investment planning',
            'Resource allocation'
        ],
        'Mathematical Power': [
            'Linear relationships & equations',
            'Multi-dimensional analysis',
            'Rate & accumulation analysis', 
            'Sequential pattern analysis',
            'Constrained optimization'
        ]
    }
    
    df_recap = pd.DataFrame(domains_data)
    st.dataframe(df_recap, use_container_width=True)
    
    st.success("""
    🎉 **Congratulations!** You've built a solid mathematical foundation that provides the 
    precise, logical framework needed for advanced analytics and intelligent systems!
    """)
    
    # Section 2: Statistics - Handling Uncertainty
    st.markdown("---")
    st.header("📊 Stage 2: Statistics - Embracing Real-World Uncertainty")
    
    st.markdown("""
    **Dr. Kavya's Reality Check:** *"When I applied my perfect formulas to real business data, 
    I discovered noise, variability, and uncertainty everywhere! I needed new tools to handle 
    the messiness of the real world."*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 Why Statistics is Essential")
        st.markdown("""
        **The Gap Mathematics Can't Fill:**
        
        **📈 Real Data is Messy:**
        - Sales vary randomly day-to-day
        - Customer behavior is unpredictable
        - Market conditions change unexpectedly
        - Measurements contain errors
        
        **❓ Questions Mathematics Can't Answer:**
        - "What's the average customer satisfaction?"
        - "How confident are we in this prediction?"
        - "Is this difference statistically significant?"
        - "What's the probability of achieving our target?"
        
        **💡 Statistics provides:**
        - Tools to summarize messy data
        - Methods to quantify uncertainty
        - Techniques to test hypotheses
        - Ways to make inferences from samples
        """)
        
        # Show the transition with example
        st.markdown("**🔄 The Transition Example:**")
        st.code("""
Mathematics Says:
Revenue = Price × Quantity (Exact)

Statistics Asks:
- What's the average revenue? (μ)
- How much does it vary? (σ)
- What's the confidence interval?
- Is the trend statistically significant?
        """)
    
    with col2:
        st.subheader("📊 Statistics Topics to Explore")
        st.markdown("""
        **🔍 Descriptive Statistics:**
        - Mean, median, mode
        - Standard deviation & variance
        - Quartiles & percentiles
        - Data visualization techniques
        
        **📈 Probability & Distributions:**
        - Probability theory basics
        - Normal, binomial, Poisson distributions
        - Central Limit Theorem
        - Risk and uncertainty quantification
        
        **🧪 Inferential Statistics:**
        - Hypothesis testing
        - Confidence intervals
        - Regression analysis
        - ANOVA (Analysis of Variance)
        
        **📊 Applied Business Statistics:**
        - A/B testing
        - Market research analysis
        - Quality control
        - Forecasting with uncertainty
        
        **🎯 Advanced Topics:**
        - Bayesian statistics
        - Time series analysis
        - Multivariate analysis
        - Statistical modeling
        """)
    
    # Interactive Statistics Demo
    st.subheader("🧪 Statistics in Action: Handling Uncertainty")
    
    # Generate sample business data with noise
    np.random.seed(42)
    days = np.arange(1, 31)
    true_sales = 1000 + 10 * days  # Perfect mathematical relationship
    noisy_sales = true_sales + np.random.normal(0, 50, len(days))  # Real-world data with noise
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Plot mathematical vs real data
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=days, y=true_sales,
            mode='lines',
            name='Mathematical Model (Perfect)',
            line=dict(color='blue', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=days, y=noisy_sales,
            mode='markers',
            name='Real Business Data (Noisy)',
            marker=dict(color='red', size=6)
        ))
        
        # Add trend line
        z = np.polyfit(days, noisy_sales, 1)
        trend_line = np.poly1d(z)(days)
        
        fig.add_trace(go.Scatter(
            x=days, y=trend_line,
            mode='lines',
            name='Statistical Trend',
            line=dict(color='green', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Mathematics vs Reality vs Statistics",
            xaxis_title="Day",
            yaxis_title="Sales",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Statistical analysis
        mean_sales = np.mean(noisy_sales)
        std_sales = np.std(noisy_sales)
        correlation = np.corrcoef(days, noisy_sales)[0, 1]
        
        st.markdown("**📊 Statistical Analysis Results:**")
        st.code(f"""
Mathematical Model: Sales = 1000 + 10×Day

Real Data Statistics:
Average Sales: {mean_sales:.0f}
Standard Deviation: {std_sales:.1f}
Correlation with Day: {correlation:.3f}

Statistical Insights:
- 68% of days fall within {mean_sales-std_sales:.0f} to {mean_sales+std_sales:.0f}
- Strong positive correlation ({correlation:.3f})
- Trend is statistically significant
- R² explains {correlation**2*100:.1f}% of variance
        """)
        
        st.info("""
        **Statistics Reveals:**
        The mathematical relationship exists, but real data has variability.
        Statistics quantifies this uncertainty and helps make confident decisions.
        """)
    
    # Section 3: Machine Learning - Intelligence from Data
    st.markdown("---")
    st.header("🤖 Stage 3: Machine Learning - Building Intelligent Systems")
    
    st.markdown("""
    **Dr. Kavya's Next Evolution:** *"Statistics helped me understand uncertainty, but I wanted 
    systems that could automatically learn patterns, make predictions, and improve over time. 
    That's where Machine Learning comes in!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🚀 Why Machine Learning?")
        st.markdown("""
        **Beyond Statistics - The Need for Intelligence:**
        
        **📊 Statistics Limitations:**
        - Requires manual model specification
        - Assumes specific distributions
        - Limited to predefined relationships
        - Human interpretation needed
        
        **🤖 Machine Learning Advantages:**
        - Discovers patterns automatically
        - Handles complex, non-linear relationships
        - Learns from data continuously
        - Makes predictions autonomously
        - Adapts to new information
        
        **💼 Business Applications:**
        - Recommendation systems
        - Fraud detection
        - Predictive maintenance
        - Customer segmentation
        - Automated decision making
        """)
        
        st.markdown("**🔄 The Evolution:**")
        st.code("""
Mathematics: Revenue = f(Price, Quantity)
Statistics: Revenue ~ Normal(μ, σ²)
ML: Revenue = learned_function(Price, Quantity, 
              Season, Competition, Weather, ...)
        """)
    
    with col2:
        st.subheader("🤖 Machine Learning Topics to Explore")
        st.markdown("""
        **🎯 Supervised Learning:**
        - Linear & Logistic Regression
        - Decision Trees & Random Forests
        - Support Vector Machines
        - Neural Networks & Deep Learning
        
        **🔍 Unsupervised Learning:**
        - Clustering (K-means, Hierarchical)
        - Dimensionality Reduction (PCA, t-SNE)
        - Association Rules
        - Anomaly Detection
        
        **🎮 Reinforcement Learning:**
        - Q-Learning
        - Policy Gradient Methods
        - Multi-Armed Bandits
        - Game Theory Applications
        
        **📊 Applied ML in Business:**
        - Predictive Analytics
        - Natural Language Processing
        - Computer Vision
        - Time Series Forecasting
        
        **🛠️ ML Engineering:**
        - Model Selection & Validation
        - Feature Engineering
        - Model Deployment
        - MLOps & Production Systems
        """)
    
    # Interactive ML Concept Demo
    st.subheader("🧠 Machine Learning in Action: Pattern Discovery")
    
    # Generate sample data for ML demo
    np.random.seed(42)
    n_customers = 200
    
    # Create synthetic customer data
    age = np.random.normal(35, 10, n_customers)
    income = age * 2000 + np.random.normal(0, 10000, n_customers)
    spending = 0.3 * income + 50 * age + np.random.normal(0, 5000, n_customers)
    
    # Normalize for clustering
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    
    try:
        # Simple clustering example
        data = np.column_stack([age, income, spending])
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        # K-means clustering
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(data_scaled)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 3D scatter plot
            fig = go.Figure(data=go.Scatter3d(
                x=age, y=income, z=spending,
                mode='markers',
                marker=dict(
                    size=5,
                    color=clusters,
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title="Cluster")
                ),
                text=[f'Customer {i+1}' for i in range(n_customers)],
                hovertemplate='<b>%{text}</b><br>Age: %{x:.0f}<br>Income: ₹%{y:,.0f}<br>Spending: ₹%{z:,.0f}'
            ))
            
            fig.update_layout(
                title="ML Customer Segmentation",
                scene=dict(
                    xaxis_title="Age",
                    yaxis_title="Income (₹)",
                    zaxis_title="Spending (₹)"
                ),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cluster analysis
            cluster_summary = pd.DataFrame({
                'Cluster': ['Cluster 0', 'Cluster 1', 'Cluster 2'],
                'Size': [np.sum(clusters == 0), np.sum(clusters == 1), np.sum(clusters == 2)],
                'Avg Age': [age[clusters == 0].mean(), age[clusters == 1].mean(), age[clusters == 2].mean()],
                'Avg Income': [income[clusters == 0].mean(), income[clusters == 1].mean(), income[clusters == 2].mean()],
                'Avg Spending': [spending[clusters == 0].mean(), spending[clusters == 1].mean(), spending[clusters == 2].mean()]
            })
            
            st.markdown("**🎯 ML-Discovered Customer Segments:**")
            st.dataframe(cluster_summary.round(0), use_container_width=True)
            
            st.success("""
            **Machine Learning Magic:**
            - **Automatically discovered** 3 customer segments
            - **No manual rules** - algorithm found patterns
            - **Actionable insights** for targeted marketing
            - **Scalable** to millions of customers
            """)
            
            st.info("""
            **Business Applications:**
            🎯 Targeted marketing campaigns
            💰 Personalized pricing strategies  
            📊 Customer lifetime value prediction
            🔮 Churn prediction and retention
            """)
            
    except ImportError:
        st.info("Machine Learning demo requires scikit-learn library")
    
    # Section 4: The Beautiful Connection
    st.markdown("---")
    st.header("🔗 How They All Connect: The Beautiful Evolution")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔢 Mathematics")
        st.markdown("""
        **Foundation Layer:**
        - Provides precise language
        - Defines relationships  
        - Enables optimization
        - Creates logical framework
        
        **Feeds into Statistics:**
        - Probability theory
        - Linear algebra for analysis
        - Calculus for optimization
        - Algebraic transformations
        """)
    
    with col2:
        st.subheader("📊 Statistics")
        st.markdown("""
        **Reality Layer:**
        - Handles uncertainty
        - Quantifies variability
        - Tests hypotheses
        - Makes inferences
        
        **Feeds into ML:**
        - Probability distributions
        - Hypothesis testing
        - Regression techniques
        - Experimental design
        """)
    
    with col3:
        st.subheader("🤖 Machine Learning")
        st.markdown("""
        **Intelligence Layer:**
        - Discovers patterns
        - Makes predictions
        - Learns continuously
        - Automates decisions
        
        **Uses Both:**
        - Mathematical optimization
        - Statistical inference
        - Algorithmic thinking
        - Computational methods
        """)
    
    # Evolution Timeline
    st.subheader("📈 Dr. Kavya's Complete Evolution Timeline")
    
    timeline_data = {
        'Stage': ['Pure Math', 'Applied Math', 'Statistics', 'Data Science', 'Machine Learning', 'AI Systems'],
        'Capability': [
            'Perfect formulas',
            'Business modeling', 
            'Uncertainty handling',
            'Pattern discovery',
            'Intelligent prediction',
            'Autonomous decisions'
        ],
        'Tools': [
            'Equations & Models',
            'Optimization & Analysis',
            'Probability & Inference', 
            'Descriptive Analytics',
            'Predictive Algorithms',
            'Learning Systems'
        ],
        'Business Impact': [
            'Precise calculations',
            'Resource optimization',
            'Risk quantification',
            'Data-driven insights', 
            'Automated predictions',
            'Intelligent automation'
        ]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    
    # Create timeline visualization
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(len(timeline_data['Stage']))),
        y=[1]*len(timeline_data['Stage']),
        mode='markers+lines+text',
        marker=dict(size=20, color=['lightblue', 'blue', 'lightgreen', 'green', 'orange', 'red']),
        line=dict(width=3, color='gray'),
        text=timeline_data['Stage'],
        textposition='top center',
        textfont=dict(size=12),
        showlegend=False
    ))
    
    fig.update_layout(
        title="Dr. Kavya's Mathematical Evolution Journey",
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0.5, 1.5]),
        height=200
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(timeline_df, use_container_width=True)
    
    # Section 5: Your Next Steps
    st.markdown("---")
    st.header("🎯 Your Learning Roadmap: Where to Go Next")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📚 Immediate Next Steps")
        st.markdown("""
        **🎯 Statistics Foundation:**
        
        **Start Here:**
        1. **Descriptive Statistics** - Summarizing data
        2. **Probability Basics** - Understanding uncertainty  
        3. **Hypothesis Testing** - Making data-driven decisions
        4. **Regression Analysis** - Modeling relationships
        
        **Tools to Learn:**
        - Excel/Google Sheets (Statistical functions)
        - Python (pandas, numpy, scipy)
        - R (Statistical computing)
        - Tableau/Power BI (Data visualization)
        
        **Business Applications:**
        - A/B testing for marketing
        - Financial risk analysis
        - Quality control
        - Market research analysis
        """)
    
    with col2:
        st.subheader("🚀 Advanced Pathway")
        st.markdown("""
        **🤖 Machine Learning Journey:**
        
        **After Statistics:**
        1. **Feature Engineering** - Data preparation 
        2. **Supervised Learning** - Prediction models
        3. **Unsupervised Learning** - Pattern discovery
        4. **Model Evaluation** - Validation techniques
    
        
        **Advanced Tools:**
        - Python (scikit-learn, TensorFlow, PyTorch, Transformers)
        - MLOps tools (Docker, CI/CD pipelines, Kubernetes)
        - SQL, NoSQL, Cloud - AWS/GCP/Azure
        - Gen AI, RAG, Agents, Agentic Workflow - Langchain, LangGraph
        
        **Career Opportunities:**
        - Data Scientist
        - ML Engineer  
        - Business Analyst
        - AI Product Manager
        - Gen AI Specialist           
        """)
    

    
    # Final Inspiration
    st.markdown("---")
    st.success("""
    🎉 **Congratulations on Completing Your Mathematical Foundation!**
    
    **You've Built:**
    ✅ **Mathematical Thinking** - Logical problem-solving framework
    ✅ **Business Applications** - Real-world problem-solving skills  
    ✅ **Analytical Mindset** - Data-driven decision making
    ✅ **Optimization Skills** - Resource allocation and efficiency
    ✅ **Quantitative Confidence** - Comfort with numbers and models
    
    **Your Journey Continues:**
    🔢 **Mathematics** (Mastered) → 📊 **Statistics** (Next) → 🤖 **Machine Learning** (Future)
    
    **Remember Dr. Kavya's Wisdom:**
    *"Each step builds on the previous one. Your mathematical foundation makes statistics easier, 
    and statistics makes machine learning possible. You're on the path to becoming a complete 
    data-driven decision maker!"*
    
    **The future of business belongs to those who can combine mathematical precision, 
    statistical wisdom, and machine learning intelligence. You're well on your way!** 🚀
    """)
    
    st.markdown("---")
    
    # Call to Action
    st.header("🎯 Ready for Your Next Adventure?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Start Statistics**
        
        Begin your journey into uncertainty and real-world data analysis.
        
        *Recommended: Start with descriptive statistics and probability basics.*
        """)
        if st.button("🚀 Explore Statistics", key="stats_btn"):
            st.balloons()
            st.info("Statistics learning resources coming soon!")
    
    with col2:
        st.markdown("""
        **🤖 Explore Machine Learning**
        
        Discover how to build intelligent systems that learn from data.
        
        *Recommended: Begin with supervised learning basics.*
        """)
        if st.button("🧠 Discover ML", key="ml_btn"):
            st.balloons()
            st.info("Machine Learning modules coming soon!")
    
    with col3:
        st.markdown("""
        **🔄 Review Mathematics**
        
        Reinforce your foundation by revisiting key mathematical concepts.
        
        *Perfect for strengthening your base before advancing.*
        """)
        if st.button("📚 Review Math", key="review_btn"):
            st.session_state.page = 'home'
            st.rerun()
    
    st.markdown("---")
    st.markdown("** Hope you enjoyed the learning experience!! - [Vivek Dhandapani](https://www.linkedin.com/in/vivekdhandapani)**")