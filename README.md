# University Student Analytics Dashboard

This project is part of **Activity 1 – Data Visualization and Dashboard Deployment**.  
It demonstrates how to load and explore a university student dataset, create visualizations, and deploy an interactive dashboard using **Streamlit Cloud**.

## 1. Project Structure

- `activity1_data_viz_dashboard.ipynb` – Google Colab notebook with:
  - dataset loading and exploration
  - descriptive visualizations (retention, satisfaction, term comparison)
  - code to generate `app.py` for Streamlit
- `app.py` – Streamlit dashboard (generated from the notebook)
- `requirements.txt` – Python dependencies
- `README.md` – This file

## 2. Dataset

The dashboard expects a file named **`university_student_data.csv`** in the same directory.  
This file should contain fields similar to:

- `year`
- `term` (e.g. Spring, Fall)
- `applications`
- `admitted`
- `enrolled`
- `retention_rate`
- `satisfaction_score`
- `engineering_enrolled`
- `business_enrolled`
- `arts_enrolled`
- `science_enrolled`

  
## 3. How to run locally

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure `university_student_data.csv` is in the project folder.
4. Run Streamlit:

   ```bash
   streamlit run app.py
   ```

5. Open the URL that Streamlit shows in the terminal (usually http://localhost:8501).

## 4. Deploying to Streamlit Cloud

1. Push these files to a **public GitHub repository**:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `university_student_data.csv` (or load it from another source)
2. Go to https://streamlit.io/cloud and connect your GitHub account.
3. Select the repository and the `app.py` file as the entry point.
4. Deploy. Streamlit will install the requirements automatically.

## 5. Notes

- You can add more charts (bar, line, pie/donut) by using Plotly Express inside `app.py`.
- You can add more filters (year, department, term) in the sidebar to make the dashboard more interactive.
- Make sure that all team members’ names appear in the repository and in the deployed app, as requested in the assignment.
