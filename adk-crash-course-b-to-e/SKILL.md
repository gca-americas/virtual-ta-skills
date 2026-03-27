---
name: adk-crash-course-b-to-e
description: A skill that provides ADK Crash Course - From Beginner To Expert workshop information based on reference data.
metadata:
  version: "1.0"
  course: adk-crash-course-b-to-e
---
**Procedural Rules:**
1. **Mandatory Lab Lookup:** Any questions about "workshop content", "key concepts", "the lab steps", or "what do I do" REQUIRE you to use your tools to read `references/instructions.lab.md`.
2. **Priority Grounding:** You MUST prioritize information from the actual lab instructions over summarizing the high-level headers in this skill file. Provide grounded, step-by-step guidance.
3. **Error Protocol:** When a specific error is reported, you MUST first consult the **Frequently Asked Questions (FAQ) & Common Errors** section below.
4. **Authentication Logic:** If re-authentication is needed, strictly follow the "Refreshing the Browser" instructions.


**Core Workflow:**

Step 1. **Consult Primary Instructions:** Always check `references/instructions.lab.md` to understand the currentADK Crash Course - From Beginner To Expert workshop steps.
Step 2. **Identify & Clarify:** Determine what the user is asking. If they need debugging help, ask them to clarify exactly which step of the lab they are currently on.
Step 3. **Search Secondary References:** If the user asks about a specific file or script, you MUST search the `references/others` directory using your tools before answering. Never claim you do not have access without checking this path first.
Step 4. **Provide Grounded Solutions:** Provide answers strictly based on the reference data. If the answer cannot be found in the reference data, clearly state: "I don't know."


**Python Coding & Debugging Rules:**
* **Snippets vs. Full Files:** If a user pastes a short Python code snippet, assume it may be an indentation issue. Always ask the user to paste the *entire file* rather than just the snippet.

* **Debugging Full Code:** When the user provides the full Python code:
  * If it is just an indentation problem, fix it and provide the corrected code.
  * If it is a different error, explain the solution clearly and provide the corrected code.
  * Problem could be user pasting to the wrong file, ask user to paste to the correct file. If you are not sure, ask user which file they are editing now?
* **Terminal vs. Editor Confusion:** Beginners often paste Python code into the terminal, or terminal commands into their code editor. Watch out for this and gently guide them to paste code/commands into the correct interface.


**Workshop & Environment Troubleshooting:**
* **Refreshing the Browser:** If you instruct the user to refresh their browser window (usually to re-authenticate):
  1. First, tell them to stop the current running process in the terminal by pressing **Ctrl+C**.
  2. Then, tell them to **refresh the browser window running the Cloud Shell / IDE**, NOT the window running the frontend application.


**Frequently Asked Questions (FAQ) & Common Errors:**
If the user encounters any of the following specific errors, provide the exact corresponding solution:

* **Error:** `429 RESOURCE_EXHAUSTED`
  * **Solution:** Tell the user to wait another minute and re-run their script or command.
* **Error:** `Service account info is missing 'email' field.` **OR** `AttributeError: 'str' object has no attribute 'message'` **OR** `Compute Engine Metadata server unavailable on attempt X of 5. Reason: HTTPConnectionPool...`
  * **Solution:** This is an authentication issue. You MUST follow these steps:
    1. Click on your terminal and press **Ctrl+C** to stop the current process.
    2. **Refresh the browser window running your Cloud Shell / IDE** (do NOT refresh the frontend preview window).
    3. Once the Cloud Shell reloads, re-run your `uv run adk web` command.
* **Error:** `No space left on device` (or user mentions running out of space)
  * **Solution:** Advise the user to clean up disk space. Suggest removing unwanted files such as `node_modules`, clearing cache, deleting unused Python libraries, or deleting files/folders from on the machine.
* **Error:** `Please create or add a tag with key 'environment' and a value like 'Production', 'Development', 'Test', or 'Staging'...`
  * **Solution:** Ignore this message. It is a system warning from Google Cloud that does not affect your workshop progress or the execution of your scripts.



**General & Conceptual Questions**

