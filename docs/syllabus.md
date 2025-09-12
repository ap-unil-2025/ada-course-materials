---
layout: default
---

<style>

/* Compact Header for Default Layout */
.syllabus-header {
  text-align: center;
  margin-bottom: 1rem;
}

.syllabus-header h1 {
  font-size: 2rem;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.syllabus-header p {
  color: var(--text-secondary);
  margin: 0;
  font-size: 1rem;
}
</style>

<div class="syllabus">
  <!-- Compact header for syllabus -->
  <div class="syllabus-header">
    <h1>Course Syllabus</h1>
    <p>Advanced Data Analytics • HEC Lausanne • Fall 2025</p>
  </div>

  <!-- Course Overview Banner -->
  <div class="course-banner">
    <div class="course-content">
      <span class="course-label">2025</span>
      <div class="course-info">
        <h2>Advanced Data Analytics</h2>
        <p>Machine Learning for Economics & Finance</p>
      </div>
    </div>
    <a href="{{ '/weekly-materials' | relative_url }}" class="course-btn">View Materials →</a>
  </div>

  <!-- Meeting Information -->
  <div style="margin: 1.5rem 0; padding: 1rem; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1px solid #3b82f6; border-radius: 0.5rem;">
    <h4 style="margin: 0 0 0.5rem 0; color: #1e40af;">📍 Meeting Time & Location</h4>
    <p style="margin: 0 0 0.25rem 0; font-size: 0.9rem; color: #1e40af;">
      <strong>Time:</strong> Mondays, 10:15 - 12:00 (Lecture) • 16:30 - 18:00 (Practice)
    </p>
    <p style="margin: 0; font-size: 0.9rem; color: #1e40af;">
      <strong>Location:</strong> Internef 126 (Morning) • Anthropole 3185 (Afternoon)
    </p>
  </div>

  <!-- Course Information -->
  <section class="syllabus-section">
    <h3 class="section-title">Course Overview</h3>
    <div class="info-grid">
      
      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Goal</span>
        </div>
        <h4>Learning Objectives</h4>
        <p>Gain practical familiarity with current computer-aided data analysis and machine learning approaches.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Format</span>
        </div>
        <h4>Course Structure</h4>
        <p>14-week Master's level course: Three 45-minute lectures + 45-minute hands-on session each Monday.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge priority">Platform</span>
        </div>
        <h4>Nuvolos Cloud</h4>
        <p>All materials distributed via cloud platform. <a href="https://app.nuvolos.cloud/enroll/class/sBsa1T_Mm5Y" target="_blank">Enroll here</a>.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Support</span>
        </div>
        <h4>TA Sessions</h4>
        <p>Mondays 17:15-18:00 with Maria Pia Lombardo. Fridays by request.</p>
      </div>

    </div>
  </section>

  <!-- Key Skills Section -->
  <section class="syllabus-section">
    <h3 class="section-title">Skills You'll Master</h3>
    <div class="skills-grid">
      
      <div class="skill-item">
        <div class="skill-icon">🧠</div>
        <h4>Supervised Learning</h4>
        <p>Regression • Classification • Deep Neural Networks</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">📊</div>
        <h4>Unsupervised Learning</h4>
        <p>Clustering • PCA • Gaussian Mixture Models</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">🎮</div>
        <h4>Reinforcement Learning</h4>
        <p>Q-Learning • Portfolio optimization • If time permits</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">🤖</div>
        <h4>Deep Learning</h4>
        <p>TensorFlow • PyTorch • RNNs • LSTMs</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">🎯</div>
        <h4>Applied ML</h4>
        <p>Stock prediction • NLP • Real-world applications</p>
      </div>

    </div>
  </section>

  <!-- Course Schedule -->
  <section class="syllabus-section">
    <h3 class="section-title">Course Schedule</h3>
    <p>Detailed weekly materials are available in the <a href="{{ '/weekly-materials' | relative_url }}">Weekly Materials Hub</a>.</p>
    
    <div class="schedule-parts">
      
      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part I</span>
          <h4>Foundations</h4>
          <span class="part-dates">Weeks 1-5</span>
        </div>
        <div class="part-topics">
          <span class="topic">ML Intro</span>
          <span class="topic">Python Crash Course</span>
          <span class="topic">Linear Regression</span>
          <span class="topic">Generative AI & Agents</span>
        </div>
      </div>

      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part II</span>
          <h4>Core ML</h4>
          <span class="part-dates">Weeks 6-10</span>
        </div>
        <div class="part-topics">
          <span class="topic">Classification</span>
          <span class="topic">Deep Learning</span>
          <span class="topic">TensorFlow/PyTorch</span>
          <span class="topic">RNNs/LSTMs</span>
          <span class="topic">Gaussian Processes</span>
        </div>
      </div>

      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part III</span>
          <h4>Advanced Topics</h4>
          <span class="part-dates">Weeks 11-14</span>
        </div>
        <div class="part-topics">
          <span class="topic">Dimensionality Reduction</span>
          <span class="topic">Clustering</span>
          <span class="topic">Reinforcement Learning</span>
          <span class="topic">Capstone Projects</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Assessment & Grading -->
  <section class="syllabus-section">
    <h3 class="section-title">Assessment & Grading</h3>
    <div class="assessment-grid">
      
      <div class="assessment-item primary">
        <div class="assessment-icon">🎯</div>
        <h4>Capstone Project</h4>
        <p>Individual data science project • 10-page report • GitHub repository • Video presentation (max 10 min)</p>
        <a href="{{ '/projects' | relative_url }}" class="project-link">View Project Guidelines →</a>
      </div>

      <div class="assessment-item">
        <div class="assessment-icon">📝</div>
        <h4>No Exams</h4>
        <p>Assessment based entirely on demonstrating understanding through the capstone project</p>
      </div>

      <div class="assessment-item">
        <div class="assessment-icon">📝</div>
        <h4>Exercise Sheets</h4>
        <p>8 problem sets distributed throughout the semester for practice and learning</p>
      </div>

    </div>
  </section>

  <!-- References -->
  <section class="syllabus-section">
    <h3 class="section-title">Course References & Textbooks</h3>
    <div class="references-grid">
      
      <div class="reference-item">
        <div class="reference-type">Statistical Learning</div>
        <h4>An Introduction to Statistical Learning</h4>
        <p>James, Witten, Hastie, Tibshirani • Springer</p>
        <p><a href="https://www.statlearning.com" target="_blank">statlearning.com</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Deep Learning</div>
        <h4>Deep Learning</h4>
        <p>Goodfellow, Bengio, Courville • MIT Press</p>
        <p><a href="http://www.deeplearningbook.org" target="_blank">deeplearningbook.org</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Pattern Recognition</div>
        <h4>Pattern Recognition and Machine Learning</h4>
        <p>Christopher Bishop • Springer</p>
        <p><a href="https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf" target="_blank">Download PDF</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Mathematics</div>
        <h4>Mathematics for Machine Learning</h4>
        <p>Essential mathematical foundations</p>
        <p><a href="https://mml-book.github.io/" target="_blank">mml-book.github.io</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Python</div>
        <h4>Python Programming</h4>
        <p>QuantEcon lectures on Python</p>
        <p><a href="https://python-programming.quantecon.org/intro.html" target="_blank">quantecon.org</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Support</div>
        <h4>Course Resources</h4>
        <p>Questions & Materials</p>
        <p><a href="https://docs.google.com/spreadsheets/d/1DWmx_bJ0NW9cZMPX_nteiCcTBt1n65LnT_BI_r4loDo/edit#gid=0" target="_blank">Google Doc</a></p>
      </div>

    </div>
  </section>

</div>

<style>
/* Syllabus Page Layout - Using Weekly Hub Patterns */
.syllabus {
  max-width: 1200px;
  margin: 0 auto;
}

/* Course Banner - Similar to Current Week Banner */
.course-banner {
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
  border-radius: 0.75rem;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2.5rem;
  margin-top: 0;
  box-shadow: 0 4px 15px rgba(5, 150, 105, 0.2);
}

.course-content {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.course-label {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.course-info h2 {
  color: white;
  font-size: 1.25rem;
  margin: 0 0 0.25rem 0;
}

.course-info p {
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-size: 0.875rem;
}

.course-btn {
  background: white;
  color: #059669;
  padding: 0.6rem 1.25rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.course-btn:hover {
  transform: translateX(2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  text-decoration: none;
  color: #059669;
}

/* Section Layout */
.syllabus-section {
  margin-bottom: 2.5rem;
}

.section-title {
  color: var(--text-secondary);
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 0 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-color);
}

/* Grid Layouts */
.info-grid,
.skills-grid,
.assessment-grid,
.contact-grid,
.references-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.skills-grid {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

/* Item Styles */
.info-item,
.skill-item,
.assessment-item,
.contact-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

/* Reference Item Specific Styles */
.reference-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.625rem;
  padding: 1.25rem;
  transition: all 0.2s ease;
  position: relative;
}

.reference-item:hover {
  border-color: #6b7280;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  background: linear-gradient(135deg, #fafafa 0%, var(--background-color) 100%);
}

.info-item:hover,
.skill-item:hover,
.assessment-item:hover,
.contact-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.info-item::before,
.skill-item::before,
.assessment-item::before,
.contact-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--primary-color);
  transform: scaleY(0);
  transition: transform 0.2s ease;
}

.info-item:hover::before,
.skill-item:hover::before,
.assessment-item:hover::before,
.contact-item:hover::before {
  transform: scaleY(1);
}

/* Headers and Icons */
.info-header,
.contact-header {
  margin-bottom: 0.5rem;
}

.info-badge,
.contact-role-badge {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.reference-type {
  background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
  color: var(--text-secondary);
  padding: 0.25rem 0.625rem;
  border-radius: 0.375rem;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.info-badge.priority {
  background: #10b981;
}

.skill-icon,
.assessment-icon {
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
  display: block;
}

/* Item Content */
.info-item h4,
.skill-item h4,
.assessment-item h4,
.contact-item h4,
.reference-item h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.info-item p,
.skill-item p,
.assessment-item p,
.contact-item p,
.reference-item p {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.4;
}

/* Special States */
.assessment-item.primary {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, var(--background-color) 100%);
}

.project-link {
  display: inline-block;
  margin-top: 0.5rem;
  color: #3b82f6;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.project-link:hover {
  color: #2563eb;
  transform: translateX(2px);
}

/* Schedule Parts */
.schedule-parts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.schedule-part {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.schedule-part:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.schedule-part::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--primary-color);
  transform: scaleY(0);
  transition: transform 0.2s ease;
}

.schedule-part:hover::before {
  transform: scaleY(1);
}

.part-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.part-badge {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.part-header h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
  flex: 1;
  text-align: center;
}

.part-dates {
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 500;
}

.part-topics {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.topic {
  background: var(--surface-color);
  color: var(--text-secondary);
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-size: 0.7rem;
  font-weight: 500;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .course-banner {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .course-content {
    flex-direction: column;
  }
  
  .info-grid,
  .skills-grid,
  .assessment-grid,
  .contact-grid,
  .references-grid,
  .schedule-parts {
    grid-template-columns: 1fr;
  }
  
  .part-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .part-header h4 {
    text-align: left;
  }
}
</style>
