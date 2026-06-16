# 🏢 Gurgaon Real Estate Analysis

> **Exploratory Data Analysis (EDA) of Gurgaon Real Estate data** to uncover property pricing trends, locality insights, and market patterns using Python data science tools.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightblue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Highlights](#key-highlights)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Contributing](#contributing)

---

## 📊 Overview

This project performs comprehensive **Exploratory Data Analysis (EDA)** on Gurgaon's real estate market to transform raw data into actionable insights. The analysis covers:

- **Property price analysis** across different localities
- **Market trends** and pricing patterns
- **Relationships** between area, BHK count, amenities, and property prices
- **Outlier detection** and market anomalies
- **Data-driven recommendations** for buyers, investors, and real estate stakeholders

---

## ✨ Key Highlights

1. ✅ **Data Cleaning & Preprocessing**
   - Handled missing values, duplicates, and inconsistencies
   - Data quality improvements from raw to cleaned dataset

2. 📈 **Comprehensive Analysis**
   - Univariate, bivariate, and multivariate analysis
   - Locality-wise property price comparisons
   - Average rates per square foot by area

3. 🎨 **Rich Visualizations**
   - Correlation heatmaps
   - Scatter plots (price vs. area, BHK vs. price)
   - Box plots (outlier detection)
   - Histograms and bar charts
   - Distribution analysis

4. 💡 **Actionable Insights**
   - Premium localities and costliest properties identified
   - Key factors affecting real estate pricing
   - Market trends and investment opportunities

---

## 📁 Dataset

| Attribute | Details |
|-----------|---------|
| **Source** | Gurgaon Real Estate Market Data |
| **Records** | 1,352 properties (cleaned) |
| **Size** | ~2.1 MB (cleaned CSV) |
| **Key Features** | Price, Area, BHK, Locality, Price per Sqft, Amenities |

### Data Files
- **`data.csv`** – Raw dataset (3.1 MB)
- **`cleaned_data.csv`** – Preprocessed dataset (2.1 MB)

---

## 📂 Project Structure

```
gurgaon-real-estate-analysis/
├── README.md                 # Project documentation
├── project.py               # Main analysis script
├── data.csv                 # Raw real estate data
├── cleaned_data.csv         # Preprocessed data
├── Figure_1.png             # Analysis visualization #1
└── Figure_2.png             # Analysis visualization #2
```

---

## 🛠 Technologies Used

| Category | Tools |
|----------|-------|
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook |
| **Techniques** | Data Cleaning, EDA, Statistical Analysis, Feature Engineering |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/cTANMAY97/gurgaon-real-estate-analysis.git
cd gurgaon-real-estate-analysis
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate          # On macOS/Linux
venv\Scripts\activate             # On Windows
```

### Step 3: Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Step 4: Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 💻 How to Use

### Running the Analysis

1. **Open the Python script or Jupyter Notebook:**
   ```bash
   python project.py
   ```
   Or in Jupyter:
   ```
   jupyter notebook
   ```

2. **Data Processing Flow:**
   - Load raw `data.csv`
   - Execute cleaning and preprocessing (handled in `project.py`)
   - Generate analysis visualizations
   - Output cleaned dataset to `cleaned_data.csv`

3. **Explore the Insights:**
   - Review generated plots and statistics
   - Analyze locality-wise price distributions
   - Study correlation patterns between features

### Quick Code Example
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('cleaned_data.csv')

# Basic statistics
print(df.describe())

# Price distribution by BHK
sns.boxplot(data=df, x='BHK', y='Price')
plt.title('Price Distribution by BHK Count')
plt.show()
```

---

## 🔍 Key Findings

- **Price Range:** Property prices vary significantly across Gurgaon localities
- **BHK Impact:** Higher BHK count correlates strongly with property price
- **Area Factor:** Property area is a primary driver of pricing
- **Locality Premium:** Select premium localities command 2-3x higher prices
- **Market Outliers:** Identified properties with unusual price-to-area ratios

---

## 📊 Visualizations

The project includes multiple analytical visualizations:

- **Figure_1.png** – Market trends and price distributions
- **Figure_2.png** – Locality-wise analysis and correlations

Sample visualizations showcase:
- Price trends across different BHK categories
- Scatter plots of area vs. price with trend lines
- Correlation heatmaps of key features
- Locality rankings by average price

---

## 🤝 Contributing

Contributions are welcome! To improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---


## 📧 Contact

For questions or feedback about this project:
- **GitHub:** [@cTANMAY97](https://github.com/cTANMAY97)

---

**Last Updated:** June 2026  
**Project Status:** ✅ Complete