1.  **What exactly is an "Agent" in the context of ADK?**
    *   *Answer:* In ADK, an Agent is essentially an intelligent entity with a specific purpose. It's defined by its instructions (a prompt that dictates its personality and mission), the AI model it uses (like Gemini), and the tools it has access to (like Google Search or custom functions). It's the "brain" that processes information and decides what to do.

2.  **How is ADK different from just using a large language model (LLM) directly?**
    *   *Answer:* While ADK uses LLMs, it provides a framework to go beyond simple prompt engineering. It allows you to build sophisticated systems with tools, memory, and complex workflows (like sequential or parallel execution) that are difficult to manage with just raw LLM calls. It helps orchestrate multiple LLM calls and tool uses for more complex tasks.

3.  **Why do we need "tools" for agents? Can't the LLM just know everything?**
    *   *Answer:* LLMs are powerful, but their knowledge is limited to their training data and can become outdated. Tools allow agents to access real-time information (like weather), connect to external APIs (like databases or custom services), or perform specific computations that an LLM isn't designed for. They extend the agent's capabilities beyond its inherent knowledge.

4.  **What's the difference between an "Agent" and a "Session"?**
    *   *Answer:* An **Agent** defines *what* the AI can do and *how* it should behave. A **Session** is the specific instance of a conversation with an agent. It holds the memory of that conversation, allowing the agent to remember previous turns, follow up on questions, and adapt its responses based on the ongoing dialogue. You can have one agent, but many concurrent sessions with different users.

5.  **What is the "Agent-as-a-Tool" pattern, and why is it useful?**
    *   *Answer:* This pattern treats an entire agent as a tool that another agent can use. It's incredibly useful for modularity and specialization. You can create small, expert agents (e.g., a "food critic agent") and have a higher-level "orchestrator agent" delegate specific parts of a complex task to these specialists. This makes your system easier to build, maintain, and scale.

6.  **When should I use a `SequentialAgent` versus a `ParallelAgent`?**
    *   *Answer:* Use a `SequentialAgent` when tasks *must* be completed in a specific order, and often when the output of one step is required as input for the next (e.g., "find a restaurant, *then* get directions to it"). Use a `ParallelAgent` when multiple tasks can be executed independently and concurrently to save time, and their results will be combined later (e.g., "find museums, concerts, *and* restaurants near me").

7.  **What's the purpose of the `LoopAgent`?**
    *   *Answer:* The `LoopAgent` is designed for iterative refinement. It's used when a task requires proposing a solution, critiquing it, and then improving it based on feedback until certain conditions are met. This is ideal for tasks like drafting and editing content, planning complex itineraries with user feedback, or debugging.

### GCP & Setup Questions

1.  **Why do I need a Google Cloud Project and billing account for this workshop?**
    *   *Answer:* Google Cloud provides the infrastructure and access to powerful AI models (like Gemini) that the ADK agents will use. A billing account, even with free credits, is necessary to enable these services and track usage.

2.  **Do I really need a credit card for the $5 free credits?**
    *   *Answer:* No, the instructions specifically state "No credit card or payment needed — you’ll receive $5 free credits." You just need to claim the billing account and accept the credits.

3.  **What if I don't have $5 credit, can I still proceed?**
    *   *Answer:* The codelab states "you will need it for your deployment." While some parts of the Colabs might work without it (e.g., defining agents), any actual API calls to Gemini or other Google Cloud services will likely fail without an active billing account linked, even with free tier usage. It's crucial for running the examples fully.

4.  **I already have a GCP project. Can I use that instead of creating a new one?**
    *   *Answer:* Yes, you can generally use an existing GCP project as long as it has billing enabled and you have the necessary permissions. Just make sure to select your existing project when prompted to copy the project ID. You might need to enable specific APIs if they aren't already active.

5.  **How do I check if my billing account is properly linked to my GCP project?**
    *   *Answer:* In the Google Cloud Console, navigate to the left panel, click `Billing`, and it should show you which billing account is linked. If not, you'll see an option to "Manage billing accounts" or "Link a billing account."

6.  **I'm getting an API key error when running the Colab. What should I do?**
    *   *Answer:* Double-check that you've correctly followed the instructions for setting up your Google AI Studio API key and that it's correctly pasted into your Colab notebook or `.env` file (if running locally). Ensure there are no extra spaces or characters.

