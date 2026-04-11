---
id: adkcourse
summary: Master the Agent Development Kit (ADK) and Google’s Gemini API to engineer sophisticated, autonomous AI systems. From fundamentals of deploying agent on Google Cloud, you will rapidly advance to designing complex workflows using Sequential, Parallel, and Loop patterns. The lab dives deep into multi-agent orchestration techniques—including Routers and the "Agent-as-a-Tool" paradigm—enabling specialized agents to collaborate effectively. By integrating Long-Term Memory for context retention and the Model Context Protocol (MCP) for connecting to external data, you will walk away with the skills to build robust, intelligent applications capable of reasoning, planning, and executing real-world tasks.
authors: Qingyue(Annie) Wang
duration: 0
keywords: docType:Codelab
award_behavior: AWARD_BEHAVIOR_ENABLE
layout: paginated

---
---
# ADK Agentic Pattern with Memory & MCP


## What you will learn

### Welcome to the ADK Master Class - Your Journey into Multi-Agent Systems
You're about to step into the exciting world of AI agents. Forget simple chatbots that just answer questions. We're diving deep into the `Agent Development Kit (ADK)` to build sophisticated, autonomous systems that can reason, plan, and use tools to accomplish complex tasks. 

> aside positive
This entire codelab will be a hands-on journey, this 1 **GitHub Repo** that contain all the code and examples for our sessions.
[github repo](https://github.com/cuppibla/adk_tutorial/tree/main)


![cover](img/cover_1.png)

By the end of this tutorial, you will be able to:
- **Build Your First AI Agent**: Go from zero to a fully functional agent that can understand a user's needs, use tools like Google Search, and generate detailed, helpful responses.

- **Construct Multi-Agent Systems**: Learn the **"Agent-as-a-Tool"** pattern, a revolutionary concept where agents delegate tasks to other specialized agents, creating a team of AI experts that work together.

- **Orchestrate Complex Workflows**: Go beyond simple delegation and master advanced patterns like **Routers**, **Sequential Chains**, **Loops**, and **Parallel Execution** to build robust, efficient, and intelligent applications that can handle almost any requests.

- **Give Your Agents Memory**: Understand the critical role of conversational memory, enabling your agents to handle follow-up questions, learn from feedback, and manage multi-step tasks seamlessly.

- **Connect with MCP**: Connect wih MCP toolbox.

Let's get started! 🚀

## Setup GCP & Gemini API Key

### Setting Up Your GCP Project & Gemini API Key
To power our AI agents, we need two things: a Google Cloud Project to provide the foundation and a Gemini API Key to access Google's powerful models. 


**Step 1: Enable Billing Account**

-  Claiming your [billing account](https://goo.gle/adkadvancedlab) with 5 dollar credit, you will need it for your deployment. Make sure to your **gmail** account.

> aside positive
**No credit card or payment needed** — you’ll receive $5 free credits. It takes less than 2 minutes, just enter your name and accept the credits.

**Step 2: Create A New GCP Project**
- Go to Google Cloud Console and create a new project.

![create a new gcp account](img/gcp_new.png)

- Go to Google Cloud Console and create a new project.

- Open left panel, click `Billing`, check whether the billing account is linked to this gcp account.

![Link the billing account to gcp account](img/billing_account.png)

If you see this page, check the `manage billing account`, choose the Google Cloud Trial One and linked to it.


**Step 3: Find your Google Cloud Project ID**

👉Click Activate Cloud Shell at the top of the Google Cloud console (It's the terminal shape icon at the top of the Cloud Shell pane),
![cloud-shell.png](img/03-01-cloud-shell.png)

👉Click on the "Open Editor" button (it looks like an open folder with a pencil). This will open the Cloud Shell Code Editor in the window. You'll see a file explorer on the left side.
![open-editor.png](img/03-02-open-editor.png)

👉Find your Google Cloud Project ID:

- Open the Google Cloud Console: [link](https://console.cloud.google.com)
- Select the project you want to use for this workshop from the project drop down at the top of the page.
- Your Project ID is displayed in the Project info card on the Dashboard

![03-04-project-id.png](img/03-04-project-id.png)

👉💻 In the terminal, verify that you're already authenticated and that the project is set to your project ID using the following command:

```bash
gcloud auth list
```

👉💻 Clone the bootstrap project from GitHub:

```bash
git clone https://github.com/cuppibla/adk_tutorial.git
```

👉💻 Run the initialization script, this script will prompt you to enter your **Google Cloud Project ID**. 
And enter Google Cloud Project ID you found from the last step when prompted by the `setup_venv.sh` script.
```bash
cd ~/adk_tutorial
./setup_venv.sh

gcloud services enable  compute.googleapis.com \
                        artifactregistry.googleapis.com \
                        run.googleapis.com \
                        iam.googleapis.com \
                        aiplatform.googleapis.com \
                        cloudresourcemanager.googleapis.com
```

## Session 1: Your First Agent in ADK Web
Open ADK Web by Running:
```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
adk web
```

After running the commands, you should see output in your terminal indicating that the ADK Web Server has started, similar to this:

```text
+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://localhost:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
👉 Next, to access the ADK Dev UI from your browser:

From the Web preview icon (often looks like an eye or a square with an arrow) in the Cloud Shell toolbar (usually top right), select Change port. In the pop-up window, **set the port to 8000** and click "**Change and Preview**". Cloud Shell will then open a new browser tab or window displaying the ADK Dev UI.

![webpreview](img/05-01-webpreview.png)

👉 Your summoning ritual is complete, and the agent is now running. The **ADK Dev UI** in your browser is your direct connection to the Familiar.

**choose the parallel workflow agent**
In the dropdown menu at the top of the UI, choose the `parallel_agent`.


You can select the `single_agent` here:
![tracing picture of single agents](img/single_agent_result.png)


You can see the tracing here:
![tracing picture of single agent](img/single_agent_tracing.png)

👉  **Test Prompt:**
```
Plan a trip from Sunnyvale to San Francisco this weekend, I love food and art.
```

## Session 2: Workflow Agent: Sequential Agent, Parallel Agent, Loop Agent
> aside positive
Open your ADK Web UI following **session 1** steps.


### Parallel Agent
**choose the parallel workflow agent**
In the dropdown menu at the top of the UI, choose the `parallel_agent`.

👉  **Test Prompt:**
```
Plan my trip to San Francisco, I want to find some good concert, restaurant and museum.
```

You can select the `parallel_agent` here:
![tracing picture of parallel agents](img/parallel_select.png)


You can see the tracing here:
![tracing picture of parallel agents](img/parallel_tracing.png)


### Sequential Agent
**choose the sequential workflow agent**
In the dropdown menu at the top of the UI, choose the `sequential_agent`.

👉  **Test Prompt:**
```
Find a good sushi near Standford and tell me how to get there.
```

You can select the `sequential_agent` here:
![tracing picture of sequential agents](img/sequential_select.png)

You can see the tracing here:
![tracing picture of sequential_agent](img/sequetial_tracing.png)

### Loop Agent

**choose the loop workflow agent**
In the dropdown menu at the top of the UI, choose the `loop_agent`.

👉  **Test Prompt:**
```
Plan a trip from Sunnyvale to San Francisco today.
```

You can select the `loop_agent` here:
![tracing picture of loop agents](img/loop_select.png)

You can see the tracing here:
![tracing picture of loop agents](img/loop_tracing.png)

## Session 3: Custom Agent
> aside positive
Open your ADK Web UI following **session 1** steps.

Once your ADK Web UI is open, you can select the `Custom_Agent` agent.

👉  **Test Prompt:**
```
Plan a trip from Sunnyvale to San Francisco this weekend, I love food and art. Make sure within budget of 100 dollars.
```

You can select the `Custom_Agent` here:
![tracing picture of Custom_Agent](img/custom_select.png)

You can see the tracing here:
![tracing picture of Custom_Agent](img/custom_tracing.png)

## Session 4: Orchestrator Pattern - Routing Agent
> aside positive
Open your ADK Web UI following **session 1** steps.

Once your ADK Web UI is open, you can select the `routing_agent`.

👉  **Test Prompt:**
```
Plan a trip from Sunnyvale to San Francisco this weekend, I love concert, restaurant and museum.
```

You can select the `routing_agent` here:
![tracing picture of routing agents](img/routing_select.png)

You can see the tracing here:
![tracing picture of routing agents](img/routing_tracing.png)


## Session 5: Agent as tool
> aside positive
Open your ADK Web UI following **session 1** steps.


Once your ADK Web UI is open, you can select the `Agent_as_tool` agent.


👉  **Test Prompt:**
```
Plan a trip from Sunnyvale to San Francisco this weekend, I love concert, restaurant and museum.
```

You can select the `agent_as_tool` here:
![tracing picture of agent as tool](img/agentastool_select.png)

You can see the tracing here:
![tracing picture of routing agents](img/agentastool_tracing.png)


## Session 6: Agent With Long Term Memory
👉💻 Test your long term memory by go to the folder and use the runner to power up the agent:
```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
cd ~/adk_tutorial/f_agent_with_memory
python main.py
```

👉  **Test Prompt:**
```bash
I like Art and Italian food.
```

Then end the session by pressing "crtl+C". Restart the session:
```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
cd ~/adk_tutorial/f_agent_with_memory
python main.py
```
👉  **Test Prompt:**
```bash
Plan a trip to San Francisco based on my preference.
```

## Session 7: Empower your agent with MCP

### Step 1: Prepare the Local Database
👉💻 run the following command in your terminal

```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
chmod +x setup_trip_database.py
./setup_trip_database.py
```


### Step 2:  Install and Run the MCP Toolbox Server
👉💻 run the following command in your terminal

```bash
cd ~/adk_tutorial/mcp_tool_box
export VERSION=0.16.0
curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
```

once finishing downloading, and then run
```bash
chmod +x toolbox
```

### Step 3

**In one terminal**
Run the following command
```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
cd ~/adk_tutorial/mcp_tool_box
./toolbox --tools-file "trip_tools.yaml" --port 7001
```

**In another terminal**
Run the following command
```bash
cd ~/adk_tutorial
source .adk_env/bin/activate
cd ~/adk_tutorial/g_agents_mcp
python main.py
```