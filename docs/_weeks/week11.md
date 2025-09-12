---
title: "Week 11: Dimensionality Reduction, PCA, Active Learning"
date: 2025-11-24
description: "The curse of Dimensionality, Bayesian active learning, Active Subspaces and Gaussian Process Regression, Principal Component Analysis, Exercise 7 distributed"
lecture_slides: 
  - title: "Lecture slides, week 11"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_11/slides/Advanced_Data_Analytics_2025_lecture_11.pdf"
ta_slides: 
  - title: "Discussion of the previous exercises; Finger exercises (with TA)"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_11/Finger_exercises/finger_exercises_lecture_11.pdf"
assignment:
  title: "Exercise 7"
  link: "/ada-course-materials/advanced_data_analytics_2025/exercises/Exercise_7/Problem_set_7.pdf"
  description: "Distribution of Exercise sheet 7"
examples:
  - title: "Multiple Demo Files"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_11/demo/"
references:
  - title: "Finger Exercises"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_11/Finger_exercises/finger_exercises_lecture_11.pdf"
    description: "Discussion of the previous exercises; Finger exercises (with TA)"
---

## Week 11: Dimensionality Reduction & Active Learning

### Learning Objectives
- Understand the curse of dimensionality and its implications
- Master Principal Component Analysis (PCA) and its variants
- Learn Bayesian active learning strategies
- Explore active subspaces in the context of Gaussian Process regression
- Apply dimensionality reduction techniques to real-world datasets
- Understand when and how to use different dimensionality reduction methods

### Topics Covered
- **Curse of Dimensionality**: Challenges in high-dimensional spaces
- **Principal Component Analysis (PCA)**: Linear dimensionality reduction
- **Kernel PCA**: Non-linear dimensionality reduction using kernel methods
- **Bayesian Active Learning**: Intelligent sampling strategies
- **Active Subspaces**: Dimension reduction for complex functions
- **GP Regression with Active Subspaces**: Combining dimensionality reduction with GPs

### Schedule
- **Lecture**: Monday, November 24, 2025 (10:15 - 12:00)
- **Practice Session**: Monday, November 24, 2025 (16:30 - 18:00)
- **TA Session**: Discussion of exercises and hands-on implementations

### Key Concepts
- **High-Dimensional Challenges**: Sparsity, distance metrics, visualization problems
- **Linear vs Non-linear Methods**: When to use PCA vs kernel PCA
- **Variance Explained**: Choosing the number of components
- **Active Learning**: Uncertainty sampling and query strategies
- **Subspace Identification**: Finding low-dimensional structure in high-dimensional functions
- **Integration with GPs**: Using active subspaces to improve GP scalability

### Dimensionality Reduction Methods
- **PCA**: Eigenvalue decomposition and SVD approaches
- **Kernel PCA**: RBF, polynomial, and custom kernels
- **Active Subspaces**: Gradient-based dimension reduction
- **Comparison**: When to use each method

### Active Learning Strategies
- **Uncertainty Sampling**: Exploiting model uncertainty
- **Query by Committee**: Ensemble-based active learning
- **Expected Model Change**: Information-theoretic approaches
- **Bayesian Optimization**: Active learning for expensive function evaluations

### Practical Applications
- **Image Processing**: PCA for image compression and visualization
- **Wine Dataset Analysis**: Multi-class dimensionality reduction
- **Financial Data**: Portfolio dimensionality reduction
- **Scientific Computing**: Active subspaces for expensive simulations

### Assignments
- **Exercise 7**: Distributed this week - PCA and active learning implementations
- Compare different dimensionality reduction techniques
- Implement active learning strategies

### Tools and Implementation
- scikit-learn for PCA and kernel PCA
- Custom implementations for active subspaces
- Visualization techniques for high-dimensional data
- Integration with previous GP implementations