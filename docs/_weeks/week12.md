---
title: "Week 12: Clustering (k-means, GMM, hierarchical)"
date: 2025-12-01
description: "k-Means, Gaussian Mixture Models, Expectation Maximization, Hierarchical Clustering, Density-based Clustering, Exercise 8 distributed"
lecture_slides: 
  - title: "Lecture slides, week 12"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_12/slides/Advanced_Data_Analytics_2025_lecture_12.pdf"
ta_slides: 
  - title: "Discussion of the previous exercises; Finger exercises (with TA)"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_12/Finger_exercises/finger_exercises_lecture_12.pdf"
assignment:
  title: "Exercise 8"
  link: "/ada-course-materials/advanced_data_analytics_2025/exercises/Exercise_8/Problem_set_8.pdf"
  description: "Distribution of Exercise sheet 8"
examples:
  - title: "Multiple Demo Files"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_12/demo/"
references:
  - title: "Finger Exercises"
    link: "/ada-course-materials/advanced_data_analytics_2025/lectures/lecture_12/Finger_exercises/finger_exercises_lecture_12.pdf"
    description: "Discussion of the previous exercises; Finger exercises (with TA)"
---

## Week 12: Clustering

### Learning Objectives
- Understand unsupervised learning and clustering fundamentals
- Master k-means clustering algorithm and its variants
- Learn Gaussian Mixture Models (GMM) and Expectation Maximization
- Explore hierarchical clustering methods
- Apply density-based clustering techniques like DBSCAN
- Compare different clustering algorithms and choose appropriate methods

### Topics Covered
- **k-Means Clustering**: Centroid-based clustering algorithm
- **Gaussian Mixture Models (GMM)**: Probabilistic clustering approach
- **Expectation Maximization**: Algorithm for parameter estimation in GMM
- **Hierarchical Clustering**: Agglomerative and divisive methods
- **Density-Based Clustering**: DBSCAN and related algorithms
- **Cluster Validation**: Metrics and techniques for evaluating clusters

### Schedule
- **Lecture**: Monday, December 1, 2025 (10:15 - 12:00)
- **Practice Session**: Monday, December 1, 2025 (16:30 - 18:00)
- **TA Session**: Discussion of exercises and clustering implementations

### Key Concepts
- **Unsupervised Learning**: Learning patterns without labeled data
- **Distance Metrics**: Euclidean, Manhattan, cosine similarity
- **Cluster Quality**: Intra-cluster vs inter-cluster distances
- **Initialization Methods**: K-means++, random initialization
- **Model Selection**: Choosing the number of clusters
- **Convergence**: When and why algorithms converge

### Clustering Algorithms
- **k-Means**: Lloyd's algorithm, k-means++, mini-batch k-means
- **GMM**: Multivariate Gaussian distributions, soft clustering
- **Hierarchical**: Ward linkage, complete linkage, single linkage
- **DBSCAN**: Density-based spatial clustering, noise detection
- **Mean Shift**: Mode-seeking algorithm for clustering

### Practical Applications
- **Customer Segmentation**: Marketing and business applications
- **Image Segmentation**: Computer vision clustering tasks
- **Gene Expression**: Bioinformatics clustering analysis
- **Market Segmentation**: Financial and economic clustering

### Evaluation Metrics
- **Internal Metrics**: Silhouette score, Davies-Bouldin index
- **External Metrics**: Adjusted Rand index, normalized mutual information
- **Visual Assessment**: Scatter plots, dendrograms, cluster visualization

### Assignments
- **Exercise 8**: Distributed this week - Clustering algorithm implementations
- Compare different clustering methods on various datasets
- Implement k-means and GMM from scratch
- Apply clustering to real-world datasets

### Tools and Implementation
- scikit-learn for standard clustering algorithms
- Custom implementations for educational purposes
- Visualization tools for cluster analysis
- Performance comparison frameworks