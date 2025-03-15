# 🚀 NeuroApps Private AI Agent Submission Guide

Welcome to **NeuroApps**, the AI Skills Marketplace! This guide explains how to **submit your AI agent privately** using GitHub **private pull requests (PRs)**.

## **📌 1. Submission Overview**
NeuroApps ensures **your agent code remains private** while allowing us to **review, wrap, and deploy it securely**.

### **How It Works:**
1️⃣ **You submit a private PR** to the `neuroapps/agents` repository.
2️⃣ **We review your code** for security, quality, and adherence to guidelines.
3️⃣ **Once approved, we wrap your agent in gRPC** and deploy it securely.
4️⃣ **Your agent is live on our platform!** 🎉

---

## **📌 2. Prerequisites**
Before you start, ensure you have:
- ✅ Python 3.9+
- ✅ `pip install -r requirements.txt` (from this repo)
- ✅ Git & GitHub CLI (`gh`) installed ([Get GitHub CLI](https://cli.github.com/))
- ✅ **Your fork of `neuroapps/agents.git`**

---

## **📌 3. Fork & Clone the Repository**
Since our repository is **private**, you need to **fork** it first.

1️⃣ **Fork the `neuroapps/agents` repository** (you will not see other forks or PRs).
👉 [https://github.com/neuroapps/agents.git](https://github.com/neuroapps/agents.git)

2️⃣ **Clone your fork to your local machine:**
```bash
# Replace "your-username" with your GitHub username
git clone https://github.com/your-username/agents.git
cd agents
```

---

## **📌 4. Implement Your AI Agent**
All agents **must** follow the `AgentServiceBase` format.

📌 **Create `agents/my_agent.py`**
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

## **📌 5. Create a Dockerfile for Your Agent**
📌 **Create `agents/my_agent/Dockerfile`**
```dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run_agent.py"]
```

---

## **📌 6. Submit Your Agent as a Private PR**
Once your agent is implemented, **submit it for approval using a private PR.**

1️⃣ **Create a new branch:**
```bash
git checkout -b my-agent-submission
```

2️⃣ **Add & commit your agent:**
```bash
git add agents/my_agent
git commit -m "Submitting my AI agent"
```

3️⃣ **Push your branch to your fork:**
```bash
git push origin my-agent-submission
```

4️⃣ **Create a Private Pull Request:**
```bash
gh pr create --repo neuroapps/agents --title "New AI Agent Submission" --body "Review this agent for deployment."
```

🚨 **Your PR is private** – only NeuroApps maintainers can see it.

---

## **📌 7. Moderation & Review Process**
Once your PR is submitted, our team will:
✅ **Review your code manually** for security & quality.
✅ **Run automated checks** (code style, security, API compliance).
✅ **Approve & merge your PR** if everything is correct.
✅ **Deploy it.**

If we need changes, we will **leave comments in your PR**.

---

## **📌 8. Deployment Process**
Once approved, we will:
1️⃣ **Prepare you code for deployment.**
2️⃣ **Build the Docker image.**
```bash
docker build -t ghcr.io/neuroapps/my_agent:latest .
docker push ghcr.io/neuroapps/my_agent:latest
```
3️⃣ **Deploy it to the platform.**
```bash
docker-compose up -d
```
✅ **Your agent is now live and accessible via API!**

---

## 🎉 **Congratulations! Your Agent is Live!**
You can now interact with your deployed AI agent via the NeuroApps API:
```bash
curl -X GET "https://api.neuroapps.tech/agent/my_agent?input=Hello"
```

---

## **💡 Need Help?**
If you run into any issues, join our **NeuroApps Developer Community**: 👉 [[Telegram](https://t.me/neuroapp_devs) / Discord Link]

🚀 Happy Coding!

