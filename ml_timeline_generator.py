import streamlit as st

st.set_page_config(page_title="ML Timeline Generator", page_icon="📅")

st.title("📅 ML Project Timeline Generator")
st.markdown("Estimate how long it takes to go from raw data to a deployed ML model based on your setup.")

# --- User Inputs ---
problem_type = st.selectbox("Select Problem Type:", ["Classification", "Regression", "Clustering"])
team_size = st.selectbox("Team Size:", ["Solo", "2–3 Members", "Full Team"])
data_quality = st.selectbox("Data Quality:", ["Clean", "Semi-Clean", "Messy"])
deployment_type = st.selectbox("Deployment Type:", ["Streamlit App", "REST API", "Enterprise Pipeline"])

# --- Button ---
if st.button("💡 Suggest Timeline"):
    
    def estimate_days(base, multiplier):
        return int(base * multiplier)

    def get_multiplier(team, data):
        team_factors = {"Solo": 1.2, "2–3 Members": 1.0, "Full Team": 0.8}
        data_factors = {"Clean": 0.8, "Semi-Clean": 1.0, "Messy": 1.4}
        return team_factors[team] * data_factors[data]

    # Base durations (in days)
    phases = {
        "Data Understanding & Cleanup": 4,
        "EDA & Feature Engineering": 3,
        "Model Building & Tuning": 5,
        "Testing & Validation": 3,
        "Deployment": {"Streamlit App": 2, "REST API": 4, "Enterprise Pipeline": 6}
    }

    multiplier = get_multiplier(team_size, data_quality)

    # --- Results ---
    st.subheader("📊 Estimated Timeline:")
    total_days = 0
    for phase, base in phases.items():
        if isinstance(base, dict):
            days = estimate_days(base[deployment_type], multiplier)
        else:
            days = estimate_days(base, multiplier)
        total_days += days
        st.write(f"**{phase}** — {days} days")

    st.markdown("---")
    st.write(f"📦 **Total Estimated Time:** ~{total_days} working days (~{round(total_days / 5)} weeks)")

    # --- Stack Suggestions ---
    st.subheader("⚙️ Suggested Stack")
    st.caption("📌 Note: Model and tool selection depends on your business needs, data type, and team expertise.")

    if problem_type == "Classification":
        st.write("Try exploring:")
        st.markdown("""
        - Logistic Regression (baseline)
        - Random Forest / Gradient Boosting
        - SVM / Decision Trees
        - Neural Networks for complex patterns
        """)
    elif problem_type == "Regression":
        st.write("Try exploring:")
        st.markdown("""
        - Linear Regression (baseline)
        - Decision Trees / Random Forest
        - Gradient Boosting (e.g., LightGBM)
        - Neural Networks for non-linear regression
        """)
    else:
        st.write("Try exploring:")
        st.markdown("""
        - KMeans / DBSCAN (unsupervised)
        - PCA / t-SNE for dimensionality reduction
        - Autoencoders for anomaly detection
        """)

    if deployment_type == "REST API":
        st.write("💡 Deployment Stack: FastAPI + Docker")
    elif deployment_type == "Enterprise Pipeline":
        st.write("💡 Deployment Stack: Airflow + MLflow + Azure/GCP")
    else:
        st.write("💡 Deployment Stack: Streamlit + GitHub")


    # --- Footer ---
st.markdown("---")
st.markdown("### 👩‍💻 Connect with Me")
st.markdown(
    """
    <div style='text-align: left; font-size: 16px;'>
        🔗 <a href='https://www.linkedin.com/in/jeslin-lois/' target='_blank'>LinkedIn</a><br>
        ✍️ <a href='https://medium.com/@jeslinloisss' target='_blank'>Medium</a>
    </div>
    """,
    unsafe_allow_html=True
)
