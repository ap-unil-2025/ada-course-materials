---
title: "Week 10: Gaussian Processes"
date: 2025-11-17
description: "Gaussian Process regression, Kernels with noise, Exercise 6 distributed"
lecture_slides: 
  - title: "Lecture slides, week 10"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/slides/Advanced_Data_Analytics_2025_lecture_10.pdf"
ta_slides: 
  - title: "Finger exercises part 1 (at the end of the lecture (with TA))"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/Finger_exercises_a/finger_exercises_lecture_10.pdf"
  - title: "Finger exercises part 2 (at the end of the lecture (with TA))"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/Finger_exercises_b/finger_exercises_lecture_10.pdf"
assignment:
  title: "Exercise 6"
  link: "/ada-course-materials/advanced_data_analytics_2025/exercises/Exercise_6/Problem_set_6.pdf"
  description: "Distribution of Exercise sheet 6"
examples:
  - title: "Multiple Demo Files"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/demo/"
  - title: "Finance Demo (Option-pricing examples, if time permits)"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/finance_demo/"
  - title: "GP Demo"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/demo_GP/"
references:
  - title: "Finger Exercises"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_10/Finger_exercises_a/"
    description: "Finger exercises part 1 and 2 (at the end of the lecture (with TA))"
---

## Week 10: Gaussian Processes

### Learning Objectives
- Understand the theoretical foundations of Gaussian Processes (GPs)
- Master Gaussian Process regression techniques
- Learn about kernels and their role in GP modeling
- Handle noisy data in GP frameworks
- Apply GPs to financial modeling and option pricing
- Understand GP classification methods

### Topics Covered
- **Gaussian Process Regression**: Theoretical foundations and practical implementation
- **Kernels with Noise**: Incorporating uncertainty and noise in GP models
- **Option-Pricing Examples**: Financial applications of Gaussian Processes
- **GP Classification**: Extending GPs to classification problems
- **Bayesian Framework**: Understanding the Bayesian perspective in GPs
- **Hyperparameter Optimization**: Tuning GP models for optimal performance

### Schedule
- **Lecture**: Monday, November 17, 2025 (10:15 - 12:00)  
- **Practice Session**: Monday, November 17, 2025 (16:30 - 18:00)
- **TA Session**: Two-part finger exercises and practical implementations

### Key Concepts
- **Gaussian Processes**: Non-parametric Bayesian approach to regression
- **Kernel Functions**: RBF, Matern, periodic kernels and their properties
- **Mean and Covariance Functions**: Defining GP priors
- **Marginal Likelihood**: Model selection and hyperparameter optimization
- **Uncertainty Quantification**: Predictive distributions and confidence intervals
- **Computational Complexity**: Scaling GPs and approximation methods

### Mathematical Foundations
- Multivariate Gaussian distributions
- Kernel methods and reproducing kernel Hilbert spaces
- Bayesian inference and posterior distributions
- Maximum likelihood estimation for hyperparameters

### Practical Applications
- **1D and 2D Regression**: Basic GP regression examples
- **Financial Modeling**: Option pricing using GP methods
- **Noise Handling**: Robust regression with noisy observations
- **Multi-dimensional Problems**: Scaling to higher dimensions
- **Classification Tasks**: GP classification with various kernels

### Assignments
- **Exercise 6**: Distributed this week - GP implementation and applications
- Complete two-part finger exercises covering theory and practice
- Implement GP regression from scratch and compare with scikit-learn

### Tools and Libraries
- GPy and GPFlow for advanced GP modeling
- scikit-learn for basic GP implementations
- Practical GP examples and case studies