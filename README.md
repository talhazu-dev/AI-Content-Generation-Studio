# ✍️ AI Content Generation Studio

A lightweight, high-performance web application built with **Streamlit** that interacts directly with Google's Gemini API to generate structured, professional content based on custom templates, tones, and target audiences.

## 🚀 The Twist (Zero External AI SDK Dependency)
Unlike standard applications that rely on heavy external Google/Gemini SDKs, this project utilizes **Python's standard libraries (`urllib`, `json`)** to construct and send direct HTTP POST requests. This ensures zero version conflicts, maximum speed, and a highly customized connection engine.

## ✨ Features
- **Dynamic API Key Activation:** No hardcoded keys or complex `.env` files required during deployment; users paste their key securely via the UI.
- **Tailored Templates:** Instantly write Blog Posts, Social Media Captions, Ad Copies, Cold Emails, and LinkedIn Posts.
- **Granular Controls:** Fine-tune the AI's output by choosing specific tones (Professional, Casual, Witty, etc.), content length, and target audiences.
- **One-Click Export:** Download generated content instantly as a clean Markdown (`.md`) file.

## 🛠️ Tech Stack
- **Frontend/Interface:** Streamlit
- **Backend/Engine:** Pure Python 3.x (`urllib`, `json`)
- **LLM Powering the App:** Gemini 1.5 Flash (via Google AI Studio)

## 🏃‍♂️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/talhazu-dev/AI-Content-Generation-Studio.git](https://github.com/talhazu-dev/AI-Content-Generation-Studio.git)