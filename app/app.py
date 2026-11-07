import json
from pathlib import Path
from random import choice

import numpy as np
import pandas as pd
import streamlit as st
from xgboost import XGBClassifier

APP_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_artifacts():
    model = XGBClassifier(n_jobs=1)
    model.load_model(APP_DIR / "xgboost_model.json")
    policy = json.loads((APP_DIR / "policy.json").read_text(encoding="utf-8"))
    return model, policy


st.title("Second-Look Lending · Team 1A")
st.caption("Class project demo. Score one synthetic applicant or upload a batch.")

mode = st.radio("Prediction mode", ["Single applicant", "Batch CSV"], horizontal=True)
single_applicant = mode == "Single applicant"

try:
    if single_applicant:
        samples = pd.read_csv(APP_DIR / "sample_applicants.csv")
        labels = {
            index: f"Sample {index + 1} · {'Thin-file' if flag == 1 else 'Established'}"
            for index, flag in samples["thin_file"].items()
        }

        def choose_random_sample():
            current = st.session_state["sample_applicant"]
            st.session_state["sample_applicant"] = choice(
                [index for index in labels if index != current]
            )

        selected = st.selectbox(
            "Synthetic applicant", list(labels), format_func=labels.__getitem__,
            key="sample_applicant",
        )
        st.button("Random applicant", on_click=choose_random_sample, disabled=len(labels) < 2)
        data = samples.loc[[selected]]
    else:
        uploaded = st.file_uploader("Engineered feature CSV", type="csv")
        if uploaded is None:
            st.stop()
        data = pd.read_csv(uploaded)

    model, policy = load_artifacts()
    features = policy["features"]
    missing = sorted(set(features) - set(data.columns))
    if missing:
        raise ValueError("Missing feature columns: " + ", ".join(missing))
    if data.empty:
        raise ValueError("The CSV must contain at least one row.")

    inputs = data[features].apply(pd.to_numeric, errors="raise").astype(float)
    if np.isinf(inputs.to_numpy()).any():
        raise ValueError("Feature values cannot contain infinity.")
    if not inputs["thin_file"].isin([0, 1]).all():
        raise ValueError("thin_file must be 0 or 1 for every row.")
except ValueError as exc:
    st.error(str(exc))
    st.stop()

thin_file = inputs["thin_file"].eq(1)
raw_pd = model.predict_proba(inputs)[:, 1]
policy_score = np.where(
    thin_file, raw_pd * policy["thin_file_factor"], raw_pd
)
cutoff = np.where(
    thin_file, policy["thin_file_cutoff"], policy["established_cutoff"]
)
approved = policy_score < cutoff

results = pd.DataFrame({
    "Row": range(1, len(inputs) + 1),
    "Segment": np.where(thin_file, "Thin-file", "Established"),
    "Raw PD": [f"{value:.4%}" for value in raw_pd],
    "Policy score": [f"{value:.4%}" for value in policy_score],
    "Cutoff": [f"{value:.0%}" for value in cutoff],
    "Simulated decision": np.where(approved, "Approve", "Decline"),
})

if single_applicant:
    result = results.iloc[0]
    pd_column, score_column, decision_column = st.columns(3)
    pd_column.metric("Raw PD", result["Raw PD"])
    score_column.metric("Policy score", result["Policy score"])
    decision_column.metric("Simulated decision", result["Simulated decision"])
    st.caption(f'{result["Segment"]} · Approval cutoff {result["Cutoff"]}')
else:
    st.metric("Simulated approval rate", f"{approved.mean():.1%}")
    st.dataframe(results, hide_index=True)
