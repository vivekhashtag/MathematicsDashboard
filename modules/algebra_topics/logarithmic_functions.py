import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import log, log2

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
    .logarithmic-highlight {
        background-color: #fce4ec;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #e91e63;
        margin: 1rem 0;
    }
    .diminishing-returns {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_logarithmic_functions():
    # Header with back navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("← Back to Algebra"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with col2:
        st.title("📉 Logarithmic Functions")
    
    # Breadcrumb
    st.markdown("**Home** > **Algebra** > **Logarithmic Functions**")
    
    # Main Title
    st.markdown('<h1 class="main-header">🎯 Maya\'s Learning Curve - Logarithmic Functions</h1>', unsafe_allow_html=True)
    
    # Business Storyline
    st.header("📖 Maya's Skill Development Journey")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Maya wants to become a tea-making master!** After growing her customer base exponentially, 
        she realizes she needs to make tea faster to serve everyone efficiently.
        
        She starts tracking her speed (cups per hour) as she practices more and more. But something puzzling happens...
        
        **"This is strange!"** Maya notices. **"In my first week, I improved by 8 cups per hour. 
        But now after months of practice, I barely improve by 1-2 cups per hour. Why is it getting so hard to improve?"**
        
        Let's help Maya understand the mathematics behind **diminishing returns**!
        """)
    
    with col2:
        st.info("""
        **What is a Logarithmic Function?**
        
        Shows **diminishing returns** - big improvements 
        at first, then smaller and smaller gains.
        
        It's the OPPOSITE of exponential growth!
        """)
    
    # Maya's Original Data
    st.header("📊 Maya's Practice Results")
    
    maya_practice_data = {
        'Weeks of Practice': [1, 2, 4, 8, 16, 32],
        'Cups per Hour': [10, 18, 25, 32, 39, 46],
        'Improvement from Previous': ['-', '+8 cups', '+7 cups', '+7 cups', '+7 cups', '+7 cups'],
        'Maya\'s Observation': [
            "I'm so slow and clumsy",
            "Getting much better!", 
            "Good improvement",
            "Still improving, but slower",
            "Tiny improvements now",
            "Almost reached my limit"
        ]
    }
    
    df_maya = pd.DataFrame(maya_practice_data)
    st.dataframe(df_maya, use_container_width=True)
    
    # Maya's Discovery
    st.markdown('<div class="discovery-highlight">', unsafe_allow_html=True)
    st.subheader("💡 Maya's Big Discovery")
    st.markdown("""
    **"Wait! I keep improving by about 7 cups each time I DOUBLE my practice time. 
    It's not about the weeks - it's about doubling the effort!"**
    
    **Pattern Maya noticed:**
    - **1 week → 2 weeks:** Double the practice = +8 cups improvement
    - **2 weeks → 4 weeks:** Double the practice = +7 cups improvement  
    - **4 weeks → 8 weeks:** Double the practice = +7 cups improvement
    - **8 weeks → 16 weeks:** Double the practice = +7 cups improvement
    
    **Every time Maya doubles her practice time, she gets roughly the same improvement!**
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Logarithmic Function Explorer
    st.header("🎛️ Interactive Learning Curve Simulator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        base_skill = st.slider("Starting Skill Level", 5, 20, 10, 1,
                              help="Maya's natural ability before practice")
    
    with col2:
        improvement_per_doubling = st.slider("Improvement per Doubling", 3, 15, 7, 1,
                                           help="How much Maya improves each time she doubles practice time")
    
    with col3:
        max_weeks = st.slider("Weeks to Show", 16, 128, 64, 16,
                             help="How far to project Maya's learning curve")
    
    # Generate logarithmic data
    weeks_range = np.logspace(0, log2(max_weeks), 100, base=2)  # From 1 to max_weeks, logarithmically spaced
    
    # Maya's logarithmic equation: Skill = base_skill + improvement_per_doubling * log2(weeks)
    def maya_skill(weeks):
        return base_skill + improvement_per_doubling * np.log2(weeks)
    
    skills = maya_skill(weeks_range)
    
    # Create comprehensive visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: The Logarithmic Learning Curve
    ax1.plot(weeks_range, skills, 'b-', linewidth=3, label=f'Skill = {base_skill} + {improvement_per_doubling} × log₂(weeks)')
    
    # Add Maya's actual data points for key weeks
    key_weeks = [1, 2, 4, 8, 16, 32]
    key_skills = [maya_skill(w) for w in key_weeks if w <= max_weeks]
    key_weeks_filtered = [w for w in key_weeks if w <= max_weeks]
    
    ax1.scatter(key_weeks_filtered, key_skills, color='red', s=100, zorder=5, label='Maya\'s Practice Milestones')
    
    # Highlight plateau effect
    plateau_weeks = max_weeks * 0.8
    plateau_skill = maya_skill(plateau_weeks)
    ax1.plot(plateau_weeks, plateau_skill, 'go', markersize=12, label=f'Plateau Region: {plateau_skill:.1f} cups/hour')
    
    ax1.set_xlabel('Weeks of Practice')
    ax1.set_ylabel('Cups per Hour')
    ax1.set_title('Maya\'s Learning Curve: Diminishing Returns')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log', base=2)
    
    # Plot 2: Linear vs Logarithmic Comparison
    # Linear improvement would be: base_skill + (weeks - 1) * improvement_rate
    linear_improvement_rate = improvement_per_doubling / 2  # Approximate linear rate
    linear_skills = base_skill + (weeks_range - 1) * linear_improvement_rate
    
    ax2.plot(weeks_range, skills, 'b-', linewidth=3, label='Logarithmic (Real Learning)')
    ax2.plot(weeks_range, linear_skills, 'r--', linewidth=3, label='Linear (Unrealistic)')
    
    ax2.set_xlabel('Weeks of Practice')
    ax2.set_ylabel('Cups per Hour')
    ax2.set_title('Why Learning Follows Logarithmic Pattern')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Add annotation showing the difference
    mid_weeks = max_weeks / 4
    log_skill_mid = maya_skill(mid_weeks)
    lin_skill_mid = base_skill + (mid_weeks - 1) * linear_improvement_rate
    
    ax2.annotate(f'Reality: Diminishing returns\nmake improvement harder', 
                xy=(mid_weeks, log_skill_mid), xytext=(mid_weeks * 2, log_skill_mid + 5),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=10, ha='center')
    
    # Plot 3: Improvement Rate Analysis
    # Calculate the derivative (rate of improvement)
    weeks_for_derivative = weeks_range[1:]
    improvement_rate = np.diff(skills) / np.diff(weeks_range)
    
    ax3.plot(weeks_for_derivative, improvement_rate, 'purple', linewidth=3, label='Rate of Improvement')
    ax3.set_xlabel('Weeks of Practice')
    ax3.set_ylabel('Cups/Hour Improvement per Week')
    ax3.set_title('Why Maya Gets Frustrated: Slowing Improvement Rate')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    ax3.annotate('Fast improvement\nat the beginning', 
                xy=(2, improvement_rate[10]), xytext=(8, improvement_rate[10] + 0.5),
                arrowprops=dict(arrowstyle='->', color='green'),
                fontsize=10, ha='center')
    
    # Plot 4: Doubling Effort Analysis
    doubling_weeks = [1, 2, 4, 8, 16, 32, 64]
    doubling_weeks_filtered = [w for w in doubling_weeks if w <= max_weeks]
    doubling_skills = [maya_skill(w) for w in doubling_weeks_filtered]
    doubling_improvements = [0] + [doubling_skills[i] - doubling_skills[i-1] for i in range(1, len(doubling_skills))]
    
    ax4.bar(range(len(doubling_weeks_filtered)), doubling_improvements, 
            color=['gray'] + ['orange'] * (len(doubling_improvements) - 1),
            alpha=0.7, label='Improvement from Doubling Effort')
    ax4.set_xlabel('Doubling Period')
    ax4.set_ylabel('Improvement (Cups/Hour)')
    ax4.set_title('Consistent Gain from Doubling Effort')
    ax4.set_xticks(range(len(doubling_weeks_filtered)))
    ax4.set_xticklabels([f'{w}w' for w in doubling_weeks_filtered])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Mathematical Representation
    st.header("🧮 Maya's Logarithmic Equation")
    
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **Maya's Learning Curve Formula:**
    
    **Cups per Hour = {base_skill} + {improvement_per_doubling} × log₂(Weeks)**
    
    **Breaking it down:**
    - **{base_skill}**: Maya's natural starting ability (no practice)
    - **{improvement_per_doubling}**: Improvement gained from each doubling of effort
    - **log₂(Weeks)**: How many doubling periods Maya has completed
    - **Weeks**: The time period we're calculating for
    
    **What log₂(Weeks) means:** "How many times did Maya double her practice from 1 week?"
    - Week 1: log₂(1) = 0 (no doublings yet)
    - Week 4: log₂(4) = 2 (doubled twice: 1→2→4)
    - Week 8: log₂(8) = 3 (doubled thrice: 1→2→4→8)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Simple Logarithm Explanation
    st.markdown('<div class="logarithmic-highlight">', unsafe_allow_html=True)
    st.subheader("🔢 What is a Logarithm? (Super Simple)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Logarithm = "How many times do I multiply?"**
        
        **Real Examples:**
        - **log₂(8) = 3** because 2 × 2 × 2 = 8 (3 times)
        - **log₂(16) = 4** because 2 × 2 × 2 × 2 = 16 (4 times)
        - **log₁₀(100) = 2** because 10 × 10 = 100 (2 times)
        """)
    
    with col2:
        st.markdown("""
        **Maya's Business Translation:**
        
        Instead of "How many times do I multiply?"
        Maya asks: **"How many times did I double my practice?"**
        
        - Week 1 → Week 8: 1→2→4→8 = **3 doublings**
        - Week 1 → Week 16: 1→2→4→8→16 = **4 doublings**
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Dashboard
    st.header("📊 Maya's Learning Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        current_skill_8_weeks = maya_skill(8)
        st.metric("Skill at 8 weeks", f"{current_skill_8_weeks:.1f} cups/hour")
    
    with col2:
        current_skill_32_weeks = maya_skill(32)
        st.metric("Skill at 32 weeks", f"{current_skill_32_weeks:.1f} cups/hour")
    
    with col3:
        improvement_8_to_32 = current_skill_32_weeks - current_skill_8_weeks
        st.metric("32w vs 8w improvement", f"+{improvement_8_to_32:.1f} cups/hour", 
                 "From 4x more practice")
    
    with col4:
        # Calculate plateau level (theoretical maximum)
        plateau_level = maya_skill(max_weeks)
        st.metric("Plateau Level", f"~{plateau_level:.1f} cups/hour", "Near maximum")
    
    # Pattern Analysis Table
    st.header("🔍 Maya's Doubling Pattern Analysis")
    
    st.markdown('<div class="diminishing-returns">', unsafe_allow_html=True)
    st.subheader("Understanding Diminishing Returns")
    
    # Create detailed analysis table
    doubling_analysis_weeks = [1, 2, 4, 8, 16, 32]
    if max_weeks >= 64:
        doubling_analysis_weeks.append(64)
    
    analysis_data = []
    
    for i, weeks in enumerate(doubling_analysis_weeks):
        skill_level = maya_skill(weeks)
        doubling_periods = log2(weeks) if weeks > 0 else 0
        
        if i == 0:
            improvement = 0
            effort_multiplier = 1
        else:
            prev_skill = maya_skill(doubling_analysis_weeks[i-1])
            improvement = skill_level - prev_skill
            effort_multiplier = weeks / doubling_analysis_weeks[0]
        
        analysis_data.append({
            'Weeks': int(weeks),
            'Doubling Periods': f'{doubling_periods:.0f}',
            'Skill Level': f'{skill_level:.1f} cups/hour',
            'Improvement': f'+{improvement:.1f}' if improvement > 0 else '-',
            'Total Effort': f'{effort_multiplier:.0f}x',
            'Efficiency': 'High' if weeks <= 4 else 'Medium' if weeks <= 16 else 'Low'
        })
    
    df_analysis = pd.DataFrame(analysis_data)
    st.dataframe(df_analysis, use_container_width=True)
    
    st.write("""
    **Key Insight:** Maya gets roughly the same improvement (+7 cups/hour) each time she doubles her effort, 
    but doubling effort becomes exponentially harder (1→2→4→8→16→32 weeks)!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Business Calculator
    st.header("🤔 Maya's Learning Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Skill Predictor")
        target_weeks = st.number_input("Predict skill after how many weeks:", 
                                      min_value=1, max_value=256, value=24, step=1)
        
        predicted_skill = maya_skill(target_weeks)
        doubling_periods = log2(target_weeks)
        
        st.success(f"📈 After {target_weeks} weeks: {predicted_skill:.1f} cups/hour")
        
        # Show the calculation
        st.info(f"Calculation: {base_skill} + {improvement_per_doubling} × log₂({target_weeks}) = {base_skill} + {improvement_per_doubling} × {doubling_periods:.2f} = {predicted_skill:.1f}")
        
        # Compare to starting skill
        total_improvement = predicted_skill - base_skill
        st.write(f"**Total improvement:** +{total_improvement:.1f} cups/hour ({((predicted_skill/base_skill - 1) * 100):.0f}% increase)")
    
    with col2:
        st.subheader("🔍 Target Skill Finder")
        target_skill = st.number_input("When will Maya reach this skill level:", 
                                      min_value=float(base_skill), max_value=float(base_skill + 50), 
                                      value=float(base_skill + 20), step=1.0)
        
        if target_skill > base_skill:
            # Solve: target_skill = base_skill + improvement_per_doubling * log2(weeks)
            # log2(weeks) = (target_skill - base_skill) / improvement_per_doubling
            # weeks = 2^((target_skill - base_skill) / improvement_per_doubling)
            
            log_weeks = (target_skill - base_skill) / improvement_per_doubling
            weeks_needed = 2 ** log_weeks
            
            st.info(f"🗓️ Maya will reach {target_skill:.1f} cups/hour after **{weeks_needed:.1f} weeks**")
            
            # Show what this means in practical terms
            months = weeks_needed / 4.33  # Average weeks per month
            years = weeks_needed / 52
            
            if years < 1:
                st.write(f"That's about **{months:.1f} months** of practice")
            else:
                st.write(f"That's about **{years:.1f} years** of practice")
                
            # Show the effort required
            st.warning(f"⚡ This requires {weeks_needed/1:.0f}x more effort than week 1!")
        else:
            st.error("Target skill must be higher than starting skill!")
    
    # Business Insights
    st.header("💡 Logarithmic Learning Insights")
    
    st.markdown('<div class="business-insight">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Why Learning is Logarithmic")
        st.write("**Skill development follows diminishing returns:**")
        st.write("• **Beginner:** Every practice session teaches something new")
        st.write("• **Intermediate:** Still learning, but fewer breakthroughs")  
        st.write("• **Advanced:** Tiny improvements require enormous effort")
        st.write("• **Expert:** Approaching human limits")
        
        st.subheader("📈 The Doubling Principle")
        st.write(f"**Maya consistently improves {improvement_per_doubling} cups/hour when she doubles practice time**")
        st.write("• Same improvement, exponentially more effort")
        st.write("• This is why mastery takes so long")
        st.write("• Early gains are deceptively easy")
    
    with col2:
        st.subheader("🏢 Business Applications")
        st.write("**Logarithmic patterns appear in:**")
        st.write("• **Employee training** - quick initial gains, slow mastery")
        st.write("• **Customer satisfaction** - basic features delight, advanced barely noticed")
        st.write("• **Market penetration** - easy first 10%, extremely hard last 10%")
        st.write("• **Product quality** - good to great costs exponentially more")
        
        st.subheader("🚨 Maya's Strategic Insights")
        st.write("**Maya now understands:**")
        st.write("• Why hiring experts costs much more")
        st.write("• When to focus on improvement vs other areas")
        st.write("• How to set realistic skill development goals")
        st.write("• Why 'good enough' is often the right business choice")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Practice Exercises
    st.header("🎯 Practice with Maya's Learning Story")
    
    with st.expander("📝 Exercise 1: Maya's Training Program"):
        st.markdown(f"""
        Maya wants to train a new employee. Based on her learning curve equation:
        **Skill = {base_skill} + {improvement_per_doubling} × log₂(weeks)**
        
        **Questions:**
        1. How skilled will the new employee be after 16 weeks?
        2. How long to reach 80% of Maya's current skill (week 32)?
        3. Is it worth training someone for 64 weeks vs 32 weeks?
        """)
        
        if st.button("Show Solutions", key="ex1_log"):
            maya_current_skill = maya_skill(32)
            employee_16_weeks = maya_skill(16)
            target_80_percent = 0.8 * maya_current_skill
            
            # Solve for 80% skill: target = base_skill + improvement_per_doubling * log2(weeks)
            log_weeks_80 = (target_80_percent - base_skill) / improvement_per_doubling
            weeks_for_80_percent = 2 ** log_weeks_80
            
            employee_64_weeks = maya_skill(64)
            employee_32_weeks = maya_skill(32)
            improvement_32_to_64 = employee_64_weeks - employee_32_weeks
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Employee skill after 16 weeks:**
               - Skill = {base_skill} + {improvement_per_doubling} × log₂(16) = {base_skill} + {improvement_per_doubling} × 4 = **{employee_16_weeks:.1f} cups/hour**
            
            2. **Time to reach 80% of Maya's skill:**
               - Maya's current skill (32 weeks): {maya_current_skill:.1f} cups/hour
               - 80% target: {target_80_percent:.1f} cups/hour
               - **Time needed: {weeks_for_80_percent:.1f} weeks** (about {weeks_for_80_percent/4.33:.1f} months)
            
            3. **32 weeks vs 64 weeks training:**
               - 32 weeks: {employee_32_weeks:.1f} cups/hour
               - 64 weeks: {employee_64_weeks:.1f} cups/hour  
               - **Additional improvement: +{improvement_32_to_64:.1f} cups/hour for 2x more training**
               - **Business decision:** Depends on cost vs benefit of that extra {improvement_32_to_64:.1f} cups/hour
            
            **Business insight:** Logarithmic learning means longer training has diminishing returns!
            """)
    
    with st.expander("📝 Exercise 2: Maya's Product Quality Dilemma"):
        st.markdown(f"""
        Maya is considering product improvements. Customer satisfaction follows a similar logarithmic pattern:
        **Satisfaction = 60 + 15 × log₂(Quality_Investment)**
        
        Maya can invest 1x, 2x, 4x, or 8x her base quality budget.
        
        **Questions:**
        1. What satisfaction level does each investment give?
        2. Which investment gives the best satisfaction per dollar?
        3. When does Maya hit diminishing returns?
        """)
        
        if st.button("Show Solutions", key="ex2_log"):
            base_satisfaction = 60
            satisfaction_per_doubling = 15
            
            investments = [1, 2, 4, 8]
            satisfactions = [base_satisfaction + satisfaction_per_doubling * log2(inv) for inv in investments]
            satisfaction_per_dollar = [sat / inv for sat, inv in zip(satisfactions, investments)]
            
            st.markdown(f"""
            **Solutions:**
            
            1. **Satisfaction levels:**""")
            
            for i, inv in enumerate(investments):
                st.write(f"   - {inv}x investment: {satisfactions[i]:.1f}% satisfaction")
            
            st.markdown(f"""
            2. **Satisfaction per dollar:**""")
            
            for i, inv in enumerate(investments):
                st.write(f"   - {inv}x investment: {satisfaction_per_dollar[i]:.1f} satisfaction points per dollar")
            
            best_investment = investments[satisfaction_per_dollar.index(max(satisfaction_per_dollar))]
            
            st.markdown(f"""
            **Best value: {best_investment}x investment** (highest satisfaction per dollar)
            
            3. **Diminishing returns start immediately!**
               - Each doubling gives +{satisfaction_per_doubling} satisfaction points
               - But costs double each time
               - **1x to 2x:** Best value ({satisfaction_per_dollar[1]:.1f} points per dollar)
               - **2x to 4x:** Lower value ({satisfaction_per_dollar[2]:.1f} points per dollar)
               - **4x to 8x:** Lowest value ({satisfaction_per_dollar[3]:.1f} points per dollar)
            
            **Business insight:** Quality improvements follow logarithmic returns - invest wisely!
            """)
    
    # Key Takeaways
    st.header("🎓 Key Learning Takeaways")
    
    st.success("""
    **Logarithmic Functions in Maya's Business:**
    
    1. **Diminishing Returns:** More effort gives smaller improvements over time - the opposite of exponential growth
    2. **Learning Curve Reality:** Quick initial progress, then mastery becomes exponentially expensive  
    3. **Doubling Principle:** Consistent improvement requires exponentially more effort each time
    4. **Strategic Planning:** Understanding logarithmic costs helps decide when to stop improving
    5. **Expertise Premium:** Why skilled professionals command much higher wages
    6. **"Good Enough" Philosophy:** Perfect is often the enemy of profitable in business
    
    **Maya's Transformation:** From frustration with slowing progress to understanding the mathematical reality of skill development!
    
    **The Insight:** Logarithmic functions help you understand the true cost of excellence in any business!
    """)
    
    # Navigation
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("← Exponential Functions"):
            st.session_state.page = 'algebra_exponential'
            st.rerun()
    
    with nav_col2:
        if st.button("🏠 Back to Algebra Overview"):
            st.session_state.page = 'algebra'
            st.rerun()
    
    with nav_col3:
        if st.button("Piecewise Functions →"):
            st.session_state.page = 'algebra_piecewise'
            st.rerun()