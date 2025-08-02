import streamlit as st
# Set page configuration - DISABLE sidebar auto-navigation
st.set_page_config(
    page_title="Mathematics Learning Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)
# Import page functions
from modules.homepage import show_homepage
from modules.algebra_overview import show_algebra_overview
from modules.algebra_topics.linear_functions import show_linear_functions
from modules.algebra_topics.quadratic_functions import show_quadratic_functions
from modules.algebra_topics.exponential_functions import show_exponential_functions
from modules.algebra_topics.logarithmic_functions import show_logarithmic_functions
from modules.algebra_topics.piecewise_functions import show_piecewise_functions
from modules.algebra_topics.inverse_functions import show_inverse_functions
from modules.algebra_topics.systems_equations import show_systems_equations



# Hide the default sidebar navigation
st.markdown("""
<style>
    .css-1d391kg {display: none;}  /* Hide sidebar */
    .css-1rs6os {display: none;}   /* Hide sidebar toggle */
    .css-17eq0hr {display: none;}  /* Hide sidebar content */
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Main navigation router
def main():
    if st.session_state.page == 'home':
        show_homepage()
    
    elif st.session_state.page == 'algebra':
        show_algebra_overview()
    
    # Individual algebra topics
    elif st.session_state.page == 'algebra_linear':
        show_linear_functions()
    
    elif st.session_state.page == 'algebra_quadratic':
        show_quadratic_functions()
    
    elif st.session_state.page == 'algebra_exponential':
        show_exponential_functions()
    
    elif st.session_state.page == 'algebra_logarithmic':
        show_logarithmic_functions()
    
    elif st.session_state.page == 'algebra_piecewise':
        show_piecewise_functions()
    
    elif st.session_state.page == 'algebra_inverse':
        show_inverse_functions()
    
    elif st.session_state.page == 'algebra_systems':
        show_systems_equations()
    
    else:
        # Default fallback to homepage
        st.session_state.page = 'home'
        show_homepage()

if __name__ == "__main__":
    main()