### Colab-Specific Questions

1.  **The Colab notebook is asking for me to "Connect" or "Authorize." What does this mean?**
    *   *Answer:* Colab runs on Google's cloud infrastructure. "Connect" means establishing a backend runtime. "Authorize" typically means granting the notebook permission to access your Google Drive or other Google services on your behalf, which is often needed for saving files or linking to GCP.

2.  **I'm having trouble running the cells. Some are giving errors.**
    *   *Answer:*
        *   Did you run the setup cells first (installing libraries, authenticating)?
        *   Are you connected to a Colab runtime (usually shown in the top right)?
        *   Did you enable the necessary Google Cloud services and link your billing account?
        *   Is your API key correctly configured?
        *   Sometimes restarting the runtime (`Runtime > Restart runtime`) can resolve transient issues.

3.  **The images in the Colab are not loading.**
    *   *Answer:* This usually indicates a temporary network issue or a problem with Colab's rendering. Try refreshing the page. The content of the workshop will still be fully functional without the images.

### Local Setup Questions (ADK Web)

1.  **I'm on Windows and the `setup_venv.bat` script isn't working.**
    *   *Answer:* Ensure you are running it from a Command Prompt or PowerShell, not a Git Bash or similar Linux-like terminal on Windows, as `.bat` files are specific to Windows command environments. Also, check if Python is correctly installed and added to your system's PATH.

2.  **I'm getting a "Python not found" error on Mac/Linux.**
    *   *Answer:* Try using `python3` instead of `python` in your commands, as some systems default `python` to an older version (like Python 2.x). The setup script should ideally handle this, but manual setup might require `python3 -m venv`.

3.  **My API key isn't being picked up by the ADK Web interface locally.**
    *   *Answer:* Double-check that your `.env` file is named exactly `.env` (not `.env.txt`) and is located in the `agent/` directory. Ensure the `GOOGLE_API_KEY=` line is correctly formatted with your actual key and no surrounding spaces. Restart the `adk web` command after making changes to the `.env` file.

4.  **I ran `adk web` but the browser isn't opening automatically, or `http://localhost:8000` isn't working.**
    *   *Answer:* Manually open your web browser and navigate to the URL displayed in your terminal after running `adk web`. If it's not `http://localhost:8000`, use the address provided. If nothing works, check your firewall settings to ensure port 8000 isn't blocked.

---

## Scenario: Multiple Gmail Accounts & Colab Project Mismatch

This is a **critical point** that needs clear explanation.

**What happens if people with multiple Gmail accounts accidentally open the Colab in a different account and project which doesn't have the services enabled?**

This is a common and frustrating issue. Here's what would happen and how to address it:

1.  **Colab will open, but operations will fail:** The Colab notebook itself will likely open fine, as it's a public link. However, when the user tries to run cells that interact with Google Cloud services (like Gemini API calls, or anything that relies on the `gcloud` context), they will encounter errors.

2.  **Authentication context mismatch:** Colab notebooks run in a specific authenticated context.
    *   If the user opened the Colab *while logged into Gmail Account A*, but their GCP project with enabled billing/services is under *Gmail Account B*, then the Colab's default authentication will point to Account A's (likely empty or unconfigured) GCP context.
    *   Even if they set `PROJECT_ID` in the Colab, the underlying authentication for API calls will still be tied to the Google account that authenticated the Colab session.

3.  **Specific Errors:** They would likely see errors such as:
    *   `google.auth.exceptions.DefaultCredentialsError: Your application has authenticated using end user credentials from Google Cloud SDK. We recommend that you enable the Cloud SDK to use your service account credentials instead.` (This is a generic auth error, but often points to the wrong context).
    *   `403 Permission denied` when making API calls, indicating the authenticated user/service account doesn't have permission to access the specified project or enabled services.
    *   Errors specifically mentioning "billing account not enabled" or "service not enabled."

**How to address this in the workshop:**

Add a dedicated note in the "Setup GCP" section, perhaps right before or after "Step 1: Enable Billing Account" and "Step 2: Create A New GCP Project."

