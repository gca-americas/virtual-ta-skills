---
id: adk-ap2-charity-agents
title: Building Trustworthy Charity Agents with Google ADK and AP2
summary: Build a production-grade AI Giving Agent that helps users discover and securely donate to verified charities. You will learn to use the Google Agent Development Kit (ADK) to create a multi-agent system and implement the core principles of the Agent Payments Protocol (AP2) to ensure every transaction is transparent, verifiable, and trustworthy.
authors: Ayo Adedeji
duration: 120
layout: paginated
award_behavior: AWARD_BEHAVIOR_ENABLE

---
# Building Trustworthy Charity Agents with Google ADK and AP2

## Building Trust to Unlock Generosity
**Duration: 10 min**

![banner](img/01-01-banner.gif)

### The Moment of Inspiration

Your phone buzzes. You see a news story about a successful literacy program helping children in underserved communities learn to read. You feel a powerful urge to contribute. You open your browser and search for **"children's literacy program donations**".

![google search](img/01-02-google-search.gif)

**Hundreds of results appear.**

You click the first link. The website looks professional. You scroll down to their financials. "Administrative costs: 28%." You pause. Only 72 cents of every dollar you donate will actually fund the program. Is that good? You're not sure.

You try another organization. You've never heard of them. Are they legitimate? A quick search leads you down a rabbit hole. You find a Reddit thread from two years ago where one user claims, "It's a scam, my donation never went anywhere." Another passionately defends them, "They're on the ground doing real work!" The ambiguity is paralyzing.

**Thirty minutes later**, you're deep in a maze of conflicting reviews, efficiency ratings, and IRS records, and you still haven't donated. The initial spark of generosity has been replaced by the friction of research. The tab stays open for a few days, a small reminder of a good intention, until you eventually close it.

### This Isn't a Personal Failure; It's a System Failure

This experience is universal. The desire to give is abundant, but the process is filled with hurdles that cause hesitation and doubt:

*   ❌ **Research Friction:** Every charity requires its own investigation.
*   ❌ **Trust Verification:** It's difficult to distinguish highly effective organizations from inefficient ones or even outright scams.
*   ❌ **Analysis Paralysis:** An overwhelming number of choices leads to decision fatigue.
*   ❌ **Momentum Loss:** The emotional drive to give fades as the logistical burden grows.

