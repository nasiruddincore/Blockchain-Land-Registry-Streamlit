# 🏢 Blockchain-Based Land Registry & Property Ownership System

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A decentralized prototype simulating a tamper-evident land-records system where property parcels are registered, verified, and traceable end-to-end, with ownership transfers requiring role-based approvals and an auditable on-chain ledger trail.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [System Objectives](#-system-objectives)
- [Industry Relevance & Use Cases](#-industry-relevance--use-cases)
- [Project Actors & Permissions](#-project-actors--permissions)
- [Folder Structure](#-folder-structure)
- [Installation & Setup Guide](#-installation--setup-guide)
- [How to Run the Application](#-how-to-run-the-application)
- [System Architecture & Data Flow](#-system-architecture--data-flow)
- [Legal & Real-World Considerations](#-legal--real-world-considerations)
- [Author & License](#-author--license)

---

## 📌 Project Overview
Traditional paper-based land records are fragmented, slow to reconcile, and vulnerable to fraud, double-sales, and tampering. This project models a next-generation PropTech solution using an immutable ledger backend and a multi-role Streamlit web dashboard to simulate safe property lifecycles from registration to verified ownership transfers.

---

## ⚠️ Problem Statement
* **Fraud & Manipulation:** Paper titles can be physically forged or illegally altered.
* **Double-Selling:** Lack of a single source of truth allows bad actors to sell the same parcel to multiple buyers.
* **Opaque History:** Tracing previous legal owners requires manual intervention through multiple bureaucratic offices.

---

## 🎯 System Objectives
1. **Secure Registration:** Enable authorized land authorities to register unique parcels (`P-001`, `P-002`, etc.) with immutable metadata and SHA-256 document hashes.
2. **Role-Based Workflows:** Enforce strict separation between administrative verification rules and owner-initiated transfers.
3. **Auditable History:** Maintain an immutable event log tracking every registration, verification, and transfer.
4. **Transparent Lookup:** Provide a public verification portal for citizens to validate title status instantly.

---

## 🏭 Industry Relevance & Use Cases
* **Government Land Registries:** Modernizing state and national title issuance offices.
* **Real-Estate Technology (PropTech):** Speeding up property due diligence for brokerages and buyers.
* **Mortgage & Loan Verification:** Allowing commercial banks to verify clean titles instantly before collateral disbursement.

---

## 👥 Project Actors & Permissions

| Actor | Responsibilities | Permissions |
| :--- | :--- | :--- |
| **Land Authority / Admin** | Registers parcels, audits information, approves verification requests | Full Admin Access |
| **Property Owner** | Views owned assets, initiates secure ownership transfers to valid buyer wallets | Owner-Gated Access |
| **Public / Buyer** | Searches property status, verifies document hashes, audits transfer history | Read-Only Access |

---

## 📂 Folder Structure
```text
Blockchain-Land-Registry-Streamlit/
│
├── requirements.txt                 # Python project dependencies
├── README.md                        # Project documentation
│
├── data/
│   └── property_registry.json       # Simulated on-chain state & history log
│
├── backend/
│   └── registry_logic.py            # Simulated smart contract state machine
│
└── frontend/
    └── app.py                       # Interactive Streamlit Dashboard