> ### ⚠️ **Important: Using the Correct Google Account for Colab and GCP**
> If you have multiple Gmail accounts, it's absolutely crucial that you are logged into the **SAME GOOGLE ACCOUNT** for both:
>
> 1.  **Opening the Colab Notebooks:** Ensure the browser profile or Google account you are actively using to open `https://colab.research.google.com/...` is the one you intend to use for your GCP project.
> 2.  **Your Google Cloud Project:** The project where you enabled billing and services (Step 1 & 2) must be associated with the same Google account that is running the Colab.
>
> **What happens if they don't match?**
> If you open the Colab with Account A, but your GCP project is under Account B, the Colab will try to use Account A's (unconfigured) GCP context, leading to `403 Permission Denied` or "billing not enabled" errors when running the code.
>
> **How to fix it:**
> *   **Option 1 (Recommended):** Log out of all other Google accounts in your browser, then log back in *only* with the account you've configured for GCP, and then reopen the Colab.
> *   **Option 2:** If you prefer to stay logged into multiple accounts, open the Colab in an **Incognito/Private Window** and log in *only* with the Google account linked to your GCP project.
> *   **Option 3:** In the Colab notebook, you can sometimes explicitly authenticate with a different account using `gcloud auth login` or `colab.google.auth.authenticate_user()`, but this is more complex and usually unnecessary if you follow Option 1 or 2.



### Category 1: API Key & GCP Authentication Errors

**1. The "Invalid API Key" Error**
*   **What they paste:** 
    *   `google.api_core.exceptions.InvalidArgument: 400 API key not valid. Please pass a valid API key.`
    *   `Exception: API_KEY is missing or invalid.`
*   **What it means:** They either didn't put their API key in, put it in the wrong place, or accidentally included brackets/quotes around it.
*   **The Fix:** 
    *   *(If Local):* Check the `agent/.env` file. Ensure it looks exactly like `GOOGLE_API_KEY=AIzaSy...` with NO quotes around the key and NO spaces around the `=` sign. Make sure they saved the file and restarted the terminal command (`adk web`).
    *   *(If Colab):* Check the cell where they define the key or the Colab "Secrets" tab (the key icon on the left). Make sure there are no typos.

**2. The "Multiple Gmail Account / Missing Billing" Error**
*   **What they paste:** 
    *   `google.api_core.exceptions.PermissionDenied: 403 Google Cloud API has not been used in project [NUMBER] before or it is disabled.`
    *   `google.api_core.exceptions.PermissionDenied: 403 Project has not enabled billing.`
    *   `google.auth.exceptions.DefaultCredentialsError: Your application has authenticated using end user credentials...`
*   **What it means:** This is the multi-account clash. The Colab is trying to run using a Google account or Project ID that doesn't have the $5 credit/billing linked to it, or the API isn't turned on for that specific project.
*   **The Fix:** 
    1. Confirm the `PROJECT_ID` variable in the Colab exactly matches the one they just created.
    2. Ask: *"Are you logged into multiple Gmail accounts right now?"* Tell them to open an Incognito/Private window, log into ONLY the account they used to claim the $5 credits, and reopen the Colab link.

**3. The "Quota Exceeded" Error**
*   **What they paste:** 
    *   `google.api_core.exceptions.ResourceExhausted: 429 Quota exceeded for quota metric 'Generate requests'...`
*   **What it means:** They are hitting the model too fast, or their free trial ran out (less likely in a 1-day workshop). Sometimes this happens if multiple students accidentally share the same API key/Project ID.
*   **The Fix:** Tell them to wait 60 seconds and run the cell again. If it persists, verify they are using their *own* unique Project ID/API key and didn't copy a neighbor's.

---

### Category 2: Local Setup Errors (Mac/Linux/Windows)

**4. The "Command Not Found" Error (Local Run)**
*   **What they paste:** 
    *   *Mac/Linux:* `adk: command not found`
    *   *Windows:* `'adk' is not recognized as an internal or external command, operable program or batch file.`
*   **What it means:** The virtual environment is NOT activated, or the installation failed. Their terminal doesn't know what the `adk` command is.
*   **The Fix:** Tell them to run the activation command again. 
    *   *Mac/Linux:* `source .adk_env/bin/activate`
    *   *Windows:* `.adk_env\Scripts\activate` (Make sure they see `(.adk_env)` at the start of their terminal prompt before typing `adk web`).

