import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def show_vectors_matrices():
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Linear Algebra"):
            st.session_state.page = 'linear_algebra'
            st.rerun()
    
    with col2:
        st.title("📊 Vectors, Matrices & Systems")
    
    # Breadcrumb
    st.markdown("**Home** > **Linear Algebra** > **Vectors & Matrices**")
    
    st.markdown("---")
    
    # Arjun's Story Introduction
    st.header("📖 Arjun's Challenge: The Overwhelming Spreadsheet")
    
    st.markdown("""
    **Arjun's Problem:** A local retail chain asks him to analyze their customer data. 
    He opens the spreadsheet and freezes - 1000+ customers, each with 8 different attributes 
    (age, income, spending, visit frequency, etc.). How can he make sense of this multi-dimensional mess?
    
    **The Discovery:** Arjun learns that mathematics has elegant tools for exactly this problem - 
    **Vectors** and **Matrices**!
    """)
    
    # Section 1: Understanding Vectors
    st.markdown("---")
    st.header("1️⃣ Vectors: Customer Profiles Made Mathematical")
    
    st.markdown("""
    **Arjun's Insight:** Instead of thinking "Customer John: Age 35, Income 50k, Spending 12k", 
    he can represent John as a **vector**: `[35, 50000, 12000]`
    
    A **vector** is simply an ordered list of numbers that describes something completely.
    """)
    
    # Interactive Customer Vector Example
    st.subheader("🧑‍💼 Build a Customer Vector")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Customer Attributes:**")
        age = st.slider("Age", 18, 80, 35)
        income = st.slider("Annual Income (₹)", 200000, 2000000, 800000, step=50000)
        spending = st.slider("Annual Spending (₹)", 50000, 500000, 150000, step=10000)
        
        # Create vector
        customer_vector = [age, income/1000, spending/1000]  # Scale for better visualization
        
        st.markdown(f"""
        **Customer Vector:** `[{age}, {income/1000:.0f}k, {spending/1000:.0f}k]`
        
        **Arjun's Realization:** This customer is now a mathematical object he can work with!
        """)
    
    with col2:
        # 3D visualization of customer vector
        fig = go.Figure(data=go.Scatter3d(
            x=[0, age],
            y=[0, income/1000],
            z=[0, spending/1000],
            mode='lines+markers',
            line=dict(color='blue', width=6),
            marker=dict(size=[8, 12], color=['red', 'blue'])
        ))
        
        fig.update_layout(
            title="Customer as a Vector in 3D Space",
            scene=dict(
                xaxis_title="Age",
                yaxis_title="Income (₹k)",
                zaxis_title="Spending (₹k)"
            ),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Vector Operations
    st.markdown("---")
    st.subheader("🔢 Vector Operations: Comparing Customers")
    
    st.markdown("""
    **Arjun's Next Challenge:** How to compare customers and find patterns?
    **Solution:** Vector operations!
    """)
    
    # Two customer comparison
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Customer A:**")
        age_a = st.number_input("Age A", 18, 80, 30, key="age_a")
        income_a = st.number_input("Income A (₹k)", 200, 2000, 600, key="income_a")
        spending_a = st.number_input("Spending A (₹k)", 50, 500, 120, key="spending_a")
        vector_a = np.array([age_a, income_a, spending_a])
    
    with col2:
        st.markdown("**Customer B:**")
        age_b = st.number_input("Age B", 18, 80, 45, key="age_b")
        income_b = st.number_input("Income B (₹k)", 200, 2000, 900, key="income_b")
        spending_b = st.number_input("Spending B (₹k)", 50, 500, 200, key="spending_b")
        vector_b = np.array([age_b, income_b, spending_b])
    
    with col3:
        st.markdown("**Vector Operations:**")
        
        # Addition
        vector_sum = vector_a + vector_b
        st.write(f"**Addition (A + B):**")
        st.write(f"`[{vector_sum[0]:.0f}, {vector_sum[1]:.0f}, {vector_sum[2]:.0f}]`")
        st.write("*Average customer profile*")
        
        # Difference
        vector_diff = vector_b - vector_a
        st.write(f"**Difference (B - A):**")
        st.write(f"`[{vector_diff[0]:.0f}, {vector_diff[1]:.0f}, {vector_diff[2]:.0f}]`")
        st.write("*How much B exceeds A*")
        
        # Dot product (similarity)
        dot_product = np.dot(vector_a, vector_b)
        st.write(f"**Dot Product:** `{dot_product:.0f}`")
        st.write("*Customer similarity measure*")
    
    # Section 2: Matrices
    st.markdown("---")
    st.header("2️⃣ Matrices: The Complete Customer Database")
    
    st.markdown("""
    **Arjun's Breakthrough:** Instead of dealing with customers one by one, he can organize 
    ALL customers into a **matrix** - a table where each row is a customer vector!
    
    **Matrix = Collection of Vectors = Complete Database**
    """)
    
    # Generate sample customer data
    np.random.seed(42)
    n_customers = st.slider("Number of Customers to Analyze", 3, 10, 5)
    
    # Generate realistic customer data
    ages = np.random.randint(25, 65, n_customers)
    incomes = np.random.randint(300, 1500, n_customers)
    spendings = incomes * 0.15 + np.random.randint(-50, 50, n_customers)
    
    customer_matrix = np.column_stack((ages, incomes, spendings))
    
    # Display matrix
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Customer Matrix")
        df = pd.DataFrame(customer_matrix, 
                         columns=['Age', 'Income (₹k)', 'Spending (₹k)'],
                         index=[f'Customer {i+1}' for i in range(n_customers)])
        st.dataframe(df, use_container_width=True)
        
        st.markdown(f"""
        **Matrix Dimensions:** {n_customers} × 3
        - **Rows:** {n_customers} customers  
        - **Columns:** 3 attributes
        - **Total elements:** {n_customers * 3}
        """)
    
    with col2:
        st.subheader("🎯 Matrix Visualization")
        fig = go.Figure(data=go.Scatter3d(
            x=customer_matrix[:, 0],
            y=customer_matrix[:, 1], 
            z=customer_matrix[:, 2],
            mode='markers',
            marker=dict(
                size=8,
                color=customer_matrix[:, 2],  # Color by spending
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Spending (₹k)")
            ),
            text=[f'Customer {i+1}' for i in range(n_customers)],
            hovertemplate='<b>%{text}</b><br>Age: %{x}<br>Income: ₹%{y}k<br>Spending: ₹%{z}k'
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis_title="Age",
                yaxis_title="Income (₹k)",
                zaxis_title="Spending (₹k)"
            ),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 3: Systems of Equations
    st.markdown("---")
    st.header("3️⃣ Systems of Equations: Predicting Customer Behavior")
    
    st.markdown("""
    **Arjun's Advanced Challenge:** The retail chain wants to predict customer spending 
    based on age and income. He needs to find the relationship:
    
    `Spending = a × Age + b × Income + c`
    
    **The Problem:** He has multiple customers, so multiple equations to solve simultaneously!
    """)
    
    # Interactive system solver
    st.subheader("🎯 Solve the Spending Prediction System")
    
    st.markdown("""
    **Arjun's Method:** Use the first 3 customers to create a system of equations:
    """)
    
    if n_customers >= 3:
        # Take first 3 customers
        sample_customers = customer_matrix[:3]
        
        # Display the system
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**System of Equations:**")
            for i, customer in enumerate(sample_customers):
                age, income, spending = customer
                st.write(f"`{spending:.0f} = a × {age:.0f} + b × {income:.0f} + c`")
            
            st.markdown("""
            **In Matrix Form:** `AX = B`
            - **A:** Coefficient matrix (ages, incomes, 1s)  
            - **X:** Unknown vector [a, b, c]  
            - **B:** Result vector (spendings)
            """)
        
        with col2:
            # Solve the system
            A = np.column_stack((sample_customers[:, 0], sample_customers[:, 1], np.ones(3)))
            B = sample_customers[:, 2]
            
            try:
                X = np.linalg.solve(A, B)
                a, b, c = X
                
                st.markdown("**Solution Found! 🎉**")
                st.write(f"**a (Age coefficient):** {a:.2f}")
                st.write(f"**b (Income coefficient):** {b:.3f}")  
                st.write(f"**c (Base spending):** {c:.0f}")
                
                st.markdown(f"""
                **Arjun's Prediction Formula:**
                `Spending = {a:.2f} × Age + {b:.3f} × Income + {c:.0f}`
                """)
                
                # Test the prediction
                st.markdown("---")
                st.subheader("🧪 Test Arjun's Formula")
                test_age = st.number_input("Test Age", 20, 70, 40)
                test_income = st.number_input("Test Income (₹k)", 300, 1500, 800)
                
                predicted_spending = a * test_age + b * test_income + c
                st.success(f"**Predicted Spending:** ₹{predicted_spending:.0f}k per year")
                
            except np.linalg.LinAlgError:
                st.error("System cannot be solved - customers might be too similar!")
    
    # Business Applications
    st.markdown("---")
    st.header("💼 Arjun's Business Applications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Customer Segmentation**
        - Each customer = vector
        - Group similar vectors  
        - Identify customer types
        - Targeted marketing
        """)
    
    with col2:
        st.markdown("""
        **📊 Predictive Modeling**
        - Multiple variables → outcome
        - Systems of equations
        - Forecasting behavior
        - Risk assessment  
        """)
    
    with col3:
        st.markdown("""
        **🔍 Pattern Recognition**
        - Matrix operations
        - Data relationships
        - Hidden insights
        - Strategic decisions
        """)
    
    # Key Takeaways
    st.markdown("---")
    st.header("🎓 Arjun's Key Discoveries")
    
    st.success("""
    **🔑 Mathematical Superpowers Unlocked:**
    
    ✅ **Vectors** → Represent complex entities (customers, products) as mathematical objects  
    ✅ **Matrices** → Organize entire databases for systematic analysis  
    ✅ **Vector Operations** → Compare, combine, and analyze relationships  
    ✅ **Systems of Equations** → Solve multi-variable business prediction problems  
    
    **🚀 Business Impact:**
    From overwhelming spreadsheets → Systematic, mathematical analysis of customer data!
    """)
    
    # Practice Exercises
    st.markdown("---")
    st.subheader("💪 Practice: Apply Arjun's Methods")
    
    
    with st.expander("📝 Exercise : Product Analysis"):
        st.markdown("""
        **Scenario:** Analyze 3 products with vectors `[price, sales, profit_margin]`
        
        - Product A: `[100, 500, 0.2]`
        - Product B: `[150, 300, 0.3]`  
        - Product C: `[80, 700, 0.15]`
        
        **Tasks:**
        1. Which product has highest total performance? (hint: dot product with `[1,1,1]`)
        2. Create the product matrix
        3. Find average product profile (matrix column means)
        """)
        
        # MOVE THESE DEFINITIONS OUTSIDE THE BUTTON BLOCK:
        product_a = np.array([100, 500, 0.2])
        product_b = np.array([150, 300, 0.3])
        product_c = np.array([80, 700, 0.15])
    
        if st.button("Show Solutions", key="exercise1_solution"):
            st.markdown("---")
            st.markdown("### 🔍 **Solutions:**")
            
            # Solution 1: Total performance
            st.markdown("**1. Total Performance Analysis:**")
            performance_vector = np.array([1, 1, 1])
            
            perf_a = np.dot(product_a, performance_vector)
            perf_b = np.dot(product_b, performance_vector) 
            perf_c = np.dot(product_c, performance_vector)
            
            st.write(f"• Product A performance: {perf_a:.1f}")
            st.write(f"• Product B performance: {perf_b:.1f}")
            st.write(f"• Product C performance: {perf_c:.1f}")
            
            best_product = max([("A", perf_a), ("B", perf_b), ("C", perf_c)], key=lambda x: x[1])
            st.success(f"🏆 **Winner:** Product {best_product[0]} with score {best_product[1]:.1f}")
            
            # Solution 2: Product matrix
            st.markdown("**2. Product Matrix:**")
            product_matrix = np.array([product_a, product_b, product_c])
            df = pd.DataFrame(product_matrix, 
                            columns=['Price (₹)', 'Sales (units)', 'Profit Margin'],
                            index=['Product A', 'Product B', 'Product C'])
            st.dataframe(df)
            
            # Solution 3: Average profile
            st.markdown("**3. Average Product Profile:**")
            avg_profile = np.mean(product_matrix, axis=0)
            st.write(f"**Average:** `[{avg_profile[0]:.0f}, {avg_profile[1]:.0f}, {avg_profile[2]:.2f}]`")
            st.write("**Interpretation:** Average price ₹110, 500 units sales, 22% profit margin")

    
    
    
    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Previous: Linear Algebra Overview"):
            st.session_state.page = 'linear_algebra'
            st.rerun()
    
    with col2:
        if st.button("Next: Eigenvalues & Eigenvectors →"):
            st.session_state.page = 'linear_algebra_eigen'
            st.rerun()
    
    st.markdown("---")
    st.info("""
    🎯 **Next in Arjun's Journey:** 
    Now that Arjun can organize and analyze multi-dimensional data, he'll discover hidden 
    patterns that remain stable even when business conditions change - the power of 
    **Eigenvalues and Eigenvectors**!
    """)