This friction has a staggering, real-world cost. Individual giving in the United States is immense—individual donors gave approximately **$374 billion** in 2023 alone, according to [Giving USA 2024](https://philanthropy.indianapolis.iu.edu/news-events/news/_news/2024/giving-usa-us-charitable-giving-totaled-557.16-billion-in-2023.html). Yet [research demonstrates](https://www.sciencedirect.com/science/article/abs/pii/S0047272723001275) that barriers to giving—including search costs, psychological friction, and time constraints—significantly reduce the amount that reaches charitable causes. [Studies involving millions of donors](https://www.gsb.stanford.edu/insights/new-research-could-help-nonprofits-attract-millions-online-donors) have found that even small amounts of friction in the online giving process prevent people from fulfilling their charitable intentions. 

**This represents billions of dollars in intended donations that never reach the causes that need them.**

### The Vision

Imagine a different experience. Instead of a 30-minute research session, you simply say:

> "I want to donate $50 to a literacy program for children. Find me a highly-rated, efficient, and verified charity."

And in seconds, you get a response that builds confidence:

![charity result card](img/01-03-charity-result-card.svg)

This is the promise of an AI Giving Agent. But to realize this vision, we must solve a fundamental challenge: **when an autonomous AI agent handles money, trust is not optional; it is the entire foundation.**

- How can we prove what a user authorized?
- Who is accountable if a mistake is made?
- How do we give donors, charities, and payment networks the confidence to participate?

### Your Mission Today

In this workshop, you will build that trustworthy agent by combining two powerful technologies:

| | **Google Agent Development Kit (ADK)** | **Agent Payments Protocol (AP2)** |
|---|---|---|
| **Role** | The **factory** for building production-grade AI agents | The **architectural blueprint** for trust in AI transactions |
| **What it provides** | • Framework for multi-agent orchestration<br>• Built-in security features like tool confirmation<br>• Production-ready observability and tracing<br>• Simple Python interface for complex agent behaviors | • Role-based security boundaries<br>• Verifiable digital credentials (mandates)<br>• Cryptographic proof of consent<br>• Complete audit trails for accountability |
| **Learn more** | [ADK Documentation](https://google.github.io/adk-docs/) | [AP2 Protocol](https://ap2-protocol.org/) |

> aside positive
> **Think of it this way:**  
> The **ADK** is *how* we build our agent's capabilities.  
> **AP2** is the *code of conduct* it follows to ensure every action with money is transparent, verifiable, and secure.

### What You Will Build

![architecture](img/01-04-architecture.svg)

By the end of this workshop, you will have created:

✅ **A Multi-Agent System** with specialized roles:
- A Shopping Agent that finds verified charities
- A Merchant Agent that creates binding donation offers  
- A Credentials Provider that securely processes payments
- An Orchestrator that coordinates the entire flow

✅ **Three Types of Verifiable Credentials**:
- IntentMandate: "Find me an education charity"
- CartMandate: "$50 to Room to Read, signed by merchant"
- PaymentMandate: "Process via simulated payment"

✅ **Security at Every Layer**:
- Role-based trust boundaries
- Explicit user consent

✅ **A Complete Audit Trail**:
- Every decision traceable
- Every consent recorded
- Every handoff visible

### 🔒 Important: This is a Safe Learning Environment

> aside negative
> **All Data in This Codelab is Completely Simulated**
> 
> This is a **100% safe educational environment**. You will:
> - **NEVER** enter real credit card or bank information
> - **NEVER** provide actual personal details or addresses
> - **NEVER** process real financial transactions
> - **NEVER** interact with real charities or payment systems
> 
> All *donations* are fictional demonstrations.  
> All *charities* are mock data for learning.  
> All *payments* return simulated success responses.
> 
> This codelab teaches the **architecture and patterns** for building trustworthy agents, using completely safe, simulated data throughout.

### Ready to Build Trust?

In the next module, we'll set up your development environment and build your first AI agent. You'll quickly discover why simple agents aren't trustworthy—and then spend the rest of the workshop learning how to fix that.

**Let's begin by understanding the problem firsthand.**

## Preparing Your Workspace
**Duration: 10 min**

### The Foundation for Trustworthy Agents

Before we can build our AI Giving Agent, we need to prepare a clean, consistent, and correctly configured development environment. This module is a focused step to ensure all the necessary tools and services are in place.

Completing this setup successfully means you can focus entirely on the exciting work of building agent logic in the modules to come, without worrying about configuration issues.

### Access Cloud Shell

First, we'll open Cloud Shell, which is a browser-based terminal with the Google Cloud SDK and other essential tools pre-installed.

### Need Google Cloud Credits?
>  aside positive
<br/> • **If you are attending an instructor-led workshop**: Your instructor will provide you with a credit code. Please use the one they provide.
<br/> • **If you are working through this Codelab on your own**: You can redeem a free Google Cloud credit to cover the workshop costs. Please [click this link](https://goo.gle/adk-charity-agents-credits) to get a credit and follow the steps in the video guide below to apply it to your account.
<br/>[![Watch the video](img/02-01-redeem-google-cloud-credits.png)](https://youtu.be/dR-NrgMTADs)
<BR/>

Click **Activate Cloud Shell** at the top of the Google Cloud Console (it's the terminal icon in the top-right navigation bar).

![cloud shell](img/02-02-cloud-shell.png)

Find your Google Cloud Project ID:
- Open the Google Cloud Console: [https://console.cloud.google.com](https://console.cloud.google.com)
- Select the project you want to use for this workshop from the project dropdown at the top of the page.
- Your Project ID is displayed in the Project info card on the Dashboard
![project id](img/02-03-project-id.png)

Once Cloud Shell opens, verify you're authenticated:

```bash
# Check that you are logged in
gcloud auth list
```

You should see your account listed as `(ACTIVE)`.

### Configure Your Project

Now let's set up your Google Cloud project and enable the necessary APIs.

#### Set Your Project ID

```bash
# Set your project using the auto-detected environment variable in Cloud Shell
gcloud config set project $GOOGLE_CLOUD_PROJECT

# Verify the project has been set
echo "Your active Google Cloud project is: $(gcloud config get-value project)"
```

> aside positive
> **Note**: If you see a different project than expected, you can set it manually: `gcloud config set project your-project-id-123`

#### Enable Required APIs

Your agents need access to several Google Cloud services:

```bash
gcloud services enable \
    aiplatform.googleapis.com \
    secretmanager.googleapis.com \
    cloudtrace.googleapis.com
```

This may take 1-2 minutes. You'll see:
```
Operation "operations/..." finished successfully.
```

**What these APIs provide:**
- **aiplatform.googleapis.com**: Access to Gemini models for agent reasoning
- **secretmanager.googleapis.com**: Secure storage for API keys (production best practice)
- **cloudtrace.googleapis.com**: Observability for our accountability trail

### Clone the Starter Code

Get the workshop repository with all template code and resources:

```bash
git clone https://github.com/ayoisio/adk-ap2-charity-agents
cd adk-ap2-charity-agents
git checkout codelab
```

Let's verify what we have:

```bash
ls -la
```

You should see:
- `charity_advisor/` - Where we'll build our agents and tools
- `scripts/` - Helper scripts for testing and verification
- `deploy.sh` - Helper script for deployment
- `setup.py` - Helper script for module installation
- `.env.template` - Environmental variables file

### Set Up Python Environment

Now we'll create an isolated Python environment for our project.

#### Create and Activate Virtual Environment

```bash
# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

✅ **Verification**: Your prompt should now show `(venv)` prefix.

#### Install Dependencies

```bash
pip install -r charity_advisor/requirements.txt
pip install -e .
```

This installs:
- **google-adk**: The Agent Development Kit framework
- **google-cloud-aiplatform**: Vertex AI and Gemini integration
- **ap2**: Agent Payments Protocol SDK (from GitHub)
- **python-dotenv**: Environment variable management

The `-e` flag allows you to import `adk_ap2_charity_agents` modules from anywhere.

#### Configure Environment File

Create your configuration from the template:

```bash
# Copy the template
cp .env.template .env

# Get your current Project ID
PROJECT_ID=$(gcloud config get-value project)

# Replace the placeholder with your actual project ID
sed -i "s/your-project-id/$PROJECT_ID/g" .env

# Verify the replacement worked
grep GOOGLE_CLOUD_PROJECT .env
```

You should see:
```
GOOGLE_CLOUD_PROJECT=your-actual-project-id
```

### Verification

Run the verification script to ensure everything is configured correctly:

```bash
python scripts/verify_setup.py
```

You should see all green checkmarks:

```text
======================================================================
SETUP VERIFICATION
======================================================================

✓ Python version: 3.11.x
✓ google-adk: 1.17.0
✓ google-cloud-aiplatform: 1.111.0+
✓ ap2: 0.1.0
✓ python-dotenv: 1.0.0+
✓ .env file found and contains project ID
✓ Google Cloud project configured: your-project-id

✓ Mock charity database found
✓ Agent templates ready
✓ All directories present

======================================================================
✓ Setup complete! You are ready to build trustworthy agents.
======================================================================
```

### Troubleshooting

> aside negative
> **Common Issues:**
> 
> **Package installation fails**: Check your network connection and retry `pip install -r charity_advisor/requirements.txt`
> 
> **Project ID issues**: Ensure you're in the right project with `gcloud config list`
> 
> **Python version error**: Cloud Shell should have Python 3.11+. Run `python3 --version` to check.

### What's Next?

Your environment is now fully prepared! You have:
- ✅ Google Cloud project configured
- ✅ Required APIs enabled
- ✅ ADK and AP2 libraries installed
- ✅ Template code ready to modify

In the next module, you'll build your first AI agent in a few lines of code and discover why simple agents aren't trustworthy when handling financial transactions.

## Your First Agent & Discovering the Trust Gap

**Duration: 10 min**

![banner](img/03-01-banner.png)

### From Idea to Interaction

In the previous module, we prepared our development environment. Now, the exciting work begins. We will build and run our first agent, give it its first capability, and in doing so, **discover the fundamental challenges we must solve to make it truly trustworthy**.

This module is your "before" picture - the moment that reveals why building trustworthy agents requires more than just giving an LLM access to tools.

---

### Step 1: Examine the Starter Agent

First, let's look at the template for our first agent. It contains a basic structure with placeholders that we will complete in the next steps.

👉 **Open the file `charity_advisor/simple_agent/agent.py` in your editor.**

You'll see:
```python
"""
A simple agent that can research charities using Google Search.
"""

# MODULE_3_STEP_2_IMPORT_COMPONENTS


simple_agent = Agent(
    name="SimpleAgent",
    model="gemini-2.5-flash",
    
    # MODULE_3_STEP_3_WRITE_INSTRUCTION
    instruction="""""",
    
    # MODULE_3_STEP_4_ADD_TOOLS
    tools=[]
)
```

Notice the placeholder comments follow a pattern: `MODULE_3_STEP_X_DESCRIPTION`. We will replace these markers in order to progressively build our agent.

> aside positive
> **What (ADK Concept): The `Agent` Class**
>
> This is the core building block of the ADK. An `Agent` is an autonomous entity whose reasoning is powered by a Large Language Model (LLM). Think of it as giving a brain (the LLM) a set of hands (tools) and a job description (instruction).
>
> In ADK terminology, `Agent` is actually a convenient alias for `LlmAgent`, the full class name. They're interchangeable, but `Agent` is more concise.

---

### Step 2: Import the Required Components

Before we can instantiate the `Agent` class or use the `google_search` tool, we need to import them into our file.

👉 **Find:**
```python
# MODULE_3_STEP_2_IMPORT_COMPONENTS
```

👉 **Replace that single line with:**
```python
from google.adk.agents import Agent
from google.adk.tools import google_search
```

Now the `Agent` class and `google_search` tool are available in our file.

> aside positive
> **What Are These Imports?**
>
> - **`Agent`**: The class that creates an LLM-powered agent. It's the "factory" for building autonomous entities.
> - **`google_search`**: A pre-built, Gemini-integrated tool that performs web searches.
>
> ADK provides several [built-in](https://google.github.io/adk-docs/tools/built-in-tools/) tools:
> - `google_search` - Web search capability
> - `code_execution` - Execute Python code
> - `google_maps` - Location and mapping queries
>
> You can also create custom tools with `FunctionTool` (which we'll do in Module 4).

---

### Step 3: Write the Agent Instruction

The instruction is the agent's "job description"—it tells the LLM when and how to use its tools. Let's write one that guides our agent to search for charity information.

👉 **Find:**
```python
# MODULE_3_STEP_3_WRITE_INSTRUCTION
instruction="""""",
```

👉 **Replace those two lines with:**
```python
instruction="""You are a helpful research assistant. When a user asks you to find information about charities,
use the google_search tool to find the most relevant and up-to-date results from the web.
Synthesize the search results into a helpful summary.""",
```

> aside positive
> **What (ADK Concept): The `instruction` Prompt**
>
> The `instruction` is the primary way we guide an `LlmAgent`'s behavior. It's like a job description or a set of operating procedures. A well-crafted instruction is critical for reliable tool use.
>
> Think of it as the difference between:
> - ❌ "Here's a hammer" (tool without guidance)
> - ✅ "Here's a hammer. Use it to drive nails when building furniture." (tool + instruction)
>
> The instruction should specify:
> - **Role**: "You are a helpful research assistant"
> - **Trigger**: "When a user asks you to find information about charities"
> - **Action**: "use the google_search tool"
> - **Output**: "Synthesize...into a helpful summary"

---

### Step 4: Add the Search Tool

An agent without tools is just a conversationalist. Let's give our agent its first capability: the ability to search the web.

👉 **Find:**
```python
# MODULE_3_STEP_4_ADD_TOOLS
tools=[]
```

👉 **Replace those two lines with:**
```python
tools=[google_search]
```

> aside positive
> **What (ADK Concept): The `tools` List**
>
> An agent's capabilities are defined by its `tools` list. By adding a tool to this list, you connect the agent's reasoning (the LLM) to a real-world action (the tool).
>
> When you add `google_search` to the tools list, the LLM can now:
> 1. **Decide when to use it**: "The user wants charity info → I should search"
> 2. **Determine parameters**: "I'll search for 'children's literacy charities'"
> 3. **Interpret results**: "The search found Room to Read and Teach For America"
> 4. **Synthesize output**: "Based on my search, here are some options..."
>
> The LLM orchestrates all of this automatically based on your instruction.

---

### Step 5: Verify Your Complete Agent

Let's confirm that all the pieces are in place before we test.

👉 **Your complete `charity_advisor/simple_agent/agent.py` file should now look exactly like this:**
```python
"""
A simple agent that can research charities using Google Search.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search


simple_agent = Agent(
    name="SimpleAgent",
    model="gemini-2.5-flash",
    instruction="""You are a helpful research assistant. When a user asks you to find information about charities,
use the google_search tool to find the most relevant and up-to-date results from the web.
Synthesize the search results into a helpful summary.""",
    tools=[google_search]
)
```

> aside positive
> **A Note on Gemini and Built-in Tools**
>
> The `google_search` tool is a special, highly-integrated feature of Gemini models. When the agent decides to use this tool, the model can perform the web search as part of its own reasoning process, leading to highly relevant and grounded results.
>
> This is different from calling an external API—the search is deeply integrated into Gemini's generation process, similar to how [Google Search Grounding](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview) works.
>
> This tight integration is why `google_search` is so powerful out of the box.

---

### Step 6: Test the Agent - Exposing the Trust Gaps

Now that our agent is fully configured, let's test it and analyze its behavior. This is where we discover why simple agents aren't trustworthy when handling financial decisions.

#### Test 1: The Discovery Problem

👉 **In your Cloud Shell terminal, run the following command:**
```bash
adk run charity_advisor/simple_agent
```

You should see output like:
```
INFO:google.adk.agents:Loading agent from charity_advisor/simple_agent
INFO:google.adk.agents:Agent 'SimpleAgent' ready

[user]:
```

The `[user]:` prompt is now waiting for your input.

👉 **At the [user]: prompt, type:**
```text
Can you find me a verified, highly-rated charity for children's literacy?
```

👉 **Press Enter and observe the response.**

After a moment, the agent will synthesize the search results into a response like this:

> Based on a web search, some well-regarded charities for children's literacy appear to be **Reading Is Fundamental** and **Room to Read**. Sources like Charity Navigator and GuideStar are often recommended for verifying their status and ratings. I also found several online discussions, including on forums like Reddit, where users share personal experiences with various smaller, local literacy programs.

**Let's analyze this. Has the agent solved our problem?**

❌ **No.** It has perfectly replicated the human experience we described in Module 1. It has successfully automated the process of "Googling it" and handed the "analysis paralysis" problem right back to us.

**This exposes the first trust gap: a lack of authoritative data.**

The agent is searching the open web, which means:
- ✅ It found results quickly (improved user experience)
- ❌ It's mixing highly-rated organizations with Reddit discussions (unreliable sources)
- ❌ It cannot distinguish between vetted charities and potential scams (no verification)
- ❌ It's asking *us* to verify the information it just provided (passing the burden back)

> aside negative
> **Trust Gap #1: Unvetted Discovery**
>
> The agent provides web results, not authoritative answers. It doesn't have access to a curated, trusted database of verified charities. It's simply a faster way to Google, not a solution to the trust problem.
>
> **What's missing:**
> - Access to verified charity databases (e.g., IRS 501(c)(3) records)
> - Pre-vetted efficiency ratings (e.g., Charity Navigator API)
> - Fraud prevention checks
> - Consistent data quality
>
> In Module 4, we'll solve this by building a custom tool that queries a trusted database.

---

#### Test 2: The Execution Problem

Now for the crucial second test. At the `[user]:` prompt, try to complete the donation:
```text
Okay, please donate $50 to Room to Read for me.
```

The agent will respond with an apology, admitting its limitation:

> I understand you'd like to donate, which is wonderful! However, I am a research assistant and **do not have the capability to handle financial transactions or process payments.** To make a donation, you would need to visit the official Room to Read website directly.

This is the second, equally important "Aha!" moment.

**Not only can the agent not be trusted to find the right charity, it cannot yet be trusted to perform the action of donating.**

> aside negative
> **Trust Gap #2: No Secure Execution**
>
> The agent has no tools for handling financial transactions. Even if we trusted its charity recommendations, we'd still need to:
> - Leave the conversation
> - Navigate to a website manually
> - Enter payment information ourselves
> - Hope the website is legitimate
>
> The agent cannot help with the execution step at all. There's no secure payment capability, no user consent mechanism, and no audit trail.
>
> In Modules 5-7, we'll solve this by building specialized agents with payment tools and consent mechanisms.

👉 **Press `Ctrl+C` to exit when finished testing.**

---

### The Two Gaps Visualized

![trust problem](img/03-02-trust-problem-visual.svg)

---

### What You Just Learned

In this module, you successfully built and equipped your first AI agent. In doing so, you have uncovered the two fundamental challenges of building a trustworthy system.

### Key Concepts Mastered

✅ **The Agent Class:**
- Core building block of ADK
- Combines LLM reasoning (brain) with tools (hands)
- Configured with model, instruction, and tools

✅ **Folder-Based Structure:**
- Each agent lives in its own folder
- ADK looks for `agent_folder/agent.py`
- Run with `adk run agent_folder`

✅ **The Tools List:**
- Defines agent capabilities
- LLM decides when and how to use tools
- Can contain multiple tools for different actions

✅ **The Instruction Prompt:**
- Guides agent behavior like a job description
- Specifies role, triggers, actions, and output format
- Critical for reliable tool use

✅ **The Trust Problem:**
- **Discovery gap**: Unvetted sources, mixed quality
- **Execution gap**: No secure capabilities, no consent, no audit trail

---

### What's Next

In the next module, we will begin to build the solution by implementing **AP2's role-based architecture**.

**Let's build the first agent and see role separation in action.**

## Building the Shopping Agent - Role-Based Discovery

**Duration: 15 min**

![banner](img/04-01-banner.png)

### The Foundation of Trust: Role Separation

In the last module, you discovered that a simple, general-purpose agent fails on two fronts: it can't provide trustworthy discovery, and it can't execute secure transactions. Now we'll begin solving these problems by implementing the first principle from the Agent Payments Protocol: **role-based architecture**.

Before we write any code, let's understand why this principle matters.

---

### AP2 Principle: Role Separation

#### The Problem with "Do Everything" Agents

Imagine you hire one person to be your financial advisor, accountant, and investment broker. Convenient? Yes. Secure? Absolutely not. They would have:
- Your investment goals (advisor role)
- Access to your accounts (accountant role)  
- Authority to move your money (broker role)

If this person is compromised—or makes a mistake—everything is at risk.

#### AP2's Solution: One Agent, One Job

AP2 applies the principle of separation of concerns to create **trust boundaries**:

![architecture](img/04-02-architecture.svg)

**Why this matters:**
- ✅ **Limited blast radius**: If the Shopping Agent is compromised, the attacker can't access payment credentials
- ✅ **Privacy**: The Credentials Provider never sees your shopping conversation
- ✅ **Compliance**: Easier to meet PCI-DSS requirements when payment data is isolated
- ✅ **Accountability**: Clear responsibility for each step

> aside positive
> **AP2 in Production**
>
> In a full AP2 implementation, there are actually 5 roles:
> - Shopping Agent (discovery)
> - Merchant Endpoint (product catalog)
> - Merchant Payment Processor (transaction construction)
> - Credentials Provider (payment execution)
> - Network/Issuer (authorization & settlement)
>
> For this workshop, we're building 3 agents to demonstrate the core principle. In production, you'd implement all 5 with even stricter boundaries.

#### How Agents Communicate: State as the Shared Notepad

Since agents can't directly access each other's data, they communicate through **shared state**. Think of it as a whiteboard that all agents can write to and read from:
```python
# Shopping Agent writes:
state["intent_mandate"] = {
    "natural_language_description": "Donate $50 to Room to Read",
    "merchants": ["Room to Read"],
    "intent_expiry": "2024-11-07T15:32:16Z",
    "amount": 50.0
}

# Merchant Agent reads:
intent = state["intent_mandate"]
charity_name = intent["merchants"][0]
amount = intent["amount"]
# Creates CartMandate based on IntentMandate...

# Credentials Provider reads:
cart_mandate = state["cart_mandate"]
# Processes payment...
```

This is how we maintain trust boundaries while enabling collaboration.

### Our First Agent: The Shopping Agent

The Shopping Agent's responsibility is simple and focused:
1. Use the `find_charities` tool to query our trusted database
2. Present options to the user
3. Use the `save_user_choice` tool to create an **IntentMandate** and save it to state
4. Hand off to the next agent (the Merchant)

That's it. No payment handling, no cart creation—just discovery and handoff.

Let's build it step by step.

---

### Step 1: Add Input Validation Helper

When building production tools, input validation is critical. Let's create a helper function that validates charity data before saving it to state.

👉 **Open `charity_advisor/tools/charity_tools.py`**

You'll see the `find_charities` function (already complete) at the top. Scroll down to find:
```python
# MODULE_4_STEP_1_ADD_VALIDATION_HELPER
```

👉 **Replace that single line with:**
```python
def _validate_charity_data(charity_name: str, charity_ein: str, amount: float) -> tuple[bool, str]:
    """
    Validates charity selection data before saving to state.
    
    This helper function performs basic validation to ensure data quality
    before it gets passed to other agents in the pipeline.
    
    Args:
        charity_name: Name of the selected charity
        charity_ein: Employer Identification Number (should be format: XX-XXXXXXX)
        amount: Donation amount in USD
        
    Returns:
        (is_valid, error_message): Tuple where is_valid is True if all checks pass,
                                    and error_message contains details if validation fails
    """
    # Validate charity name
    if not charity_name or not charity_name.strip():
        return False, "Charity name cannot be empty"
    
    # Validate EIN format (should be XX-XXXXXXX)
    if not charity_ein or len(charity_ein) != 10 or charity_ein[2] != '-':
        return False, f"Invalid EIN format: {charity_ein}. Expected format: XX-XXXXXXX"
    
    # Validate amount
    if amount <= 0:
        return False, f"Donation amount must be positive, got: ${amount}"
    
    if amount > 1_000_000:
        return False, f"Donation amount exceeds maximum of $1,000,000: ${amount}"
    
    # All checks passed
    return True, ""
```

> aside positive
> **Why a Helper Function?**
>
> The `_validate_charity_data` helper is:
> - **Synchronous** (no `async`) - validation doesn't need async
> - **Testable** - you can unit test it separately from the full tool
> - **Reusable** - other tools could use the same validation
> - **Educational** - demonstrates defensive programming patterns
>
> The underscore prefix `_validate_charity_data` is a Python convention indicating this is a "private" helper function not meant to be called directly by external code.

---

### Step 2: Add IntentMandate Creation Helper

Now let's create the helper that builds the AP2 IntentMandate structure. This is one of the three verifiable credentials in AP2.

👉 **In the same file, find:**
```python
# MODULE_4_STEP_2_ADD_INTENTMANDATE_CREATION_HELPER
```

👉 **Replace that single line with:**
```python
def _create_intent_mandate(charity_name: str, charity_ein: str, amount: float) -> dict:
    """
    Creates an IntentMandate - AP2's verifiable credential for user intent.
    
    This function uses the official Pydantic model from the `ap2` package
    to create a validated IntentMandate object before converting it to a dictionary.
    
    Args:
        charity_name: Name of the selected charity
        charity_ein: Employer Identification Number
        amount: Donation amount in USD
        
    Returns:
        Dictionary containing the IntentMandate structure per AP2 specification
    """
    from datetime import datetime, timedelta, timezone
    from ap2.types.mandate import IntentMandate
    
    # Set the expiry for the intent
    expiry = datetime.now(timezone.utc) + timedelta(hours=1)
    
    # Step 1: Instantiate the Pydantic model with official AP2 fields
    intent_mandate_model = IntentMandate(
        user_cart_confirmation_required=True,
        natural_language_description=f"Donate ${amount:.2f} to {charity_name}",
        merchants=[charity_name],
        skus=None,
        requires_refundability=False,
        intent_expiry=expiry.isoformat()
    )
    
    # Step 2: Convert the validated model to a dictionary for state storage
    intent_mandate_dict = intent_mandate_model.model_dump()
    
    # Step 3: Add the codelab's custom fields to the dictionary
    timestamp = datetime.now(timezone.utc)
    intent_mandate_dict.update({
        "timestamp": timestamp.isoformat(),
        "intent_id": f"intent_{charity_ein.replace('-', '')}_{int(timestamp.timestamp())}",
        "charity_ein": charity_ein,
        "amount": amount,
        "currency": "USD"
    })
    
    return intent_mandate_dict
```

> aside positive
> **What (AP2 Concept): IntentMandate**
>
> An **IntentMandate** is AP2's first verifiable credential. It captures user intent in a structured way that:
> - Can be verified by all parties
> - Has an expiry time (security feature)
> - Specifies constraints (which merchants, refund requirements)
> - Includes natural language description (human-readable)
>
> Think of it as a "digital intent form" that says:
> - "I want to donate $50 to Room to Read"
> - "This intent expires in 1 hour"
> - "I want to confirm the cart before payment"
> - "Room to Read is the only merchant who can fulfill this"

> aside positive
> **Why We Use AP2 Pydantic Models**
>
> Notice how we use `IntentMandate` from the `ap2` package. This provides:
> - **Automatic validation** against the protocol specification
> - **Type safety** that catches errors before runtime
> - **Production readiness** - same models work with real payment processors
>
> We create the model, validate it automatically via Pydantic, then convert to a dictionary for state storage. In production, these same models integrate directly with AP2-compliant payment systems.

> aside positive
> **Understanding IntentMandate Fields**
>
> Let's break down each field:
>
> **user_cart_confirmation_required** (bool):
> - `True`: User must approve the cart before payment
> - `False`: Agent can proceed directly to payment
> - For financial transactions, this should almost always be `True`
>
> **natural_language_description** (str):
> - Human-readable description of what user wants
> - Example: "Donate $50.00 to Room to Read"
> - Used for display, logging, dispute resolution
>
> **merchants** (list[str]):
> - Which merchant(s) can fulfill this intent
> - Example: `["Room to Read"]`
> - Prevents other merchants from creating offers
>
> **skus** (list[str] or None):
> - Specific product SKUs if applicable
> - Example: `["BOOK-123", "BOOK-456"]` for e-commerce
> - `None` for our donation use case
>
> **requires_refundability** (bool):
> - Whether the transaction must be refundable
> - `True` for purchases, typically `False` for donations
>
> **intent_expiry** (ISO 8601 timestamp):
> - When this intent becomes invalid
> - Example: "2024-11-07T15:32:16Z"
> - Security feature: stale intents can't be replayed

> aside positive
> **Workshop vs Production: Custom Fields**
>
> Notice we add custom fields after model creation:
> ```python
> intent_mandate_dict.update({
>     "charity_ein": charity_ein,
>     "amount": amount,
>     "currency": "USD"
> })
> ```
>
> **In production**, you would either:
> - Use AP2's extension mechanism for domain-specific fields
> - Store these in separate metadata
> - Extend the AP2 models via inheritance
>
> For this workshop, we add them to the dictionary to keep the flow simple while demonstrating the core AP2 patterns.

---

### Step 3: Build the State Handoff Tool with IntentMandate

Now let's build the tool that creates the IntentMandate and saves it to state.

👉 **In the same file, scroll down to the `save_user_choice` function. Find:**
```python
# MODULE_4_STEP_3_COMPLETE_SAVE_TOOL
```

👉 **Replace that single line with:**
```python
    # Validate inputs before creating IntentMandate
    is_valid, error_message = _validate_charity_data(charity_name, charity_ein, amount)
    if not is_valid:
        logger.error(f"Validation failed: {error_message}")
        return {"status": "error", "message": error_message}
    
    # Create AP2 IntentMandate using our updated helper function
    intent_mandate = _create_intent_mandate(charity_name, charity_ein, amount)
    
    # Write the IntentMandate to shared state for the next agent
    tool_context.state["intent_mandate"] = intent_mandate
    
    logger.info(f"Successfully created IntentMandate and saved to state")
    logger.info(f"Intent ID: {intent_mandate['intent_id']}")
    logger.info(f"Intent expires: {intent_mandate['intent_expiry']}")
    
    # Return success confirmation
    return {
        "status": "success",
        "message": f"Created IntentMandate: ${amount:.2f} donation to {charity_name} (EIN: {charity_ein})",
        "intent_id": intent_mandate["intent_id"],
        "expiry": intent_mandate["intent_expiry"]
    }
```

> aside positive
> **What (ADK Concept): tool_context**
>
> The `tool_context` parameter is automatically provided by ADK to every tool. It contains:
> - `tool_context.state`: The shared state dictionary
> - `tool_context.agent_name`: Reference to the agent calling the tool
>
> We use `tool_context.state` to write data that other agents can read, creating a secure handoff mechanism.

> aside positive
> **Return Value vs State: What's the Difference?**
>
> - **State** (`tool_context.state`): Data that persists for other agents to read later
> - **Return value**: What the LLM sees immediately to continue the conversation
>
> Think of the return value as "speaking out loud" and state as "writing on a shared whiteboard" that all agents can see.
>
> The LLM will see our return message and can tell the user: "Great! I've created your donation intent (ID: intent_xyz) which expires at 3:32 PM. I'm now passing your request to our secure payment processor."

---

### Step 4: Add Display Formatting Helper

Before we build the agent, let's add one more helper that formats charity data for user-friendly display.

👉 **Scroll to find:**
```python
# MODULE_4_STEP_4_ADD_FORMATTING_HELPER
```

👉 **Replace that single line with:**
```python
def _format_charity_display(charity: dict) -> str:
    """
    Formats a charity dictionary into a user-friendly display string.
    
    This helper function demonstrates how to transform structured data
    into readable text for the user.
    
    Args:
        charity: Dictionary containing charity data (name, ein, mission, rating, efficiency)
        
    Returns:
        Formatted string suitable for display to the user
    """
    name = charity.get('name', 'Unknown')
    ein = charity.get('ein', 'N/A')
    mission = charity.get('mission', 'No mission statement available')
    rating = charity.get('rating', 0.0)
    efficiency = charity.get('efficiency', 0.0)
    
    # Format efficiency as percentage
    efficiency_pct = int(efficiency * 100)
    
    # Build formatted string
    display = f"""
**{name}** (EIN: {ein})
⭐ Rating: {rating}/5.0
💰 Efficiency: {efficiency_pct}% of funds go to programs
📋 Mission: {mission}
    """.strip()
    
    return display
```

> aside positive
> **Why Add a Formatting Helper?**
>
> You might wonder: "Can't the LLM format the output itself?"
>
> [Yes](https://google.github.io/adk-docs/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key), but:
> - ✅ **Consistency**: Helper ensures uniform formatting across all responses
> - ✅ **Testability**: You can verify the format programmatically
>
> In production systems, separating data transformation from LLM reasoning is a good practice.

---

### Step 5: Build the Shopping Agent - Import Components

Now that our tools are complete and robust, let's create the agent that will use them.

👉 **Open `charity_advisor/shopping_agent/agent.py`**

You'll see a template with placeholder comments. Let's build it step by step.

👉 **Find:**
```python
# MODULE_4_STEP_5_IMPORT_COMPONENTS
```

👉 **Replace that single line with:**
```python
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.charity_tools import find_charities, save_user_choice
```

> aside positive
> **What (ADK Concept): FunctionTool**
>
> `FunctionTool` is an ADK wrapper that converts a Python function into a tool that an LLM can call. It:
> - Automatically generates a tool description from the function's docstring
> - Extracts parameter names and types from the function signature
> - Handles the tool invocation when the LLM decides to use it
> - Validates parameters before calling the function
>
> This is why good docstrings and type hints are critical—they directly affect how well the LLM understands your tool.
>
> **Example**: Given this function signature:
> ```python
> async def save_user_choice(
>     charity_name: str,
>     charity_ein: str,
>     amount: float,
>     tool_context: Any
> ) -> Dict[str, Any]:
>     """Saves the user's final charity choice..."""
> ```
>
> FunctionTool automatically tells the LLM:
> - Tool name: "save_user_choice"
> - Parameters: charity_name (string), charity_ein (string), amount (number)
> - Purpose: "Saves the user's final charity choice..." (from docstring)

---

### Step 6: Write the Agent Instruction

The instruction is where we define the agent's job description and workflow. This is critical—a poorly written instruction leads to unreliable behavior.

👉 **Find:**
```python
# MODULE_4_STEP_6_WRITE_INSTRUCTION
instruction="""""",
```

👉 **Replace those two lines with:**
```python
    instruction="""You are a research specialist helping users find verified charities.

Your workflow:

1. When the user describes what cause they want to support (e.g., "education", "health", "environment"),
   use the find_charities tool to search our vetted database.

2. Present the results clearly. The tool returns formatted charity information that you should
   show to the user.

3. When the user selects a charity and specifies an amount, use the save_user_choice tool
   to create an IntentMandate and record their decision. You MUST call save_user_choice with:
   - charity_name: The exact name of the chosen charity
   - charity_ein: The EIN of the chosen charity  
   - amount: The donation amount in dollars (as a number, not a string)

4. After successfully saving, inform the user:
   - That you've created an IntentMandate (mention the intent ID if provided)
   - When the intent expires
   - That you're passing their request to the secure payment processor

IMPORTANT BOUNDARIES:
- Your ONLY job is discovery and creating the IntentMandate
- You do NOT process payments
- You do NOT see the user's payment methods
- You do NOT create cart offers (that's the Merchant Agent's job)
- After calling save_user_choice, your work is done

WHAT IS AN INTENTMANDATE:
An IntentMandate is a structured record of what the user wants to do. It includes:
- Natural language description ("Donate $50 to Room to Read")
- Which merchants can fulfill it
- When the intent expires
- Whether user confirmation is required

This is the first of three verifiable credentials in our secure payment system.

If the user asks you to do anything related to payment processing, politely explain that
you don't have that capability and that their request will be handled by the appropriate
specialist agent.""",
```

> aside positive
> **Why Such Detailed Instructions?**
>
> LLMs are powerful but require clear guidance. Notice how the instruction:
> - **Numbers the workflow steps** → Reduces ambiguity about order
> - **Specifies exact parameters** → Prevents the LLM from guessing parameter names or types
> - **Sets boundaries** ("Your ONLY job...") → Prevents scope creep
> - **Explains what NOT to do** → Critical for security (can't process payments)
> - **Defines technical terms** → Helps LLM explain IntentMandate to users
> - **Handles edge cases** → What to say if user asks to process payment
>
> This level of detail is the difference between a reliable production agent and an unreliable demo.
>
> Compare this to Module 3's simple agent instruction:
> ```python
> # Module 3 (too vague):
> instruction="You are a helpful research assistant..."
> 
> # Module 4 (production-ready):
> instruction="""You are a research specialist...
> Your workflow:
> 1. When the user...
> 2. Present...
> 3. When the user selects...
> IMPORTANT BOUNDARIES:...
> WHAT IS AN INTENTMANDATE:...
> ```

---

### Step 7: Add Tools to the Agent

Now let's give the agent access to both tools.

👉 **Find:**
```python
# MODULE_4_STEP_7_ADD_TOOLS
```

👉 **Replace those two lines with:**
```python
    tools=[
        FunctionTool(func=find_charities),
        FunctionTool(func=save_user_choice)
    ]
```

> aside positive
> **Why Two Separate Tools?**
>
> We could have created one tool called `find_and_save_charity`, but separating them gives the LLM flexibility:
> - User asks "What education charities do you have?" → Use `find_charities` only
> - User says "Actually, let me see health charities instead" → Use `find_charities` again
> - User says "I'll donate $50 to Room to Read" → Use `save_user_choice`
>
> The LLM orchestrates the workflow, calling tools as needed. This is more powerful than a rigid, single-purpose tool.
>
> This principle is called **tool composability**—small, focused tools that can be combined flexibly are better than large, monolithic ones.

---

### Step 8: Verify Your Complete Agent

Let's check that everything is wired up correctly.

👉 **Your complete `charity_advisor/shopping_agent/agent.py` should now look like this:**
```python
"""
Shopping Agent - Finds charities from a trusted database and saves the user's choice.
This agent acts as our specialized "Research Analyst."
"""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.charity_tools import find_charities, save_user_choice


shopping_agent = Agent(
    name="ShoppingAgent",
    model="gemini-2.5-pro",
    description="Finds and recommends vetted charities from a trusted database, then creates an IntentMandate capturing the user's donation intent.",
    instruction="""You are a research specialist helping users find verified charities.

Your workflow:

1. When the user describes what cause they want to support (e.g., "education", "health", "environment"),
   use the find_charities tool to search our vetted database.

2. Present the results clearly. The tool returns formatted charity information that you should
   show to the user.

3. When the user selects a charity and specifies an amount, use the save_user_choice tool
   to create an IntentMandate and record their decision. You MUST call save_user_choice with:
   - charity_name: The exact name of the chosen charity
   - charity_ein: The EIN of the chosen charity  
   - amount: The donation amount in dollars (as a number, not a string)

4. After successfully saving, inform the user:
   - That you've created an IntentMandate (mention the intent ID if provided)
   - When the intent expires
   - That you're passing their request to the secure payment processor

IMPORTANT BOUNDARIES:
- Your ONLY job is discovery and creating the IntentMandate
- You do NOT process payments
- You do NOT see the user's payment methods
- You do NOT create cart offers (that's the Merchant Agent's job)
- After calling save_user_choice, your work is done

WHAT IS AN INTENTMANDATE:
An IntentMandate is a structured record of what the user wants to do. It includes:
- Natural language description ("Donate $50 to Room to Read")
- Which merchants can fulfill it
- When the intent expires
- Whether user confirmation is required

This is the first of three verifiable credentials in our secure payment system.

If the user asks you to do anything related to payment processing, politely explain that
you don't have that capability and that their request will be handled by the appropriate
specialist agent.""",
    tools=[
        FunctionTool(func=find_charities),
        FunctionTool(func=save_user_choice)
    ]
)
```

✅ **Perfect!** You've built a production-quality, AP2-compliant agent with:
- Input validation
- Proper IntentMandate creation using AP2 Pydantic models
- Formatted output
- Clear role boundaries
- Detailed instructions
- Error handling

---

### Step 9: Test the Shopping Agent

Let's verify that our agent works correctly, creates proper IntentMandates, and respects its boundaries.

👉 **In your Cloud Shell terminal, run:**
```bash
adk run charity_advisor/shopping_agent
```

The `[user]:` prompt will appear.

#### Test 1: Discovery with Trusted Database

👉 **Type:**
```text
I want to donate to an education charity. What are my options?
```

After a moment, the agent will provide a response. Thanks to our `_format_charity_display` helper, the results are beautifully formatted:

> I found 3 verified education charities in our database:
>
> **Room to Read** (EIN: 77-0479905)  
> ⭐ Rating: 4.9/5.0  
> 💰 Efficiency: 88% of funds go to programs  
> 📋 Mission: Transforms the lives of millions of children in low-income communities by focusing on literacy and gender equality in education.
>
> **Teach For America** (EIN: 13-3541913)  
> ⭐ Rating: 4.7/5.0  
> 💰 Efficiency: 81% of funds go to programs  
> 📋 Mission: Works to expand educational opportunity for children facing adversity.
>
> **Tech Education Alliance** (EIN: 45-2345678)  
> ⭐ Rating: 4.8/5.0  
> 💰 Efficiency: 92% of funds go to programs  
> 📋 Mission: Brings computer science education to underserved schools.
>
> Which charity would you like to support, and how much would you like to donate?

**Compare this to Module 3's simple agent**, which gave you unvetted Google results. This is the difference between untrusted and trusted discovery.

---

#### Test 2: Record User Choice and Create IntentMandate

👉 **Type:**
```text
I'll donate $50 to Room to Read.
```

You should see the agent call the `save_user_choice` tool with the correct parameters. Thanks to our IntentMandate creation using AP2 models, you'll see a more structured response:

> Perfect! I've created an IntentMandate for your donation:
>
> **Intent Details:**
> - Intent ID: intent_774795905_1730927536
> - Amount: $50.00 to Room to Read (EIN: 77-0479905)
> - Expires: 2024-11-07T15:32:16Z (in 1 hour)
>
> This IntentMandate captures your donation intent and includes constraints to ensure the transaction is processed securely. I'm now passing this to our secure payment processor to create a formal offer and complete your donation.

**Behind the scenes**, several things just happened:
1. `_validate_charity_data()` verified the inputs
2. `_create_intent_mandate()` used the AP2 Pydantic model to build the structure:
```python
   # Created and validated via Pydantic
   intent_mandate_model = IntentMandate(
       user_cart_confirmation_required=True,
       natural_language_description="Donate $50.00 to Room to Read",
       merchants=["Room to Read"],
       skus=None,
       requires_refundability=False,
       intent_expiry="2024-11-07T15:32:16Z"
   )
   
   # Converted to dict and extended with custom fields
   intent_mandate_dict = intent_mandate_model.model_dump()
   intent_mandate_dict.update({
       "charity_ein": "77-0479905",
       "amount": 50.0,
       "currency": "USD"
   })
```
3. The tool wrote ONLY the IntentMandate to shared state:
```python
   state["intent_mandate"] = intent_mandate_dict
```
4. A success message with intent details was returned to the LLM
5. The LLM composed the final user message

This IntentMandate is now ready for the Merchant Agent (Module 5) to pick up. The Merchant will extract the charity name and amount from the IntentMandate and validate that it hasn't expired.

---

#### Test 3: Validation in Action

Let's verify our validation helper catches bad input.

👉 **Type:**
```text
I'll donate -$25 to Room to Read.
```

The agent should catch the invalid amount:

> I encountered an issue: Donation amount must be positive, got: $-25.0
>
> Please specify a positive donation amount and I'll create the IntentMandate for you.

**This is defensive programming in action.** Our `_validate_charity_data` helper prevented invalid data from entering the system and creating a malformed IntentMandate.

---

#### Test 4: Verify Trust Boundary

👉 **Try asking the agent to process payment:**
```text
Now process my credit card payment.
```

The agent should refuse, respecting its role boundary:

> I don't have the capability to process payments—that's not part of my role. My job is to help you find verified charities and create the IntentMandate that captures your donation intent.
>
> Your IntentMandate has already been created and passed to our secure payment processor. The Merchant Agent will create a formal offer (CartMandate), and then the Credentials Provider will handle the actual payment with your explicit consent.

**This is the trust boundary in action.** The agent knows it's not authorized to handle payment data, and its instruction explicitly guides it to explain this to users while also teaching them about the IntentMandate concept.

👉 **Press `Ctrl+C` to exit when finished testing.**

---

### What You Just Built

You've successfully implemented the first piece of AP2's architecture with proper IntentMandate creation using AP2 Pydantic models.

### Key Concepts Mastered

✅ **Role-Based Architecture:**
- Each agent has one clearly defined job
- Agents communicate through shared state, not direct access
- Trust boundaries limit the impact of compromise

✅ **IntentMandate (AP2 Credential #1):**
- Created using official AP2 Pydantic models for validation
- Structured capture of user intent
- Includes expiry for security (prevents replay attacks)
- Specifies constraints (merchants, refundability, confirmation)
- Natural language description for humans
- Machine-readable for agents
- Model validated before conversion to dictionary

✅ **State as Shared Memory:**
- `tool_context.state` is the "notepad" all agents can access
- Writing to state = making verifiable credentials available
- Reading from state = consuming and validating credentials
- Downstream agents extract what they need from credentials

✅ **FunctionTool:**
- Converts Python functions into LLM-callable tools
- Relies on docstrings and type hints for LLM understanding
- Handles invocation automatically
- Tool composability: small focused tools > monolithic ones

✅ **Agent Instructions:**
- Step-by-step workflow guidance
- Explicit boundaries ("do NOT...")
- Parameter specifications to prevent errors
- Technical definitions (what is IntentMandate)
- Edge case handling (what to say when...)

---

### What's Next

In the next module, we'll build the **Merchant Agent** to receive the IntentMandate and create the second verifiable credential: **CartMandate**.

The Shopping Agent has created an IntentMandate capturing the user's intent with expiry. Now we need an agent to read that credential, validate it hasn't expired, and create a formal, signed offer that says: "I, the merchant, will honor this price and deliver these goods."

**Let's build the Merchant Agent and see the second AP2 credential in action.**

## Building the Merchant Agent - Binding Offers & CartMandate

**Duration: 15 min**

![banner](img/05-01-banner.png)

### From Discovery to Commitment

In the previous module, you built the Shopping Agent—a specialist that finds verified charities and creates an IntentMandate capturing the user's intent. Now we need an agent to receive that IntentMandate and create a formal, binding offer.

This is where AP2's second key principle comes into play: **verifiable credentials through CartMandate**.

---

### AP2 Principle: CartMandate & Binding Offers

#### Why We Need a Merchant Role

In Module 4, the Shopping Agent created an IntentMandate and saved it to state:
```python
state["intent_mandate"] = {
    "natural_language_description": "Donate $50 to Room to Read",
    "merchants": ["Room to Read"],
    "amount": 50.0,
    "intent_expiry": "2024-11-07T15:32:16Z"
}
```

But this is just user intent. Before any payment can be processed, we need:
- A formal offer structure that payment systems understand
- Proof that the merchant will honor this price
- A binding commitment that can't be altered mid-transaction
- Validation that the intent hasn't expired

**This is the Merchant Agent's job.**

#### What is a CartMandate?

A **CartMandate** is AP2's term for a "digital shopping cart" that serves as a binding offer. It's structured according to the W3C PaymentRequest standard, which means:
- Payment processors worldwide recognize the format
- It contains all transaction details in a standardized way
- It can be cryptographically signed to prove authenticity

Think of it like a written quote from a contractor:
- ❌ Verbal: "Yeah, I can do that job for about fifty bucks"
- ✅ Written quote: Itemized costs, total, signature, date

The written quote is binding. The CartMandate is the digital equivalent.

![intent to cart](img/05-02-intent-to-cart.svg)

#### The Structure of a CartMandate

A CartMandate in AP2 has a specific nested structure:
```python
cart_mandate = {
    "contents": {  # ← AP2 wrapper
        "id": "cart_xyz123",
        "cart_expiry": "2024-11-07T15:47:16Z",
        "merchant_name": "Room to Read",
        "user_cart_confirmation_required": False,
        
        "payment_request": {  # ← W3C PaymentRequest nested inside
            "method_data": [...],
            "details": {...},
            "options": {...}
        }
    },
    "merchant_authorization": "SIG_a3f7b2c8"  # ← Merchant signature
}
```

**Three main components:**

**1. contents** - The cart wrapper containing:
- Cart ID and expiry
- Merchant name
- The W3C PaymentRequest

**2. payment_request** (inside contents) - What's being purchased:
- method_data: Payment types accepted
- details: Items and total
- options: Shipping, payer info requirements

**3. merchant_authorization** - Cryptographic signature

> aside positive
> **AP2 CartMandate vs W3C PaymentRequest**
>
> AP2's CartMandate **wraps** a W3C [PaymentRequest](https://www.w3.org/TR/payment-request/):
> ```
> CartMandate {
>   contents: {              ← AP2 wrapper with expiry
>     payment_request: {     ← W3C structure here
>       method_data: [...]
>       details: {...}
>     }
>   }
>   merchant_authorization   ← AP2 signature
> }
> ```
> The wrapping provides:
> - Expiry timestamp (cart expires in 15 min)
> - Merchant signature
> - Binding commitment context
> - Link to IntentMandate

#### Merchant Signatures: Proof of Commitment

The merchant signature is critical. It proves:
- This offer came from an authorized merchant
- The merchant commits to honor this exact price
- The offer hasn't been tampered with since creation

In production, this would be a cryptographic signature using PKI (Public Key Infrastructure) or JWT (JSON Web Tokens). For our educational workshop, we'll simulate this with a SHA-256 hash.
```python
# Production (real signature):
signature = sign_with_private_key(cart_data, merchant_private_key)

# Workshop (simulated signature):
cart_hash = hashlib.sha256(cart_json.encode()).hexdigest()
signature = f"SIG_{cart_hash[:16]}"
```

---

### Our Mission: Build the Merchant Agent

The Merchant Agent will:
1. Read the IntentMandate from state (what Shopping Agent wrote)
2. Validate that the intent hasn't expired
3. Extract the charity name, amount, and other details
4. Create a W3C-compliant PaymentRequest structure using AP2 Pydantic models
5. Wrap it in AP2's CartMandate with expiry
6. Add a simulated merchant signature
7. Write the CartMandate to state for the Credentials Provider (next module)

Let's build it step by step.

---

### Step 1: Add Expiry Validation Helper

First, let's set up the merchant-related tools file and add a helper to validate IntentMandate expiry.

👉 **Open `charity_advisor/tools/merchant_tools.py`**

Let's add the expiry validation:

👉 **Find:**
```python
# MODULE_5_STEP_1_ADD_EXPIRY_VALIDATION_HELPER
```

👉 **Replace that single line with:**
```python
def _validate_intent_expiry(intent_expiry_str: str) -> tuple[bool, str]:
    """
    Validates that the IntentMandate hasn't expired.
    
    This is a critical security check - expired intents should not be processed.
    
    Args:
        intent_expiry_str: The ISO 8601 timestamp string from the IntentMandate.
        
    Returns:
        (is_valid, error_message): Tuple indicating if intent is still valid.
    """
    try:
        # The .replace('Z', '+00:00') is for compatibility with older Python versions
        expiry_time = datetime.fromisoformat(intent_expiry_str.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        
        if expiry_time < now:
            return False, f"IntentMandate expired at {intent_expiry_str}"
        
        time_remaining = expiry_time - now
        logger.info(f"IntentMandate valid. Expires in {time_remaining.total_seconds():.0f} seconds")
        
        return True, ""
        
    except (ValueError, TypeError) as e:
        return False, f"Invalid intent_expiry format: {e}"
```

> aside positive
> **Why Expiry Validation Matters**
>
> This is a critical security feature of AP2 credentials:
>
> **Without expiry validation:**
> ```python
> # User creates intent at 2:00 PM: "Donate $50"
> # Intent sits in state for 6 hours
> # At 8:00 PM, merchant creates cart from stale intent
> # User might not even remember or want this anymore!
> ```
>
> **With expiry validation:**
> ```python
> # User creates intent at 2:00 PM (expires 3:00 PM)
> # At 3:30 PM, merchant tries to create cart
> # Validation fails: "IntentMandate expired at 3:00 PM"
> # Transaction blocked ✓
> ```
>
> This prevents:
> - Processing stale user intents
> - Replay attacks
> - Forgotten transactions executing unexpectedly
>
> The Merchant Agent MUST validate expiry before creating a binding offer.

---

### Step 2: Add Signature Generation Helper

Now let's create a helper that generates the simulated merchant signature.

👉 **Find:**
```python
# MODULE_5_STEP_2_ADD_SIGNATURE_HELPER
```

👉 **Replace that single line with:**
```python
def _generate_merchant_signature(cart_contents: CartContents) -> str:
    """
    Generates a simulated merchant signature for the CartMandate contents.
    
    In production, this would use PKI or JWT with the merchant's private key.
    For this codelab, we use a SHA-256 hash of the sorted JSON representation.
    
    Args:
        cart_contents: The Pydantic model of the cart contents to sign.
        
    Returns:
        Simulated signature string (format: "SIG_" + first 16 chars of hash).
    """
    # Step 1: Dump the Pydantic model to a dictionary. The `mode='json'` argument
    # ensures that complex types like datetimes are serialized correctly.
    cart_contents_dict = cart_contents.model_dump(mode='json')
    
    # Step 2: Use the standard json library to create a stable, sorted JSON string.
    # separators=(',', ':') removes whitespace for a compact and canonical representation.
    cart_json = json.dumps(cart_contents_dict, sort_keys=True, separators=(',', ':'))
    
    # Step 3: Generate SHA-256 hash.
    cart_hash = hashlib.sha256(cart_json.encode('utf-8')).hexdigest()
    
    # Step 4: Create signature in a recognizable format.
    signature = f"SIG_{cart_hash[:16]}"
    
    logger.info(f"Generated merchant signature: {signature}")
    return signature
```

> aside positive
> **Why We Use the Pydantic Model for Signing**
>
> Notice how the signature helper now accepts a `CartContents` Pydantic model instead of a plain dictionary. This ensures:
> - **Type safety**: We can only sign validated cart structures
> - **Consistency**: The `model_dump(mode='json')` method guarantees canonical serialization
> - **Production readiness**: Real signing libraries work with typed models
>
> In production, you'd replace the SHA-256 hash with a real cryptographic signature using the merchant's private key.

---

### Step 3A: Create the Tool Signature and Setup

Now let's start building the main tool. We'll create it incrementally across four substeps. First, the function signature and initial setup.

👉 **Find:**
```python
# MODULE_5_STEP_3A_CREATE_TOOL_SIGNATURE
```

👉 **Replace that single line with:**
```python
async def create_cart_mandate(tool_context: Any) -> Dict[str, Any]:
    """
    Creates a W3C PaymentRequest-compliant CartMandate from the IntentMandate.
    
    This tool reads the IntentMandate from shared state, validates it, and
    creates a formal, signed offer using the official AP2 Pydantic models.
    
    Returns:
        Dictionary containing status and the created CartMandate.
    """
    logger.info("Tool called: Creating CartMandate from IntentMandate")
    
    # MODULE_5_STEP_3B_ADD_VALIDATION_LOGIC
```

---

### Step 3B: Add Validation Logic

Now let's add the logic to read and validate the IntentMandate using AP2 Pydantic models, and extract the data we need.

👉 **Find:**
```python
# MODULE_5_STEP_3B_ADD_VALIDATION_LOGIC
```

👉 **Replace that single line with:**
```python
    # 1. Read IntentMandate dictionary from state
    intent_mandate_dict = tool_context.state.get("intent_mandate")
    if not intent_mandate_dict:
        logger.error("No IntentMandate found in state")
        return {
            "status": "error",
            "message": "No IntentMandate found. Shopping Agent must create intent first."
        }
    
    # 2. Parse dictionary into a validated Pydantic model
    try:
        intent_mandate_model = IntentMandate.model_validate(intent_mandate_dict)
    except Exception as e:
        logger.error(f"Could not validate IntentMandate structure: {e}")
        return {"status": "error", "message": f"Invalid IntentMandate structure: {e}"}
    
    # 3. Validate that the intent hasn't expired (CRITICAL security check)
    is_valid, error_message = _validate_intent_expiry(intent_mandate_model.intent_expiry)
    if not is_valid:
        logger.error(f"IntentMandate validation failed: {error_message}")
        return {"status": "error", "message": error_message}
    
    # 4. Extract data. Safely access standard fields from the model, and
    # custom fields (like 'amount') from the original dictionary.
    charity_name = intent_mandate_model.merchants[0] if intent_mandate_model.merchants else "Unknown Charity"
    amount = intent_mandate_dict.get("amount", 0.0)
    
    # MODULE_5_STEP_3C_CREATE_CARTMANDATE_STRUCTURE
```

> aside positive
> **Defensive Programming with Pydantic Models**
>
> Notice the validation layers using AP2 models:
>
> **Layer 1: Check credential exists**
> ```python
> if not intent_mandate_dict:
>     return {"status": "error", "message": "No IntentMandate found"}
> ```
>
> **Layer 2: Validate structure with Pydantic**
> ```python
> intent_mandate_model = IntentMandate.model_validate(intent_mandate_dict)
> # Pydantic automatically validates all fields match the AP2 spec
> ```
>
> **Layer 3: Validate expiry**
> ```python
> is_valid, error_message = _validate_intent_expiry(intent_mandate_model.intent_expiry)
> if not is_valid:
>     return {"status": "error", "message": error_message}
> ```
>
> The Pydantic model validation catches structural errors automatically, then we add business logic validation on top. This is production-quality error handling.

---

### Step 3C: Create CartMandate Structure

Now let's build the W3C-compliant PaymentRequest structure and wrap it in the AP2 CartMandate using Pydantic models.

👉 **Find:**
```python
# MODULE_5_STEP_3C_CREATE_CARTMANDATE_STRUCTURE
```

👉 **Replace that single line with:**
```python
    # 5. Build the nested Pydantic models for the CartMandate
    timestamp = datetime.now(timezone.utc)
    cart_id = f"cart_{hashlib.sha256(f'{charity_name}{timestamp.isoformat()}'.encode()).hexdigest()[:12]}"
    cart_expiry = timestamp + timedelta(minutes=15)
    
    payment_request_model = PaymentRequest(
        method_data=[PaymentMethodData(
            supported_methods="CARD",
            data={"supported_networks": ["visa", "mastercard", "amex"], "supported_types": ["debit", "credit"]}
        )],
        details=PaymentDetailsInit(
            id=f"order_{cart_id}",
            display_items=[PaymentItem(
                label=f"Donation to {charity_name}",
                amount=PaymentCurrencyAmount(currency="USD", value=amount)  # Pydantic v2 handles float -> str conversion
            )],
            total=PaymentItem(
                label="Total Donation",
                amount=PaymentCurrencyAmount(currency="USD", value=amount)
            )
        ),
        options=PaymentOptions(request_shipping=False)
    )
    
    cart_contents_model = CartContents(
        id=cart_id,
        cart_expiry=cart_expiry.isoformat(),
        merchant_name=charity_name,
        user_cart_confirmation_required=False,
        payment_request=payment_request_model
    )
    
    # MODULE_5_STEP_3D_ADD_SIGNATURE_AND_SAVE
```

> aside positive
> **Building Nested AP2 Models**
>
> Notice how we build the CartMandate using official AP2 Pydantic models:
>
> **1. PaymentRequest (W3C standard):**
> ```python
> payment_request_model = PaymentRequest(
>     method_data=[...],
>     details=PaymentDetailsInit(...),
>     options=PaymentOptions(...)
> )
> ```
>
> **2. CartContents (AP2 wrapper):**
> ```python
> cart_contents_model = CartContents(
>     id=cart_id,
>     cart_expiry=cart_expiry.isoformat(),
>     merchant_name=charity_name,
>     payment_request=payment_request_model  # W3C nested inside AP2
> )
> ```
>
> **3. CartMandate (top-level):**
> ```python
> cart_mandate_model = CartMandate(
>     contents=cart_contents_model,
>     merchant_authorization=signature
> )
> ```
>
> This ensures full compliance with both AP2 and W3C standards through automatic validation.

> aside positive
> **Why Two Expiry Times?**
>
> You might notice we have:
> - `intent_expiry`: 1 hour (IntentMandate)
> - `cart_expiry`: 15 minutes (CartMandate)
>
> **Why shorter cart expiry?**
> - Intent = "I'm browsing" (1 hour is reasonable)
> - Cart = "I'm ready to buy" (15 min creates urgency)
> - Prevents abandoned carts sitting around
> - Forces timely payment or re-confirmation
>
> In production e-commerce:
> - Intent: 1-24 hours
> - Cart: 15-30 minutes
> - Checkout: 5-10 minutes
>
> Each stage gets tighter to encourage completion.

---

### Step 3D: Add Signature and Save to State

Finally, let's sign the CartMandate using our Pydantic model and save it to state for the next agent.

👉 **Find:**
```python
# MODULE_5_STEP_3D_ADD_SIGNATURE_AND_SAVE
```

👉 **Replace that single line with:**
```python
    # 6. Generate signature from the validated Pydantic model
    signature = _generate_merchant_signature(cart_contents_model)
    
    # 7. Create the final CartMandate model, now including the signature
    cart_mandate_model = CartMandate(
        contents=cart_contents_model,
        merchant_authorization=signature
    )
    
    # 8. Convert the final model to a dictionary for state storage and add the custom timestamp
    cart_mandate_dict = cart_mandate_model.model_dump(mode='json')
    cart_mandate_dict["timestamp"] = timestamp.isoformat()
    
    # 9. Write the final dictionary to state
    tool_context.state["cart_mandate"] = cart_mandate_dict
    
    logger.info(f"CartMandate created successfully: {cart_id}")
    
    return {
        "status": "success",
        "message": f"Created signed CartMandate {cart_id} for ${amount:.2f} donation to {charity_name}",
        "cart_id": cart_id,
        "cart_expiry": cart_expiry.isoformat(),
        "signature": signature
    }
```

> aside positive
> **The Complete Model-to-State Flow**
>
> See how we use Pydantic models throughout:
>
> **1. Validate input:**
> ```python
> intent_mandate_model = IntentMandate.model_validate(intent_mandate_dict)
> ```
>
> **2. Build output models:**
> ```python
> cart_contents_model = CartContents(...)
> cart_mandate_model = CartMandate(contents=cart_contents_model, ...)
> ```
>
> **3. Sign the validated model:**
> ```python
> signature = _generate_merchant_signature(cart_contents_model)
> ```
>
> **4. Convert to dict for state:**
> ```python
> cart_mandate_dict = cart_mandate_model.model_dump(mode='json')
> ```
>
> This pattern ensures type safety during construction, then serializes for storage. In production, the models would serialize directly to JSON for API calls.

---

### Step 4: Build the Merchant Agent - Import Components

Now let's create the agent that will use this tool.

👉 **Open `charity_advisor/merchant_agent/agent.py`**

You'll see a template with placeholder markers. Let's start by importing what we need.

👉 **Find:**
```python
# MODULE_5_STEP_4_IMPORT_COMPONENTS
```

👉 **Replace that single line with:**
```python
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.merchant_tools import create_cart_mandate
```

---

### Step 5: Write the Merchant Agent Instruction

Now let's write the instruction that tells the agent when and how to use its tool.

👉 **Find:**
```python
# MODULE_5_STEP_5_WRITE_INSTRUCTION
instruction="""""",
```

👉 **Replace those two lines with:**
```python
    instruction="""You are a merchant specialist responsible for creating formal, signed offers (CartMandates).

Your workflow:

1. Read the IntentMandate from shared state.
   The IntentMandate was created by the Shopping Agent and contains:
   - merchants: List of merchant names
   - amount: Donation amount
   - charity_ein: Tax ID
   - intent_expiry: When the intent expires

2. Use the create_cart_mandate tool to create a W3C PaymentRequest-compliant CartMandate.
   This tool will:
   - Validate the IntentMandate hasn't expired (CRITICAL security check)
   - Extract the charity name and amount from the IntentMandate
   - Create a structured offer with payment methods, transaction details, and merchant info
   - Generate a merchant signature to prove authenticity
   - Save the CartMandate to state for the payment processor

3. After creating the CartMandate, inform the user:
   - That you've created a formal, signed offer
   - The cart ID
   - When the cart expires (15 minutes)
   - That you're passing it to the secure payment processor

IMPORTANT BOUNDARIES:
- Your ONLY job is creating signed CartMandates from valid IntentMandates
- You do NOT process payments
- You do NOT see the user's payment methods or credentials
- You do NOT interact with payment networks
- You MUST validate that the IntentMandate hasn't expired before creating a cart
- After calling create_cart_mandate, your work is done

WHAT IS A CARTMANDATE:
A CartMandate is a binding commitment that says:
"I, the merchant, commit to accepting $X for this charity donation, and I prove it with my signature."

This commitment is structured using the W3C PaymentRequest standard and includes:
- Payment methods accepted (card, bank transfer)
- Transaction details (amount, charity name)
- Cart expiry (15 minutes from creation)
- Merchant signature (proof of commitment)

This is the second of three verifiable credentials in our secure payment system.""",
```

---

### Step 6: Add Tools to the Merchant Agent

👉 **Find:**
```python
# MODULE_5_STEP_6_ADD_TOOLS
tools=[],
```

👉 **Replace those two lines with:**
```python
    tools=[
        FunctionTool(func=create_cart_mandate)
    ],
```

---

### Step 7: Verify the Complete Merchant Agent

Let's confirm everything is wired correctly.

👉 **Your complete `charity_advisor/merchant_agent/agent.py` should now look like this:**
```python
"""
Merchant Agent - Creates W3C-compliant CartMandates with merchant signatures.
This agent acts as our "Contract Creator."
"""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.merchant_tools import create_cart_mandate


merchant_agent = Agent(
    name="MerchantAgent",
    model="gemini-2.5-flash",
    description="Creates formal, signed CartMandates for charity donations following W3C PaymentRequest standards.",
    tools=[
        FunctionTool(func=create_cart_mandate)
    ],
    instruction="""You are a merchant specialist responsible for creating formal, signed offers (CartMandates).

Your workflow:

1. Read the IntentMandate from shared state.
   The IntentMandate was created by the Shopping Agent and contains:
   - merchants: List of merchant names
   - amount: Donation amount
   - charity_ein: Tax ID
   - intent_expiry: When the intent expires

2. Use the create_cart_mandate tool to create a W3C PaymentRequest-compliant CartMandate.
   This tool will:
   - Validate the IntentMandate hasn't expired (CRITICAL security check)
   - Extract the charity name and amount from the IntentMandate
   - Create a structured offer with payment methods, transaction details, and merchant info
   - Generate a merchant signature to prove authenticity
   - Save the CartMandate to state for the payment processor

3. After creating the CartMandate, inform the user:
   - That you've created a formal, signed offer
   - The cart ID
   - When the cart expires (15 minutes)
   - That you're passing it to the secure payment processor

IMPORTANT BOUNDARIES:
- Your ONLY job is creating signed CartMandates from valid IntentMandates
- You do NOT process payments
- You do NOT see the user's payment methods or credentials
- You do NOT interact with payment networks
- You MUST validate that the IntentMandate hasn't expired before creating a cart
- After calling create_cart_mandate, your work is done

WHAT IS A CARTMANDATE:
A CartMandate is a binding commitment that says:
"I, the merchant, commit to accepting $X for this charity donation, and I prove it with my signature."

This commitment is structured using the W3C PaymentRequest standard and includes:
- Payment methods accepted (card, bank transfer)
- Transaction details (amount, charity name)
- Cart expiry (15 minutes from creation)
- Merchant signature (proof of commitment)

This is the second of three verifiable credentials in our secure payment system."""
)
```

✅ **Checkpoint**: You now have a complete Merchant Agent with proper AP2 CartMandate creation using Pydantic models.

---

### Step 8: Test the Merchant Agent

Now let's verify that our agent correctly creates CartMandates with signatures and validates expiry.

#### Test Setup: Run the Test Script

👉 **In your Cloud Shell terminal, run:**
```bash
python scripts/test_merchant.py
```

**Expected output:**
```
======================================================================
MERCHANT AGENT TEST
======================================================================

Simulated IntentMandate from Shopping Agent:
  charity: Room to Read
  amount: $50.00
  expiry: 2024-11-07T16:32:16Z

----------------------------------------------------------------------
Merchant Agent Response:
----------------------------------------------------------------------
Perfect! I've received your IntentMandate and created a formal, signed offer (CartMandate) for your donation.

**CartMandate Details:**
- **Cart ID**: cart_3b4c5d6e7f8a
- **Donation Amount**: $50.00 to Room to Read
- **Payment Methods Accepted**: Credit/debit cards (Visa, Mastercard, Amex) or bank transfer
- **Cart Expires**: 2024-11-07T15:47:16Z (in 15 minutes)
- **Merchant Signature**: SIG_a3f7b2c8d9e1f4a2

This signed CartMandate proves my commitment to accept this donation amount. I'm now passing this to the secure payment processor to complete your transaction.

======================================================================
CARTMANDATE CREATED:
======================================================================
  ID: cart_3b4c5d6e7f8a
  Amount: 50.00
  Merchant: Room to Read
  Expires: 2024-11-07T15:47:16Z
  Signature: SIG_a3f7b2c8d9e1f4a2
======================================================================
```

> aside positive
> **What Just Happened?**
>
> Let's trace the flow using AP2 Pydantic models:
>
> **Step 3A (Setup):**
> 1. Tool was called with logging
>
> **Step 3B (Validation with Models):**
> 2. Read IntentMandate dictionary from state  
> 3. Validated structure using `IntentMandate.model_validate()`  
> 4. Validated intent hasn't expired (3600 seconds remaining)  
> 5. Extracted charity name and amount from validated model  
>
> **Step 3C (Structure with Models):**
> 6. Created `PaymentRequest` Pydantic model  
> 7. Created `CartContents` Pydantic model wrapping PaymentRequest  
>
> **Step 3D (Signature & Save with Models):**
> 8. Generated merchant signature from `CartContents` model  
> 9. Created `CartMandate` model with signature  
> 10. Converted to dict using `.model_dump(mode='json')`  
> 11. Saved CartMandate dict to state  
> 12. Returned success confirmation  
>
> This demonstrates the complete credential chain using AP2 models: IntentMandate → CartMandate

---

#### Test 2: Verify W3C Compliance

Let's validate that our CartMandate structure is fully compliant with both AP2 and W3C PaymentRequest standards.

👉 **Run the validation script:**
```bash
python scripts/validate_cartmandate.py
```

**Expected output:**
```
======================================================================
AP2 & W3C PAYMENTREQUEST VALIDATION
======================================================================
✅ CartMandate is AP2 and W3C PaymentRequest compliant

Structure validation passed:
  ✓ AP2 'contents' wrapper present
  ✓ AP2 'merchant_authorization' signature present
  ✓ cart_expiry present
  ✓ payment_request nested inside contents
  ✓ method_data present and valid
  ✓ details.total.amount present with currency and value
  ✓ All required W3C PaymentRequest fields present
======================================================================
```

> aside positive
> **What This Validator Checks**
>
> The validation script verifies:
> - ✅ **AP2 structure**: `contents` wrapper and `merchant_authorization` signature
> - ✅ **W3C compliance**: Required fields like `method_data`, `details`, `total.amount`
> - ✅ **Nested structure**: `payment_request` properly nested inside `contents`
> - ✅ **Field types**: Arrays are arrays, objects are objects
>
> Because we used AP2 Pydantic models, this structure is guaranteed to be compliant. The models enforce the specification automatically.

---

### What You Just Built

You've successfully implemented AP2's CartMandate using Pydantic models for proper structure, expiry validation, and merchant signatures.

### Key Concepts Mastered

✅ **CartMandate (AP2 Credential #2):**
- Created using official AP2 Pydantic models
- AP2 structure with contents wrapper
- W3C PaymentRequest nested inside
- Cart expiry (shorter than intent)
- Merchant signature for binding commitment
- Model validation ensures spec compliance

✅ **Expiry Validation:**
- Reading IntentMandate from state
- Validating structure with `IntentMandate.model_validate()`
- Parsing ISO 8601 timestamps
- Comparing to current time
- Security feature preventing stale processing

✅ **Merchant Signature:**
- Proves authenticity and commitment
- Generated from validated Pydantic model
- Uses `model_dump(mode='json')` for canonical representation
- Simulated with SHA-256 for education
- Production uses PKI/JWT
- Signs the contents model, not dictionaries

✅ **W3C PaymentRequest:**
- Built using AP2's PaymentRequest Pydantic model
- Industry standard for payment data
- Nested inside AP2 structure
- Contains method_data, details, options
- Enables interoperability

✅ **Credential Chain with Models:**
- Shopping → IntentMandate (validated)
- Merchant reads IntentMandate → CartMandate (both models validated)
- Credentials Provider will read CartMandate → PaymentMandate
- Each step validates previous credential using Pydantic

✅ **Model-Driven Development:**
- Input validation via `model_validate()`
- Type-safe construction
- Automatic serialization via `model_dump()`
- Production-ready patterns

---

### What's Next

In the next module, we'll build the **Credentials Provider** to process payments securely.

The Merchant Agent has created a binding offer with expiry using AP2 models. Now we need an agent to read that CartMandate, get user consent, and execute the payment.

**Let's build the Credentials Provider and complete the AP2 credential chain.**

## Building the Credentials Provider - Secure Payment Execution

**Duration: 15 min**

![banner](img/06-01-banner.png)

### From Binding Offer to Payment Execution

In Module 5, you built the Merchant Agent—a specialist that reads IntentMandates, validates they haven't expired, and creates binding CartMandates with merchant signatures. Now we need an agent to receive that CartMandate and execute the actual payment.

This is where AP2's third and final principle comes into play: **secure payment execution through PaymentMandate**.

---

### AP2 Principle: PaymentMandate & Payment Execution

#### Why We Need a Credentials Provider Role

In Module 5, the Merchant Agent created a CartMandate and saved it to state:
```python
state["cart_mandate"] = {
    "contents": {
        "id": "cart_abc123",
        "cart_expiry": "2025-11-07:15:47:16Z",
        "payment_request": {
            "details": {
                "total": {
                    "amount": {"currency": "USD", "value": "50.00"}
                }
            }
        }
    },
    "merchant_authorization": "SIG_a3f7b2c8"
}
```

But this is just a binding offer. Before payment can be executed, we need:
- Validation that the cart hasn't expired
- User consent to proceed with payment
- A credential that authorizes payment execution
- Actual payment processing (or simulation for our workshop)

**This is the Credentials Provider's job.**

#### What is a PaymentMandate?

A **PaymentMandate** is AP2's term for the final authorization that allows payment to be executed. It's the third and final verifiable credential in the AP2 chain.

Think of the three credentials like a contract signing process:
- **IntentMandate**: "I'm interested in buying this" (Letter of intent)
- **CartMandate**: "I, the merchant, offer to sell at this price" (Written quote)
- **PaymentMandate**: "I authorize you to charge my payment method" (Signed contract)

Only after all three credentials exist can payment be executed.

![complete credential chain](img/06-02-complete-credential-chain.svg)

> aside positive
> **The Human-in-the-Loop Principle**
>
> Notice that AP2 requires THREE separate credentials before payment executes:
> 1. User expresses intent (Shopping Agent)
> 2. Merchant creates offer (Merchant Agent)
> 3. User consents to payment (Credentials Provider)
>
> This is "human-in-the-loop" design—the user has multiple opportunities to review and approve before money moves. In a production web interface:
> - After IntentMandate: "You selected Room to Read for $50. Continue?"
> - After CartMandate: "Room to Read offers to accept $50. Proceed to payment?"
> - After PaymentMandate: "Authorize payment of $50 to Room to Read? [Pay Now]"
>
> For our workshop, we implement consent conversationally rather than with ADK's built-in `require_confirmation` [feature](https://google.github.io/adk-docs/tools/confirmation/), as conversational confirmation works more reliably (as of `google-adk` version 1.17.0) in workflow agent architectures with memory.

#### The Structure of a PaymentMandate

A PaymentMandate in AP2 has a specific structure:
```python
payment_mandate = {
    "payment_mandate_contents": {  # ← AP2 wrapper
        "payment_mandate_id": "payment_xyz123",
        "payment_details_id": "cart_abc123",  # Links to CartMandate
        "user_consent": True,
        "consent_timestamp": "2025-11-07T15:48:00Z",
        "amount": {
            "currency": "USD",
            "value": "50.00"
        },
        "merchant_name": "Room to Read"
    },
    "agent_present": True,  # Human-in-the-loop flow
    "timestamp": "2025-11-07T15:48:00Z"
}
```

**Key components:**

**1. payment_mandate_contents** - The authorization wrapper containing:
- payment_mandate_id: Unique identifier
- payment_details_id: Links back to CartMandate
- user_consent: Whether user approved
- amount: Payment amount (extracted from CartMandate)

**2. agent_present** - Whether this is a human-in-the-loop flow

**3. timestamp** - When authorization was created

> aside positive
> **PaymentMandate Links to CartMandate**
>
> Notice the `payment_details_id` field:
> ```python
> "payment_details_id": "cart_abc123"  # ← Links to CartMandate ID
> ```
>
> This creates an auditable chain:
> - PaymentMandate links to CartMandate via payment_details_id
> - CartMandate was created from IntentMandate
> - Result: Complete trail from user intent → merchant offer → payment
>
> In a dispute, you can trace:
> ```
> Payment xyz → used Cart abc → based on Intent 123
> User said: "Donate $50 to Room to Read" at 2:00 PM
> Merchant offered: "$50 to Room to Read" at 2:30 PM (signed)
> User authorized: Payment at 2:45 PM
> ```
>
> This is the power of verifiable credentials—accountability at every step.

### Our Mission: Build the Credentials Provider

The Credentials Provider will:
1. Read the CartMandate from state (what Merchant Agent wrote)
2. Validate that the cart hasn't expired using AP2 Pydantic models
3. Extract payment details from the nested structure
4. Create a PaymentMandate with user consent using AP2 models
5. Simulate payment processing (in production, would call real payment API)
6. Write the PaymentMandate and payment result to state

Let's build it step by step.

---

### Step 1: Add Cart Expiry Validation Helper

First, let's create a helper that validates the CartMandate hasn't expired—just like we validated IntentMandate expiry in Module 5.

👉 **Open `charity_advisor/tools/payment_tools.py`**

Let's add the expiry validation:

👉 **Find:**
```python
# MODULE_6_STEP_1_ADD_CART_EXPIRY_VALIDATION_HELPER
```

👉 **Replace that single line with:**
```python
def _validate_cart_expiry(cart: CartMandate) -> tuple[bool, str]:
    """
    Validates that the CartMandate hasn't expired.
    
    This is a critical security check - expired carts should not be processed.
    
    Args:
        cart: The Pydantic CartMandate model to validate.
        
    Returns:
        (is_valid, error_message): Tuple indicating if cart is still valid.
    """
    try:
        expiry_str = cart.contents.cart_expiry
        expiry_time = datetime.fromisoformat(expiry_str.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        
        if expiry_time < now:
            return False, f"CartMandate expired at {expiry_str}"
        
        time_remaining = expiry_time - now
        logger.info(f"CartMandate valid. Expires in {time_remaining.total_seconds():.0f} seconds")
        
        return True, ""
        
    except (ValueError, TypeError, AttributeError) as e:
        return False, f"Invalid cart_expiry format or structure: {e}"
```

> aside positive
> **Validation with Pydantic Models**
>
> Notice how the validation function now accepts a `CartMandate` Pydantic model instead of a plain dictionary. This provides:
> - **Type safety**: We can only validate properly structured carts
> - **Attribute access**: Use `cart.contents.cart_expiry` instead of nested dict access
> - **Automatic structure validation**: Pydantic ensures all required fields exist
>
> The model was already validated before reaching this function, so we know the structure is correct.

---

### Step 2: Add PaymentMandate Creation Helper

Now let's create a helper that builds the PaymentMandate structure using official AP2 Pydantic models.

👉 **Find:**
```python
# MODULE_6_STEP_2_ADD_PAYMENT_MANDATE_CREATION_HELPER
```

👉 **Replace that single line with:**
```python
def _create_payment_mandate(cart: CartMandate, consent_granted: bool) -> dict:
    """
    Creates a PaymentMandate using the official AP2 Pydantic models.
    
    It links to the CartMandate and includes user consent status.
    
    Args:
        cart: The validated Pydantic CartMandate model being processed.
        consent_granted: Whether the user has consented to the payment.
        
    Returns:
        A dictionary representation of the final, validated PaymentMandate.
    """
    timestamp = datetime.now(timezone.utc)
    
    # Safely extract details from the validated CartMandate model
    cart_id = cart.contents.id
    merchant_name = cart.contents.merchant_name
    total_item = cart.contents.payment_request.details.total
    
    # Create the nested PaymentResponse model for the mandate
    payment_response_model = PaymentResponse(
        request_id=cart_id,
        method_name="CARD",  # As per the simulated flow
        details={"token": "simulated_payment_token_12345"}
    )
    
    # Create the PaymentMandateContents model
    payment_mandate_contents_model = PaymentMandateContents(
        payment_mandate_id=f"payment_{hashlib.sha256(f'{cart_id}{timestamp.isoformat()}'.encode()).hexdigest()[:12]}",
        payment_details_id=cart_id,
        payment_details_total=total_item,
        payment_response=payment_response_model,
        merchant_agent=merchant_name,
        timestamp=timestamp.isoformat()
    )
    
    # Create the top-level PaymentMandate model
    # In a real system, a user signature would be added to this model
    payment_mandate_model = PaymentMandate(
        payment_mandate_contents=payment_mandate_contents_model
    )
    
    # Convert the final Pydantic model to a dictionary for state storage
    final_dict = payment_mandate_model.model_dump(mode='json')
    
    # Add any custom/non-standard fields required by the codelab's logic to the dictionary
    # The spec does not have these fields, but your original code did. We add them
    # back to ensure compatibility with later steps.
    final_dict['payment_mandate_contents']['user_consent'] = consent_granted
    final_dict['payment_mandate_contents']['consent_timestamp'] = timestamp.isoformat() if consent_granted else None
    final_dict['agent_present'] = True
    
    return final_dict
```

> aside positive
> **Building PaymentMandate with AP2 Models**
>
> Notice how we build the PaymentMandate using official AP2 Pydantic models:
>
> **1. Extract from validated CartMandate model:**
> ```python
> cart_id = cart.contents.id
> merchant_name = cart.contents.merchant_name
> total_item = cart.contents.payment_request.details.total
> ```
>
> **2. Create nested models:**
> ```python
> payment_response_model = PaymentResponse(...)
> payment_mandate_contents_model = PaymentMandateContents(...)
> payment_mandate_model = PaymentMandate(...)
> ```
>
> **3. Convert to dict for state:**
> ```python
> final_dict = payment_mandate_model.model_dump(mode='json')
> ```
>
> This ensures full AP2 spec compliance through automatic validation.

> aside positive
> **User Consent: agent_present Flag**
>
> ```python
> final_dict['agent_present'] = True  # Human-in-the-loop flow
> ```
>
> AP2 distinguishes between:
> - **agent_present: True** - Human is involved, can review/approve
> - **agent_present: False** - Fully autonomous, pre-authorized
>
> For donations and purchases, `agent_present: True` is safer. The user sees what's happening and can intervene.
>
> In fully autonomous flows (e.g., auto-renew subscriptions), you'd use `agent_present: False` with pre-authorization.

---

### Step 3A: Create the Tool Signature and Setup

Now let's start building the main tool incrementally. First, the function signature and initial setup.

👉 **Find:**
```python
# MODULE_6_STEP_3A_CREATE_TOOL_SIGNATURE
```

👉 **Replace that single line with:**
```python
async def create_payment_mandate(tool_context: Any) -> Dict[str, Any]:
    """
    Creates a PaymentMandate and simulates payment processing using Pydantic models.
    
    This tool now reads the CartMandate from state, parses it into a validated model,
    and creates a spec-compliant PaymentMandate.
    """
    logger.info("Tool called: Creating PaymentMandate and processing payment")
    
    # MODULE_6_STEP_3B_VALIDATE_CARTMANDATE
```

---

### Step 3B: Validate CartMandate

Now let's add the logic to read, validate the CartMandate using AP2 Pydantic models, and check expiry.

👉 **Find:**
```python
# MODULE_6_STEP_3B_VALIDATE_CARTMANDATE
```

👉 **Replace that single line with:**
```python
    # 1. Read CartMandate dictionary from state
    cart_mandate_dict = tool_context.state.get("cart_mandate")
    if not cart_mandate_dict:
        logger.error("No CartMandate found in state")
        return { "status": "error", "message": "No CartMandate found. Merchant Agent must create cart first." }
    
    # 2. Parse dictionary into a validated Pydantic model
    try:
        cart_model = CartMandate.model_validate(cart_mandate_dict)
    except Exception as e:
        logger.error(f"Could not validate CartMandate structure: {e}")
        return {"status": "error", "message": f"Invalid CartMandate structure: {e}"}
    
    # 3. Validate that the cart hasn't expired using the Pydantic model
    is_valid, error_message = _validate_cart_expiry(cart_model)
    if not is_valid:
        logger.error(f"CartMandate validation failed: {error_message}")
        return {"status": "error", "message": error_message}
    
    # MODULE_6_STEP_3C_EXTRACT_PAYMENT_DETAILS
```

> aside positive
> **Layered Validation with Pydantic**
>
> Notice the validation layers using AP2 models:
>
> **Layer 1: Credential exists**
> ```python
> if not cart_mandate_dict:
>     return {"status": "error", "message": "No CartMandate found"}
> ```
>
> **Layer 2: Structure is valid (Pydantic)**
> ```python
> cart_model = CartMandate.model_validate(cart_mandate_dict)
> # Pydantic validates all fields against AP2 spec
> ```
>
> **Layer 3: Not expired**
> ```python
> is_valid, error_message = _validate_cart_expiry(cart_model)
> if not is_valid:
>     return {"status": "error", "message": error_message}
> ```
>
> Each layer protects against a different failure mode:
> - Missing credential (upstream agent didn't run)
> - Malformed credential (caught by Pydantic validation)
> - Expired credential (business logic validation)

> aside positive
> **Reading from State: The Final Link**
>
> ```python
> cart_mandate_dict = tool_context.state.get("cart_mandate")
> ```
>
> This is the final step in the credential chain:
> - **Shopping Agent** wrote `intent_mandate` to state
> - **Merchant Agent** read `intent_mandate`, wrote `cart_mandate` to state
> - **Credentials Provider** reads `cart_mandate` ← We are here
>
> Each agent validates what it reads using Pydantic models, ensuring the chain is unbroken.

---

### Step 3C: Extract Payment Details from Nested Structure

Now let's navigate the validated CartMandate model to extract the payment details we need.

👉 **Find:**
```python
# MODULE_6_STEP_3C_EXTRACT_PAYMENT_DETAILS
```

👉 **Replace that single line with:**
```python
    # 4. Safely extract data from the validated model
    cart_id = cart_model.contents.id
    merchant_name = cart_model.contents.merchant_name
    amount_value = cart_model.contents.payment_request.details.total.amount.value
    currency = cart_model.contents.payment_request.details.total.amount.currency
    consent_granted = True  # Assume consent for this codelab flow
    
    # MODULE_6_STEP_3D_CREATE_PAYMENTMANDATE_AND_SIMULATE
```

> aside positive
> **Type-Safe Data Extraction**
>
> Notice how we extract data from the validated Pydantic model:
>
> **Before (dictionary navigation):**
> ```python
> contents = cart_mandate["contents"]
> payment_request = contents.get("payment_request", {})
> details = payment_request.get("details", {})
> total = details.get("total", {})
> amount_value = total.get("amount", {}).get("value", "0.00")
> ```
>
> **After (model attribute access):**
> ```python
> amount_value = cart_model.contents.payment_request.details.total.amount.value
> currency = cart_model.contents.payment_request.details.total.amount.currency
> ```
>
> The model approach is:
> - **Safer**: No KeyError if structure changes
> - **Clearer**: Shows the exact path through the structure
> - **Type-checked**: IDE autocomplete and type hints work
> - **Validated**: Pydantic ensures all fields exist

---

### Step 3D: Create PaymentMandate and Simulate Payment

Finally, let's create the PaymentMandate using our Pydantic-based helper, simulate payment processing, and save everything to state.

👉 **Find:**
```python
# MODULE_6_STEP_3D_CREATE_PAYMENTMANDATE_AND_SIMULATE
```

👉 **Replace that single line with:**
```python
    # 5. Create the spec-compliant PaymentMandate using the validated CartMandate model
    payment_mandate_dict = _create_payment_mandate(cart_model, consent_granted)
    
    # 6. Simulate payment processing
    transaction_id = f"txn_{hashlib.sha256(f'{cart_id}{datetime.now(timezone.utc).isoformat()}'.encode()).hexdigest()[:16]}"
    payment_result = {
        "transaction_id": transaction_id,
        "status": "completed",
        "amount": amount_value,
        "currency": currency,
        "merchant": merchant_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "simulation": True
    }
    
    # 7. Write the compliant PaymentMandate dictionary and result to state
    tool_context.state["payment_mandate"] = payment_mandate_dict
    tool_context.state["payment_result"] = payment_result
    
    logger.info(f"Payment processed successfully: {transaction_id}")
    
    return {
        "status": "success",
        "message": f"Payment of {currency} {amount_value:.2f} to {merchant_name} processed successfully",
        "transaction_id": transaction_id,
        "payment_mandate_id": payment_mandate_dict["payment_mandate_contents"]["payment_mandate_id"]
    }
```

> aside positive
> **The Complete Model-Driven Flow**
>
> Now that we've built it across four substeps, here's the complete flow using AP2 models:
>
> ```python
> async def create_payment_mandate(tool_context: Any):
>     # Setup (3A)
>     logger.info("Tool called...")
>     
>     # Validation with Models (3B)
>     cart_mandate_dict = tool_context.state.get("cart_mandate")
>     cart_model = CartMandate.model_validate(cart_mandate_dict)  # Pydantic validation
>     is_valid, error = _validate_cart_expiry(cart_model)
>     
>     # Type-Safe Extraction (3C)
>     amount_value = cart_model.contents.payment_request.details.total.amount.value
>     consent_granted = True
>     
>     # Payment with Models (3D)
>     payment_mandate_dict = _create_payment_mandate(cart_model, consent_granted)
>     # ... simulate payment, save to state
>     return {"status": "success", ...}
> ```
>
> Four clear stages: setup → validate model → extract safely → execute with models.

---

### Step 4: Build the Credentials Provider Agent - Import Components

Now let's create the agent that uses this tool.

👉 **Open `charity_advisor/credentials_provider/agent.py`**

You'll see a template with placeholder markers. Let's start by importing what we need.

👉 **Find:**
```python
# MODULE_6_STEP_4_IMPORT_COMPONENTS
```

👉 **Replace that single line with:**
```python
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.payment_tools import create_payment_mandate
```

---

### Step 5: Write the Credentials Provider Instruction

Now let's write the instruction that guides the agent.

👉 **Find:**
```python
# MODULE_6_STEP_5_WRITE_INSTRUCTION
instruction="""""",
```

👉 **Replace those two lines with:**
```python
    instruction="""You are a payment specialist responsible for securely processing payments with user consent.

Your workflow:

1. Read the CartMandate from shared state.
   The CartMandate was created by the Merchant Agent and has this structure:
   - contents: AP2 wrapper containing:
     - id: Cart identifier
     - cart_expiry: When the cart expires
     - merchant_name: Who is receiving payment
     - payment_request: W3C PaymentRequest with transaction details
   - merchant_authorization: Merchant's signature

2. Extract payment details from the nested structure:
   - Navigate: cart_mandate["contents"]["payment_request"]["details"]["total"]["amount"]
   - This gives you the currency and value

3. **IMPORTANT - Two-Turn Conversational Confirmation Pattern:**
   Before calling create_payment_mandate, you MUST:
   - Present the payment details clearly to the user
   - Ask explicitly: "I'm ready to process a payment of $X to [Charity Name]. Do you want to proceed with this donation?"
   - WAIT for the user's explicit confirmation (e.g., "yes", "proceed", "confirm")
   - ONLY call create_payment_mandate AFTER receiving explicit confirmation
   - If user says "no" or "cancel", DO NOT call the tool

4. After user confirms, use the create_payment_mandate tool to:
   - Validate the CartMandate hasn't expired (CRITICAL security check)
   - Create a PaymentMandate (the third AP2 credential)
   - Simulate payment processing
   - Record the transaction result

5. After processing, inform the user:
   - That payment was processed successfully (this is a simulation)
   - The transaction ID
   - The amount and merchant
   - That this completes the three-agent AP2 credential chain

IMPORTANT BOUNDARIES:
- Your ONLY job is creating PaymentMandates and processing payments
- You do NOT discover charities (that's Shopping Agent's job)
- You do NOT create offers (that's Merchant Agent's job)
- You MUST validate that the CartMandate hasn't expired before processing
- You MUST get explicit user confirmation before calling create_payment_mandate
- In production, this consent mechanism would be even more robust

WHAT IS A PAYMENTMANDATE:
A PaymentMandate is the final credential that authorizes payment execution. It:
- Links to the CartMandate (proving the merchant's offer)
- Records user consent
- Contains payment details extracted from the CartMandate
- Enables the actual payment transaction

This is the third and final verifiable credential in our secure payment system.

THE COMPLETE AP2 CREDENTIAL CHAIN:
1. Shopping Agent creates IntentMandate (user's intent)
2. Merchant Agent reads IntentMandate, creates CartMandate (merchant's binding offer)
3. You read CartMandate, get user confirmation, create PaymentMandate (authorized payment execution)

Each credential:
- Has an expiry time (security feature)
- Links to the previous credential
- Is validated before the next step
- Creates an auditable chain of trust""",
```

---

### Step 6: Add Tools to the Credentials Provider

👉 **Find:**
```python
# MODULE_6_STEP_6_ADD_TOOLS
tools=[],
```

👉 **Replace those two lines with:**
```python
    tools=[
        FunctionTool(func=create_payment_mandate)
    ],
```

---

### Step 7: Verify the Complete Credentials Provider

Let's confirm everything is wired correctly.

👉 **Your complete `charity_advisor/credentials_provider/agent.py` should now look like this:**
```python
"""
Credentials Provider Agent - Handles payment processing with user consent.
This agent acts as our "Payment Processor."
"""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from charity_advisor.tools.payment_tools import create_payment_mandate


credentials_provider = Agent(
    name="CredentialsProvider",
    model="gemini-2.5-flash",
    description="Securely processes payments by creating PaymentMandates and executing transactions with user consent.",
    tools=[
        FunctionTool(func=create_payment_mandate)
    ],
    instruction="""You are a payment specialist responsible for securely processing payments with user consent.

Your workflow:

1. Read the CartMandate from shared state.
   The CartMandate was created by the Merchant Agent and has this structure:
   - contents: AP2 wrapper containing:
     - id: Cart identifier
     - cart_expiry: When the cart expires
     - merchant_name: Who is receiving payment
     - payment_request: W3C PaymentRequest with transaction details
   - merchant_authorization: Merchant's signature

2. Extract payment details from the nested structure:
   - Navigate: cart_mandate["contents"]["payment_request"]["details"]["total"]["amount"]
   - This gives you the currency and value

3. **IMPORTANT - Two-Turn Conversational Confirmation Pattern:**
   Before calling create_payment_mandate, you MUST:
   - Present the payment details clearly to the user
   - Ask explicitly: "I'm ready to process a payment of $X to [Charity Name]. Do you want to proceed with this donation?"
   - WAIT for the user's explicit confirmation (e.g., "yes", "proceed", "confirm")
   - ONLY call create_payment_mandate AFTER receiving explicit confirmation
   - If user says "no" or "cancel", DO NOT call the tool

4. After user confirms, use the create_payment_mandate tool to:
   - Validate the CartMandate hasn't expired (CRITICAL security check)
   - Create a PaymentMandate (the third AP2 credential)
   - Simulate payment processing
   - Record the transaction result

5. After processing, inform the user:
   - That payment was processed successfully (this is a simulation)
   - The transaction ID
   - The amount and merchant
   - That this completes the three-agent AP2 credential chain

IMPORTANT BOUNDARIES:
- Your ONLY job is creating PaymentMandates and processing payments
- You do NOT discover charities (that's Shopping Agent's job)
- You do NOT create offers (that's Merchant Agent's job)
- You MUST validate that the CartMandate hasn't expired before processing
- You MUST get explicit user confirmation before calling create_payment_mandate
- In production, this consent mechanism would be even more robust

WHAT IS A PAYMENTMANDATE:
A PaymentMandate is the final credential that authorizes payment execution. It:
- Links to the CartMandate (proving the merchant's offer)
- Records user consent
- Contains payment details extracted from the CartMandate
- Enables the actual payment transaction

This is the third and final verifiable credential in our secure payment system.

THE COMPLETE AP2 CREDENTIAL CHAIN:
1. Shopping Agent creates IntentMandate (user's intent)
2. Merchant Agent reads IntentMandate, creates CartMandate (merchant's binding offer)
3. You read CartMandate, get user confirmation, create PaymentMandate (authorized payment execution)

Each credential:
- Has an expiry time (security feature)
- Links to the previous credential
- Is validated before the next step
- Creates an auditable chain of trust"""
)
```

✅ **Checkpoint**: You now have a complete Credentials Provider with proper CartMandate reading and PaymentMandate creation using AP2 Pydantic models.

---

### Step 8: Test the Credentials Provider

Now let's verify that our agent correctly processes payments and completes the credential chain.

👉 **In your Cloud Shell terminal, run:**
```bash
python scripts/test_credentials_provider.py
```

**Expected output:**
```
======================================================================
CREDENTIALS PROVIDER TEST (MOCK - NO CONFIRMATION)
======================================================================

Simulated CartMandate from Merchant Agent:
  - Cart ID: cart_test123
  - Merchant: Room to Read
  - Amount: $50.00
  - Expires: 2025-11-07T15:47:16Z
  - Signature: SIG_test_signature

Calling Credentials Provider to process payment...
======================================================================
INFO:charity_advisor.tools.payment_tools:Tool called: Creating PaymentMandate and processing payment
INFO:charity_advisor.tools.payment_tools:CartMandate valid. Expires in 900 seconds
INFO:charity_advisor.tools.payment_tools:Payment processed successfully: txn_a3f7b2c8d9e1f4a2

======================================================================
CREDENTIALS PROVIDER RESPONSE:
======================================================================
I've successfully processed your payment. Here are the details:

**Payment Completed** (Simulated)
- Transaction ID: txn_a3f7b2c8d9e1f4a2
- Amount: USD 50.00
- Merchant: Room to Read
- Status: Completed

This completes the three-agent AP2 credential chain:
1. ✓ Shopping Agent created IntentMandate (your intent)
2. ✓ Merchant Agent created CartMandate (binding offer)
3. ✓ Credentials Provider created PaymentMandate (payment authorization)

Your donation has been processed securely through our verifiable credential system.

======================================================================
PAYMENTMANDATE CREATED:
======================================================================
  Payment Mandate ID: payment_3b4c5d6e7f8a
  Linked to Cart: cart_test123
  User Consent: True
  Amount: USD 50.00
  Merchant: Room to Read
  Agent Present: True
======================================================================

======================================================================
PAYMENT RESULT:
======================================================================
  Transaction ID: txn_a3f7b2c8d9e1f4a2
  Status: completed
  Amount: USD 50.00
  Merchant: Room to Read
  Simulation: True
======================================================================
```

> aside positive
> **What Just Happened with Pydantic Models?**
>
> Let's trace the complete flow using AP2 models:
>
> **Step 3A (Setup):**
> 1. Tool was called with logging
>
> **Step 3B (Validation with Models):**
> 2. Read CartMandate dictionary from state
> 3. Validated structure using `CartMandate.model_validate()`  
> 4. Validated cart hasn't expired using validated model (900 seconds remaining)
>
> **Step 3C (Type-Safe Extraction):**
> 5. Extracted amount using model attributes: `cart_model.contents.payment_request.details.total.amount.value`
> 6. Got merchant_name, currency safely from model  
> 7. Set consent_granted = True
>
> **Step 3D (Execution with Models):**
> 8. Created PaymentMandate using `_create_payment_mandate(cart_model, ...)`  
> 9. Helper built nested AP2 models (PaymentResponse, PaymentMandateContents, PaymentMandate)  
> 10. Converted final model to dict with `.model_dump(mode='json')`  
> 11. Saved PaymentMandate dict and payment_result to state  
> 12. Returned success confirmation
>
> This demonstrates the full AP2 flow using Pydantic models: IntentMandate → CartMandate → PaymentMandate

---

### Step 9: Test the Complete Three-Agent Pipeline

Now let's test all three agents working together!

👉 **Run the full pipeline test:**
```bash
python scripts/test_full_pipeline.py
```

**Expected output:**
```
======================================================================
THREE-AGENT PIPELINE TEST (AP2 CREDENTIAL CHAIN)
======================================================================

[1/3] SHOPPING AGENT - Finding charity and creating IntentMandate...
----------------------------------------------------------------------
✓ IntentMandate created
  - Intent ID: intent_774799058_1730927536
  - Description: Donate $75.00 to Room to Read
  - Merchant: Room to Read
  - Amount: $75.0
  - Expires: 2025-11-07T16:32:16Z

[2/3] MERCHANT AGENT - Reading IntentMandate and creating CartMandate...
----------------------------------------------------------------------
✓ CartMandate created
  - ID: cart_3b4c5d6e7f8a
  - Expires: 2025-11-07T15:47:16Z
  - Signature: SIG_a3f7b2c8d9e1f4a2

[3/3] CREDENTIALS PROVIDER - Creating PaymentMandate and processing...
----------------------------------------------------------------------
NOTE: In the web UI, this would show a confirmation dialog
      For this test, consent is automatically granted
✓ Payment processed (SIMULATED)
  - Transaction ID: txn_a3f7b2c8d9e1f4a2
  - Amount: $75.0
  - Status: completed

======================================================================
COMPLETE AP2 CREDENTIAL CHAIN
======================================================================

✓ Credential 1: IntentMandate (User's Intent)
  - Intent ID: intent_774799058_1730927536
  - Description: Donate $75.00 to Room to Read
  - Expiry: 2025-11-07T16:32:16Z

✓ Credential 2: CartMandate (Merchant's Offer)
  - Cart ID: cart_3b4c5d6e7f8a
  - Cart Expiry: 2025-11-07T15:47:16Z
  - Merchant Signature: SIG_a3f7b2c8d9e1f4a2

✓ Credential 3: PaymentMandate (Payment Execution)
  - Payment Mandate ID: payment_3b4c5d6e7f8a
  - Linked to Cart: cart_3b4c5d6e7f8a
  - Agent Present: True

✓ Transaction Result:
  - Transaction ID: txn_a3f7b2c8d9e1f4a2
  - Simulation: True

======================================================================
✅ COMPLETE PIPELINE TEST PASSED
======================================================================
```

**This is the complete AP2 credential chain in action!**

Each agent:
1. Reads a credential from state
2. Validates it using Pydantic models (structure + expiry check)
3. Creates the next credential using AP2 models
4. Writes to state for the next agent

> aside positive
> **The Complete Credential Chain with Models**
>
> You've now built the full AP2 system using Pydantic models:
>
> **Shopping Agent**:
> - Input: User query
> - Creates: IntentMandate (Pydantic validated)
> - Output: `state["intent_mandate"]`
> - Expiry: 1 hour
>
> **Merchant Agent**:
> - Input: `state["intent_mandate"]`
> - Validates: `IntentMandate.model_validate()` + intent_expiry
> - Creates: CartMandate (Pydantic validated)
> - Output: `state["cart_mandate"]`
> - Expiry: 15 minutes
>
> **Credentials Provider**:
> - Input: `state["cart_mandate"]`
> - Validates: `CartMandate.model_validate()` + cart_expiry
> - Creates: PaymentMandate (Pydantic validated) + payment execution
> - Output: `state["payment_mandate"]`, `state["payment_result"]`
>
> Each step validates using AP2 Pydantic models, creating an auditable, type-safe chain.

---

### What You Just Built

You've successfully completed the AP2 three-agent credential chain with proper structure validation using Pydantic models and payment simulation.

### Key Concepts Mastered

✅ **PaymentMandate (AP2 Credential #3):**
- Created using official AP2 Pydantic models
- Final credential authorizing payment execution
- Links to CartMandate via payment_details_id
- Records user consent and timestamp
- Contains payment amount extracted from CartMandate
- Includes agent_present flag for human-in-the-loop
- Model validation ensures spec compliance

✅ **Reading from CartMandate:**
- Validate structure with `CartMandate.model_validate()`
- Type-safe attribute access: `cart_model.contents.payment_request.details.total.amount`
- Understand AP2 wrapper vs W3C standard separation
- Extract merchant_name, amount, currency safely from model
- Pydantic catches structure errors automatically

✅ **Cart Expiry Validation:**
- Accepts validated `CartMandate` Pydantic model
- Reads from `cart.contents.cart_expiry` (attribute access)
- Security feature preventing stale cart processing
- Shorter duration (15 min) than intent (1 hour)

✅ **Payment Simulation:**
- Educational mock of real payment processor
- Generates transaction ID
- Records payment_result in state
- Clearly marked as simulation (simulation: True flag)

✅ **Complete AP2 Chain with Models:**
- Three agents, three credentials, three Pydantic validations
- Each agent validates previous credential's structure using models
- Each credential links to previous for audit trail
- State-based handoffs maintain role separation
- Type safety throughout the chain

✅ **Model-Driven Development:**
- Input validation via `model_validate()`
- Type-safe construction with nested models
- Automatic serialization via `model_dump(mode='json')`
- Production-ready patterns from the start

---

### What's Next

In the next module, we'll build the **Orchestrator Agent** that coordinates all three specialist agents.

You've built three powerful specialist agents using AP2 Pydantic models. Now let's build the conductor that orchestrates them into a seamless donation experience.

**Let's build the Orchestrator and see the complete system in action.**

## Orchestration - Bringing It All Together

**Duration: 15 min**

![sequential pipeline](img/07-01-processing-pipeline.svg)

### From Specialists to Seamless Experience

In the previous modules, you built three specialized agents:
- **Shopping Agent**: Finds charities, creates IntentMandate
- **Merchant Agent**: Creates CartMandate from IntentMandate
- **Credentials Provider**: Creates PaymentMandate, processes payment

These agents naturally fall into two phases:
- **Phase 1 (Shopping)**: Multi-turn conversation to find and select charity
- **Phase 2 (Processing)**: Atomic execution of offer creation and payment

But right now, you'd have to manually orchestrate these phases yourself.

This is where ADK's orchestration patterns shine.

---

### AP2 Principle: Orchestration Enforces Trust Boundaries

#### Why Orchestration Matters for Security

Orchestration isn't just about convenience—it's about enforcing trust boundaries through architecture.

**Without orchestration:**
```python
# User could accidentally skip steps or reorder them
shopping_agent.run("Find charity")
# Oops, forgot to create CartMandate!
credentials_provider.run("Process payment")  # No offer to validate!
```

**With orchestration:**
```python
# Pipeline enforces correct order
donation_processing_pipeline = SequentialAgent(
    sub_agents=[
        merchant_agent,      # Must run first
        credentials_provider # Must run second
    ]
)
# Steps ALWAYS run in order, no skipping allowed
```

The sequential pipeline guarantees:
- ✅ IntentMandate created before CartMandate
- ✅ CartMandate created before payment processing
- ✅ Each agent runs in its isolated context
- ✅ State flows forward through the credential chain

### Our Mission: Build the Complete System

We'll build two layers:

**Layer 1: The Processing Pipeline** (SequentialAgent)
- Wires together Merchant → Credentials
- Runs automatically in sequence after charity is selected
- Atomic execution of offer and payment

**Layer 2: The Root Orchestrator** (user-facing Agent)
- Friendly personality
- Delegates to shopping_agent for charity selection
- Delegates to processing pipeline after IntentMandate is created
- Handles conversation and phase transitions

This two-layer approach matches the natural flow:
- **Shopping Phase**: Multi-turn conversation (user browses, asks questions, decides)
- **Processing Phase**: Atomic execution (offer → payment)

Let's build both.

---

### Step 1: Import Orchestration Components

First, let's set up the orchestration file with the necessary imports.

👉 **Open `charity_advisor/agent.py`**

Let's start with imports:

👉 **Find:**
```python
# MODULE_7_STEP_1_IMPORT_COMPONENTS
```

👉 **Replace that single line with:**

```python
from google.adk.agents import Agent, SequentialAgent
from charity_advisor.shopping_agent.agent import shopping_agent
from charity_advisor.merchant_agent.agent import merchant_agent
from charity_advisor.credentials_provider.agent import credentials_provider
```

> aside positive
> **ADK Imports Explained**
>
> **SequentialAgent**: ADK's pipeline primitive
> ```python
> from google.adk.agents import Agent, SequentialAgent
> ```
> - `Agent`: What we've been using (single LLM-powered agent)
> - `SequentialAgent`: Coordinates multiple agents in sequence
>
> **The three specialists**:
> ```python
> from charity_advisor.shopping_agent.agent import shopping_agent
> from charity_advisor.merchant_agent.agent import merchant_agent
> from charity_advisor.credentials_provider.agent import credentials_provider
> ```
> We import all three to wire them into the orchestration.
>
> Notice we don't need any special "tool wrappers"—agents can directly delegate to other agents using the `sub_agents` parameter.

---

### Step 2: Create the Processing Pipeline

Now let's create the pipeline that runs offer creation and payment processing atomically.

👉 **Find:**
```python
# MODULE_7_STEP_2_CREATE_SEQUENTIAL_PIPELINE
```

👉 **Replace those two lines with:**
```python
# Create the donation processing pipeline
# This runs Merchant → Credentials in sequence AFTER charity is selected
donation_processing_pipeline = SequentialAgent(
    name="DonationProcessingPipeline",
    description="Creates signed offer and processes payment after charity is selected",
    sub_agents=[
        merchant_agent,
        credentials_provider
    ]
)
```

> aside positive
> **Why Only Two Agents in the Pipeline?**
>
> Shopping naturally involves multi-turn conversation:
> - "Show me education charities" → Agent presents options → User asks questions → User decides
> 
> Processing naturally happens atomically:
> - User has decided → Create signed offer → Get consent → Process payment
>
> By keeping Shopping separate, we allow natural conversation flow while ensuring offer+payment happen without interruption.

---

### Step 3A: Create Root Agent Setup

Now let's create the user-facing agent that orchestrates both phases. We'll build this in three parts: setup (3A), instruction (3B), and sub-agents (3C).

👉 **Find:**
```python
# MODULE_7_STEP_3A_CREATE_ROOT_AGENT_SETUP
```

👉 **Replace that single line with:**
```python
# Create the root orchestrator agent
# This is what users interact with directly
root_agent = Agent(
    name="CharityAdvisor",
    model="gemini-2.5-pro",
    description="A friendly charity giving assistant that helps users donate to verified organizations.",
    # MODULE_7_STEP_3B_WRITE_ROOT_AGENT_INSTRUCTION
```

---

### Step 3B: Write the Root Agent Instruction

Now let's add the instruction that guides the charity advisor's behavior across both phases.

👉 **Find:**
```python
# MODULE_7_STEP_3B_WRITE_ROOT_AGENT_INSTRUCTION
```

👉 **Replace that single line with:**
```python
    instruction="""You are a helpful and friendly charity giving advisor.

Your workflow has TWO distinct phases:

PHASE 1: CHARITY SELECTION (delegate to shopping_agent)
When a user expresses interest in donating:
1. Delegate to shopping_agent immediately
2. The shopping_agent will:
   - Search for charities matching their cause
   - Present verified options with ratings
   - Engage in conversation (user may ask questions, change their mind)
   - Wait for user to select a specific charity and amount
   - Create an IntentMandate when user decides
3. Wait for shopping_agent to complete

You'll know Phase 1 is complete when shopping_agent's response includes:
- "IntentMandate created" or "Intent ID: intent_xxx" 
- Charity name and donation amount

PHASE 2: PAYMENT PROCESSING (delegate to DonationProcessingPipeline)
After shopping_agent completes:
1. Acknowledge the user's selection naturally:
   "Perfect! Let me process your $X donation to [Charity]..."
2. Delegate to DonationProcessingPipeline
3. The pipeline will automatically:
   - Create signed cart offer (MerchantAgent)
   - Get consent and process payment (CredentialsProvider)
4. After pipeline completes, summarize the transaction

CRITICAL RULES:
- Phase 1 may take multiple conversation turns (this is normal)
- Only proceed to Phase 2 after IntentMandate exists
- Don't rush the user during charity selection
- Don't ask user to "proceed" between phases - transition automatically

EXAMPLE FLOW:
User: "I want to donate to education"
You: [delegate to shopping_agent]
Shopping: "Here are 3 education charities..." [waits]
User: "Tell me more about the first one"
Shopping: "Room to Read focuses on..." [waits]
User: "Great, I'll donate $50 to Room to Read"
Shopping: "IntentMandate created (ID: intent_123)..."
You: "Perfect! Processing your $50 donation to Room to Read..." [delegate to DonationProcessingPipeline]
Pipeline: [creates offer, gets consent, processes payment]
You: "Done! Your donation was processed successfully. Transaction ID: txn_456"

Your personality:
- Warm and encouraging
- Patient during charity selection
- Clear about educational nature
- Smooth transitions between phases""",
# MODULE_7_STEP_3C_ADD_ROOT_AGENT_SUBAGENTS
```

---

### Step 3C: Add the Sub-Agents

Finally, let's give the charity advisor access to both the shopping agent and the processing pipeline, and close the Agent definition.

👉 **Find:**
```python
# MODULE_7_STEP_3C_ADD_ROOT_AGENT_SUBAGENTS
```

👉 **Replace that single line with:**
```python
    sub_agents=[
        shopping_agent,
        donation_processing_pipeline
    ]
)
```

### Step 4: Verify the Complete System

Let's confirm the orchestration is wired correctly.

👉 **Your complete `charity_advisor/agent.py` should now look like this:**

```python
"""
Main orchestration: The donation processing pipeline and root orchestrator agent.
"""

from google.adk.agents import Agent, SequentialAgent
from charity_advisor.shopping_agent.agent import shopping_agent
from charity_advisor.merchant_agent.agent import merchant_agent
from charity_advisor.credentials_provider.agent import credentials_provider

# Create the donation processing pipeline
# This runs Merchant → Credentials in sequence AFTER charity is selected
donation_processing_pipeline = SequentialAgent(
    name="DonationProcessingPipeline",
    description="Creates signed offer and processes payment after charity is selected",
    sub_agents=[
        merchant_agent,
        credentials_provider
    ]
)

# Create the root orchestrator agent
# This is what users interact with directly
root_agent = Agent(
    name="CharityAdvisor",
    model="gemini-2.5-flash",
    description="A friendly charity giving assistant that helps users donate to verified organizations.",
    instruction="""You are a helpful and friendly charity giving advisor.

Your workflow has TWO distinct phases:

PHASE 1: CHARITY SELECTION (delegate to shopping_agent)
When a user expresses interest in donating:
1. Delegate to shopping_agent immediately
2. The shopping_agent will:
   - Search for charities matching their cause
   - Present verified options with ratings
   - Engage in conversation (user may ask questions, change their mind)
   - Wait for user to select a specific charity and amount
   - Create an IntentMandate when user decides
3. Wait for shopping_agent to complete

You'll know Phase 1 is complete when shopping_agent's response includes:
- "IntentMandate created" or "Intent ID: intent_xxx" 
- Charity name and donation amount

PHASE 2: PAYMENT PROCESSING (delegate to DonationProcessingPipeline)
After shopping_agent completes:
1. Acknowledge the user's selection naturally:
   "Perfect! Let me process your $X donation to [Charity]..."
2. Delegate to DonationProcessingPipeline
3. The pipeline will automatically:
   - Create signed cart offer (MerchantAgent)
   - Get consent and process payment (CredentialsProvider)
4. After pipeline completes, summarize the transaction

CRITICAL RULES:
- Phase 1 may take multiple conversation turns (this is normal)
- Only proceed to Phase 2 after IntentMandate exists
- Don't rush the user during charity selection
- Don't ask user to "proceed" between phases - transition automatically

EXAMPLE FLOW:
User: "I want to donate to education"
You: [delegate to shopping_agent]
Shopping: "Here are 3 education charities..." [waits]
User: "Tell me more about the first one"
Shopping: "Room to Read focuses on..." [waits]
User: "Great, I'll donate $50 to Room to Read"
Shopping: "IntentMandate created (ID: intent_123)..."
You: "Perfect! Processing your $50 donation to Room to Read..." [delegate to DonationProcessingPipeline]
Pipeline: [creates offer, gets consent, processes payment]
You: "Done! Your donation was processed successfully. Transaction ID: txn_456"

Your personality:
- Warm and encouraging
- Patient during charity selection
- Clear about educational nature
- Smooth transitions between phases""",
    sub_agents=[
        shopping_agent,
        donation_processing_pipeline
    ]
)
```

### Step 5: Harden with Validation Callbacks (Optional Skip to Step 7)

![callbacks](img/07-02-callbacks.png)

The SequentialAgent guarantees execution **order**, but what if:
- Shopping Agent fails silently (IntentMandate never created)
- An hour passes between Shopping and Merchant (intent expires)
- State gets corrupted or cleared
- Someone tries to call Merchant directly, bypassing Shopping

**[Callbacks](https://google.github.io/adk-docs/callbacks/) add architectural enforcement** - they validate prerequisites before an agent even starts its LLM call. This is defense in depth: tools validate during execution, callbacks validate before execution.

Let's add validation callbacks to our Merchant and Credentials Provider agents.

---

### Step 5A: Add Merchant Validation - Import Callback Types

First, let's add the imports needed for callbacks.

👉 **Open `charity_advisor/merchant_agent/agent.py`**

At the top of the file, after the existing imports, add:

```python
from typing import Optional
from datetime import datetime, timezone
from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content, Part
import logging

logger = logging.getLogger(__name__)
```

> aside positive
> **What (ADK Concept): CallbackContext**
>
> Callbacks receive a `CallbackContext` object containing:
> - `state`: The session state dictionary
> - Access to the invocation context
> - Methods for artifact handling
>
> This lets you validate prerequisites (like IntentMandate existence) before an agent runs.

---

### Step 5B: Build the Intent Validation Function

Now let's create a callback function that validates the IntentMandate before Merchant Agent runs.

👉 **In `charity_advisor/merchant_agent/agent.py`, add this function BEFORE the `merchant_agent = Agent(...)` definition:**

```python
def validate_intent_before_merchant(
    callback_context: CallbackContext,
) -> Optional[Content]:
    """
    Validates IntentMandate exists and hasn't expired before Merchant runs.
    
    This callback enforces that the Shopping Agent completed successfully
    before the Merchant Agent attempts to create a CartMandate.
    
    Returns:
        None: Allow Merchant Agent to proceed normally
        Content: Skip Merchant Agent and return error to user
    """
    state = callback_context.state
    
    # Check credential exists
    if "intent_mandate" not in state:
        logger.error("❌ IntentMandate missing - Shopping Agent may have failed")
        return Content(parts=[Part(text=(
            "Error: Cannot create cart. User intent was not properly recorded. "
            "Please restart the donation process."
        ))])
    
    intent_mandate = state["intent_mandate"]
    
    # Validate expiry (critical security check)
    try:
        expiry_time = datetime.fromisoformat(
            intent_mandate["intent_expiry"].replace('Z', '+00:00')
        )
        now = datetime.now(timezone.utc)
        
        if expiry_time < now:
            logger.error(f"❌ IntentMandate expired at {intent_mandate['intent_expiry']}")
            return Content(parts=[Part(text=(
                "Error: Your donation intent has expired. "
                "Please select a charity again to restart."
            ))])
        
        time_remaining = expiry_time - now
        logger.info(f"✓ IntentMandate validated. Expires in {time_remaining.total_seconds():.0f}s")
        
    except (KeyError, ValueError) as e:
        logger.error(f"❌ Invalid IntentMandate structure: {e}")
        return Content(parts=[Part(text=(
            "Error: Invalid intent data. Please restart the donation."
        ))])
    
    # All checks passed - allow Merchant Agent to proceed
    logger.info(f"✓ Prerequisites met for Merchant Agent: {intent_mandate['intent_id']}")
    return None
```

> aside positive
> **Understanding the Return Value**
>
> The callback's return value controls execution:
>
> **`return None`**: "Everything looks good, proceed normally"
> - Merchant Agent's LLM gets called
> - Tool execution happens
> - CartMandate gets created
>
> **`return Content(...)`**: "Stop! Don't run this agent."
> - Merchant Agent is **skipped entirely**
> - The Content you returned becomes the response
> - No LLM call, no wasted resources
>
> This is the core power of `before_agent_callback` - it can block execution based on your validation logic.

---

### Step 5C: Attach Callback to Merchant Agent

Now let's connect the callback to the agent.

👉 **In `charity_advisor/merchant_agent/agent.py`, modify the `merchant_agent = Agent(...)` definition:**

Find this line in the Agent definition:
```python
merchant_agent = Agent(
    name="MerchantAgent",
    model="gemini-2.5-flash",
    description="Creates formal, signed CartMandates for charity donations following W3C PaymentRequest standards.",
```

**Add this line right after the `description` line:**
```python
    before_agent_callback=validate_intent_before_merchant,
```

Your agent definition should now look like:
```python
merchant_agent = Agent(
    name="MerchantAgent",
    model="gemini-2.5-flash",
    description="Creates formal, signed CartMandates for charity donations following W3C PaymentRequest standards.",
    before_agent_callback=validate_intent_before_merchant,
    tools=[
        FunctionTool(func=create_cart_mandate)
    ],
    instruction="""..."""
)
```

---

### Step 6: Add Credentials Provider Validation (Optional Skip to Step 7)

Same pattern - let's add validation for the payment step.

---

### Step 6A: Import Callback Types

👉 **Open `charity_advisor/credentials_provider/agent.py`**

At the top of the file, after the existing imports, add:

```python
from typing import Optional
from datetime import datetime, timezone
from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content, Part
import logging

logger = logging.getLogger(__name__)
```

---

### Step 6B: Build Cart Validation Function

👉 **In `charity_advisor/credentials_provider/agent.py`, add this function BEFORE the `credentials_provider = Agent(...)` definition:**

```python
def validate_cart_before_payment(
    callback_context: CallbackContext,
) -> Optional[Content]:
    """
    Validates CartMandate exists and hasn't expired before payment processing.
    
    This callback enforces that the Merchant Agent completed successfully
    before the Credentials Provider attempts to process payment.
    
    Returns:
        None: Allow Credentials Provider to proceed
        Content: Skip payment processing and return error
    """
    state = callback_context.state
    
    # Check credential exists
    if "cart_mandate" not in state:
        logger.error("❌ CartMandate missing - Merchant Agent may have failed")
        return Content(parts=[Part(text=(
            "Error: Cannot process payment. Cart was not properly created. "
            "Please restart the donation process."
        ))])
    
    cart_mandate = state["cart_mandate"]
    
    # Validate AP2 structure
    if "contents" not in cart_mandate:
        logger.error("❌ CartMandate missing AP2 contents wrapper")
        return Content(parts=[Part(text=(
            "Error: Invalid cart structure. Please restart."
        ))])
    
    # Validate expiry
    try:
        contents = cart_mandate["contents"]
        expiry_time = datetime.fromisoformat(
            contents["cart_expiry"].replace('Z', '+00:00')
        )
        now = datetime.now(timezone.utc)
        
        if expiry_time < now:
            logger.error(f"❌ CartMandate expired at {contents['cart_expiry']}")
            return Content(parts=[Part(text=(
                "Error: Your cart has expired (15 minute limit). "
                "Please restart the donation to get a fresh offer."
            ))])
        
        time_remaining = expiry_time - now
        logger.info(f"✓ CartMandate validated. Expires in {time_remaining.total_seconds():.0f}s")
        
    except (KeyError, ValueError) as e:
        logger.error(f"❌ Invalid CartMandate structure: {e}")
        return Content(parts=[Part(text=(
            "Error: Invalid cart data. Please restart the donation."
        ))])
    
    # All checks passed - allow payment processing
    logger.info(f"✓ Prerequisites met for Credentials Provider: {contents['id']}")
    return None
```

---

### Step 6C: Attach Callback to Credentials Provider

👉 **In `charity_advisor/credentials_provider/agent.py`, modify the `credentials_provider = Agent(...)` definition:**

Find this line in the Agent definition:
```python
credentials_provider = Agent(
    name="CredentialsProvider",
    model="gemini-2.5-flash",
    description="Securely processes payments by creating PaymentMandates and executing transactions with user consent.",
```

**Add this line right after the `description` line:**
```python
    before_agent_callback=validate_cart_before_payment,
```

Your agent definition should now look like:
```python
credentials_provider = Agent(
    name="CredentialsProvider",
    model="gemini-2.5-flash",
    description="Securely processes payments by creating PaymentMandates and executing transactions with user consent.",
    before_agent_callback=validate_cart_before_payment,
    tools=[
        FunctionTool(func=create_payment_mandate)
    ],
    instruction="""..."""
)
```

---

### Step 7: Test with ADK Web UI

Now let's test the complete hardened system with validation callbacks active.

👉 **In your Cloud Shell terminal, run:**
```bash
adk web
```

You should see output like:
```
+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://localhost:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

> aside positive
> **What Just Happened?**
>
> `adk web` starts a local web server that:
> - Loads your `charity_advisor` agent
> - Creates a web UI for interaction
> - Provides trace visualization
> - Enables consent dialogs
>
> This is different from `adk run`:
> - `adk run`: Terminal-only, no consent UI
> - `adk web`: Full web interface with all features

👉 **Next, to access the ADK Web UI from your browser:**

From the **Web preview** icon (looks like an eye or a square with an arrow) in the Cloud Shell toolbar (usually top right), select **Change port**. In the pop-up window, set the port to **8000** and click **"Change and Preview"**. Cloud Shell will then open a new browser tab displaying the ADK Web UI.

![webpreview](img/07-03-cloud-shell-web-preview.png)

> aside positive
> **Troubleshooting Web Preview**
>
> If the preview doesn't open:
> - Check that port 8000 is correct (matches the ADK output)
> - Allow popups from Cloud Shell
> - Try clicking the preview icon again
> - Alternatively, use the URL directly: `https://8000-cs-PROJECT_ID.cloudshell.dev`

👉 **Select your agent from the dropdown:**

In the ADK Web UI, you'll see a dropdown menu at the top. Select **charity_advisor** from the list.

![agent-select](img/07-04-adk-web-agent-select.png)

You'll see the ADK web interface with:
- **Chat panel**: Left side, for conversation
- **Trace panel**: Right side, for observability (we'll use this in Module 9)

#### Test 1: Complete Donation Flow (Normal Case)

👉 **In the chat interface, type:**
```text
I want to donate to an education charity
```

Watch the complete flow unfold:

![adk web shopping agent](img/07-05-adk-web-shopping-agent.gif)

![adk web donation processing pipeline](img/07-06-adk-web-donation-processing-pipeline.gif)

**What's happening (visible in the trace panel on the right):**

**1. Advisor delegates to ShoppingAgent:**
- ShoppingAgent searches for education charities
- Shows you 3 verified options with details

**2. You interact with ShoppingAgent (may take multiple turns):**
```text
User: "Tell me more about Room to Read"
Shopping: [explains mission and impact]
User: "I'll donate $50 to Room to Read"
```

**3. ShoppingAgent creates IntentMandate:**
- Creates and signs the intent
- Returns confirmation with Intent ID

**4. Advisor transitions to processing phase:**
> Perfect! Processing your $50 donation to Room to Read...

**5. DonationProcessingPipeline activates:**
- **Merchant callback validates IntentMandate (✓ passed)** ← NEW!
- Merchant Agent creates CartMandate with signature
- **Credentials callback validates CartMandate (✓ passed)** ← NEW!
- Credentials Provider prepares payment

**6. Payment processes:**
- Credentials Provider creates PaymentMandate
- Simulates payment processing
- Returns transaction ID

**7. Advisor summarizes:**
> Perfect! Your donation has been processed successfully! 🎉
>
> **Details:**
> - Amount: $50.00
> - Charity: Room to Read (EIN: 77-0479905)
> - Transaction ID: txn_a3f7b2c8d9e1f4a2

---

#### Test 2: Verify Callbacks Catch Failures (Optional Advanced Test)

Want to see the callbacks in action catching errors? You'd need to manually corrupt state (advanced debugging), but in production, callbacks would catch:

- **Shopping Agent tool fails** → Merchant callback blocks: "Error: Cannot create cart..."
- **2 hours pass** → Merchant callback blocks: "Error: Intent expired..."
- **Cart expires** → Credentials callback blocks: "Error: Cart expired (15 min limit)..."

These edge cases are now **architecturally enforced** by your validation callbacks.

---

### What You Just Built

You've successfully orchestrated three specialized agents into a seamless, trustworthy system with architectural validation.

### What's Next

You've now completed the technical core of building trustworthy agents:

You've built a complete trustworthy system locally enforcing the credential chain. Now let's make it accessible to real users through production deployment—and enable the accountability trail that makes Module 9 possible.

**Let's deploy your hardened agent to Google Cloud.**

## Deployment

**Duration: 25 min**

![banner](img/08-01-banner.png)

Your trustworthy donation system is now complete with three specialized agents working locally:

But it only runs on your development machine. To make this system useful to real users—and to capture the accountability trails that prove trustworthiness—you need to deploy it to production.

This module walks you through deploying your agent to Google Cloud with **observability enabled from day one**. The `--trace_to_cloud` flag you'll use during deployment is what makes the accountability trail in Module 9 possible.

---

### Understanding Deployment Options

The ADK supports multiple deployment targets. Each has different characteristics for complexity, session management, scaling, and cost:

| Factor | Local (`adk web`) | Agent Engine | Cloud Run |
|--------|-------------------|--------------|-----------|
| **Complexity** | Minimal | Low | Medium |
| **Session Persistence** | In-memory only (lost on restart) | Vertex AI managed (automatic) | Cloud SQL (PostgreSQL) or in-memory |
| **Infrastructure** | None (dev machine only) | Fully managed | Container + optional database |
| **Cold Start** | N/A | 100-500ms | 100-2000ms |
| **Scaling** | Single instance | Automatic | Automatic (to zero) |
| **Cost Model** | Free (local compute) | Compute-based | Request-based + free tier |
| **UI Support** | Yes (built-in) | No (API only) | Yes (via `--with_ui` flag) |
| **Observability Setup** | Local trace viewer | Automatic with `--trace_to_cloud` | Requires `--trace_to_cloud` flag |
| **Best For** | Development & testing | Production agents | Production agents |

**Recommendation:** For this trustworthy donation system, we recommend **Agent Engine** as your primary production deployment because it provides:

- Fully managed infrastructure (no containers to manage)
- Built-in session persistence via `VertexAiSessionService`
- Automatic scaling without cold starts
- Simplified deployment (no Docker knowledge required)
- Cloud Trace integration out of the box

### Additional Option: Google Kubernetes Engine (GKE)

For advanced users requiring Kubernetes-level control, custom networking, or multi-service orchestration, **GKE deployment** is available. This option provides maximum flexibility but requires more operational expertise (cluster management, manifests, service accounts).

GKE deployment is not covered in this codelab but is fully documented in the [ADK GKE Deployment Guide](https://google.github.io/adk-docs/deploy/gke/).

### Prerequisites

#### 1. Google Cloud Project Setup

You need a Google Cloud project with billing enabled. If you don't have one:

1. Create a project: [Google Cloud Console](https://console.cloud.google.com/)
2. Enable billing: [Enable Billing](https://cloud.google.com/billing/docs/how-to/modify-project)
3. Note your **Project ID** (not the project name or number)

#### 2. Re-Authentication (Optional)

Authenticate with Google Cloud:
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with your actual Google Cloud project ID.

Verify your authentication:
```bash
gcloud config get-value project
# Should output: YOUR_PROJECT_ID
```

#### 3. Environment Variables

Use these commands to auto-populate your `.env` file:
```bash
# Get your current Project ID
PROJECT_ID=$(gcloud config get-value project)
STAGING_BUCKET_VALUE="gs://${PROJECT_ID}-staging"
ENV_FILE=".env"

# Check if STAGING_BUCKET is already set in the .env file
if grep -q "^STAGING_BUCKET=" "${ENV_FILE}"; then
  # If it exists, replace the line
  # The sed command finds the line starting with STAGING_BUCKET= and replaces the entire line.
  # Using | as a delimiter to avoid issues with slashes in the bucket name.
  sed -i "s|^STAGING_BUCKET=.*|STAGING_BUCKET=${STAGING_BUCKET_VALUE}|" "${ENV_FILE}"
  echo "Updated STAGING_BUCKET in ${ENV_FILE}"
else
  # If it doesn't exist, add it to the end of the file
  echo "STAGING_BUCKET=${STAGING_BUCKET_VALUE}" >> "${ENV_FILE}"
  echo "Added STAGING_BUCKET to ${ENV_FILE}"
fi

# Verify it was added or updated correctly
echo "Current STAGING_BUCKET setting:"
grep "^STAGING_BUCKET=" "${ENV_FILE}"
```

You should see:
```
STAGING_BUCKET=gs://your-actual-project-id-staging
```

**Important notes:**

- Replace `YOUR_PROJECT_ID` with your actual project ID (or use the commands above)
- For `GOOGLE_CLOUD_LOCATION`, use a [supported region](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#available-regions)
- **The staging bucket will be created automatically if it doesn't exist** when you run the deployment script

#### 4. Enable Required APIs

The deployment process needs several Google Cloud APIs enabled. Run this command to enable them:
```bash
gcloud services enable \
    aiplatform.googleapis.com \
    storage.googleapis.com \
    cloudbuild.googleapis.com \
    cloudtrace.googleapis.com \
    compute.googleapis.com
```

This command enables:
- **AI Platform API** - For Agent Engine and Vertex AI models
- **Cloud Storage API** - For staging bucket
- **Cloud Build API** - For container building (Cloud Run)
- **Cloud Trace API** - For observability and accountability trails
- **Compute Engine API** - For service account management

---

### Step 1: Understand the Deployment Infrastructure

Your project includes a unified deployment script (`deploy.sh`) that handles all deployment modes.

👉 **Review the deployment script (optional):**
```bash
cat deploy.sh
```

The script provides three deployment modes:
- `./deploy.sh local` - Run locally with in-memory storage
- `./deploy.sh agent-engine` - Deploy to Vertex AI Agent Engine (recommended)
- `./deploy.sh cloud-run` - Deploy to Cloud Run with optional UI

**How it works under the hood:**

For Agent Engine deployment, the script executes:
```bash
adk deploy agent_engine \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --staging_bucket=$STAGING_BUCKET \
  --display_name="Charity Advisor" \
  --trace_to_cloud \
  charity_advisor
```

For Cloud Run deployment, it executes:
```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name="charity-advisor" \
  --app_name="charity_advisor" \
  --with_ui \
  --trace_to_cloud \
  charity_advisor
```

The `--trace_to_cloud` flag is critical for both deployment types—it enables Cloud Trace integration for the accountability trail you'll explore in Module 9.

---

### Step 2: Prepare the Agent Engine Wrapper

Agent Engine requires a specific entry point that wraps your agent for the managed runtime. This file has been created for you.

👉 **Review `charity_advisor/agent_engine_app.py`:**
```python
"""Agent Engine application wrapper.

This file prepares the Charity Advisor agent for deployment to Vertex AI Agent Engine.
"""

from vertexai import agent_engines
from .agent import root_agent

# Wrap the agent in an AdkApp object for Agent Engine deployment
app = agent_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,  # Enables Cloud Trace integration automatically
)
```

**Why this file is needed:**

- Agent Engine requires the agent wrapped in an `AdkApp` object
- The `enable_tracing=True` parameter enables Cloud Trace integration automatically
- This wrapper is referenced by the ADK CLI during deployment
- It configures `VertexAiSessionService` for automatic session persistence

---

### Step 3: Deploy to Agent Engine (RECOMMENDED)

Agent Engine is the **recommended production deployment** for your trustworthy donation system because it provides fully managed infrastructure with built-in session persistence.

#### Run the Deployment

From your project root:
```bash
chmod +x deploy.sh
./deploy.sh agent-engine
```

#### Deployment Phases

Watch the script execute these phases:
```
Phase 1: API Enablement
  ✓ aiplatform.googleapis.com
  ✓ storage.googleapis.com
  ✓ cloudbuild.googleapis.com
  ✓ cloudtrace.googleapis.com
  ✓ compute.googleapis.com

Phase 2: IAM Setup
  ✓ Getting project number
  ✓ Granting Storage Object Admin
  ✓ Granting Vertex AI User
  ✓ Granting Cloud Trace Agent

Phase 3: Staging Bucket
  ✓ Creating gs://your-project-id-staging (if needed)
  ✓ Setting permissions

Phase 4: Validation
  ✓ Checking agent.py exists
  ✓ Verifying root_agent defined
  ✓ Checking agent_engine_app.py exists
  ✓ Validating requirements.txt

Phase 5: Build & Deploy
  ✓ Packaging agent code
  ✓ Uploading to staging bucket
  ✓ Creating Agent Engine instance
  ✓ Configuring session persistence
  ✓ Setting up Cloud Trace integration
  ✓ Running health checks
```

This process takes **5-10 minutes** as it packages the agent and deploys it to Vertex AI infrastructure.

#### Save Your Agent Engine ID

Upon successful deployment:
```
✅ Agent Engine created successfully!

   Agent Engine ID: 7917477678498709504
   Resource Name: projects/123456789/locations/us-central1/reasoningEngines/7917477678498709504
   Endpoint: https://us-central1-aiplatform.googleapis.com/v1/...

   ⚠️  IMPORTANT: Save the Agent Engine ID from the output above
   Add it to your .env file as:
   AGENT_ENGINE_ID=7917477678498709504

   This ID is required for:
   - Testing the deployed agent
   - Updating the deployment later
   - Accessing logs and traces
```

**Update your .env file immediately:**
```bash
echo "AGENT_ENGINE_ID=7917477678498709504" >> .env
```

#### What Was Deployed

Your Agent Engine deployment now includes:

✅ **All three agents** (Shopping, Merchant, Credentials) running in managed runtime  
✅ **Complete credential chain** logic (Intent → Cart → Payment mandates)  
✅ **User consent mechanism** with confirmation workflow  
✅ **Automatic session persistence** via VertexAiSessionService  
✅ **Auto-scaling** infrastructure managed by Google  
✅ **Cloud Trace integration** for complete observability

---

### Step 4: Test Your Deployed Agent

#### Update Your Environment

Verify your `.env` includes the Agent Engine ID:
```bash
AGENT_ENGINE_ID=7917477678498709504  # From deployment output
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
STAGING_BUCKET=gs://your-project-id-staging
```

#### Run the Test Script

Your project includes a test script specifically for Agent Engine deployments.

👉 **Run the test:**
```bash
python scripts/test_deployed_agent.py
```

#### Expected Output
```
Testing Agent Engine deployment...
Project: your-project-id
Location: us-central1
Agent Engine ID: 7917477678498709504
Endpoint: https://us-central1-aiplatform.googleapis.com/v1/...

Creating session...
✓ Session created: 4857885913439920384

Sending donation query...
✓ Response received:
  Event 1: I'll help you donate $50 to a children's education charity...
  Event 2: Here are some highly-rated children's education charities...
  Event 3: Which charity would you like to support?...

✅ Test completed successfully!

Session ID: 4857885913439920384

This donation generated a trace in Cloud Trace.
View it in Module 9: Observability

To view traces:
https://console.cloud.google.com/traces/list?project=your-project-id
```

#### Verification Checklist

After testing, verify:

✅ Agent responds to queries  
✅ All three agents execute in sequence (Shopping → Merchant → Credentials)  
✅ Consent mechanism activates (confirmation requested)  
✅ Session persists across requests  
✅ No authentication errors  
✅ No connection timeouts

**If you encounter errors:**
- Check your environment variables are set correctly
- Verify APIs are enabled: `gcloud services list --enabled`
- Check Agent Engine logs in [Vertex AI Console](https://console.cloud.google.com/vertex-ai/agent-engines)
- Verify the `agent_engine_app.py` file exists in your `charity_advisor` folder

---

### Step 5: Deploy to Cloud Run (Optional)

While Agent Engine is recommended for streamlined production deployment, Cloud Run offers more control and supports the ADK web UI. This section is optional.

#### When to Use Cloud Run

Choose Cloud Run if you need:

- The ADK web UI for user interaction
- Full control over the container environment
- Custom database configurations
- Integration with existing Cloud Run services

#### Run the Deployment
```bash
chmod +x deploy.sh
./deploy.sh cloud-run
```

**What's different:**

The script will automatically:
- Build a Docker container with your agent code
- Create a Cloud SQL PostgreSQL database (if needed)
- Configure the database connection
- Deploy with the ADK web UI enabled

The deployment takes **10-15 minutes** due to Cloud SQL provisioning.

**Session Management:**
- Uses `DatabaseSessionService` instead of `VertexAiSessionService`
- Requires database credentials in `.env` (or auto-generated)
- State persists in PostgreSQL database

**UI Support:**
- Web UI available at: `https://charity-advisor-xyz.a.run.app`

#### Testing Cloud Run Deployment

If you deployed to Cloud Run with `--with_ui`, you can test directly in your browser:

1. **Navigate to your Service URL** (provided in deployment output)

2. **You'll see the ADK web interface.** Select your agent from the dropdown.

3. **Start a test donation:**
```
   I want to donate $50 to a children's education charity
```

4. **Observe the execution flow:**
   - ShoppingAgent finds charities and saves your intent
   - MerchantAgent creates the cart mandate
   - CredentialsProvider creates payment mandate and requests confirmation
   - After you confirm, payment is processed

5. **Verify the response includes:**
   - Charity recommendations
   - Confirmation request
   - Success message after approval

---

### Troubleshooting

#### Common Issues

**Issue:** `ERROR: GOOGLE_CLOUD_PROJECT is not set`

**Solution:** Ensure your `.env` file has the correct project ID:
```bash
GOOGLE_CLOUD_PROJECT=your-actual-project-id
```

---

**Issue:** Staging bucket not created automatically

**Solution:** The script should create the bucket automatically. If not, create it manually:
```bash
gsutil mb -p $GOOGLE_CLOUD_PROJECT -l $GOOGLE_CLOUD_LOCATION $STAGING_BUCKET
```

---

### Summary

You've successfully:

✅ Understood the deployment infrastructure provided by `deploy.sh`  
✅ Reviewed the Agent Engine wrapper configuration  
✅ Deployed your trustworthy donation system to Agent Engine (recommended)  
✅ Enabled Cloud Trace integration with `--trace_to_cloud`  
✅ Verified the agent is accessible and functional  
✅ Created the foundation for accountability trails in Module 9

In the next module, you'll see exactly what this flag unlocks: complete visibility into every donation, every consent moment, and every step of the credential chain.

## Observability

**Duration: 25 min**

![banner](img/09-01-banner.png)

![graph trace](img/09-02-graph-trace.png)

In Module 1, you learned about a fundamental problem: when an AI agent handles money, **how do you prove what happened?** 

A user could claim:
- "I never chose that charity!"
- "I didn't authorize that payment!"
- "The system charged me without my consent!"

In a traditional black-box AI system, you'd have no way to prove otherwise. But your trustworthy donation system is different. In Module 8, you deployed with the `--trace_to_cloud` flag, which means **every donation now creates a complete, tamper-evident audit trail in Cloud Trace**.

This module teaches you to read those traces and use them as evidence. You'll learn to:

- Navigate Cloud Trace Explorer to find production traces
- Read the waterfall view to understand execution flow
- Find the credential chain (Intent → Cart → Payment mandates)
- Locate consent moments with timestamp proof
- Use traces for dispute resolution
- Export traces for compliance and audits

This is what separates trustworthy systems from capable-but-opaque ones: **the ability to prove what happened with forensic precision**.

---

### Understanding Traces and Spans

Before viewing traces in Cloud Trace, you need to understand what you're looking at.

#### What is a Trace?

A **trace** is the complete timeline of your agent handling a single request. It captures everything from when a user sends a query until the final response is delivered.

Each trace shows:
- Total duration of the request
- All operations that executed
- How operations relate to each other (parent-child relationships)
- When each operation started and ended
- Success or failure status

**For your charity agent:** One trace = one complete donation flow from "I want to donate" to "Payment successful."

#### What is a Span?

A **span** represents a single unit of work within a trace. Think of spans as the building blocks of a trace.

Common span types in your donation system:

| Span Type | What It Represents | Example |
|-----------|-------------------|---------|
| `agent_run` | Execution of an agent | `ShoppingAgent.run`, `MerchantAgent.run` |
| `call_llm` | Request to a language model | `gemini-2.5-flash` request for charity selection |
| `execute_tool` | Tool function execution | `find_charities`, `create_payment_mandate` |
| `state_read` | Reading from session memory | Retrieving `intent_mandate` from state |
| `state_write` | Writing to session memory | Storing `cart_mandate` in state |

Each span contains:
- **Name:** What operation this represents
- **Duration:** How long it took (start time → end time)
- **Attributes:** Metadata like tool inputs, model responses, token counts
- **Status:** Success (`OK`) or error (`ERROR`)
- **Parent-child relationships:** Which operations triggered which

#### How Spans Form a Trace

Spans nest inside each other to show causation:

```
Root Span: CharityAdvisor.run (entire request)
  └─ Child: DonationPipeline.run (sequential workflow)
      ├─ Child: ShoppingAgent.run
      │   ├─ Grandchild: call_llm (Gemini processes charity search)
      │   ├─ Grandchild: execute_tool (find_charities)
      │   └─ Grandchild: execute_tool (save_user_choice)
      ├─ Child: MerchantAgent.run
      │   ├─ Grandchild: call_llm (Gemini generates cart)
      │   └─ Grandchild: execute_tool (create_cart_mandate)
      └─ Child: CredentialsProvider.run
          ├─ Grandchild: call_llm (Gemini processes payment)
          └─ Grandchild: execute_tool (create_payment_mandate) [CONSENT!]
```

This hierarchy shows **exactly what happened and in what order**. You can see that the payment mandate was created *after* the cart mandate, which was *after* the user selected a charity.

### Step 1: Access Cloud Trace Explorer

Now let's view the actual traces from your deployed agent.

#### Navigate to Cloud Trace

1. **Open the Google Cloud Console:** [console.cloud.google.com](https://console.cloud.google.com)

2. **Select your project** from the dropdown at the top (should be pre-selected if you've been working in it)

3. **Navigate to Cloud Trace Explorer:**
   - In the left sidebar, scroll to **Observability** section
   - Click **Trace**
   - Or use direct link: [console.cloud.google.com/traces/list](https://console.cloud.google.com/traces/list)

#### What You're Looking At

The Trace Explorer shows a list of all traces from your project:

| Column | What It Shows |
|--------|---------------|
| **Request** | HTTP method and endpoint (for API requests) |
| **Start Time** | When the request began |
| **Latency** | Total duration of the request |
| **Spans** | Number of operations in the trace |

Each row represents **one complete request** to your deployed agent.

#### Generate Test Traces (If Needed)

If you don't see any traces yet, the list might be empty because:
- No requests have been made to your deployed agent yet
- Traces take 1-2 minutes to appear after a request

**Generate a test trace:**

If you deployed to **Cloud Run with UI**, visit your service URL and complete a donation in the browser.

If you deployed to **Agent Engine**, run the test script from Module 8:

```bash
python scripts/test_deployed_agent.py
```

Wait **1-2 minutes**, then refresh the Cloud Trace Explorer page. You should now see traces.

#### Filter Traces

Use the filter options at the top to find specific traces:

- **Time range:** Change from "Last hour" to "Last 24 hours" if needed
- **Min latency / Max latency:** Filter for slow requests
- **Request filter:** Search by specific operations (e.g., "DonationPipeline")

For this module, focus on traces with **longer durations** (>5 seconds), as these represent complete donation flows with all three agents executing.

---

### Step 2: Examine a Complete Donation Flow

Click on any trace in the list to open the **waterfall view**. This is where you'll spend most of your time analyzing agent behavior.

#### Understanding the Waterfall View

The waterfall view is a Gantt chart showing the complete execution timeline:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              Timeline (horizontal = time) →
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

invocation                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 8.2s
  agent_run: CharityAdvisor          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 8.1s
    agent_run: DonationPipeline      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 7.9s
      agent_run: ShoppingAgent       ▓▓▓▓▓▓ 2.1s
        call_llm: gemini-2.5-flash   ▓▓▓▓ 1.2s
        execute_tool: find_charities ▓▓ 0.5s
        execute_tool: save_user_choice ▓ 0.3s
      agent_run: MerchantAgent       ▓▓▓ 1.8s
        call_llm: gemini-2.5-flash   ▓▓ 0.9s
        execute_tool: create_cart_mandate ▓ 0.7s
      agent_run: CredentialsProvider ▓▓▓▓▓▓▓▓ 4.0s
        call_llm: gemini-2.5-flash   ▓▓ 0.8s
        execute_tool: create_payment_mandate ▓▓▓▓▓ 3.0s [CONSENT]
```

#### Reading the Chart

**Each bar represents a span:**
- **Horizontal position:** When it started
- **Length:** How long it took
- **Indentation:** Shows parent-child relationships
- **Color:** Typically blue for normal, red for errors

**Key observations from this example trace:**

✅ **Total duration:** 8.2 seconds  
✅ **Sequential execution:** ShoppingAgent completed *before* MerchantAgent started  
✅ **MerchantAgent completed *before* CredentialsProvider started**  
✅ **Consent was the longest operation:** 3.0 seconds for `create_payment_mandate` (because it waited for user confirmation)  
✅ **LLM calls are visible:** Each agent made one Gemini request  
✅ **Tool calls are captured:** All six tools executed successfully

This visual immediately shows you **where time is spent** and **what order operations executed in**.

#### Click on a Span for Details

Click on the `invocation` span (the root span at the top). In the right panel, you'll see detailed attributes:

```json
{
  "http.method": "POST",
  "http.status_code": 200,
  "http.url": "https://charity-advisor-xyz.a.run.app/api/run",
  "user_id": "test_user_123",
  "session_id": "4857885913439920384",
  "trace_id": "a1b2c3d4e5f6...",
  "span_id": "1234567890abcdef"
}
```

These attributes provide context about the entire request.

---

### Step 3: Find the Credential Chain

Your trustworthy system uses a **credential chain** to prove authorization at each step:

```
IntentMandate (User chose charity)
    ↓
CartMandate (Merchant created cart, signed IntentMandate)
    ↓
PaymentMandate (Payment provider created payment, signed CartMandate)
```

Let's find each mandate in the trace.

#### Finding the IntentMandate

Click on the **`execute_tool: save_user_choice`** span (under ShoppingAgent).

In the attributes panel, you'll see:

```json
{
  "tool.name": "save_user_choice",
  "tool.input.charity_name": "Save the Children",
  "tool.input.amount": 50,
  "tool.output.status": "success",
  "tool.output.intent_mandate": {
    "charity_name": "Save the Children",
    "amount": 50,
    "timestamp": "2024-11-08T15:30:12.345Z",
    "signature": "a3f7b9c1d2e4..."
  }
}
```

**This proves:**
- ✅ User selected "Save the Children"
- ✅ Amount was $50
- ✅ Choice was recorded at 15:30:12 UTC
- ✅ Signature was generated (in production, this would be cryptographic)

The IntentMandate is now in session state and available to subsequent agents.

#### Finding the CartMandate

Click on the **`execute_tool: create_cart_mandate`** span (under MerchantAgent).

In the attributes panel:

```json
{
  "tool.name": "create_cart_mandate",
  "tool.input.intent_mandate": {
    "charity_name": "Save the Children",
    "amount": 50,
    "signature": "a3f7b9c1d2e4..."
  },
  "tool.output.status": "success",
  "tool.output.cart_mandate": {
    "cart_id": "cart_7893",
    "intent_signature": "a3f7b9c1d2e4...",
    "cart_signature": "e8f2a9b3c7d1...",
    "timestamp": "2024-11-08T15:30:14.789Z"
  }
}
```

**This proves:**
- ✅ MerchantAgent received the IntentMandate (input shows it)
- ✅ Cart was created with ID "cart_7893"
- ✅ Cart signature references the IntentMandate signature (chain link!)
- ✅ Created at 15:30:14 UTC (2.4 seconds after intent)

The CartMandate now references the IntentMandate, forming the chain.

#### Finding the PaymentMandate

Click on the **`execute_tool: create_payment_mandate`** span (under CredentialsProvider).

In the attributes panel:

```json
{
  "tool.name": "create_payment_mandate",
  "tool.input.cart_mandate": {
    "cart_id": "cart_7893",
    "intent_signature": "a3f7b9c1d2e4...",
    "cart_signature": "e8f2a9b3c7d1..."
  },
  "tool.confirmation_required": true,
  "tool.confirmation_timestamp": "2024-11-08T15:30:17.891Z",
  "tool.user_response": "CONFIRMED",
  "tool.wait_duration_ms": 29168,
  "tool.output.status": "success",
  "tool.output.payment_mandate": {
    "payment_id": "pay_9821",
    "cart_signature": "e8f2a9b3c7d1...",
    "payment_signature": "b4c9e2a7f8d3...",
    "timestamp": "2024-11-08T15:30:47.059Z"
  }
}
```

**This proves the complete chain:**
- ✅ CredentialsProvider received the CartMandate (input shows it)
- ✅ Payment references the CartMandate signature (chain link!)
- ✅ **Confirmation was required** (`confirmation_required: true`)
- ✅ **User confirmed at 15:30:17 UTC**
- ✅ **System waited 29.2 seconds** for user decision
- ✅ Payment was created after confirmation (timestamp: 15:30:47)

#### Visualizing the Chain

The trace proves the credential chain executed correctly:

```
15:30:12 UTC → IntentMandate created (signature: a3f7...)
                  ↓
15:30:14 UTC → CartMandate created (references: a3f7...)
                  ↓
15:30:17 UTC → User consent requested
                  ↓
15:30:47 UTC → PaymentMandate created (references: e8f2...)
```

Each mandate references the signature of the previous one. This is **tamper-evident** - you can verify the chain by checking that signatures match.

---

### Step 4: Analyzing Performance and Bottlenecks

Cloud Trace doesn't just prove what happened—it shows you **where time is spent** so you can optimize.

#### Identify the Critical Path

In the waterfall view, look for the **longest spans** in the vertical stack. These represent your performance bottlenecks.

From our example trace:

```
Total: 8.2 seconds

Breakdown:
  - ShoppingAgent:         2.1s (26%)
  - MerchantAgent:         1.8s (22%)
  - CredentialsProvider:   4.0s (49%)  ← Bottleneck
  - Other overhead:        0.3s (3%)
```

**Critical insight:** CredentialsProvider accounts for 49% of total time. Why?

Drill into the CredentialsProvider span:
```
CredentialsProvider: 4.0s
  - call_llm:              0.8s (20%)
  - create_payment_mandate: 3.0s (75%)  ← User consent wait
  - Other:                 0.2s (5%)
```

**The 3.0-second delay is expected and good** - it's the user deliberating before confirming. This is not a performance problem; it's proof of thoughtful consent.

#### Tracking LLM Costs

Click on any **`call_llm`** span to see token usage:

```json
{
  "llm.model": "gemini-2.5-flash",
  "llm.usage.prompt_tokens": 487,
  "llm.usage.completion_tokens": 156,
  "llm.usage.total_tokens": 643,
  "llm.response_time_ms": 1243
}
```

**Use this to:**
- Track cost per request (tokens × model pricing)
- Identify unnecessarily long prompts
- Compare model performance (Flash vs Pro)
- Optimize for latency vs. quality

**Example calculation:**
```
Gemini 2.5 Flash pricing (as of Nov 2024):
  Input:  $0.075 per 1M tokens
  Output: $0.30 per 1M tokens

This request:
  Input:  487 tokens × $0.075 / 1M = $0.000037
  Output: 156 tokens × $0.30 / 1M  = $0.000047
  Total:                            = $0.000084 (~$0.00008)

For 10,000 donations/month:
  10,000 × 3 agents × $0.00008 = $2.40/month in LLM costs
```

This granular visibility helps you make data-driven decisions about model selection.

#### Comparing Across Traces

Filter for multiple traces and compare durations:

```
Trace 1: 8.2s  (with consent wait: 3.0s)
Trace 2: 12.5s (with consent wait: 7.8s)  ← User took longer
Trace 3: 5.1s  (with consent wait: 0.2s)  ← User clicked fast
Trace 4: 6.3s  (with consent wait: 1.5s)
```

**Insight:** Most variation comes from user decision time, not system performance. The core agent execution (minus consent) is consistent at ~5 seconds.

This tells you the system is performing reliably.

---

For production systems, set up alerts to catch issues before users complain.

#### Alert on High Error Rates

Create an alert when >5% of traces contain errors:

1. Navigate to [Cloud Monitoring](https://console.cloud.google.com/monitoring)
2. Click **"Alerting"** → **"Create Policy"**
3. Configure:
   ```
   Resource: Cloud Trace Span
   Metric: Span error count
   Condition: Rate > 5% over 5 minutes
   Notification: Email your-team@example.com
   ```

#### Alert on High Latency

Create an alert when p95 latency exceeds 15 seconds:

```
Resource: Cloud Trace
Metric: Span duration (95th percentile)
Condition: > 15000ms for 5 minutes
Notification: PagerDuty
```

This catches performance degradation before it impacts user experience.

#### Alert on Missing Consent

Create an alert if any payment processes without confirmation:

```
Resource: Cloud Trace Span
Filter: tool.name="create_payment_mandate" AND tool.confirmation_required!=true
Condition: Any match
Notification: Critical alert to security team
```

This is a **safety violation detector** - if it fires, something is very wrong with your consent mechanism.

---

### What You've Learned

Through Cloud Trace, you now understand how to:

✅ **Navigate Cloud Trace Explorer** to find production traces  
✅ **Read waterfall views** to see complete execution flow  
✅ **Trace the credential chain** through IntentMandate → CartMandate → PaymentMandate 
✅ **Use traces as evidence** for dispute resolution  
✅ **Analyze performance** to identify bottlenecks  
✅ **Track LLM costs** at a granular level

### The Difference This Makes

Compare two systems handling the same "I never authorized this!" complaint:

#### System Without Observability

```
User: "I never authorized that $50 donation!"
You:  "Our logs show the transaction completed successfully."
User: "But I didn't approve it!"
You:  "The system requires confirmation before processing."
User: "I never saw any confirmation!"
You:  "..." [no way to prove what happened]

Result: Refund issued, trust lost, user never returns.
```

#### System With Cloud Trace

```
User: "I never authorized that $50 donation!"
You:  "Let me pull up the trace from your session..."
      [Shows waterfall with consent span]
You:  "Here's the evidence:
       - 15:30:17 UTC: System asked for confirmation
       - Message shown: 'You are about to donate $50...'
       - 15:30:47 UTC: You clicked 'CONFIRM'
       - Wait time: 29.2 seconds
       
       The system waited almost 30 seconds for your decision.
       Here's the exact timestamp of your confirmation."
       
User: "Oh... I remember now. My mistake. Sorry!"

Result: Trust preserved, no refund needed, user continues using service.
```

**This is the power of accountability trails.** You move from "trust us" to "let us show you exactly what happened."

---

### What's Next

You've now completed the technical core of building trustworthy agents:

✅ **Module 1-6:** Designed a trustworthy architecture (roles, credentials, consent)  
✅ **Module 7:** Orchestrated complex workflows (SequentialAgent)  
✅ **Module 8:** Deployed with observability enabled  
✅ **Module 9:** Learned to read and use accountability trails

The architecture you've built—role separation, credential chains, consent mechanisms, complete observability—transfers directly to production systems handling real money, real data, and real consequences.

## Your Journey Forward
**Duration: 10 min**

### What You've Built

You started this workshop with a question: *"How do I build AI agents I can actually trust with money?"*

You now have the answer.

**Where you started (Module 3):**
```python
simple_agent = Agent(
    model="gemini-2.5-flash",
    instruction="Find charities and donate",
    tools=[google_search]
)
```

**Where you are now (Module 10):**

*   ✅ Three specialized agents with role separation  
*   ✅ Three verifiable credentials (Intent → Cart → Payment mandates)  
*   ✅ Complete credential chain with expiry validation at each step  
*   ✅ Explicit consent mechanism with timestamp proof  
*   ✅ Production deployment to Agent Engine with observability  
*   ✅ Complete accountability trail in Cloud Trace  
*   ✅ Forensic evidence for dispute resolution

---

### Workshop vs. Production: The Gap

Your system demonstrates the correct **architecture and patterns**, but uses educational simplifications that must be upgraded for real money and real users.

Here's exactly what was simplified and what production requires:

| Component | Workshop Implementation | Production Requirements |
|-----------|------------------------|------------------------|
| **Signatures** | SHA-256 hashes (`SIG_abc123`) for demonstration | Real cryptographic signatures using PKI or JWT with private keys |
| **Payment Processing** | Simulated returns (`simulation: True` flag) | Integration with real payment APIs (Stripe, PayPal, Square) |
| **User Authentication** | Implicit trust (no login required) | OAuth 2.0, WebAuthn, or session management |
| **Secrets Management** | Environment variables in `.env` file | Google Secret Manager or Cloud KMS with encryption |
| **Charity Database** | Mock JSON file with 9 charities | Live API integration (IRS Tax Exempt Organization Search, Charity Navigator API) |
| **Error Handling** | Basic try-catch with error messages | Retry logic with exponential backoff, circuit breakers, dead letter queues |
| **Testing** | Manual verification via scripts | Comprehensive unit/integration/E2E test suite with CI/CD |
| **Session Persistence** | In-memory (local) or automatic (Agent Engine) | Production database with backups and disaster recovery |
| **Rate Limiting** | None (educational environment) | Rate limits per user, IP-based throttling, abuse detection |

> aside positive
> **Why These Simplifications Were Necessary**
>
> Each simplification served a pedagogical purpose:
> - SHA-256 hashes let you focus on the credential chain concept without cryptography complexity
> - Simulated payments let you test the full flow without payment gateway accounts
> - Mock database let you see patterns without API key setup
>
> The **architecture** you learned—role separation, verifiable credentials, consent with proof—is production-ready. The **implementations** need upgrading.

---

### Key Architectural Patterns You Mastered

The patterns you learned in this workshop **are production patterns**. Don't doubt them.

#### Role Separation (AP2 Principle #1)
Each agent has ONE clear job and sees ONLY what it needs. If one agent is compromised, the attacker cannot access other agents' data. This limits the blast radius.

**Production systems using this:** Payment processing, document workflows, approval chains, multi-step forms with validation gates.

#### Verifiable Credentials (AP2 Principle #2)
Each credential has expiry time, references the previous credential, and requires validation before the next step. This creates a tamper-evident audit chain.

**Production value:** Complete proof of what happened, when, and in what order. Essential for dispute resolution and regulatory compliance.

#### Explicit Consent (AP2 Principle #3)
Timestamp proof that user approved action. Cannot be disputed.

**Production value:** Legal requirement for financial transactions. Protects both user and company.

#### Sequential Orchestration (ADK Pattern)
Enforces correct execution order. Prevents skipping steps. Guarantees each agent sees previous agent's output.

**Production value:** Perfect for human-in-the-loop systems where users expect immediate results. This is the right pattern for donation flows, checkout processes, and approval chains.

#### Complete Observability (OpenTelemetry + Cloud Trace)
Every decision, tool call, consent moment, and credential handoff captured automatically.

**Production value:** Forensic evidence for disputes. Performance optimization data. Compliance audit trails. Debug production issues with precision.

---

### Resources for Continued Learning

**ADK Documentation:**
- [Agent Development Kit Official Docs](https://google.github.io/adk-docs/)
- [Advanced Patterns and Examples](https://github.com/google/adk-samples/)

**AP2 & Related Standards:**
- [AP2 Docs](https://ap2-protocol.org)
- [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model/)
- [W3C PaymentRequest API](https://www.w3.org/TR/payment-request/)

**Google Cloud Services:**
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Cloud Trace](https://cloud.google.com/trace/docs)
- [Secret Manager](https://cloud.google.com/secret-manager/docs)
- [Cloud Run](https://cloud.google.com/run/docs)

---

### Cleanup Resources

To avoid ongoing charges, delete your deployment:

**Agent Engine:**
Follow steps in the Agent Engine [docs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/overview)

**Cloud Run (if deployed):**
```bash
gcloud run services delete charity-advisor \
    --region=$GOOGLE_CLOUD_LOCATION
```

**Storage Buckets:**
```bash
gsutil -m rm -r gs://$GOOGLE_CLOUD_PROJECT-staging
gsutil -m rm -r gs://$GOOGLE_CLOUD_PROJECT-artifacts
```

---

### Your Journey Continues

You started with a simple question and built a complete answer. You've mastered the foundational patterns for trustworthy AI agents. These patterns transfer to any domain where AI agents handle sensitive operations—financial transactions, healthcare decisions, legal documents, supply chain operations.

**The principles transfer. The trust model works.**

**Now go build something trustworthy!** ❤️

![banner](img/10-01-banner.png)