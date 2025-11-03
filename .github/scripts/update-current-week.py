#!/usr/bin/env python3
"""
Update the main page with the current week's information based on the current date.
"""

import re
from datetime import datetime
import sys
from pathlib import Path

# Week schedule with start dates (Mondays)
WEEK_SCHEDULE = [
    {"week": "1", "start": "2025-09-15", "title": "Introduction to Machine Learning", "topics": "ML Basics • Nuvolos Setup"},
    {"week": "2", "start": "2025-09-22", "title": "No Class - Swiss Federal Fast", "topics": "Holiday"},
    {"week": "3", "start": "2025-09-29", "title": "Get up to speed - week 2", "topics": "Python • Jupyter • GitHub"},
    {"week": "4", "start": "2025-10-06", "title": "Supervised Learning - Regression", "topics": "Linear Regression • Gradient Descent"},
    {"week": "5", "start": "2025-10-13", "title": "Programming with Generative AI", "topics": "LLMs • Autonomous Agents"},
    {"week": "6", "start": "2025-10-20", "title": "Classification", "topics": "Logistic Regression • Decision Trees"},
    {"week": "7", "start": "2025-10-27", "title": "Deep Learning Basics", "topics": "Neural Networks • Backpropagation"},
    {"week": "8", "start": "2025-11-03", "title": "Tensorflow/PyTorch, RNNs, LSTMs", "topics": "Deep Learning Frameworks • Sequence Models"},
    {"week": "9", "start": "2025-11-10", "title": "Recap Week", "topics": "Review • Q&A • Practice"},
    {"week": "10", "start": "2025-11-17", "title": "Gaussian Processes", "topics": "Probabilistic Models • Uncertainty"},
    {"week": "11", "start": "2025-11-24", "title": "Dimensionality Reduction, PCA, Active Learning", "topics": "Feature Reduction • Active Learning"},
    {"week": "12", "start": "2025-12-01", "title": "Clustering", "topics": "k-means • GMM • Hierarchical"},
    {"week": "13", "start": "2025-12-08", "title": "Reinforcement Learning", "topics": "RL Basics • Q-Learning • Policy Gradient"},
    {"week": "14", "start": "2025-12-15", "title": "Wrap-up and project presentations", "topics": "Final Projects • Presentations"}
]

def get_current_week():
    """Determine which week should be displayed based on current date."""
    today = datetime.now().date()

    # Find the appropriate week
    current_week = WEEK_SCHEDULE[0]  # Default to first week

    for week in WEEK_SCHEDULE:
        week_start = datetime.strptime(week["start"], "%Y-%m-%d").date()
        if today >= week_start:
            current_week = week
        else:
            break

    return current_week

def update_index_file(file_path, current_week):
    """Update the index.html file with current week information."""

    with open(file_path, 'r') as f:
        content = f.read()

    # Pattern to match the current week banner section
    pattern = r'(<div class="current-info">[\s\S]*?<h2>)(Week [^<]+)(<\/h2>[\s\S]*?<p>)([^<]+)(<\/p>)'

    # Build replacement string
    replacement = (
        r'\1Week {}: {}\3{}\5'.format(
            current_week["week"],
            current_week["title"],
            current_week["topics"]
        )
    )

    # Perform replacement
    updated_content = re.sub(pattern, replacement, content)

    # Check if replacement was made
    if updated_content == content:
        print("⚠️  Warning: No changes made. Pattern might not match.")
        return False

    # Write updated content
    with open(file_path, 'w') as f:
        f.write(updated_content)

    return True

def main():
    # Get repository root (assuming script is in .github/scripts/)
    repo_root = Path(__file__).parent.parent.parent
    index_path = repo_root / "docs" / "index.html"

    if not index_path.exists():
        print(f"❌ Error: {index_path} not found")
        sys.exit(1)

    # Get current week
    current_week = get_current_week()
    print(f"📅 Current week: Week {current_week['week']} - {current_week['title']}")
    print(f"   Topics: {current_week['topics']}")

    # Update index file
    if update_index_file(index_path, current_week):
        print(f"✅ Successfully updated index.html")
    else:
        print(f"❌ Failed to update index.html")
        sys.exit(1)

if __name__ == "__main__":
    main()
