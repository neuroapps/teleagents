# 🚀 NeuroApps AI Agent Developer Guide

Welcome to the **NeuroApps AI Agent Submission Guide**! This document will help you set up, develop, and deploy your AI agent to **NeuroApps** using **GitHub Container Registry (GHCR)**.

## 📌 1. Prerequisites
Before you start, ensure you have:
- ✅ A **GitHub account**
- ✅ **Docker installed** ([Get Docker](https://docs.docker.com/get-docker/))
- ✅ **GitHub CLI (`gh`) installed** ([Get GitHub CLI](https://cli.github.com/))
- ✅ **Python 3.9+ installed**

---

## 📌 2. Fork and Clone the `agents` Repository

First, fork the **NeuroApps Agents Repository**:
👉 [https://github.com/neuroapps/agents.git](https://github.com/neuroapps/agents.git)

Then, clone it to your machine:
```bash
# Replace "your-username" with your GitHub username
git clone https://github.com/your-username/agents.git
cd agents
```

---

## 📌 3. Create a New AI Agent
Navigate to the `agents/` directory and create a new folder for your agent:
```bash
mkdir agents/my_agent
cd agents/my_agent
```
Create the following files inside `my_agent/`:

### **🔹 `main.py` (Your AI Agent Code)**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from My AI Agent!"}
```

### **🔹 `requirements.txt` (Dependencies)**
```text
fastapi
uvicorn
```

### **🔹 `Dockerfile` (Container Definition)**
```dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50051"]
```

---

## 📌 4. Build and Test the Agent Locally
Test your agent locally before deploying it.
```bash
# Install dependencies
pip install -r requirements.txt

# Run the agent
uvicorn main:app --host 0.0.0.0 --port 50051
```
Now, open your browser and go to:
👉 `http://127.0.0.1:50051/`

✅ **You should see:**
```json
{"message": "Hello from My AI Agent!"}
```

---

## 📌 5. Build and Push the Agent to GitHub Container Registry (GHCR)
1️⃣ **Log in to GitHub Container Registry:**
```bash
echo "YOUR_GITHUB_TOKEN" | docker login ghcr.io -u your-username --password-stdin
```
> **Note:** If you don’t have a GitHub token, create one with `write:packages` permissions [here](https://github.com/settings/tokens).

2️⃣ **Build the Docker image:**
```bash
docker build -t ghcr.io/neuroapps/my_agent:latest .
```

3️⃣ **Push the image to GHCR:**
```bash
docker push ghcr.io/neuroapps/my_agent:latest
```

---

## 📌 6. Submit Your Agent for Deployment
Now that your agent is containerized, submit it for approval.

1️⃣ **Create a new file inside `agents/` named `my_agent.md`**
```bash
touch agents/my_agent.md
```

2️⃣ **Edit `my_agent.md` and add the following information:**
```md
# My AI Agent
- **Agent Name:** My AI Agent
- **GitHub Container URL:** ghcr.io/neuroapps/my_agent:latest
- **Description:** A simple AI agent for testing.
- **Keywords:** AI, API, chatbot
```

3️⃣ **Commit and push your submission:**
```bash
git add agents/my_agent.md
git commit -m "Submitting My AI Agent for deployment"
git push origin main
```

4️⃣ **Create a Pull Request in GitHub:**
```bash
gh pr create --repo neuroapps/agents --title "New AI Agent Submission" --body "Submitting my AI agent for review and deployment."
```

---

## 📌 7. Moderation and Approval
- 🛠️ **Your submission will be reviewed** by the NeuroApps moderation team.
- ✅ **Once approved**, your agent will be automatically deployed and made available via API.
- 🔥 **You will receive a notification** when your agent is live!

---

## 🎉 **Congratulations! Your Agent is Live!**
You can now interact with your deployed AI agent via the NeuroApps API:
```bash
curl -X GET "https://api.neuroapps.tech/agent/my_agent?input=Hello"
```

---

## **💡 Need Help?**
If you run into any issues, join our **NeuroApps Developer Community**: 👉 [Telegram / Discord Link]

🚀 Happy Coding!

