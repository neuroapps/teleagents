# 🚀 NeuroApps AI Agent Development Guide

Welcome to **NeuroApps**, the AI Agents Marketplace! This guide explains how to **create, format, and submit your AI agent** for deployment in our ecosystem.

---
## **📌 1. Prerequisites**
Before you start, ensure you have:
- ✅ Python 3.9+
- ✅ `pip install -r requirements.txt` (from this repo)
- ✅ Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- ✅ GitHub account
- ✅ GitHub CLI (`gh`) installed ([Get GitHub CLI](https://cli.github.com/))

---

## **📌 2. Fork & Clone the `agents` Repository**

Fork the **NeuroApps Agents Repository**:
👉 [https://github.com/neuroapps/agent.git](https://github.com/neuroapps/agent.git)

Clone it to your local machine:
```bash
# Replace "your-username" with your GitHub username
git clone https://github.com/neuroapps/agent.git
cd agents
```

---

## **📌 3. Implement Your AI Agent**
All agents **must** follow the `AgentServiceBase` format.

📌 **Create `agent/agent.py`**
```python
from schemas import Message, IntroResponse, HelpResponse
from agent_base import AgentServiceBase

class MyAgent(AgentServiceBase):
    def Intro(self):
        return IntroResponse(name="My AI Agent", description="A powerful AI assistant")

    def Help(self):
        return HelpResponse(instructions="Send a text message to get started.")

    def ExecuteStream(self, request: Message):
        yield Message(text=f"Processing: {request.text}")

    def HandleCallbackStream(self, request: Message):
        yield Message(text=f"Callback received: {request.callback_data}")
```
✅ **This ensures your agent is compatible with our system.**

---

## **📌 4. Create a Dockerfile for Your Agent**
📌 **Create `agents/my_agent/Dockerfile`**
```dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run_agent.py"]
```

---

## **📌 5. Build & Push Your Agent to GitHub Container Registry (GHCR)**
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

## **📌 6. Submit Your Agent for Deployment**
Once your agent is containerized, submit it for approval.

1️⃣ **Create a new metadata file inside `agents/`**
```bash
touch agent/agent.md
```

2️⃣ **Edit `agents/agent.md` and add the following:**
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

## **📌 7. Moderation and Approval**
- 🛠️ **Your submission will be reviewed** by the NeuroApps moderation team.
- ✅ **Once approved**, your agent will be **automatically deployed**.
- 🔥 **You will receive a notification** when your agent is live!

---

## 🎉 **Congratulations! Your Agent is Live!**
You can now interact with your deployed AI agent via the NeuroApps API:
```bash
curl -X GET "https://api.neuroapps.tech/agent/<your-dev-token>/my_agent?input=Hello"
```

---

## **💡 Need Help?**
If you run into any issues, join our **NeuroApps Developer Community**: 👉 [[Telegram](https://t.me/neuroapps_devs) / Discord Link]

🚀 Happy Coding!

