
# Precision Navigation and Timing (PNT) Self-Study Program

## Audience
Senior undergraduate and MS students in mechanical, aerospace, electrical, robotics, or related engineering fields.

## Program goal
By the end of this program, a student should be able to:
1. explain how GNSS produces position, velocity, and time (PVT)
2. distinguish geometric range from pseudorange
3. recognize common GNSS error sources and failure modes
4. implement a simple residual-based spoofing detector
5. fuse GNSS and IMU data in a basic Kalman filter
6. explain why multi-receiver systems improve resilience

## Suggested pacing
- **Duration:** 5 weeks + capstone
- **Time:** 6–8 hours per week
- **Structure each week:**
  - 2–3 hours curated reading/video
  - 2–3 hours notebook work
  - 1–2 hours written synthesis

---

## Week 1 — GNSS basics and pseudorange positioning
### Learning objectives
- Understand PVT, ECEF, geometric range, and pseudorange
- See why receiver clock bias creates a fourth unknown
- Solve a simple position problem with nonlinear least squares

### Curated resources
- ESA Navipedia — GNSS Basic Observables  
  https://gssc.esa.int/navipedia/index.php/GNSS_Basic_Observables
- ESA Navipedia — An intuitive approach to the GNSS positioning  
  https://gssc.esa.int/navipedia/index.php/An_intuitive_approach_to_the_GNSS_positioning
- ESA Navipedia — GNSS Receivers General Introduction  
  https://gssc.esa.int/navipedia/index.php/GNSS_Receivers_General_Introduction
- YouTube playlist — GPS: An Introduction to Satellite Navigation  
  https://www.youtube.com/playlist?list=PLGvhNIiu1ubyEOJga50LJMzVXtbUq6CPo

### Assignment
Complete `week1/week1_gnss_basics.ipynb` and estimate receiver position and clock bias from satellite ECEF positions and pseudoranges.

---

## Week 2 — Error sources and failure signatures
### Learning objectives
- Distinguish noise, bias, multipath-like behavior, and spoofing-like drift
- Interpret residual plots
- Explain why PNT systems need integrity monitoring

### Curated resources
- ESA Navipedia — GNSS Measurements Modelling  
  https://gssc.esa.int/navipedia/index.php/GNSS_Measurements_Modelling
- Penn State open courseware — GEOG 862: GPS and GNSS for Geospatial Professionals  
  https://www.e-education.psu.edu/geog862/
- Inside GNSS — Detecting GNSS Spoofing  
  https://insidegnss.com/detecting-gnss-spoofing/
- Inside GNSS — Nobody's Fool: Spoofing Detection in a High-Precision Receiver  
  https://insidegnss.com/nobodys-fool-spoofing-detection-in-a-high-precision-receiver/

### Assignment
Complete `week2/week2_error_sources.ipynb` and classify each residual trace as clean, noisy, biased, or spoofing-like.

---

## Week 3 — Residual-based spoofing detection
### Learning objectives
- Aggregate residuals across satellites
- Build a threshold detector
- Compute false positives, false negatives, and detection delay

### Curated resources
- Inside GNSS — Thwarting GNSS Spoofing Attacks  
  https://insidegnss.com/thwarting-gnss-spoofing-attacks/
- YouTube — What is RAIM | Receiver Autonomous Monitoring  
  https://www.youtube.com/watch?v=7ESZcUCKieA
- YouTube — Special Topics - GPS (40 of 100) What is the Pseudorange?  
  https://www.youtube.com/watch?v=PXvZYy9ZbaY

### Assignment
Complete `week3/week3_detection.ipynb` and build a detector from aggregated residual statistics.

---

## Week 4 — GNSS + IMU fusion
### Learning objectives
- Understand the role of inertial sensing in degraded GNSS conditions
- Implement a basic Kalman filter
- Compare GNSS-only and fused estimates under spoofing

### Curated resources
- MIT OpenCourseWare — Identification, Estimation, and Learning: lecture notes on Kalman filtering  
  https://ocw.mit.edu/courses/2-160-identification-estimation-and-learning-spring-2006/resources/lecture_5/
- MIT OpenCourseWare — Stochastic Estimation and Control  
  https://ocw.mit.edu/courses/16-322-stochastic-estimation-and-control-fall-2004/
- YouTube — Kalman Filter for Beginners, Part 1  
  https://www.youtube.com/watch?v=HCd-leV8OkU
- YouTube — GPS/GNSS and Inertial Navigation  
  https://www.youtube.com/watch?v=lWJpM2tbh_U

### Assignment
Complete `week4/week4_sensor_fusion.ipynb` and evaluate whether fusion reduces navigation error during spoofing.

---

## Week 5 — Multi-receiver resilience
### Learning objectives
- Understand baseline consistency and common-mode attacks
- See why multiple receivers can expose spatial inconsistencies
- Connect the topic to DGNSS and networked monitoring concepts

### Curated resources
- ESA Navipedia — DGNSS Fundamentals  
  https://gssc.esa.int/navipedia/index.php/DGNSS_Fundamentals
- YouTube — GNSS Spoofing Detection through Spatial Processing  
  https://www.youtube.com/watch?v=A7W8vVqjC2I
- Inside GNSS — Detecting GNSS Spoofing  
  https://insidegnss.com/detecting-gnss-spoofing/

### Assignment
Complete `week5/week5_multi_receiver.ipynb` and detect spoofing by monitoring the measured baseline between two static receivers.

---

## Capstone — Resilient navigation under spoofing
### Problem
Use the capstone dataset to:
1. detect spoofing
2. maintain a resilient position estimate
3. report quantitative performance

### Deliverables
- code
- one detection plot
- one navigation plot
- one short memo (2–3 pages) summarizing the method and results

### File
- `capstone/capstone_project.ipynb`

---

## Repository contents
- `datasets/` synthetic datasets used by all notebooks
- `week1/` through `week5/` starter notebooks
- `capstone/` capstone notebook
- `docs/` handout-ready syllabus files

---

## Instructor notes
This package is intentionally designed so a faculty member can deploy it quickly:
- the internet resources are already curated
- the datasets are already generated
- the notebooks are scaffolded but not fully solved
- the capstone can be completed individually or in pairs

## Suggested grading rubric
- 25% weekly notebook completion
- 25% code quality and reproducibility
- 25% technical interpretation of results
- 25% capstone performance and memo

<\> Markdown
