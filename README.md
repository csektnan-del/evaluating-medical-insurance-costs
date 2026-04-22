# Medical Insurance Cost Analysis

## Overview

This project explores the factors that influence medical insurance costs using a dataset of patient demographics and billing data.

The goal is to identify which variables—such as smoking status, BMI, age, and region—have the greatest impact on insurance charges, and to quantify those differences in a clear, interpretable way.

---

## Key Question

Which factors most significantly drive higher medical insurance costs, and how can high-risk groups be identified?

---

## Dataset

The dataset includes the following features:

* Age
* Sex
* BMI (Body Mass Index)
* Number of children
* Smoking status
* Region
* Insurance charges (USD)

---

## Approach

### Data Processing

* Loaded raw CSV data using Python
* Converted each row into a structured dictionary
* Grouped individuals into demographic segments
* In order to further focus anaylsis and control for some variables, centered analysis on the subgroup of women under 50 without children and preformed additional segmentation of this group by
    * Smoking status
    * BMI category: underweight/normal (collapsed to increase sample size), overweight, obese
    * Geographic region

### Analysis

* Calculated average insurance costs for each subgroup
* Compared differences between key categories:

  * Smokers vs non-smokers
  * Obese vs overweight individuals
* Measured both absolute cost differences and percentage increases

---

## Key Findings

### Smoking Impact

* Smoking is the strongest cost driver in the dataset
* Smokers have significantly higher average insurance costs than non-smokers
* The percentage increase highlights a substantial financial risk associated with smoking

### BMI Impact

* Obese individuals have notably higher insurance costs than overweight individuals
* The increase suggests a clear relationship between higher BMI and increased healthcare expenses

### Regional Differences

* Insurance costs vary by region, though differences show less of a clear relationship than smoking or BMI

---

## Dataset Output

| Group                 | Avg Cost ($) | Sample Size |
|----------------------|--------------|-------------|
| Women <50 no kids    | 9,551        | 191         |
| **Smokers**          | **28,495**   | 39          |
| Non-Smokers          | 4,691        | 152         |
| Under/Normal BMI     | 7,906        | 36          |
| Overweight           | 7,025        | 61          |
| **Obese**            | **11,821**   | 94          |
| Northeast            | 7,604        | 47          |
| Northwest            | 10,303       | 46          |
| Southeast            | 11,570       | 52          |
| Southwest            | 8,507        | 46          |

Key comparisons:

*  Smoking (Yes vs No)             23804.15   507.48%
*  Obese vs Overweight              4796.22    68.28%

---

## Tools Used

* Python
* CSV module
* Basic data structures (dictionaries, loops)

---

## Project Structure

├── data/
│   └── insurance.csv
├── analysis.py
└── README.md
##_Data Source: 
This dataset is commonly used for exploratory analysis and is provided as part of the Codecademy Data Analytics career path._
---

## Limitations

* Analysis is limited to a subset of the dataset (women under 50 with no children)
* No statistical modeling or hypothesis testing was performed
* Results are based on averages and may be influenced by outliers

---

## Future Improvements

* Expand analysis to the full population
* Build a predictive model for estimating insurance costs
* Explore interaction effects between variables (e.g., smoking + BMI)

---

## Takeaway

Smoking status and BMI are the most significant drivers of insurance costs in this dataset. Identifying and targeting high-risk groups could help inform pricing strategies and preventative healthcare initiatives.

---

