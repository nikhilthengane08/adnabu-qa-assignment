# 🧪 Test Automation – Search Product & Add to Cart

## 📌 Overview
This project automates a basic e-commerce scenario using Python + Selenium WebDriver:

Search for a product and successfully add it to the cart.

The goal is to demonstrate functional UI automation using proper waits and clean, modular code.

---

## ⚙️ Tech Stack
- Python 3.x
- Selenium WebDriver
- Pytest (optional for execution)
- Google Chrome Browser

---

## 📁 Project Structure
adnabu-qa-assignment/
│
├── tests/
│   └── test_add_to_cart.py
│
├── requirements.txt
└── README.md

---

## 🚀 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/nikhilthengane08/adnabu-qa-assignment.git  
cd adnabu-qa-assignment

---

### 2. Create Virtual Environment (Optional but recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing:
pip install selenium pytest

---

### 4. Browser Setup
- Ensure Google Chrome is installed  
- ChromeDriver should match your Chrome version  

OR use:
pip install webdriver-manager

---

## ▶️ How to Run Tests

### Run using Python:
python tests/test_add_to_cart.py

### Run using Pytest (recommended):
pytest -v -s

---

## 🧪 Test Scenario Covered

✔ Search Product and Add to Cart

Steps:
1. Open website  
2. Search for a product  
3. Select product from results  
4. Click Add to Cart  
5. Verify product is added successfully  

---

## ⏳ Synchronization Strategy
- Uses Explicit Waits (WebDriverWait)
- No hardcoded sleep used
- Ensures stable execution

Example:
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button"))
)

---

## 📊 Reporting
- No external reporting tool required
- Results shown in terminal

---

## 📤 Submission
GitHub Repository:
https://github.com/nikhilthengane08/adnabu-qa-assignment

---

## ✅ Notes
- Simple and clean Selenium automation
- No framework overhead (as per assignment requirement)
- Focus on reliability and readability
