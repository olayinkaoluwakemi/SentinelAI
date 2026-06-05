import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡️",
    layout="wide"
)

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
        reasons.append("unusually high failed login attempts")
    if row["cpu_usage"] >= 80:
        reasons.append("abnormally high CPU usage")
    if row["data_transfer_mb"] >= 75:
        reasons.append("large data transfer volume")
    if row["latency_ms"] >= 180:
        reasons.append("elevated network latency")
    if row["predicted_anomaly"] == 1:
        reasons.append("machine learning model flagged this event as anomalous")

    if not reasons:
        return "No major risk indicators detected."
    return "Potential risk due to " + ", ".join(reasons) + "."

data = load_data()

features = ["packet_count", "failed_logins", "cpu_usage", "memory_usage", "data_transfer_mb", "latency_ms"]
scaler = StandardScaler()
scaled = scaler.fit_transform(data[features])

model = IsolationForest(contamination=0.09, random_state=42)
data["model_output"] = model.fit_predict(scaled)
data["predicted_anomaly"] = data["model_output"].apply(lambda x: 1 if x == -1 else 0)
data["risk_level"] = data.apply(classify_risk, axis=1)
data["explanation"] = data.apply(explain_event, axis=1)

st.title("🛡️ SentinelAI")
st.caption("Intelligent cybersecurity assistant for IoT systems")

with st.sidebar:
    st.header("Filters")
    location = st.multiselect("Location", sorted(data["location"].unique()), default=sorted(data["location"].unique()))
    device_type = st.multiselect("Device Type", sorted(data["device_type"].unique()), default=sorted(data["device_type"].unique()))
    risk = st.multiselect("Risk Level", ["High", "Medium", "Low"], default=["High", "Medium", "Low"])

filtered = data[
    data["location"].isin(location)
    & data["device_type"].isin(device_type)
    & data["risk_level"].isin(risk)
]

total_events = len(filtered)
anomalies = int(filtered["predicted_anomaly"].sum())
high_risk = int((filtered["risk_level"] == "High").sum())
avg_latency = round(filtered["latency_ms"].mean(), 1) if total_events else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Events", f"{total_events:,}")
c2.metric("Detected Anomalies", f"{anomalies:,}")
c3.metric("High-Risk Events", f"{high_risk:,}")
c4.metric("Avg Latency", f"{avg_latency} ms")

st.divider()

left, right = st.columns([1.2, 1])

with left:
    st.subheader("Risk Events Over Time")
    risk_time = filtered.groupby([pd.Grouper(key="timestamp", freq="2H"), "risk_level"]).size().reset_index(name="events")
    fig = px.line(risk_time, x="timestamp", y="events", color="risk_level", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Risk Distribution")
    risk_counts = filtered["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["risk_level", "count"]
    fig2 = px.pie(risk_counts, values="count", names="risk_level", hole=0.45)
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Device Risk by Location")
device_risk = filtered.groupby(["location", "device_type", "risk_level"]).size().reset_index(name="events")
fig3 = px.bar(device_risk, x="location", y="events", color="risk_level", barmode="group", hover_data=["device_type"])
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Incident Review Queue")
review = filtered.sort_values(["risk_level", "timestamp"], ascending=[True, False]).copy()
review = review[[
    "timestamp", "device_id", "device_type", "location", "risk_level",
    "failed_logins", "cpu_usage", "data_transfer_mb", "latency_ms", "explanation"
]]
st.dataframe(review, use_container_width=True, hide_index=True)

st.info(
    "Product note: SentinelAI is designed for teams that need explainable IoT security monitoring, not just raw technical alerts."
)