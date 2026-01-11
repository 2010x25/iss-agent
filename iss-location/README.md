# ISS Location MCP Server & Google ADK Agent

A simple MCP server built with **FastMCP** that provides real time International Space Station (ISS) data — including position and current crew — and is used by a **Google ADK agent** to fetch and expose that data.

This project demonstrates how to:

- Build an **MCP server** using FastMCP
- Query the **free ISS REST API** for live data
- Expose tools and resources that an ADK agent can call

## 🚀 Features

✔ FastMCP‑powered MCP server — lightweight and easy to extend  
✔ Tools and resources for:
- ISS **current geographic position**
- ISS **current crew manifest**  
✔ Designed to integrate with a **Google ADK agent**

## 📦 Project Structure

```
iss-location/
|── iss_assistant
|────agent.py
├── iss_mcp_server.py
├── requirements.txt
└── README.md
```

## 🧠 What It Does

When the MCP server runs, it exposes functions that:

1. Fetch ISS current location data from the free ISS REST API  
2. Fetch current ISS crew data  
3. Return that information as JSON tools/resources for clients (e.g., agents) to consume

## 📥 Installation

```bash
git clone https://github.com/2010x25/iss-agent.git
cd iss-agent/iss-location
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
.\venv\Scripts\activate # Windows
pip install -r requirements.txt
```

## 🏃 Running the Agent

```bash
adk web
```
<img src="adk-web.PNG">

## 📡 ISS REST API

Uses free public ISS endpoints:
- Current location http://api.open-notify.org/iss-now.json
- Current crew aboard ISS http://api.open-notify.org/astros.json

No API key required.

## 🛠️ Extending

You can extend this MCP server by adding more tools, resources, or prompts using FastMCP decorators.

## 📄 License

Open-source. Free to use and modify.
