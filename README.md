# Data Cleaning Project

A Python-based project for cleaning, processing, and visualizing data with an interactive dashboard.

## Project Structure

```
data-cleaning-project/
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebook/
│   └── cleaning.ipynb
│
├── src/
│   └── clean_data.py
│
├── dashboard/
│   └── app.py
│
├── README.md
└── requirements.txt
```

## Overview

- **data/**: Raw and cleaned data files
- **notebook/**: Jupyter notebook for exploratory data analysis
- **src/**: Python scripts for data processing
- **dashboard/**: Streamlit dashboard for visualization

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone or download the project
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

#### Run Data Cleaning Script

```bash
python src/clean_data.py
```

#### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

#### Jupyter Notebook

```bash
jupyter notebook notebook/cleaning.ipynb
```

## Requirements

See `requirements.txt` for all dependencies.

## License

This project is open source and available under the MIT License.
