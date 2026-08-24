# Second-Look Lending

**Company / Org:** American Express  
**Challenge Advisor:** SAURABH GUPTA, saurabh.gupta13@aexp.com   
**AI Studio Coach:** Swagath Babu, swagath.babu@breakthroughtech.org    
**Program:** Break Through Tech AI Studio - Fall 2026  

---

## 🏢 About American Express
American Express is a globally integrated payments company that provides customers with access to products, insights, and experiences that enrich lives and build business success. 

---

## 🎯 The Challenge
### Project Summary
In this project, you will use synthetic consumer-loan data and classical ML logistic regression, random forests, and gradient boosting to predict each applicant's default risk and convert it into a profit-aware, fair lending decision that better serves applicants with little credit history. This will help the company address making credit decisions that maximize profit while extending fair access to underserved borrowers.
- Look for More Details here
- https://docs.google.com/presentation/d/1M2VaMNXbUiA_RR0YYfVhTT88Jx19B48C/edit?slide=id.p1#slide=id.p1

### Success Criteria
Evaluation has two levels, both computed on a time-based, held-out test set used only once. 

- Model quality is measured with ROC-AUC and LogLoss, plus a calibration check (reliability curve and Brier score), and must beat a logistic-regression baseline.

- Decision quality - the project’s original contribution — is measured by expected portfolio profit under a defined cost model (held below a maximum default-rate ceiling) and by the thin-file inclusion gap (the difference in approval rate, among applicants who would actually repay, between established and thin-file borrowers). These combine into the team’s headline metric, the Inclusive Profit Score = expected profit − penalty × inclusion gap, compared against a naïve single-threshold policy.

### Stretch Goals
Implementing Transformer based architecture (Mainly Self Attention) to find the feature combinations that drive clicks, automatically and to high order.

### Project Milestones
Use these milestones to guide your work. Your team will create a GitHub Projects board to track tasks within each milestone.
| Month | Milestone | Key Activities |
|-------|-----------|----------------|
| **September** | Business Problem + Data Understanding , EDA , Feature Engineering |
| **October** | Training and Validation Data Preparation, ML Algorithms Explorations, Candidate Models Identification, Model building , Hyper-parameter Fine tuning using Grid Search and Baysian Search |
| **November** | Model Finalization, Model Scoring and Final Deployment, A very basic  frontend app creation using streamlit to show case model capability |

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset
**Name and Source:** Second Look Dataset
**Format:** CSV/TSV  
**Size:** 1gb to 5gb  
**Location:** https://drive.google.com/drive/folders/1bJpa87n6HCwRR3Pvr5xqocNZrGo7dufT

### Key Details
- synthetic consumer-loan data, numerical/quantitative, categorical, time series, CSV/TSV format, requires cleaning/preprocessing
- Data requires robust handling of time-series constraints and specific preprocessing to ensure categorical variables are correctly encoded for gradient-boosting algorithms.

---

## 🛠️ Suggested Approach

**ML Problem Type:**  Classification, Clustering, Recommendation Systems, Deep Learning / Neural Networks  

**Recommended Libraries:**
- pandas, numpy (Data manipulation & feature engineering)
- scikit-learn (Baseline models, calibration, evaluation metrics)
- xgboost, lightgbm, catboost (Gradient boosted decision trees)
- streamlit (Frontend application dashboard)
- scikit-learn (GridSearchCV / RandomizedSearchCV for hyperparameter tuning)

**Evaluation Metrics:**
- Model Quality: ROC-AUC, LogLoss, Calibration Check (Reliability Curve & Brier Score)
- Decision Quality: Expected Portfolio Profit, Thin-File Inclusion Gap, Inclusive Profit Score
  
---

## 📚 Resources to Get Started

The following resources will help your team understand the problem space and potential technical approaches for this project:

**Background Reading:**
- CFPB Guidance on Algorithmic Credit Scoring & Fairness
- American Express Company Overview & Credit Risk Principles

**Technical Tutorials:**
- Scikit-Learn Probability Calibration Guide
- Streamlit Documentation & Quickstart
- Scikit-Learn Tabular Classification Examples
- Credit Risk Modeling in Python Overview
- https://aman.ai/primers/ai/evaluation-metrics/
- https://towardsai.com/p/l/machine-learning-project-in-python-step-by-step-loan-defaulters-prediction
  
  


*Feel free to explore beyond these, and share anything interesting you find with me!*

---

## 🤝 How We'll Work Together

**Official check-ins:** During our biweekly 45-minute AI Studio Lab Section meeting block (2nd and 4th week of every month)
 Preferred Mode of Communication : EMAIL ( saurabh.gupta13@aexp.com or algoexpert.saurabh@gmail.com
 Typically Respond With in 24-48 hrs 
 **Other ways to reach out to me with questions:** 
* [e.g., Your team's channel within Break Through Tech’s Discord space]
* [e.g., Email; please copy your teammates and AI Studio Coach]
* [e.g., Request a team check-in on Zoom]
* [Note: I will aim to respond within 48 hours. Please reach out to your AI Studio Coach with urgent questions.]

> 💡 **Challenge Advisor: Please update the above based on your availability and preference. If you are not able to answer questions or meet with fellows outside of the biweekly Lab Section check-ins, simply write in "N/A (only available during the official check-in times)"**

**Recommended free coding / collaboration tools**
* Google Colab
* VS CODE 

---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting
2. **Begin reviewing the dataset** using the link above
3. **Read the GitHub Projects documentation** [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

I’m excited to work with you!

---
