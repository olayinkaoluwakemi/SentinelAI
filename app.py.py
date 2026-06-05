import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="SentinelAI | IoT Cybersecurity Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: white;
    margin-bottom: 24px;
}
.hero h1 {
    font-size: 44px;
    margin-bottom: 6px;
}
.hero p {
    font-size: 17px;
    color: #dbeafe;
}
.section-title {
    font-size: 23px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    data = pd.read_csv("data/iot_security_events.csv")
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    return data

def classify_risk(row):
    score = 0
    if row["failed_logins"] >= 10:
        score += 3
    if row["cpu_usage"] >= 80:
        score += 2
    if row["data_transfer_mb"] >= 75:
        score += 2
    if row["latency_ms"] >= 180:
        score += 1
    if row["predicted_anomaly"] == 1:
        score += 3

    if score >= 7:
        return "High"
    if score >= 4:
        return "Medium"
    return "Low"

def explain_event(row):
    reasons = []

    if row["failed_logins"] >= 10:
        reasons.append("high failed login attempts")
    if row["cpu_usage"] >= 80:
        reasons.append("abnormally high CPU usage")
    if row["data_transfer_mb"] >= 75:
        reasons.append("unusual data transfer volume")
    if row["latency_ms"] >= 180:
        reasons.append("elevated network latency")
    if row["predicted_anomaly"] == 1:
        reasons.append("machine learning anomaly flag")

    if not reasons:
        return "No major risk indicators detected."

    return "Flagged for " + ", ".join(reasons) + "."

data = load_data()

features = [
    "packet_count",
    "failed_logins",
    "cpu_usage",
    "memory_usage",
    "data_transfer_mb",
    "latency_ms"
]

scaler = StandardScaler()
scaled = scaler.fit_transform(data[features])

model = IsolationForest(contamination=0.09, random_state=42)
data["model_output"] = model.fit_predict(scaled)
data["predicted_anomaly"] = data["model_output"].apply(lambda value: 1 if value == -1 else 0)
data["risk_level"] = data.apply(classify_risk, axis=1)
data["explanation"] = data.apply(explain_event, axis=1)

st.markdown("""
<div class="hero">
    <h1>🛡️ SentinelAI</h1>
    <p>AI-powered cybersecurity monitoring for IoT systems. Detect anomalies, classify risk, and explain suspicious device behavior in plain English.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Dashboard Controls")
    st.caption("Filter incident activity by operational context.")

    location = st.multiselect(
        "Location",
        sorted(data["location"].unique()),
        default=sorted(data["location"].unique())
    )

    device_type = st.multiselect(
        "Device Type",
        sorted(data["device_type"].unique()),
        default=sorted(data["device_type"].unique())
    )

    risk = st.multiselect(
        "Risk Level",
        ["High", "Medium", "Low"],
        default=["High", "Medium", "Low"]
    )

    st.divider()
    st.caption("Portfolio Project")
    st.write("Built with Python, Streamlit, Scikit-learn, Plotly, and Pandas.")

filtered = data[
    data["location"].isin(location)
    & data["device_type"].isin(device_type)
    & data["risk_level"].isin(risk)
]

total_events = len(filtered)
anomalies = int(filtered["predicted_anomaly"].sum())
high_risk = int((filtered["risk_level"] == "High").sum())
medium_risk = int((filtered["risk_level"] == "Medium").sum())
avg_latency = round(filtered["latency_ms"].mean(), 1) if total_events else 0

st.markdown('<div class="section-title">Executive Security Overview</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Events", f"{total_events:,}")
c2.metric("Anomalies", f"{anomalies:,}")
c3.metric("High Risk", f"{high_risk:,}")
c4.metric("Medium Risk", f"{medium_risk:,}")
c5.metric("Avg Latency", f"{avg_latency} ms")

st.caption("These metrics help security and operations teams prioritize suspicious device activity.")

st.divider()

left, right = st.columns([1.25, 1])

with left:
    st.markdown('<div class="section-title">Risk Events Over Time</div>', unsafe_allow_html=True)
    risk_time = (
        filtered
        .groupby([pd.Grouper(key="timestamp", freq="2H"), "risk_level"])
        .size()
        .reset_index(name="events")
    )

    fig = px.line(
        risk_time,
        x="timestamp",
        y="events",
        color="risk_level",
        markers=True,
        labels={
            "timestamp": "Time",
            "events": "Event Count",
            "risk_level": "Risk Level"
        }
    )
    fig.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown('<div class="section-title">Risk Distribution</div>', unsafe_allow_html=True)
    risk_counts = filtered["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["risk_level", "count"]

    fig2 = px.pie(
        risk_counts,
        values="count",
        names="risk_level",
        hole=0.55
    )
    fig2.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig2, use_container_width=True)

left2, right2 = st.columns([1.1, 1])

with left2:
    st.markdown('<div class="section-title">Device Risk by Location</div>', unsafe_allow_html=True)
    device_risk = (
        filtered
        .groupby(["location", "risk_level"])
        .size()
        .reset_index(name="events")
    )

    fig3 = px.bar(
        device_risk,
        x="location",
        y="events",
        color="risk_level",
        barmode="group",
        labels={
            "location": "Location",
            "events": "Event Count",
            "risk_level": "Risk Level"
        }
    )
    fig3.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig3, use_container_width=True)

with right2:
    st.markdown('<div class="section-title">Top Devices by Failed Logins</div>', unsafe_allow_html=True)
    device_logins = (
        filtered
        .groupby("device_id")["failed_logins"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig4 = px.bar(
        device_logins,
        x="failed_logins",
        y="device_id",
        orientation="h",
        labels={
            "failed_logins": "Failed Logins",
            "device_id": "Device ID"
        }
    )
    fig4.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis=dict(autorange="reversed")
    )
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.markdown('<div class="section-title">Incident Review Queue</div>', unsafe_allow_html=True)
st.caption("Plain-English explanations help analysts and non-technical stakeholders understand why a device was flagged.")

review = filtered.copy()
risk_order = {"High": 0, "Medium": 1, "Low": 2}
review["risk_rank"] = review["risk_level"].map(risk_order)
review = review.sort_values(["risk_rank", "timestamp"], ascending=[True, False])

review = review[[
    "timestamp",
    "device_id",
    "device_type",
    "location",
    "risk_level",
    "failed_logins",
    "cpu_usage",
    "data_transfer_mb",
    "latency_ms",
    "explanation"
]]

st.dataframe(review, use_container_width=True, hide_index=True)

st.divider()

st.markdown('<div class="section-title">Product Thinking</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.subheader("User Problem")
    st.write(
        "Security and operations teams often face too many technical alerts without enough context to prioritize urgent threats."
    )

with p2:
    st.subheader("Product Solution")
    st.write(
        "SentinelAI combines anomaly detection, risk scoring, and plain-language explanations to improve incident review."
    )

with p3:
    st.subheader("Success Metrics")
    st.write(
        "Time to detect high-risk events, analyst review efficiency, alert prioritization accuracy, and user satisfaction."
    )

st.success(
    "SentinelAI is a portfolio MVP demonstrating product strategy, AI systems thinking, cybersecurity awareness, and data-driven execution."
)