import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def show_pca():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Linear Algebra"):
            st.session_state.page = 'linear_algebra'
            st.rerun()
    
    with col2:
        st.title("🔬 Principal Component Analysis (PCA)")
    
    # Breadcrumb
    st.markdown("**Home** > **Linear Algebra** > **Principal Component Analysis**")
    
    st.markdown("---")
    
    # Story Introduction
    st.header("📖 Arjun's Customer Data Overwhelm")
    
    st.markdown("""
    **Mr. Patel's Challenge:** *"Arjun, I have customer data with 50 different attributes per customer! 
    Age, income, purchase history across 20 product categories, website behavior... I'm drowning in data! 
    Can you find the 2-3 most important things I should focus on?"*
    
    **Arjun's Mission:** Transform overwhelming multi-dimensional data into clear, actionable insights.
    """)
    
    # Section 1: The Overwhelming Data Problem
    st.markdown("---")
    st.header("1️⃣ The Information Overload Problem")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("😵 Too Many Dimensions!")
        
        # Generate sample customer data with many attributes
        np.random.seed(42)
        n_customers = 100
        n_attributes = 8  # We'll show 8 attributes for demonstration
        
        # Create correlated customer data (realistic business scenario)
        base_customer_level = np.random.normal(0, 1, n_customers)
        spending_style = np.random.normal(0, 0.5, n_customers)
        
        customer_data = pd.DataFrame({
            'Age': 30 + base_customer_level * 10 + np.random.normal(0, 3, n_customers),
            'Income': 500 + base_customer_level * 200 + np.random.normal(0, 50, n_customers),
            'Spending': 100 + base_customer_level * 60 + spending_style * 30 + np.random.normal(0, 20, n_customers),
            'Online_Hours': 20 + base_customer_level * 10 + spending_style * 5 + np.random.normal(0, 5, n_customers),
            'Store_Visits': 8 + base_customer_level * 3 + np.random.normal(0, 2, n_customers),
            'Product_Categories': 5 + base_customer_level * 2 + spending_style * 1 + np.random.normal(0, 1, n_customers),
            'Loyalty_Score': 60 + base_customer_level * 20 + np.random.normal(0, 10, n_customers),
            'Review_Count': 10 + base_customer_level * 5 + spending_style * 3 + np.random.normal(0, 3, n_customers)
        })
        
        # Ensure positive values
        customer_data = customer_data.clip(lower=0)
        
        st.dataframe(customer_data.head(10), use_container_width=True)
        
        st.warning("""
        **Mr. Patel's Frustration:**
        - 8 attributes per customer (imagine 50!)
        - Can't see patterns in this table
        - Which attributes actually matter?
        - How to make business decisions?
        """)
    
    with col2:
        st.subheader("📊 Correlation Chaos")
        
        # Show correlation matrix
        correlation_matrix = customer_data.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            text=np.round(correlation_matrix.values, 2),
            texttemplate="%{text}",
            textfont={"size": 10}
        ))
        
        fig.update_layout(
            title="Customer Attribute Correlations",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Arjun's Observations:**
        - Many attributes are highly correlated
        - Age, Income, Spending move together
        - Online behavior clusters together  
        - Redundant information everywhere!
        """)
    
    # Section 2: PCA Concept Introduction
    st.markdown("---")
    st.header("2️⃣ Arjun's PCA Solution Concept")
    
    st.markdown("""
    **Arjun's Insight:** *"What if I could create 2-3 'super attributes' that capture the essence 
    of all 8 original attributes? Like finding the Customer DNA!"*
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 The PCA Goal")
        st.markdown("""
        **Transform:** 8 confusing attributes → 2 clear insights
        
        **Method:** Find directions where customers vary MOST
        
        **Result:** New dimensions that capture maximum information
        
        **Analogy:** Like finding the best camera angle to photograph a 3D object in 2D
        """)
        
        # Simple 2D demonstration
        st.markdown("**Simple Example: Age vs Income**")
        
        # Show age vs income scatter
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=customer_data['Age'],
            y=customer_data['Income'],
            mode='markers',
            marker=dict(size=8, color='blue', opacity=0.6),
            name='Customers'
        ))
        
        fig.update_layout(
            title="Age vs Income: Looking for Patterns",
            xaxis_title="Age",
            yaxis_title="Income (₹k)",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🔍 Finding the Main Direction")
        
        # Perform simple 2D PCA for demonstration
        simple_data = customer_data[['Age', 'Income']].values
        scaler = StandardScaler()
        simple_data_scaled = scaler.fit_transform(simple_data)
        
        pca_2d = PCA(n_components=2)
        pca_2d.fit(simple_data_scaled)
        
        # Get PCA components for plotting
        mean_point = np.mean(simple_data_scaled, axis=0)
        pc1_direction = pca_2d.components_[0] * 3  # Scale for visibility
        pc2_direction = pca_2d.components_[1] * 3
        
        # Transform back to original scale for plotting
        mean_original = scaler.inverse_transform(mean_point.reshape(1, -1))[0]
        pc1_original = scaler.inverse_transform((mean_point + pc1_direction).reshape(1, -1))[0]
        pc2_original = scaler.inverse_transform((mean_point + pc2_direction).reshape(1, -1))[0]
        
        fig = go.Figure()
        
        # Original data points
        fig.add_trace(go.Scatter(
            x=customer_data['Age'],
            y=customer_data['Income'],
            mode='markers',
            marker=dict(size=6, color='lightblue', opacity=0.6),
            name='Customers'
        ))
        
        # PC1 direction (main variation)
        fig.add_trace(go.Scatter(
            x=[mean_original[0], pc1_original[0]],
            y=[mean_original[1], pc1_original[1]],
            mode='lines+markers',
            line=dict(color='red', width=4),
            marker=dict(size=10),
            name=f'PC1 ({pca_2d.explained_variance_ratio_[0]:.1%} variance)'
        ))
        
        # PC2 direction
        fig.add_trace(go.Scatter(
            x=[mean_original[0], pc2_original[0]],
            y=[mean_original[1], pc2_original[1]],
            mode='lines+markers',
            line=dict(color='green', width=4),
            marker=dict(size=10),
            name=f'PC2 ({pca_2d.explained_variance_ratio_[1]:.1%} variance)'
        ))
        
        fig.update_layout(
            title="PCA Finds Main Directions of Variation",
            xaxis_title="Age",
            yaxis_title="Income (₹k)",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"""
        **Discovery:**
        - **PC1** captures {pca_2d.explained_variance_ratio_[0]:.1%} of variation
        - **PC2** captures {pca_2d.explained_variance_ratio_[1]:.1%} of variation
        - **Total:** {pca_2d.explained_variance_ratio_.sum():.1%} of all information!
        """)
    
    # Section 3: Full PCA Analysis
    st.markdown("---")
    st.header("3️⃣ Complete Customer Analysis with PCA")
    
    st.subheader("🔬 PCA on All 8 Customer Attributes")
    
    # Perform full PCA
    data_scaled = StandardScaler().fit_transform(customer_data)
    pca_full = PCA()
    pca_transformed = pca_full.fit_transform(data_scaled)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**📊 Explained Variance by Component**")
        
        # Variance explained plot
        variance_ratio = pca_full.explained_variance_ratio_
        cumulative_variance = np.cumsum(variance_ratio)
        
        fig = go.Figure()
        
        # Individual variance
        fig.add_trace(go.Bar(
            x=[f'PC{i+1}' for i in range(len(variance_ratio))],
            y=variance_ratio * 100,
            name='Individual Variance',
            marker_color='lightblue'
        ))
        
        # Cumulative variance
        fig.add_trace(go.Scatter(
            x=[f'PC{i+1}' for i in range(len(variance_ratio))],
            y=cumulative_variance * 100,
            mode='lines+markers',
            name='Cumulative Variance',
            yaxis='y2',
            line=dict(color='red', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="How Much Information Each Component Captures",
            xaxis_title="Principal Component",
            yaxis_title="Individual Variance Explained (%)",
            yaxis2=dict(
                title="Cumulative Variance Explained (%)",
                overlaying='y',
                side='right'
            ),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Key Insight:**
        - **PC1 + PC2** explain {cumulative_variance[1]:.1%} of all customer variation
        - **First 3 components** explain {cumulative_variance[2]:.1%} of all information
        - Can focus on just 2-3 dimensions instead of 8!
        """)
    
    with col2:
        st.markdown("**🔍 Component Interpretation**")
        
        # Show component loadings
        components_df = pd.DataFrame(
            pca_full.components_[:3].T,
            columns=['PC1', 'PC2', 'PC3'],
            index=customer_data.columns
        )
        
        # Create heatmap of loadings
        fig = go.Figure(data=go.Heatmap(
            z=components_df.values,
            x=components_df.columns,
            y=components_df.index,
            colorscale='RdBu',
            zmid=0,
            text=np.round(components_df.values, 2),
            texttemplate="%{text}",
            textfont={"size": 10}
        ))
        
        fig.update_layout(
            title="Component Loadings (What Each PC Represents)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Interpret components
        pc1_interpretation = ""
        pc2_interpretation = ""
        
        # PC1 interpretation
        pc1_high = components_df['PC1'].abs().nlargest(3).index.tolist()
        pc1_interpretation = f"**PC1 - 'Customer Tier':** {', '.join(pc1_high)}"
        
        # PC2 interpretation  
        pc2_high = components_df['PC2'].abs().nlargest(3).index.tolist()
        pc2_interpretation = f"**PC2 - 'Engagement Style':** {', '.join(pc2_high)}"
        
        st.success(f"""
        **Arjun's Interpretation:**
        
        {pc1_interpretation}
        
        {pc2_interpretation}
        
        **PC3:** Captures remaining nuances
        """)
    
    # Section 4: Customer Segmentation
    st.markdown("---")
    st.header("4️⃣ Customer Segmentation Using PCA")
    
    st.subheader("🎯 2D Customer Map (PC1 vs PC2)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create 2D scatter plot of customers in PC space
        fig = go.Figure()
        
        # Color customers based on original spending for context
        fig.add_trace(go.Scatter(
            x=pca_transformed[:, 0],
            y=pca_transformed[:, 1],
            mode='markers',
            marker=dict(
                size=8,
                color=customer_data['Spending'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Spending (₹k)")
            ),
            text=[f'Customer {i+1}' for i in range(len(customer_data))],
            hovertemplate='<b>%{text}</b><br>PC1: %{x:.2f}<br>PC2: %{y:.2f}<br>Spending: %{marker.color:.0f}k<extra></extra>',
            name='Customers'
        ))
        
        # Add quadrant lines
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)
        
        # Add quadrant labels
        fig.add_annotation(x=2, y=2, text="High Tier<br>High Engagement", 
                          showarrow=False, bgcolor="rgba(255,255,255,0.8)")
        fig.add_annotation(x=-2, y=2, text="Low Tier<br>High Engagement", 
                          showarrow=False, bgcolor="rgba(255,255,255,0.8)")
        fig.add_annotation(x=2, y=-2, text="High Tier<br>Low Engagement", 
                          showarrow=False, bgcolor="rgba(255,255,255,0.8)")
        fig.add_annotation(x=-2, y=-2, text="Low Tier<br>Low Engagement", 
                          showarrow=False, bgcolor="rgba(255,255,255,0.8)")
        
        fig.update_layout(
            title="Customer Segmentation in PCA Space",
            xaxis_title=f"PC1 - Customer Tier ({variance_ratio[0]:.1%} variance)",
            yaxis_title=f"PC2 - Engagement Style ({variance_ratio[1]:.1%} variance)",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**🎯 Customer Segments Discovered:**")
        
        # Define segments based on PC scores
        pc1_scores = pca_transformed[:, 0]
        pc2_scores = pca_transformed[:, 1]
        
        q1_customers = np.sum((pc1_scores > 0) & (pc2_scores > 0))
        q2_customers = np.sum((pc1_scores < 0) & (pc2_scores > 0))
        q3_customers = np.sum((pc1_scores > 0) & (pc2_scores < 0))
        q4_customers = np.sum((pc1_scores < 0) & (pc2_scores < 0))
        
        st.metric("🏆 Premium Engaged", f"{q1_customers} customers")
        st.metric("💡 Budget Engaged", f"{q2_customers} customers")
        st.metric("💼 Premium Conservative", f"{q3_customers} customers")
        st.metric("🛒 Budget Conservative", f"{q4_customers} customers")
        
        st.markdown("---")
        st.markdown("**📈 Business Strategy:**")
        
        st.markdown("""
        **🏆 Premium Engaged:**
        - Luxury products, exclusive offers
        - High-touch customer service
        
        **💡 Budget Engaged:**
        - Value-focused engagement
        - Social media campaigns
        
        **💼 Premium Conservative:**
        - Quality-focused messaging
        - Traditional channels
        
        **🛒 Budget Conservative:**
        - Discount offers, basic service
        - Email marketing
        """)
    
    # Section 5: Interactive PCA Explorer
    st.markdown("---")
    st.header("5️⃣ Interactive PCA Explorer")
    
    st.subheader("🧪 Experiment with Different Numbers of Components")
    
    n_components = st.slider("Number of Principal Components to Use", 1, 8, 2)
    
    # Perform PCA with selected number of components
    pca_selected = PCA(n_components=n_components)
    pca_selected_transformed = pca_selected.fit_transform(data_scaled)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Show information retention
        total_variance_explained = np.sum(pca_selected.explained_variance_ratio_)
        
        st.metric(
            "Information Retained", 
            f"{total_variance_explained:.1%}",
            delta=f"{total_variance_explained - 0.5:.1%} vs random"
        )
        
        st.markdown("**🔍 What You're Keeping/Losing:**")
        
        for i in range(n_components):
            st.write(f"**PC{i+1}:** {pca_selected.explained_variance_ratio_[i]:.1%} of information")
        
        information_lost = 1 - total_variance_explained
        st.warning(f"**Information Lost:** {information_lost:.1%}")
        
        if total_variance_explained > 0.8:
            st.success("✅ Excellent information retention!")
        elif total_variance_explained > 0.6:
            st.info("✅ Good information retention")
        else:
            st.warning("⚠️ Significant information loss")
    
    with col2:
        # Show dimensionality reduction benefit
        original_dimensions = len(customer_data.columns)
        reduction_ratio = n_components / original_dimensions
        
        st.metric(
            "Dimension Reduction",
            f"{original_dimensions} → {n_components}",
            delta=f"{(1-reduction_ratio)*100:.0f}% reduction"
        )
        
        st.markdown("**💰 Business Benefits:**")
        
        analysis_time_saved = (1 - reduction_ratio) * 100
        storage_saved = (1 - reduction_ratio) * 100
        
        st.write(f"**Analysis Time:** {analysis_time_saved:.0f}% faster")
        st.write(f"**Storage Requirements:** {storage_saved:.0f}% less")
        st.write(f"**Visualization:** Possible in {min(n_components, 3)}D")
        st.write(f"**Model Training:** {analysis_time_saved:.0f}% faster")
    
    # Section 6: Business Implementation
    st.markdown("---")
    st.header("6️⃣ Mr. Patel's Business Implementation")
    
    st.success("""
    ## 🎯 **Arjun's Final Recommendation**
    
    **Mr. Patel, here's how PCA transforms your customer analysis:**
    
    ### **Before PCA (Overwhelming):**
    - 8 customer attributes to track and analyze
    - Unclear which factors drive business results  
    - Can't visualize customer patterns
    - Analysis paralysis from too much data
    
    ### **After PCA (Clear Insights):**
    ✅ **Focus on 2 key dimensions:** Customer Tier + Engagement Style
    
    ✅ **Clear Customer Segments:** 4 distinct groups with specific strategies
    
    ✅ **Visual Dashboard:** Simple 2D plot shows all customer patterns
    
    ✅ **Resource Optimization:** 75% reduction in analysis complexity
    
    ✅ **Actionable Strategy:** Tailored approach for each customer segment
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### **📊 Implementation Plan:**
        
        **Week 1:** Set up PCA analysis pipeline
        
        **Week 2:** Segment existing customer base
        
        **Week 3:** Design targeted campaigns for each segment
        
        **Week 4:** Launch and monitor results
        
        **Ongoing:** Monthly PCA refresh to track segment evolution
        """)
    
    with col2:
        st.markdown("""
        ### **💰 Expected ROI:**
        
        **Analysis Efficiency:** 75% time reduction
        
        **Marketing Precision:** 40% better targeting
        
        **Customer Insights:** Clear, actionable segments
        
        **Decision Making:** Data-driven, not gut-feel
        
        **Competitive Advantage:** Mathematical customer understanding
        """)
    
    # Key Concepts Summary
    st.markdown("---")
    st.header("🎓 Key PCA Concepts Mastered")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔍 Principal Components**
        - New "super attributes" 
        - Capture maximum variation
        - Independent directions
        - Business-interpretable
        """)
    
    with col2:
        st.markdown("""
        **📊 Explained Variance**  
        - Information retention measure
        - Guides component selection
        - Cost-benefit analysis
        - Quality assurance
        """)
    
    with col3:
        st.markdown("""
        **🎯 Dimensionality Reduction**
        - Simplify complex data
        - Enable visualization  
        - Faster analysis
        - Clearer insights
        """)
    
    # Practice Exercise
    st.markdown("---")
    st.subheader("💪 Practice: Apply PCA to Product Analysis")
    
    with st.expander("📝 Exercise: Product Feature Analysis"):
        st.markdown("""
        **Scenario:** A tech company has products with 10 features: 
        price, performance, battery, design, camera, storage, display, durability, software, support.
        
        Customer ratings create a 10-dimensional feature space. 
        
        **Tasks:**
        1. How many principal components capture 90% of product variation?
        2. What do the first 2 components represent in business terms?
        3. How would you segment products using PCA?
        4. What's the business value of this analysis?
        """)
        
        if st.button("Show Solution Approach", key="pca_exercise"):
            st.markdown("---")
            st.markdown("### 🔍 **Solution Approach:**")
            
            st.code("""
# Step 1: Data Preparation
product_features = StandardScaler().fit_transform(product_data)

# Step 2: PCA Analysis  
pca = PCA()
pca_result = pca.fit_transform(product_features)

# Step 3: Variance Analysis
cumsum_variance = np.cumsum(pca.explained_variance_ratio_)
n_components_90 = np.argmax(cumsum_variance >= 0.9) + 1

# Step 4: Interpretation
PC1 = "Overall Product Quality" (performance + features)
PC2 = "Price vs Premium Features" (cost vs luxury)

# Step 5: Segmentation
- Budget Products: Low PC1, Low PC2
- Value Products: High PC1, Low PC2  
- Premium Products: High PC1, High PC2
- Overpriced Products: Low PC1, High PC2
            """)
            
            st.success("""
            **Business Value:**
            - Simplify 10 features → 2-3 key dimensions
            - Clear product positioning strategy
            - Identify market gaps and opportunities  
            - Optimize R&D resource allocation
            """)
    
    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Previous: Eigenvalues & Eigenvectors"):
            st.session_state.page = 'linear_algebra_eigen'
            st.rerun()
    
    with col2:
        if st.button("🏠 Back to Linear Algebra Overview"):
            st.session_state.page = 'linear_algebra'
            st.rerun()
    
    st.markdown("---")
    st.success("""
    🎉 **Congratulations! You've Completed Arjun's Linear Algebra Journey!**
    
    From organizing multi-dimensional data with vectors and matrices, to finding stable patterns 
    with eigenvalues, to extracting key insights with PCA - you now have the mathematical tools 
    to transform complex business data into clear, actionable strategies!
    
    **Next Steps:** Apply these concepts to your own business challenges and discover the hidden 
    patterns in your data!
    """)