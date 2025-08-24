[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-red?logo=pytorch&logoColor=white)](https://pytorch.org/) 
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/transformers/) 
[![T5 Model](https://img.shields.io/badge/Model-T5-lightgrey?logo=google&logoColor=white)](https://huggingface.co/t5-base) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)



# 🏥 Healthcare Q&A System using T5 Transformer

This project implements an **AI-powered healthcare Question-Answering (Q&A) chatbot** using the **T5 (Text-to-Text Transfer Transformer)** model.  
Unlike traditional rule-based systems, this chatbot generates **context-aware, human-like responses** for medical-related queries.  

Built with **Flask + SocketIO**, it supports **real-time chat interaction** via a user-friendly web interface.  

---

## 📌 Features
- 🤖 Deep Learning-based chatbot using **T5 Transformer**  
- 🧠 Trained & fine-tuned on **MedQuAD Medical Dataset**  
- ⚡ Real-time interactive chat using **Flask-SocketIO**  
- 📊 Model evaluation with **BLEU, ROUGE-L, and Exact Match (EM)** metrics  
- 💬 GUI-based chatbot interface for smooth interaction  
- 🔒 Preprocessing pipeline for **clean, high-quality medical text**  

---

## 🛠️ Tech Stack
- **Backend**: Flask, Flask-SocketIO  
- **Frontend**: HTML, CSS, JavaScript (chat interface)  
- **AI / ML**: PyTorch, Hugging Face Transformers (T5 model)  
- **Dataset**: MedQuAD (~28 GB medical Q&A dataset)  

---


## 📊 Model Evaluation
- **Exact Match (EM):** High accuracy in matching correct medical responses
- <img width="955" height="547" alt="image" src="https://github.com/user-attachments/assets/9afe736d-0302-4fdb-85cd-b45ace611d8b" />

- **BLEU Score:** Strong fluency & semantic similarity with reference answers
- <img width="941" height="540" alt="image" src="https://github.com/user-attachments/assets/1fc83b1d-f2cf-4ae5-bd4e-318a2cf12984" />
 
- **ROUGE-L Score:** High overlap with longest common subsequences → good summarization ability
- <img width="811" height="432" alt="image" src="https://github.com/user-attachments/assets/361edcb7-883f-4795-a8b3-c082810ca2a5" />


📌 Example Confusion Analysis:
| Metric          | Value |
|-----------------|-------|
| Exact Match     | 78%   |
| BLEU            | 0.65  |
| ROUGE-L         | 0.72  |

