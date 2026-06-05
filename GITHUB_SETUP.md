# GitHub Setup Guide for SentinelAI

## Step 1: Create a GitHub Repository

1. Go to GitHub.
2. Click **New repository**.
3. Repository name: `SentinelAI`
4. Description: `Intelligent cybersecurity assistant for IoT systems`
5. Choose Public.
6. Do not add a README because this project already includes one.
7. Click Create repository.

## Step 2: Upload the Project

Open Terminal on your computer and run:

```bash
cd path/to/SentinelAI
git init
git add .
git commit -m "Initial SentinelAI project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/SentinelAI.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Step 3: Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

On Windows:

```bash
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Step 4: Add to Resume

Suggested resume bullet:

Built SentinelAI, an AI-powered IoT cybersecurity dashboard using Python, Streamlit, Scikit-learn, and Plotly to detect anomalies, classify risk levels, and explain suspicious device behavior for security and operations teams.