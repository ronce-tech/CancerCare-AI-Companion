CancerCare AI Companion

AI Companion for Cancer Patients, Survivors & Caregivers
CancerCare AI is a multilingual educational and emotional support companion designed to help cancer patients and their families better understand their care journey.
Inspired by biomedical models (BioGPT, Med-PaLM), this project focuses on support, clarity, and navigation, not diagnosis.

Features (Modules A → G)

A) Chat Companion
Safe medical explanations
Emotional support
Structured summaries
Questions to ask your doctor
Multilingual (EN/FR/ES)

B) Risk Explorer (Educational Only)
Lifestyle input
Educational scoring
Visualizations
Evidence-based prevention tips

C) Doctor Visit Planner
Pre-appointment notes
Auto-generated questions
Visit summaries
PDF export (FastAPI)

D) Emotional Journal
Day-to-day reflections
Mood tracking
Private entries
Future: shared caregiver mode

E) Hospital Finder
Hospitals by city/ZIP
Cancer centers
Phone, address, website
(FR / USA / EU)

F) Insurance & Billing Helper
Upload bills (admin only)
Explanations of terms (CPT, copay, deductible…)
Navigation of US/FR systems

G) Resources Hub
Official links (WHO, ACS, Ligue Contre le Cancer)
Glossary
Trusted PDFs

Premium Features (v1.0+)
Multilingual FR/EN/ES
Firebase Authentication (users + caregivers)
Dark mode / Light mode
PDF generator (visits & journal)
Backend API (FastAPI)
React Native mobile app (iOS/Android)
Cloud sync (Firebase / iCloud)
Notifications (appointments, journaling)
Caregiver mode (shared entries)

📁 Project Structure
CancerCare-AI-Companion/
│
├─ backend/     # FastAPI AI API
├─ web/         # Streamlit web app
├─ mobile/      # React Native iOS/Android app
├─ docs/        # Roadmap, vision, architecture
├─ assets/      # Logos, UI mockups
└─ README.md

Tech Stack
Backend
FastAPI
Firebase Auth
OpenAI API
PDF toolkit
Pydantic models
Web App
Streamlit
Plotly
Requests → FastAPI backend
Mobile App
React Native
Expo
Firebase (Auth + Firestore)
Dark/light mode

Disclaimer
CancerCare AI is an educational and emotional support tool.
It does not provide diagnosis, medical interpretation, or treatment recommendations.

Roadmap
Phase 1 (Web V1 – MVP)
Streamlit interface
Chat Companion
Risk Explorer
Visit Planner
Journaling
Hospital Finder
Resources Hub
Phase 2 (Backend API)
Full FastAPI backend
Firebase Auth
DB for journal, visits, settings
PDF export
i18n API layer
Phase 3 (Mobile App v1.0)
React Native
Push notifications
Dark/light mode
Sync
Caregiver mode

Author
Alex Ronce
Santa Monica College — CS/Engineering Student
Founder of CancerCare AI Companion