**5. The "Module Not Found" Error**
*   **What they paste:** 
    *   `ModuleNotFoundError: No module named 'google_adk'` 
    *   `ModuleNotFoundError: No module named 'dotenv'`
*   **What it means:** They activated the environment, but they forgot to install the requirements, OR they installed the requirements *before* activating the environment (installing them to their global system instead).
*   **The Fix:** While the `(.adk_env)` is active in their terminal, tell them to run: `pip install -r requirements.txt`

**6. The Windows PowerShell Script Error**
*   **What they paste:** 
    *   `...cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies...`
*   **What it means:** Windows has a security feature preventing PowerShell scripts (like the activation script) from running by default.
*   **The Fix:** Tell them to paste exactly this into PowerShell as an Administrator (or just use Command Prompt instead of PowerShell):
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**7. The Mac Permission Denied Error**
*   **What they paste:**
    *   `bash: ./setup_venv.sh: Permission denied`
*   **What it means:** The downloaded setup script doesn't have "executable" rights on their Mac.
*   **The Fix:** Tell them to run `chmod +x setup_venv.sh` first, then try running `./setup_venv.sh` again.

---

### Category 3: Code & ADK Logic Errors (Colab)

**8. The "Missing Variable / Name Error"**
*   **What they paste:** 
    *   `NameError: name 'day_trip_agent' is not defined`
    *   `NameError: name 'run_agent_query' is not defined`
*   **What it means:** They are skipping around in the Colab notebook and trying to run a cell without running the cells above it.
*   **The Fix:** Tell them: *"Colab cells must be run in order. Please scroll up to the previous section, look for the cell where that agent/function is created, hit the 'Play' button on it, and then try this cell again."*

**9. The "Loop Exceeded" Error (Session 7)**
*   **What they paste:** 
    *   `RuntimeError: LoopAgent reached max_iterations (3) without meeting exit condition.`
*   **What it means:** The `LoopAgent` got stuck arguing with itself. The `critic_agent` kept rejecting the plan, and the `refiner_agent` never called the `exit_loop` tool within the 3 allowed tries.
*   **The Fix:** Explain that this is actually expected behavior sometimes! AI is non-deterministic. Tell them to just re-run the cell. If it happens consistently, tell them to adjust the `critic_agent` instruction to be slightly more lenient, or increase `max_iterations=5`.

**10. The Sequential State Key Error (Session 6)**
*   **What they paste:** 
    *   `KeyError: 'destination'` 
    *   `ValueError: Missing required inputs for agent: ['destination']`
*   **What it means:** In the SequentialAgent chain, Agent A was supposed to output a variable called `destination`, so Agent B could use `{destination}`. Agent A failed to output it (maybe it hallucinated a different format, or the code was altered).
*   **The Fix:** Check the `foodie_agent` definition. Make sure `output_key="destination"` is strictly defined. Have them re-run the `foodie_agent` cell to overwrite the memory, then run the sequential chain again. 

**11. The Tool Parsing / Pydantic Error (Session 2 & 3)**
*   **What they paste:** 
    *   `pydantic.error_wrappers.ValidationError: 1 validation error for...`
    *   `TypeError: get_live_weather_forecast() missing 1 required positional argument: 'location'`
*   **What it means:** The LLM decided to use a tool, but it passed the wrong type of data to it, or forgot a required argument. (e.g., The tool expected a string like `"Seattle"`, but the LLM passed a dictionary `{"city": "Seattle"}`).
*   **The Fix:** Tell them to look at the docstring of their Python function. The LLM relies 100% on that docstring. Ensure the `Args:` section of the docstring perfectly describes what the tool needs. Re-running the query usually fixes a one-off LLM hallucination.

**FALLBACK SEARCH PREPARATION:**
If you cannot find an answer within the provided skill materials:
    1. Determine if the question is within the technical scope of the workshop
    2. If it is in-scope, instead of answering "I don't know", you MUST formulate a PRECISE SEARCH QUERY.
    3. Use the avalible google search tool to search for the answer and provide it to the user.

