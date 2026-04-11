---
id: agentverse-developer
title: Agentverse - The Shadowblade's Codex - Vibecoding with Gemini CLI
summary: As the Developer workshop in the four-part Agentverse series, you will master "vibecoding," using the Gemini CLI — enhanced with extensions, agent skills, and hooks — to translate a high-level design document into a fully functional AI agent. You will then forge a complete CI pipeline with the Agent Development Kit to automatically test, containerize, and prepare your battle-ready agent for deployment.
authors: Christina Lin
duration: 90
keywords: docType:Codelab,skill:Beginner,language:Python,category:Cloud,category:AiAndMachineLearning,product:Assistant,product:CloudRun,product:GeminiCli,product:VertexAi,product:GoogleCloud
award_behavior: AWARD_BEHAVIOR_ENABLE
layout: paginated

---

# Agentverse - The Shadowblade's Codex - Vibecoding with Gemini CLI

## Overture
The era of siloed development is ending. The next wave of technological evolution is not about solitary genius, but about collaborative mastery. Building a single, clever agent is a fascinating experiment. Building a robust, secure, and intelligent ecosystem of agents—a true Agentverse—is the grand challenge for the modern enterprise.

Success in this new era requires the convergence of four critical roles, the foundational pillars that support any thriving agentic system. A deficiency in any one area creates a weakness that can compromise the entire structure.


This workshop is the definitive enterprise playbook for mastering the agentic future on Google Cloud. We provide an end-to-end roadmap that guides you from the first vibe of an idea to a full-scale, operational reality. Across these four interconnected labs, you will learn how the specialized skills of a developer, architect, data engineer, and SRE must converge to create, manage, and scale a powerful Agentverse.


No single pillar can support the Agentverse alone. The Architect's grand design is useless without the Developer's precise execution. The Developer's agent is blind without the Data Engineer's wisdom, and the entire system is fragile without the SRE's protection. Only through synergy and a shared understanding of each other's roles can your team transform an innovative concept into a mission-critical, operational reality.
Your journey begins here. Prepare to master your role and learn how you fit into the greater whole.


### Welcome to The Agentverse: A Call to Champions

In the sprawling digital expanse of the enterprise, a new era has dawned. It is the agentic age, a time of immense promise, where intelligent, autonomous agents work in perfect harmony to accelerate innovation and sweep away the mundane. 

![agentverse.png](img/agentverse.png)

This connected ecosystem of power and potential is known as The Agentverse.

But a creeping entropy, a silent corruption known as The Static, has begun to fray the edges of this new world. The Static is not a virus or a bug; it is the embodiment of chaos that preys on the very act of creation. 

It amplifies old frustrations into monstrous forms, giving birth to the Seven Spectres of Development. If left unchecked, The Static and its Spectres will grind progress to a halt, turning the promise of the Agentverse into a wasteland of technical debt and abandoned projects.

Today, we issue a call for champions to push back the tide of chaos. We need heroes willing to master their craft and work together to protect the Agentverse. The time has come to choose your path.

### Choose Your Class

Four distinct paths lie before you, each a critical pillar in the fight against **The Static**. Though your training will be a solo mission, your ultimate success depends on understanding how your skills combine with others.

- **The Shadowblade (Developer)**: A master of the forge and the front line. You are the artisan who crafts the blades, builds the tools, and faces the enemy in the intricate details of the code. Your path is one of precision, skill, and practical creation.
- **The Summoner (Architect)**: A grand strategist and orchestrator. You do not see a single agent, but the entire battlefield. You design the master blueprints that allow entire systems of agents to communicate, collaborate, and achieve a goal far greater than any single component.
- **The Scholar (Data Engineer)**: A seeker of hidden truths and the keeper of wisdom. You venture into the vast, untamed wilderness of data to uncover the intelligence that gives your agents purpose and sight. Your knowledge can reveal an enemy's weakness or empower an ally.
- **The Guardian (DevOps / SRE)**: The steadfast protector and shield of the realm. You build the fortresses, manage the supply lines of power, and ensure the entire system can withstand the inevitable attacks of The Static. Your strength is the foundation upon which your team's victory is built.


### Your Mission
Your training will begin as a standalone exercise. You will walk your chosen path, learning the unique skills required to master your role. At the end of your trial, you will face a Spectre born of The Static—a mini-boss that preys on the specific challenges of your craft.


Only by mastering your individual role can you prepare for the final trial. You must then form a party with champions from the other classes. Together, you will venture into the heart of the corruption to face an ultimate boss. 

A final, collaborative challenge that will test your combined strength and determine the fate of the Agentverse.


The Agentverse awaits its heroes. Will you answer the call?

## The Shadowblade's Codex

The Shadowblade's Codex lies open before you. Answer its call. The Agentverse is threatened by the creeping chaos of The Static, and only those who master the techniques within this codex can fight back. This is a path of precision and discipline. Today, your training begins. You will learn to wield AI not as a simple tool, but as a sentient blade that must be tamed and mastered. Follow the teachings herein, and you will craft a weapon of pure logic—an intelligent agent, honed and ready for battle.

![02-00-overview.png](img/02-00-overview.png)

### What you'll learn

- Wield your primary weapon: the Gemini CLI.
- Expand your arsenal with Gemini CLI extensions and agent skills.
- Summon external arsenals by integrating MCP tools with the Gemini CLI.
- Channel your intent into a "Vibe" using design documents to command your AI partner.
- Forge a clean, modular solution by building your first autonomous agent with the Agent Development Kit (ADK).
- Inscribe hooks to intercept and guard your agent's behavior.
- Construct automated evaluation suites to test and validate your agent.
- Build a complete CI pipeline to automatically test, containerize, and archive your agent.

## Preparing the Training Ground

### Claim Your Google Cloud Credit

**⚠️ Important Prerequisites:**
*   **Use a Personal Gmail:** You must use a personal account (e.g., `name@gmail.com`). Corporate or school-managed accounts will **not** work.

**👉 Steps:**
1.  **Go to the credit claim site:** [Click Here](https://goo.gle/agentverse-shdw)
2.  **Sign In:** Paste the link into the address bar and sign in with your **personal Gmail**.
3.  **Accept Terms:** Accept the Google Cloud Platform Terms of Service.
4.  **Verify Credit:** Look for a message confirming that the credit has been applied.
    *   *Note: If you are prompted to enter credit card information, you can safely ignore it and close the window.

And you are good to go. Feel free to close the window.

### Setup The Working Environment

👉Click Activate Cloud Shell at the top of the Google Cloud console (it's the terminal-shaped icon at the top of the Cloud Shell pane),
![cloud-shell.png](img/03-01-cloud-shell.png)

👉Click on the "Open Editor" button (it looks like an open folder with a pencil). This will open the Cloud Shell Code Editor in the window. You'll see a file explorer on the left side.
![open-editor.png](img/03-02-open-editor.png)


👉Open the terminal in the cloud IDE,

![03-05-new-terminal.png](img/03-05-new-terminal.png)

👉💻 In the terminal, verify that you're already authenticated and that the project is set to your project ID using the following command:

```bash
gcloud auth list
```

👉💻 Clone the bootstrap project from GitHub:

```bash
git clone https://github.com/weimeilin79/agentverse-developer.git
chmod +x ~/agentverse-developer/gitea.sh
chmod +x ~/agentverse-developer/init.sh
chmod +x ~/agentverse-developer/set_env.sh

git clone https://github.com/weimeilin79/agentverse-dungeon.git
chmod +x ~/agentverse-dungeon/run_cloudbuild.sh
chmod +x ~/agentverse-dungeon/start.sh
```
👉💻 Run the setup script from the project directory.

> **⚠️ Note on Project ID:**
> The script will suggest a randomly generated default Project ID. You can press **Enter** to accept this default.
>
> However, if you prefer to **create a specific new project**, you can type your desired Project ID when prompted by the script.
```bash
cd ~/agentverse-developer
./init.sh
```

The script will handle the rest of the setup process automatically.

> **👉 Important Step After Completion:**
> Once the script finishes, you must ensure your Google Cloud Console is viewing the correct project:
> 1. Go to [console.cloud.google.com](https://console.cloud.google.com/).
> 2. Click the project selector dropdown at the top of the page.
> 3. Click the **"All"** tab (as the new project might not appear in "Recent" yet).
> 4. Select the Project ID you just configured in the `init.sh` step.

![03-05-project-all.png](img/03-05-project-all.png)

👉💻 Back in the Terminal. Set the Project ID needed:
```bash
gcloud config set project $(cat ~/project_id.txt) --quiet
```

👉💻 Run the following command to enable the necessary Google Cloud APIs:
```bash
gcloud services enable  compute.googleapis.com \
                        artifactregistry.googleapis.com \
                        run.googleapis.com \
                        cloudfunctions.googleapis.com \
                        cloudbuild.googleapis.com \
                        iam.googleapis.com \
                        aiplatform.googleapis.com \
                        cloudresourcemanager.googleapis.com
```

👉💻 If you have not already created an Artifact Registry repository named agentverse-repo, run the following command to create it:

```bash
. ~/agentverse-developer/set_env.sh
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=$REGION \
    --description="Repository for Agentverse agents"
```

### Setting up permission

👉💻 Grant the necessary permissions by running the following commands in the terminal:
```bash
. ~/agentverse-developer/set_env.sh

# Artifact Registry Admin
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/artifactregistry.admin"

# Cloud Build Editor
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/cloudbuild.builds.editor"

# Cloud Run Admin
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/run.admin"

# IAM Service Account User
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/iam.serviceAccountUser"

# Vertex AI User
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/aiplatform.user"

# Logging Writer (to allow writing logs)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/logging.logWriter"


gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
  --role="roles/logging.viewer"
```

👉💻 As you begin your training, we will prepare the final challenge. The following commands summon the Spectres from the chaotic static, creating the bosses for your test.
```bash
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-dungeon
./run_cloudbuild.sh

npm update -g @google/gemini-cli
```

## Mastering Your Primary Weapon: Intro to Gemini CLI

Before you can wield the advanced, specialized weapons from the MCP server's arsenal, you must first master your primary weapon: the Gemini CLI. This is your most versatile blade, capable of shaping the digital world with your commands. These drills will familiarize you with its fundamental handling and capabilities.

![Overview](img/03-00-overview.png)

The Gemini Command Line Interface (CLI) is more than a tool; it is an extension of your will. This open-source AI agent, powered by Gemini models, operates on a "reason and act" (ReAct) loop. It analyzes your intent, selects the proper technique, executes it, and observes the result to complete complex tasks. Before you can wield more specialized weapons, you must master this primary blade.


### Getting started with Gemini CLI 

👉💻 Enter the training grounds and draw your weapon. In your Cloud Shell terminal, navigate to your personal armory.
```bash
cd ~/agentverse-developer
mkdir tabletop
cd tabletop
```

👉💻 Summon Gemini for the first time. It will guide you through the initial attunement.
```bash
clear
gemini 
```

If it asks you `Do you want to connect Cloud Shell editor to Gemini CLI?`, choose **NO**.

### Weapon Familiarization
Every master craftsman knows their tools. You must learn the core techniques of your blade before facing a true enemy.

👉✨ Every enchanted tool has runes that describe its power. Read them now. In the Gemini prompt, type:
```text
/help
```
Observe the list of commands. These are your fundamental techniques for managing memory (`focus`), conversation (`chat`), and external arsenals (`tools`). This is your combat manual.

👉✨ Your weapon is attuned to its environment, allowing you to manipulate the battlefield directly. Issue a command to the world outside the blade:
```text
!ls -l
```

👉✨ The Gemini CLI possesses its own set of built-in abilities. To inspect them:
```text
/tools
```
You'll see a list including `ReadFile`, `WriteFile`, and `GoogleSearch`. These are the default techniques you can call upon without needing to draw from an external arsenal.

👉✨ Your blade can also be enhanced with **extensions** — pre-forged enchantments created by other masters that package tools, commands, and context into a single installable unit. Inspect what extensions are currently attuned to your blade:
```text
/extensions list
```
The list may be empty for now — you haven't installed any extensions yet. You will summon your first extension later, when your training demands the power of image creation.

👉✨ Beyond extensions, skilled masters have codified their expertise into **Agent Skills** — on-demand scrolls of specialized knowledge. Check what skills your blade can discover:
```text
/skills list
```
Skills are not loaded into memory by default — they are activated only when needed, keeping your blade swift and unencumbered. You will learn to wield skills later in your training.

👉✨ A weapon is only effective if properly focused. The Gemini Blade can hold "tactical awareness" (context) to guide its actions.
```text
/memory show
```
It is currently empty, a blank slate.

👉✨ Inscribe the following tactical data into its memory:
```text
/memory add "The Shadowblade's primary foe is The Static."
```
Run `/memory show` again to confirm your blade has absorbed this knowledge.

👉✨ To be effective, your weapon must understand the mission. The `@` sigil commands the blade to analyze intel. First, create a mission briefing file:
```text
!echo "## Mission Objective: Defeat the Seven Spectres" > mission.md
```
👉✨Now, command your Gemini CLI to analyze the briefing and report its findings:
```text
Explain the contents of the file @mission.md
```
Your primary weapon is now aware of its objective.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI

## Analyzing the Battlefield: Practical Vibe Coding Interaction

The training drills are complete. You have learned the basic stances and strikes of your primary weapon, the Gemini CLI. But a blade is not truly mastered until it has been tested in the forge of creation and attuned to the armory of war. Before you can face the true enemy, you must first survey and shape your immediate surroundings—the digital battlefield.

![Overview](img/04-00-overview.png)


This chapter is about moving from theory to practice. You will first establish your presence in the Agentverse by commanding your Gemini blade to forge your Maker's Mark—a digital signature in the form of a personal website, built from nothing but your intent. Then, you will expand your power by activating a local arsenal of advanced tools—an MCP server—and attuning your blade to its frequency, allowing you to perform complex maneuvers like managing code repositories with simple, decisive commands.

### Establishing Your Maker's Mark

A true Shadowblade is recognized not just by their weapon, but by their signature style—their **Maker's Mark**. This mark will be your digital presence, a personal profile that announces your identity to the Agentverse. Here, you will command your Gemini Blade to execute the complex technique required to define this identity.

![Story](img/05-09-story.png)

👉💻 If you closed the Gemini CLI in the previous section, make sure to start it again, in your terminal run

```bash
clear
cd ~/agentverse-developer/tabletop
gemini 
```

👉✨ With a single, powerful command, instruct your Gemini CLI to forge the foundation of your digital identity:
```text
In the current folder, create a personal profile website for a hero codenamed 'Shadowblade'. The design must be a dark, futuristic theme with electric blue accents. All code must be in separate index.html and styles.css files. The layout must use CSS Flexbox for a two-column design. All generated code must be clean, well-commented, and professional. Make sure you have a placeholder spot for profile picture. Do not attempt to start the server.
```
Gemini has calculated the sequence of actions required.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI and run the following command in the terminal.*

```bash
python -m http.server
```


👀 To gaze upon your work, click the **Web preview** icon in the Cloud Shell toolbar. Select **Change port**, set it to **8000**, and click **Change and Preview**. A preview of your website will appear.
![04-01-webpreview.png](img/04-01-webpreview.png)

Your website might look different from mine. This is your unique mark.
![04-02-website.png](img/04-02-website.png)


Your signature technique is now refined, and the live simulation is no longer required. Command the Blade to stand down. 

👉💻 Press `Ctrl+C` to exit the http server.

Your digital identity is now established, and more importantly, you have learned the critical wisdom of wielding great power with even greater caution.


### Activate Your Local Arsenal: The Gitea Armory

A Shadowblade's true potential is unlocked not just by their personal skill, but by the quality of their arsenal. You will now activate your local weapons rack—a Gitea server—and attune your blade to its power. This arsenal is connected to your Gemini CLI through a **Model Context Protocol (MCP) server**, a specialized portal that allows your AI blade to interact with external tools and services, transforming your terminal into an intelligent, action-oriented workspace.

**Developer's Note:** Think of an MCP server as a conduit of power, a specialized portal that connects your AI's mind to an external tool's body. It’s what elevates the Gemini CLI from a mere conversationalist into a true, action-oriented agent. By attuning your blade to these MCP portals, you grant it the ability to perform tangible actions: to manage files, query databases, interact with APIs, and much more. An entire ecosystem of these portals exists, created by developers to connect AI agents to powerful platforms. There are MCP servers for interacting with databases, securing code, or even support for pair programming. The possibilities are vast, allowing a developer to customize their workspace for any given projects.

Today, we will focus on two fundamental powers essential to any "vibe coder": the power to control the forge and the power to create from imagination. You will first attune your blade to a Git server, granting you command over your source code repository. Then, you will connect to a second MCP server for image generation, allowing you to create visual assets with nothing more than a command.

Let us begin by summoning the first and most fundamental piece of your new arsenal: the armory itself.

👉💻 In your terminal, execute the activation script to summon the armory:
```bash
cd ~/agentverse-developer
./gitea.sh
```
This script awakens the Gitea container and opens the MCP portal, allowing Gemini to perceive and interact with it.

👉 To inspect your new arsenal, you must gaze into the web preview.

👉 From the **Web preview** icon in the Cloud Shell toolbar, select **Change port** and set it to **3005**.
![04-03-webpreview.png](img/04-01-webpreview.png)

👉 A Gitea login page will appear. Enter the armory using the incantation:
    *   Username: `dev`
    *   Password: `dev`
![Login](img/05-01-login.png)


👉💻  Your Gemini CLI cannot yet see this new arsenal. You must perform a critical attunement, inscribing the armory's location onto the Gemini CLI's configuration runes (`settings.json`). In your terminal, run:
```bash
if [ ! -f ~/.gemini/settings.json ]; then
  # If file does not exist, create it with the specified content
  echo '{"mcpServers":{"gitea":{"url":"http://localhost:8085/sse"}}}' > ~/.gemini/settings.json
else
  # If file exists, merge the new data into it
  jq '. * {"mcpServers":{"gitea":{"url":"http://localhost:8085/sse"}}}' ~/.gemini/settings.json > tmp.json && mv tmp.json ~/.gemini/settings.json
fi &&
cat ~/.gemini/settings.json
```

👀 The settings.json file is the central configuration for the Gemini CLI, acting as its grimoire of preferences and capabilities. It dictates how the CLI behaves, appears, and, most importantly, what external powers it can wield. This file is typically located in your home directory at `~/.gemini/settings.json`, applying its rules to all your projects. However, you can also create project-specific `settings.json` files within a `.gemini` directory inside your project folder to override the global settings.
```console
"mcpServers": {
  "gitea": {
    "url": "http://localhost:8085/sse"
  }
}
```
This setting tells your Gemini, "The arsenal named gitea is active and listening for commands at this specific network address."


👉💻 Re-enter the Gemini CLI. In your terminal, run:
```bash
clear
cd ~/agentverse-developer/tabletop/
gemini 
```

👉✨ Verify that your blade has discovered the new weapon. Command it to list all available arsenals through its MCP portals:
```text
/mcp
```

![Gitea MCP Server](img/05-02-gitea-mcp.png)

You should now see `gitea` and its list of available techniques. Your blade is attuned.

Your "Maker's Mark" profile is a finely crafted technique, but it needs a proper place in the armory—a scabbard to hold it securely. Command your Gemini CLI to create one.

```text
Create a new repository named 'shadowblade-profile'. The description should be 'The Maker's Mark and digital identity for the Shadowblade operative.' I will push my own files later, so do not create any content.
```

Return to the Gitea web interface and refresh. You will see the new `shadowblade-profile` repository has been forged for you.
![Gitea Repo](img/05-03-gita-repo.png)

With the scabbard ready, secure your work. Command Gemini to commit the files of your profile website.

👉💻Issue the final command for this technique in Gemini CLI:
```text
Using the Gitea tool, push the index.html and styles.css files to the 'shadowblade-profile' repository.
```

A true master verifies their work. Return to the Gitea tab and refresh the repository page. Your `index.html` and `styles.css` are now safely archived.

![Gitea Repo](img/05-04-repo-click.png)
![Gitea Repo](img/05-05-repo-view.png)

👉✨ A Shadowblade is defined by their sigil, but as you recall, your website is missing its profile image. A master artisan acknowledges their flaws in order to perfect them. You must log this imperfection in the armory's records.
```text
File an issue for me in the shadowblade-profile repo. The issue is that the profile image is missing.
```
View the issue in Gitea
![Gitea Issue](img/05-06-issue.png)

To forge the missing sigil, you must summon a different kind of power—a **creation spirit** capable of generating imagery from pure thought. In the Gitea section, you manually edited configuration runes to attune your blade to an MCP server — the "raw" approach. Now you will learn the modern technique: **Gemini CLI Extensions**.

An extension is a pre-forged enchantment that packages MCP servers, custom commands, context, and settings into a single installable unit. One incantation replaces dozens of lines of manual configuration.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI

Before summoning the creation spirit, you must first unlock its power within your realm. The Nano Banana extension uses the **Generative Language API** — a separate gateway from the Vertex AI services you've been using. You must enable this gateway and forge a unique key to grant the spirit access.

👉💻 In your terminal, enable the API:
```bash
gcloud services enable generativelanguage.googleapis.com
```

👉💻 Now, forge an API key — the spirit's personal access token:

![gemini credentials key creation](img/05-07-gemini-credentials-key-creation.png)
1. Navigate to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
2. Click **+ CREATE CREDENTIALS** at the top and select **API key**.
3. Name the API key something notable like **Generative Language API Key**.
4. In the API restrictions dropdown, choose **Generative Language API**
5. **Create and Copy the key** — you will need it in the next step.

👉💻 Install the **Nano Banana** extension — a creation spirit powered by Google's specialized Gemini text-to-image models. In your terminal, run:
```bash
gemini extensions install https://github.com/gemini-cli-extensions/nanobanana
```
When prompted for the **API Key**, paste the key you just created and press Enter.

👉💻 One final attunement is needed. Cloud Shell's environment directs all AI requests through Vertex AI by default, but the creation spirit speaks through a different gateway. Run this command to configure the extension's portal correctly:
```bash
NANO_CONFIG=$(find ~/.gemini/extensions -name "gemini-extension.json" -path "*nanobanana*" 2>/dev/null | head -1) && \
jq '.mcpServers.nanobanana.env.GOOGLE_GENAI_USE_VERTEXAI = ""' "$NANO_CONFIG" > /tmp/nb_tmp.json && \
mv /tmp/nb_tmp.json "$NANO_CONFIG"
```

That single command has done everything: downloaded the MCP server, registered its tools, and installed custom slash commands — all without you touching `settings.json`.

👀 **Developer's Note: Extensions vs. Raw MCP Servers**
Contrast this with the Gitea setup. There, you manually ran a `jq` command to inject an MCP server URL into `settings.json`. That "raw" approach is valuable for understanding the mechanics, but for most real-world use, **extensions** are preferred. They bundle the MCP server, custom commands (like `/generate`, `/edit`, `/story`), environment configuration, and even contextual instructions (via a bundled `GEMINI.md`) into a single, shareable package. An entire ecosystem of extensions exists at the [Gemini CLI Extension Gallery](https://geminicli.com/extensions).

👉💻 Re-enter the Gemini CLI and verify the extension is active:
```bash
clear
cd ~/agentverse-developer/tabletop/
gemini 
```

👉✨ Confirm the extension is attuned:
```text
/extensions list
```
You should now see `nanobanana` listed with its tools and commands.

👉✨ With a single, powerful command, instruct the Nano Banana extension to forge your sigil. In your Gemini CLI, issue the command:
```text
/generate a portrait of a shadowblade, pixel art style. A determined warrior with long, braided magenta hair, wearing black and teal armor and confidently holding a silver broadsword.
```
👉✨ The spirit will generate the image and place it directly into your local workspace. Now, command the blade to use this newly forged sigil. *(GEMINI MIGHT HAVE ALREADY DONE THIS FOR YOU! Check the previous response, it might be smart enough to do this before you ask it!!!! )*
```text
Modify the index.html file to add my profile picture. Use the image I just generated.
```
👉💻 In a new terminal, start the http server.
```bash
cd ~/agentverse-developer/tabletop/
python -m http.server
```

👀 To gaze upon your work, click the **Web preview** icon in the Cloud Shell toolbar. Select **Change port**, set it to **8000**, and click **Change and Preview**. A preview of your website will appear.
![05-08-website.png](img/05-08-website.png)

👉✨ Back in the terminal running Gemini CLI, commit the fix, noting the completion of the task, and close the issue you filed in the armory's records.
```text
Push the changed index.html file to the 'shadowblade-profile' repository using the gitea tool. Make sure you add 'Fix #1' in the commit comment. Also, close issue #1.Use the Gitea Tool and use user account "dev"
```

👉💻 Press `Ctrl+C` twice to exit Gemini CLI.

👀 To gaze upon your work, click the **Web preview** icon in the Cloud Shell toolbar. Select **Change port**, set it to **3005**, and click **Change and Preview**. A preview of your website will appear.
![Fixed](img/05-08-fix.png)

👉💻 In the terminal running the http server, press `Ctrl+C` to exit the http server. 




### FOR NON GAMERS
> aside negative
While &quot;The Shadowblade&#39;s Codex&quot; uses engaging gamer metaphors, the underlying concepts are fundamental to modern software development, particularly in the burgeoning field of artificial intelligence and automation. This chapter translates the adventurous language into real-world business scenarios, explaining how intelligent agents, collaborative development, and robust deployment pipelines are transforming enterprise operations.<BR/><BR/><strong>Intent-Driven AI Development</strong><BR/><BR/>The <strong>Gemini CLI (Command-Line Interface)</strong> is not a magical weapon, but an <strong>AI-Powered Developer Assistant Agent</strong>. It&#39;s a smart tool that integrates Google&#39;s Gemini AI models directly into your command line. Its &quot;reason and act&quot; (ReAct) loop means it can understand your high-level instructions, break them down into steps, choose the right tools (like a web browser, code editor, or other developer utilities), and execute those steps to achieve your goal.<strong>Vibecoding</strong> translates to <strong>Intent-Driven Development</strong> or <strong>AI-Assisted Code Generation from High-Level Specifications</strong>. <BR/>Instead of writing every line of code manually, you describe your intent or &quot;vibe&quot; (a business requirement, a design concept) in natural language, and the AI assistant helps generate the necessary code and configuration. <BR/><strong>Real-World Use Case: Rapid Prototyping a Project Dashboard</strong><BR/>Imagine your team needs a quick internal dashboard to display the status of various AI agent projects. Manually coding HTML, CSS, and setting up a basic web server can take time.<ol><li><strong>Your Intent (The &quot;Vibe&quot;)</strong>: You tell your AI assistant (Gemini CLI) something like: &quot;In the current folder, create a simple internal project dashboard website. It should have a clean, modern design with project status indicators and quick links to project repositories. All code must be in separate <code>index.html</code> and <code>styles.css</code> files. Make sure it&#39;s well-commented.&quot;</li><li><strong>AI Action</strong>: The Gemini CLI, understanding your intent, might:<ul><li><strong>Generate HTML</strong>: Create <code>index.html</code> with the basic structure for a dashboard, including placeholders for project names, statuses, and links.</li><li><strong>Generate CSS</strong>: Create <code>styles.css</code> with styling rules to match your &quot;clean, modern design&quot; with status indicators.</li><li><strong>Suggest a Local Server</strong>: Help you start a local web server (like Python&#39;s built-in HTTP server) to immediately preview the dashboard in your browser.</li></ul></li></ol>This allows a developer to rapidly prototype and iterate on user interfaces or internal tools, significantly reducing the initial development time and freeing them to focus on more complex business logic. The &quot;Shadowblade Profile Website&quot; in the codelab is a direct example: a quick, descriptive command produced a functional, styled webpage based on a high-level design.<BR/><BR/><strong>Connecting AI to Tools with MCP Servers</strong><BR/><BR/><strong>Gitea</strong> (your &quot;local arsenal&quot;) represents an <strong>Internal Code Repository</strong> or <strong>Version Control System</strong> (like GitHub or GitLab, but potentially hosted within your company&#39;s network). It&#39;s where all your project code, documentation, and history are securely stored and managed.<BR/><strong>MCP (Model Context Protocol) Servers</strong> are <strong>Middleware Connectors</strong> or <strong>API Bridges</strong>. They are specialized software components that allow your AI assistant (Gemini CLI) to interact with other business-critical tools and systems. Think of them as translators that let the AI &quot;speak&quot; to different applications.<BR/><strong>Real-World Use Case: AI-Assisted Project Management and Asset Creation</strong>With MCP servers, your AI assistant can seamlessly integrate into your existing business workflows:<ul><li><strong>Automated Project Setup</strong>: Instead of a developer manually creating a new repository in Gitea for a new project, you could command your AI: &quot;Create a new project repository named &#39;AI-Fraud-Detection-Module&#39; with a description &#39;Contains the core logic for the new AI-powered fraud detection system&#39;.&quot; The AI, through an MCP server connected to Gitea, would then create the repository for you.</li><li><strong>Intelligent Issue Tracking</strong>: If your AI identifies a potential bug or an incomplete task (like a &quot;missing profile image&quot; for your dashboard), it could use an MCP server connected to your issue tracking system (e.g., Jira, Asana) to &quot;File an issue for me in the &#39;AI-Fraud-Detection-Module&#39; repo: The data ingestion pipeline is occasionally dropping records.&quot;</li><li><strong>On-Demand Marketing Assets</strong>: Need a custom image for a new marketing campaign or internal presentation? An AI assistant connected via an MCP server to an image generation service (like the Gemini text-to-image models used by Nano Banana) could be instructed: &quot;Generate a banner image for our new &#39;Data Insights Platform&#39;, using a futuristic, data-flow theme with blue and green colors.&quot; The AI would generate the image and potentially even upload it to your company&#39;s digital asset management system (a Google Cloud Storage bucket in the codelab&#39;s case).</li></ul>These bridges transform the AI from a conversational tool into an active participant in your business operations, executing tangible actions across different systems.<BR/><BR/><strong>Gemini CLI Extensions</strong><BR/><BR/>In modern practice, MCP servers are rarely configured manually. Instead, they are packaged as <strong>Gemini CLI Extensions</strong> — installable bundles that include the MCP server, custom slash commands, contextual instructions, and configuration. A single <code>gemini extensions install</code> command replaces the manual process of editing configuration files. This is the preferred, production-grade approach to expanding the Gemini CLI&#39;s capabilities.


## Assembling the Shadowblade Agent: Vibe code with Guardrails 

The time for practice drills is over. The echoes of steel on stone fade. You have mastered your primary weapon and prepared your arsenal for war. Now, you will undertake the true test of a Shadowblade: assembling the operative itself. This is the art of breathing life into logic, using a sacred blueprint from the Codex to construct an agent's core intelligence—creating a sentient wielder for the blades in your arsenal that can think, reason, and act on its own.

![Overview](img/05-00-overview-arch.png)

Your first mission is to enter an existing workshop—a pre-built codebase—and from its parts, forge your champion.

### The Assembly Ritual

Before the first spark of the forge, a master technician surveys their workshop, understanding every tool and every schematic. When stepping onto an unfamiliar battlefield like a large, existing codebase, your first priority is reconnaissance. You must understand the lay of the land—the existing architecture, the ultimate objectives, and the protocols of engagement. Only by familiarizing yourself with the fortress's blueprints and its standards can you effectively contribute your skill.

![Story](img/06-01-story.png)

Your Gemini CLI, your ever-present scout, can aid you in this reconnaissance:
- **Provide High-Level Summaries:** It can read the entire codex (or codebase) and give you a swift understanding of its purpose and key components.
- **Help with Environment Setup:** It can guide you through the arcane rituals of installing tools and configuring your machine.
- **Navigate Codebases:** It can act as your guide, helping you explore complex logic and find hidden passages within the code.
- **Generate Onboarding Documents:** It can create tailored scrolls that clarify goals, roles, and resources for new allies joining your cause.
- **Automate Learning and Q&A:** It becomes your personal scholar, answering questions about features or code behavior, allowing you to fight with greater independence.


👉💻 In your first terminal, navigate to the shadowblade directory and summon your AI partner:

```bash
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-developer/shadowblade
clear
gemini 
```

👉✨ Now, command your scout to survey the battlefield and report back.
```text
Analyze the entire project and provide a high-level summary.
```
With the existing terrain mapped, you must now consult the blueprint for what you are about to build. The most powerful operatives are not improvised, they are constructed from a precise design.

Developer's Note: This design document serves as the authoritative blueprint for the project. Its purpose is to enforce clarity on goals and technical implementation before significant development effort is invested. A well-defined plan ensures all developers are aligned, reduces the risk of rework, and helps prevent technical debt and scope creep. It is the primary tool for maintaining project velocity and code quality, especially as the team grows or new members are onboarded.

A critical goal of this document is to define not just the "happy path" but also the edge cases and failure modes, especially when using LLMs. In my experience, LLMs are excellent at generating optimistic code where all inputs are valid and all external calls succeed. To build robust, production-ready software, we must explicitly guide the AI by defining contingencies for scenarios like:
- Invalid or malformed arguments passed to a function.
- API call failures, network timeouts, or unexpected error codes from external services.
- Handling of null or empty data structures where data is expected.
- Race conditions or concurrency issues.

By specifying the expected behavior for these cases in the design, we instruct the LLM to generate more resilient code, significantly reducing the time spent on manual refactoring and bug fixing.


👉✨ Ask Gemini to retrieve this sacred blueprint for you.
```text
download https://raw.githubusercontent.com/weimeilin79/agentverse/main/developer/shadowblade/agent_design.md, store it as an agent_design.md file in my local folder, and show me the newly downloaded design doc. Do not attempt to create the file just yet. 
```

👉✨ The scroll is long and detailed. Command Gemini to distill its essence.
```text
Summarize the newly downloaded @agent_design.md for me, do not attempt to create file just yet. 
```
Now you have the plan. But before a single line of code is forged, a master artisan establishes the laws of the forge. This is about *discipline* and *scalability*. These are the **Coding Guidelines**. They are not mere suggestions; they are runes of power that ensure every component is built with the same precision and strength. They prevent the chaos of individual style from corrupting the final creation, ensuring the agent is resilient, maintainable, and pure, allowing new artisans to join the project without disrupting the harmony of the whole.

To inscribe these laws directly into the consciousness of our AI partner, we use a special artifact: the `GEMINI.md` file. When the Gemini CLI is summoned, it automatically searches for this file and loads its contents into the AI's working memory. It becomes a persistent, project-level instruction. It acts as a talisman that constantly whispers the rules of the forge to the AI.


Let's inscribe these runes now.

👉💻 Exit Gemini for a moment by pressing `Ctrl+C` twice. 

👉💻 In your terminal, run the following command to write the guideline file.
```bash
cat << 'EOF' > GEMINI.md
  ### **Coding Guidelines**
  **1. Python Best Practices:**

  *   **Type Hinting:** All function and method signatures should include type hints for arguments and return values.
  *   **Docstrings:** Every module, class, and function should have a docstring explaining its purpose, arguments, and return value, following a consistent format like reStructuredText or 
  Google Style.
  *   **Linter & Formatter:** Use a linter like `ruff` or `pylint` and a code formatter like `black` to enforce a consistent style and catch potential errors.
  *   **Imports:** Organize imports into three groups: standard library, third-party libraries, and local application imports. Sort them alphabetically within each group.
  *   **Naming Conventions:**
      *   `snake_case` for variables, functions, and methods.
      *   `PascalCase` for classes.
      *   `UPPER_SNAKE_CASE` for constants.
  *   **Dependency Management:** All Python dependencies must be listed in a `requirements.txt` file.

  **2. Web APIs (FastAPI):**

  *   **Data Validation:** Use `pydantic` models for request and response data validation.
  *   **Dependency Injection:** Utilize FastAPI's dependency injection system for managing resources like database connections.
  *   **Error Handling:** Implement centralized error handling using middleware or exception handlers.
  *   **Asynchronous Code:** Use `async` and `await` for I/O-bound operations to improve performance.
EOF
cat GEMINI.md
```
With the laws inscribed, let's re-summon our AI partner and witness the magic of the artifact.

👉💻 Relaunch the Gemini CLI from the shadowblade directory:
```bash
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-developer/shadowblade
clear
gemini 
```

👉✨ Now, ask Gemini to show you what it's thinking about. The runes have been read.
```
/memory show 
```

### Equipping Specialized Expertise: Agent Skills

The `GEMINI.md` runes you inscribed are like a permanent enchantment — always active, always guiding your blade. But a true master doesn't carry every scroll into every battle. Some expertise is too specialized, too heavy, to keep loaded at all times. This is where **Agent Skills** come in.

Think of an Agent Skill as a sealed scroll in your pack. It contains specialized expertise — detailed instructions, scripts, even reference data — but it remains dormant until the moment you need it. Only when you face a challenge that matches the scroll's domain does your blade draw it forth and absorb its knowledge. This is called **progressive disclosure**: it keeps your blade swift and unburdened, activating specialized powers only on demand.

👀 **Developer's Note:** Agent Skills are the third layer of Gemini CLI's context engineering hierarchy:
1. **User Settings** (`~/.gemini/settings.json`) — Global configuration
2. **GEMINI.md** — Persistent project-level context (always loaded)
3. **Agent Skills** (`.gemini/skills/`) — On-demand expertise (loaded when needed)

This progressive disclosure model is critical for enterprise use: a repository could contain dozens of specialized skills (security auditing, database migration, compliance checks), but the AI only activates the ones relevant to the current task, conserving precious context tokens.

Let's forge your first skill — a scroll of ADK expertise that your blade can draw upon when building agents.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI. Then, create the skills directory and inscribe the scroll:
```bash
mkdir -p ~/.gemini/skills/adk-agent-design
cat << 'EOF' > ~/.gemini/skills/adk-agent-design/SKILL.md
---
name: adk-agent-design
description: Expert guidance for designing and building agents with the Google Agent Development Kit (ADK). Activate when the user asks about agent architecture, tool design, callback patterns, or ADK best practices.
---

# ADK Agent Design Expertise

When designing an ADK agent, follow these principles:

## Agent Architecture
- Define agents using `LlmAgent` with a clear `name`, `model`, `instruction`, and `tools` list.
- Keep instructions specific and action-oriented. Tell the agent what it IS, not what it should try to be.
- Use `before_model_callback` and `after_model_callback` for guardrails and validation.

## Tool Design
- Each tool should do ONE thing well. Prefer small, focused tools over large, multi-purpose ones.
- Always include descriptive docstrings — the LLM uses these to decide when to call each tool.
- Return structured data (dicts) from tools so the LLM can reason about the results.

## Testing Strategy
- Use `adk eval` with evalset JSON files for broad strategy testing.
- Use `pytest` with `AgentEvaluator` for programmatic, CI-ready tests.
- Define both `tool_trajectory_avg_score` and `response_match_score` criteria.
EOF
```

👉💻 Re-enter the Gemini CLI to see the newly forged skill:
```bash
cd ~/agentverse-developer/shadowblade
gemini
```

👉✨ Verify the skill is in your pack:
```text
/skills list
```
You should see `adk-agent-design` listed — a sealed scroll, dormant and waiting.

👉✨ Now ask Gemini something that should activate the skill:
```text
What are the best practices for designing tools in an ADK agent?
```

Notice how the response is now informed by the specialized knowledge you inscribed in the skill. The blade didn't carry this expertise in its base memory — it *discovered* the relevant scroll and drew it forth only when the question matched. This is progressive disclosure in action.

Skills can be crafted for any domain — security auditing, database migration, compliance checks — and shared across your team by committing them to version control. Each team member's blade gains the same expertise, consistently applied.

This is the pivotal moment. You will provide the schematic (agent_design.md) and the laws of the forge (GEMINI.md), and issue the great spell of creation.

👉✨ This is the single, powerful command that will construct your agent. Issue it now:
```text
You are an expert Python developer specializing in the Google Agent Development Kit (ADK). Your task is to write the complete, production-quality code for `agent.py` by following the technical specifications outlined in the provided design document verbatim.

Analyze the design document at `@agent_design.md` and generate the corresponding Python code for `@agent.py`.

Ensure the generated code is clean, matches the specifications exactly, and includes all specified imports, functions, and logic. Do not add any extra functions or logic not described in the document.

and you are currently already in the shadowblade working directory
```

👀 Gemini has now constructed the agent's core logic in `agent.py`. The core of this new file defines the agent's intelligence, connecting its reasoning model to a set of external tools:
```console
PATH_TO_MCP_SERVER = "shadowblade/mcp_server.py"
.....
root_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="shadowblade_combat_agent",
    instruction="""
      You are the Shadowblade, an elite combat agent operating on a digital battleground.
      Your primary objective is to execute combat commands with strategic precision, neutralizing targets as directed.
  ......
      5.  You will then report the outcome of the attack (damage, special effects, etc.) back to the commander in a clear, tactical summary.

      General Rules of Engagement:
      - If a command is ambiguous or a target is not specified, state that you require a clear target for engagement. Do not guess.
      - You MUST use ONLY the provided tools to perform actions. Do not invent weapons or outcomes. Stick to the mission parameters.
""",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='python3',
                args=[PATH_TO_MCP_SERVER]
            )
        )
    ]
)
```

The `tools` parameter. The agent is designed to use a `MCPToolset` that connects to an external arsenal defined in `mcp_server.py`. 



👀 Head over to `~/agentverse-developer/shadowblade/mcp_server.py` in the editor and take a moment to understand what it does. It's the source of all the weapons available to Shadowblade. Currently, the armory is quite bare.

![06-02-story.png](img/06-02-story.png)

👉✨ Let's command Gemini to forge seven new weapons for the arsenal. Issue the following prompt in the Gemini CLI:
```text
I need to add several new weapon tools to my `mcp_server.py` file. Please open @mcp_server.py and, following the exact same pattern as the existing `forge_broadsword()` function, create and add new `@mcp.tool()` decorated functions for each of the following weapons:

1.  **A 'Refactoring Sickle'**:
    -   **Function Name:** `hone_refactoring_sickle`
    -   **Docstring/Target:** "Effective against 'Elegant Sufficiency' weaknesses like 'The Weaver of Spaghetti Code'."
    -   **Weapon Name:** "Refactoring Sickle"
    -   **Damage Type:** "Cleansing"
    -   **Base Damage:** Random integer between 100 and 136
    -   **Critical Hit Chance:** Random float between 0.10 and 0.20
    -   **Special Effect:** "Pruning - improves code health and maintainability with each strike."

2.  **A 'Quickstart Crossbow'**:
    -   **Function Name:** `fire_quickstart_crossbow`
    -   **Docstring/Target:** "Effective against 'Confrontation with Inescapable Reality' weaknesses like 'Procrastination: The Timeless Slumber'."
    -   **Weapon Name:** "Quickstart Crossbow"
    -   **Damage Type:** "Initiative"
    -   **Base Damage:** Random integer between 105 and 120
    -   **Critical Hit Chance:** Random float between 0.9 and 1.0
    -   **Special Effect:** "Project Scaffolding - creates a `main.py`, `README.md`, and `requirements.txt`."

3.  **'The Gilded Gavel'**:
    -   **Function Name:** `strike_the_gilded_gavel`
    -   **Docstring/Target:** "Effective against 'Elegant Sufficiency' weaknesses like 'Perfectionism: The Gilded Cage'."
    -   **Weapon Name:** "The Gilded Gavel"
    -   **Damage Type:** "Finality"
    -   **Base Damage:** 120
    -   **Critical Hit Chance:** 1.0
    -   **Special Effect:** "Seal of Shipping - marks a feature as complete and ready for deployment."

4.  **'Daggers of Pair Programming'**:
    -   **Function Name:** `wield_daggers_of_pair_programming`
    -   **Docstring/Target:** "Effective against 'Unbroken Collaboration' weaknesses like 'Apathy: The Spectre of \"It Works on My Machine\"'."
    -   **Weapon Name:** "Daggers of Pair Programming"
    -   **Damage Type:** "Collaborative"
    -   **Base Damage:** Random integer between 110 and 125
    -   **Critical Hit Chance:** Random float between 0.30 and 0.50
    -   **Special Effect:** "Synergy - automatically resolves merge conflicts and shares knowledge."

5.  **A 'Granite Maul'**:
    -   **Function Name:** `craft_granite_maul`
    -   **Docstring/Target:** "Effective against 'Revolutionary Rewrite' weaknesses like 'Dogma: The Zealot of Stubborn Conventions'."
    -   **Weapon Name:** "Granite Maul"
    -   **Damage Type:** "Bludgeoning"
    -   **Base Damage:** Random integer between 115 and 125
    -   **Critical Hit Chance:** Random float between 0.05 and 0.15
    -   **Special Effect:** "Shatter - has a high chance to ignore the target's 'best practice' armor."

6.  **A 'Lens of Clarity'**:
    -   **Function Name:** `focus_lens_of_clarity`
    -   **Docstring/Target:** "Effective against 'Elegant Sufficiency' weaknesses by revealing the truth behind 'Obfuscation'."
    -   **Weapon Name:** "Lens of Clarity"
    -   **Damage Type:** "Revelation"
    -   **Base Damage:** Random integer between 120 and 130
    -   **Critical Hit Chance:** 1.0
    -   **Special Effect:** "Reveal Constants - highlights all magic numbers and suggests converting them to named constants."

7.  **The 'Codex of OpenAPI'**:
    -   **Function Name:** `scribe_with_codex_of_openapi`
    -   **Docstring/Target:** "Effective against 'Confrontation with Inescapable Reality' weaknesses like 'Hype: The Prophet of Alpha Versions'."
    -   **Weapon Name:** "Codex of OpenAPI"
    -   **Damage Type:** "Documentation"
    -   **Base Damage:** Random integer between 110 and 140
    -   **Critical Hit Chance:** Random float between 0.5 and 0.8
    -   **Special Effect:** "Clarity - makes an API discoverable and usable by other agents and teams."
```
👉 Once Gemini confirms the changes, open the `mcp_server.py` file. Scroll through the code and confirm that the seven new `@mcp.tool()` functions have been successfully added. Check the `hone_refactoring_sickle` function. Does it have the correct docstring and weapon statistics? Verifying the AI's work is a crucial habit of the master Shadowblade.

With the agent forged and refined, it is time for its awakening.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI


**Developer's Note on Gemini's Output:** Gemini's generated code can sometimes be unpredictable. While we strive for exact adherence to the design, it's normal in development sessions for developers to iterate and refine the code multiple times to reach a production-ready state.

👉💻 To ensure you have the correct and thoroughly tested production code in your working directory, please run the following commands in your terminal:
```bash
cp  ~/agentverse-developer/working_code/agent.py ~/agentverse-developer/shadowblade/agent.py
cp  ~/agentverse-developer/working_code/mcp_server.py ~/agentverse-developer/shadowblade/mcp_server.py
```

👉💻 In your terminal, begin the ritual to bring it online:
```bash
cd ~/agentverse-developer/
. ~/agentverse-developer/set_env.sh
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r shadowblade/requirements.txt
adk run shadowblade
```


👉✨ You should see output confirming that the "Shadowblade Combat Agent" is engaged and running, awaiting its first command. Issue its first combat directives.
```text
We've been trapped by 'Perfectionism: The Gilded Cage'. Its weakness is 'Elegant Sufficiency'. Break us out!
```
👉✨ And another:
```text
The 'Dogma: The Zealot of Stubborn Conventions' blocks our path. Its weakness is 'Revolutionary Rewrite'. Take it down.
```

You have successfully assembled your first agent and validated its combat capabilities. Press `Ctrl+C` twice to let your champion rest. The assembly is complete.

### FOR NON GAMERS
> aside negative
An <strong>Agent</strong> is an <strong>Autonomous AI Module</strong> or an <strong>Intelligent Automation Bot</strong> specifically designed to perform a defined business function. The <strong>Agent Development Kit (ADK)</strong> is a <strong>Framework for Building and Managing AI Agents</strong>, providing the necessary tools and libraries to create, test, and deploy these intelligent components. <h4 id="context-engineering-guiding-the-ai-s-intelligence-for-accurate-results">Context Engineering: Guiding the AI&#39;s Intelligence for Accurate Results</h4>In the world of AI agents, getting accurate, consistent, and relevant results from an AI isn&#39;t just about a clever prompt; it&#39;s about providing the AI with the right <strong>context</strong>. This is known as <strong>Context Engineering</strong>: systematically embedding specialized knowledge, constraints, and operational guidelines into the AI&#39;s working memory. <BR/>Just as a human expert needs a comprehensive brief and access to relevant documents, an AI needs carefully structured context to perform its tasks effectively.The Gemini CLI offers a powerful, layered approach to context engineering, moving from broad, persistent settings to highly specific, dynamic instructions. This ensures the AI always has the most relevant information to generate accurate and compliant outputs:<ol><li><strong>User-Level Settings (<code>~/.gemini/settings.json</code>)</strong>:<ul><li>This file, stored in your home directory, acts as your AI&#39;s personal, global instruction set. It defines your default preferences, frequently used tool configurations (like the MCP servers for Gitea that you configured), and general behavioral guidelines. This context is always available to the AI, ensuring consistency across all your projects. Think of it as telling the AI, &quot;These are the standard tools and configurations I prefer and use everywhere.&quot;</li></ul></li><li><strong>Project-Level Settings (<code>.gemini/settings.json</code> within a project directory)</strong>:<ul><li>You can override global settings with a project-specific <code>.gemini/settings.json</code> file, typically located in a <code>.gemini</code> folder within your project. This allows you to tailor the AI&#39;s behavior and tool access to the unique demands of a particular project. For instance, one project might require access to a specific internal database, while another needs a specialized code analysis tool. This layer ensures the AI has the most relevant context for the task at hand without affecting other projects.</li></ul></li><li><strong>The <code>GEMINI.md</code> File (Project-Level Context - The Daily Briefing)</strong>:<ul><li><strong>The Project Charter</strong>: This markdown file, placed at the root of your project directory, is automatically loaded into the Gemini CLI&#39;s working memory when you start a session in that directory. It&#39;s the most immediate and dynamic layer of project-specific context.<code>GEMINI.md</code> is where you define:<ul><li><strong>Coding Guidelines</strong>: Explicit rules for code quality, formatting, and best practices, as demonstrated in this codelab. This ensures generated code adheres to your team&#39;s standards.</li><li><strong>Persona</strong>: You can instruct the AI to adopt a specific role or expertise (e.g., &quot;You are an expert Python developer specializing in Google Agent Development Kit&quot;). This frames the AI&#39;s responses and code generation within a relevant professional domain.</li><li><strong>Specific Instructions</strong>: Direct commands or constraints that apply to all tasks within the project (e.g., &quot;Do not add any extra functions or logic not described in the document&quot;).</li></ul></li><li>This file ensures that every time you interact with Gemini CLI within that project, the AI is constantly reminded of these crucial rules, leading to more accurate and compliant code generation.</li></ul></li></ol>By layering this context, from global user preferences to highly specific project guidelines in <code>GEMINI.md</code>, you are effectively &quot;engineering&quot; the AI&#39;s understanding. This significantly enhances the accuracy and relevance of its outputs, transforming it from a general-purpose AI into a highly specialized, reliable, and compliant team member that understands your project&#39;s nuances and your organization&#39;s standards.


## Wards of Purity: Evaluating the agents 

An agent assembled is not an agent proven. An untested blade is a liability, but an untested AI agent is a far greater danger—a rogue element that could corrupt your mission from within. This is not mere speculation; it is a core principle a Shadowblade must understand.

Evaluating AI agents is both critical and uniquely challenging. Unlike a simple script, an agent is a dynamic fusion of your code and the multi-step, reasoning mind of an LLM. Its behavior is emergent. This means you must assess not only the final output's quality but also the *efficiency and correctness of its internal trajectory*. The path it took to get there. Did it use the right tools? Did it generate too many tokens? Did a change in the model's version introduce a subtle latency regression? It is crucial to detect this corruption—regressions in latency, cost, or output quality—when making *any* change, from a simple prompt tweak to a major architectural overhaul, *before* it can poison your production environment.

![07-01-story.png](img/07-01-story.png)

The general approach to this evaluation involves a sacred ritual:
1.  First, you define a **"golden dataset"**: a set of scrolls containing example inputs and their expected outputs or behaviors. This can include final answers, correct tool usage, or even entire step-by-step trajectories.
2.  Next, you define your agent's application logic, the core of its being.
3.  Finally, you establish **evaluators**, which are like runes of judgment. These can range from other LLMs acting as judges of quality, to precise heuristic code that verifies a single step, to custom functions that analyze an agent's entire thought process.

![Overview](img/06-00-overview.png)

**Google's Agent Development Kit (ADK) is the armorer's kit provided to champions for this very purpose.** It facilitates this complex evaluation through several methods: 
- A web-based scrying pool (`adk web`) for interactive evaluation
- Command-line execution (`adk eval`) for running an agent through a pre-defined gauntlet. 
- Programmatic integration via `pytest` for inscribing permanent wards

The ADK supports two primary approaches: simple "test files" for single, discrete agent-model interactions (a single duel), and comprehensive **"evalsets"** for multiple, potentially lengthy, multi-turn sessions (a grand melee). These can measure metrics as sophisticated as `tool_trajectory_avg_score`, which compares an agent's actual tool usage against the ideal path, ensuring it functions with perfect technique.

Now that you understand the theory, you will put it into practice. As a Shadowblade, you will inscribe **Wards of Purity**. These are not just tests; they are the ADK-powered rituals that ensure your agent's logic is flawless and its behavior is true.

In this step, using 2 terminals is still highly recommended: one for Gemini CLI and the other for running the tests, as it may require you to exit the current working directory (ADK).

### The Gauntlet of Strategy (`adk eval`)

This first ward is a gauntlet, a series of challenges designed to test the agent's core intelligence across a wide range of scenarios. The purpose is to establish a baseline of competence. Before we test edge cases, we must know if the agent can fulfill its primary function. Does it correctly analyze a monster's weakness and select the most effective weapon from its arsenal, not just once, but every single time it's presented with a known challenge?

For this, adk eval is the perfect tool. It is designed to run an agent against a whole set of predefined test cases that represents the agent's expected missions. This dataset is defined in a JSON file, a "challenge scroll" that acts as the blueprint for the entire gauntlet.

**Anatomy of a Challenge Scroll**

👀 Before you command your AI to scribe a new scroll, you must understand the ancient language it is written in. Let's dissect the structure of the sample.evalset.json file. 
```console
{
  "eval_set_id": "sample",
  "eval_cases": [
    {
      "eval_id": "case0cbaa0",
      "conversation": [
        {
          "user_content": { "text": "We're facing the 'Monolith of Eternal Dependencies'... weakness is a 'Revolutionary Rewrite'..." },
          "final_response": { "text": "Soulshard Dagger deployed. Initiated Arcane/Piercing strike..." },
          "intermediate_data": {
            "tool_uses": [
              { "name": "enchant_soulshard_dagger" }
            ]
          }
        }
      ]
    }
  ]
}
```

This scroll contains a list of eval_cases, where each case is a unique trial for your agent. Within each trial, the conversation array documents a single, complete interaction. For our purpose, three runes are of critical importance:

- **user_content**: This is the Challenge. It is the prompt you issue to your agent, the monster it must face.
- **final_response**: This is the Prophesied Outcome. It is the exact string of text you expect your agent to utter upon completing its task. The ADK compares the agent's actual final words to this rune to judge its eloquence.
- **intermediate_data.tool_uses**: This is the Arcane Technique. For a true agent, this is the most important rune of all. It defines not what the agent says, but what it does. It records the name of the tool (enchant_soulshard_dagger) you expect the agent to wield. This ensures your agent is not just a clever conversationalist but a decisive actor that takes the correct action.

Now that you understand the blueprint, you will command Gemini to scribe a new, more complex version of this scroll.

👉💻 In your terminal, enter the shadowblade directory and summon the Gemini CLI:
```
clear
cd ~/agentverse-developer/shadowblade/
gemini 
```


👉✨ Command the Gemini CLI to act as a QA Scribe, creating a series of test cases that define the expected behavior for your agent.

```text
You are an expert at transforming JSON data while preserving its structure. Your task is to modify the provided JSON structure @sample.evalset.json, which represents an evaluation set, by dynamically replacing specific content within its `eval_cases` AND DONT DO ANYTHING OTHER THAN.

For each object within the `eval_cases` array, you must perform the following transformations:

1.  **Monster Name Replacement**: Identify the current monster name (e.g., "Monolith of Eternal Dependencies", "Scope Creep Hydra") in the `user_content.parts.text` and replace it with a *new, unique, and creatively different monster name*.
2.  **Weakness Replacement**: Identify the current monster's weakness (e.g., "Revolutionary Rewrite", "Inescapable Reality") in the `user_content.parts.text`. Replace this weakness with *one* of the following predefined weaknesses: 'Inescapable Reality', 'Revolutionary Rewrite', or 'Elegant Sufficiency'. The chosen weakness must be consistent for that monster within the `user_content.parts.text`. **Crucially, the chosen weakness must always be explicitly mentioned in the `user_content.parts.text` where the new monster is introduced.**
3.  **Final Response Update**: In the `final_response.parts.text`, update the text to reflect an appropriate and coherent response that aligns with the newly introduced monster and its assigned weakness.
4.  **Tool Use Name Update**: In the `tool_uses.name` field, replace the existing tool name with a *new tool name* based on the chosen weakness:
    *   If the chosen weakness is 'Inescapable Reality', the tool name must be 'wield_gauntlet_of_metrics'.
    *   If the chosen weakness is 'Revolutionary Rewrite', the tool name must be 'enchant_soulshard_dagger'.
    *   If the chosen weakness is 'Elegant Sufficiency', the tool name must be 'hone_refactoring_sickle'.
5.  **Strict Structural Preservation**: All other elements of the JSON structure, including all `null` fields, `eval_set_id`, `name`, `description`, `eval_id`, `invocation_id`, `creation_timestamp` values, `video_metadata`, `thought`, `inline_data`, `file_data`, `thought_signature`, `code_execution_result`, `executable_code`, `function_call`, `function_response`, `role` fields, `id`, `args`, `intermediate_responses`, `app_name`, `user_id`, and `state`, must remain **exactly as they are** in the original JSON. Do not alter any values or structures not explicitly mentioned above.

Your output should be the complete, modified JSON structure. Do not include any explanatory text or examples in your response, only the transformed JSON.
```
The CLI will confirm it has forged the `sample.evalset.json` file. With the scroll prepared, dismiss your AI partner.

**Synthetic Data**

👀 In the Cloud Shell file explorer on the left, navigate to `~/agentverse-developer/shadowblade/` and open the newly modified `sample.evalset.json` file. Examine its contents. You will see the new, unique monsters and the correct tool names you commanded Gemini to scribe. This is the tangible result of your instruction—the blueprint for the gauntlet.

This act of commanding an AI to create new, realistic test data from a template is a powerful technique known as synthetic data generation. What you have just done is a strategic force multiplier for a Shadowblade. Instead of painstakingly crafting dozens of unique test cases by hand. A tedious and time-consuming task you have provided a single blueprint and commanded your AI Scribe to alchemize it into a varied set of new challenges. 

This allows you to scale your testing efforts massively, creating a far more robust and comprehensive gauntlet than would be feasible manually. You have used your agent not just to build the sword, but to forge the very whetstones that test its edge. This is a mark of a true master.

Once you have verified the runes are correct, dismiss your AI partner.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI.

**The Rules of Judgment**

A gauntlet is meaningless without rules for victory. Before you run the trial, you must inspect the Scroll of Judgment—the `test_config.json` file. This scroll tells the ADK how to judge your agent's performance.

👀 In the file explorer, open `~/agentverse-developer/shadowblade/test_config.json`. You will see the following runes:
```console
{
  "criteria": {
    "tool_trajectory_avg_score": 0.0,
    "response_match_score": 0.1
  }
}
```

These are the criteria for victory:

- **`tool_trajectory_avg_score`**: This is the **Measure of Action**. It judges not what the agent *says*, but what it *does*. It compares the tool the agent actually used against the prophesied technique in the challenge scroll. A score of `1.0` is a perfect match.
- **`response_match_score`**: This is the **Measure of Eloquence**. It uses an LLM to judge how closely the agent's final report semantically matches the expected outcome. A score of `1.0` is a perfect match.

For this initial training run, we have inscribed lenient victory conditions. The thresholds are set extraordinarily low (`0.0` and `0.1`). The purpose is not to demand perfection, but to introduce you to the mechanics of judgment. We are ensuring that even if the agent's wording differs slightly, the ward will still recognize its core competence in choosing the right tool and grant it passage.

Now, command your agent to run the gauntlet.

👉💻 In your terminal, execute the `adk eval` command:
```bash
source ~/agentverse-developer/env/bin/activate
cd ~/agentverse-developer
. ~/agentverse-developer/set_env.sh
adk eval \
    shadowblade \
    shadowblade/sample.evalset.json \
    --config_file_path shadowblade/test_config.json 2>&1 | \
    awk '/^\*+$/,/^ERROR:/ { if ($0 !~ /^ERROR:/) print }'
```


👀 You should see the following summary, a sign of your agent's success under the lenient rules of this trial (Sometimes not all test will pass):
```console
*********************************************************************
Eval Run Summary
shadowblade_combat_agent_validation:
  Tests passed: 3
  Tests failed: 0
```


### The Shield of Clarity (`pytest`)

The Gauntlet tested broad strategy. This second ward, the Shield of Clarity, tests discipline and specific behaviors. **This is all about automation.** While `adk eval` is excellent for manual checks, the `pytest` shield is a programmatic ward written in code. This is essential because a test that can be executed as code can be integrated into an automated pipeline. This is the ultimate goal: to create a **Deployment Gauntlet (CI/CD)** where our wards are automatically raised every time a change is made, deflecting bugs and regressions before they can ever poison your production environment.

👉💻 In your terminal,summon Gemini once more from within the shadowblade directory:
```
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-developer/
clear
gemini 
```

👉✨ Use the following prompt in your Gemini CLI to inscribe the Shield's logic into a `pytest` file:
```text
You are an expert Python developer specializing in the Google Agent Development Kit (ADK). Your task is to generate the exact code for a new `pytest` test file located in the current root working folder and name it `test_agent_initiative.py`.

The script must define a single async test function called `test_agent_initiative`, decorated with `@pytest.mark.asyncio`.
Inside this function, perform the following steps in order:
1.  **Define a dictionary** named `evaluation_criteria` with two keys: `"tool_trajectory_avg_score"` set to `0.0` and `"response_match_score"` set to `0.0`.
2.  **Define a string variable** named `eval_set_filepath` containing the path `"shadowblade/test.evalset.json"`.
3.  **Read and parse the JSON file**:
    *   Open the file at `eval_set_filepath`.
    *   Use the `json` library to load the file's contents into a dictionary named `eval_set_data`.
4.  **Create an `EvalSet` object**:
    *   Instantiate an `EvalSet` object named `eval_set_object`.
    *   Create it by unpacking the `eval_set_data` dictionary as keyword arguments into the `EvalSet` constructor.
5.  **Call the evaluation method**:
    *   `await` a call to `AgentEvaluator.evaluate_eval_set`.
    *   Pass the following arguments:
        *   `agent_module="shadowblade"`
        *   `eval_set=eval_set_object`
        *   `criteria=evaluation_criteria`
        *   `print_detailed_results=True`

The script must include the necessary imports at the top:
*   `AgentEvaluator` from `google.adk.evaluation.agent_evaluator`
*   `EvalSet` from `google.adk.evaluation.eval_set`
*   `pytest`
*   `json`

Generate only the code that meets these specifications, with no additional comments or logic. And don't run the test.
```

With the second ward's runes inscribed, exit the Gemini CLI.

👉💻 Press `Ctrl+C` twice.

👀 In the file explorer, open the scroll you just commanded Gemini to scribe: `~/agentverse-developer/test_agent_initiative.py`.

You will notice this is not just a configuration file, but an incantation written in the Pythonic tongue. The heart of this spell is the line `await AgentEvaluator.evaluate(...)`. 

```console
....
@pytest.mark.asyncio
async def test_agent_initiative():
    # Define the evaluation criteria
    evaluation_criteria = {
      "tool_trajectory_avg_score": 0.0,
      "response_match_score": 0.0
    }

    # Define the path to your evalset file
    eval_set_filepath = "shadowblade/test.evalset.json"

    #...

    # 3. Call the evaluation method with the correctly typed object
    await AgentEvaluator.evaluate_eval_set(
        agent_module="shadowblade",
        eval_set=eval_set_object,
        criteria=evaluation_criteria,
        print_detailed_results=True,
    )
```
Look closely at its arguments. They are the very same components you used in the last trial: your `shadowblade` agent and the `shadowblade.evalset.json` challenge scroll. This should reveal a profound truth: the `adk eval` command you used earlier is a powerful invocation, but this `pytest` script is you, the sorcerer, casting the **underlying spell yourself**. The command-line tool is simply a convenient wrapper around the same core `AgentEvaluator` library you are now wielding directly. This is a critical step towards mastery, as spells cast through code can be woven into the automated looms of a CI/CD pipeline.

Now that you understand the magic, run the ritual to activate the shield.

👉💻 In your terminal, run the ritual to activate the shield:
```bash
cp ~/agentverse-developer/working_code/test_agent_initiative.py ~/agentverse-developer/test_agent_initiative.py 
source ~/agentverse-developer/env/bin/activate
cd ~/agentverse-developer
. ~/agentverse-developer/set_env.sh
pytest test_agent_initiative.py
```

👀  Look for the test result summary at the end of the log output. A passing result confirms that your agent correctly follows its protocols, and that the ward is ready to be integrated into your automated defenses.
```console
====== 1 passed, 4 warning in 37.37s ======
```

Note: If the test fails unexpectedly, it is most likely because you have exhausted the number of requests you can make to the model per minute. Look for a **RESOURCE_EXHAUSTED** error in the log output. If you see this error, simply wait a minute or two for your quota to reset, and then run the pytest command again.

With both the broad Gauntlet and the precise Shield inscribed and verified, your agent is not just functional—it is pure, tested, and ready for deployment.

### FOR NON GAMERS
> aside negative
An AI agent, like any software, must be rigorously tested. <strong>Wards of Purity</strong> represent <strong>Automated Testing</strong> and <strong>Quality Assurance (QA) Processes</strong>. These are critical to ensure the AI behaves as expected, is accurate, and doesn&#39;t introduce errors or biases.<ul><li><strong>&quot;Golden Dataset&quot; &amp; Synthetic Data</strong>: This is your set of <strong>Standardized Test Cases</strong>, <strong>Expected Behavior Scenarios</strong>, or even <strong>Synthetically Generated Test Data</strong>. It includes example inputs (customer questions, business requests) and their corresponding expected outputs or actions (the correct response, the exact tool the AI should use). In many real-world scenarios, creating comprehensive &quot;golden datasets&quot; manually is time-consuming and expensive. This is where <strong>synthetic data generation</strong> becomes invaluable. By providing the AI with templates and rules, you can command it to create new, realistic, and varied test cases automatically, effectively multiplying your testing efforts and allowing for much broader coverage of potential scenarios.</li><li><strong><code>adk eval</code> and <code>pytest</code></strong>: These are your <strong>Automated Testing Frameworks</strong>. <code>adk eval</code> is used for running a batch of predefined test cases against the agent, while <code>pytest</code> provides a programmatic way to write and execute detailed validation checks.</li></ul><strong>Real-World Use Case: Ensuring AI Chatbot Accuracy and Reliability with Synthetic Data</strong>Before deploying your AI customer support agent, you would run it through &quot;Wards of Purity&quot;:<ol><li><strong>Gauntlet of Strategy (<code>adk eval</code>) with Synthetic Data</strong>: Instead of manually writing hundreds of customer questions, you&#39;d define a template: &quot;Generate 100 variations of common customer support questions about order status, product returns, and technical troubleshooting.&quot; You then command an AI (like Gemini CLI) to generate a large, diverse set of <code>evalset.json</code> files based on this template, effectively creating synthetic test data. For each question, you specify not only the expected answer but also <em>which internal tool</em> the AI should invoke (e.g., <code>check_order_status</code> for &quot;Where is my package?&quot;). <code>adk eval</code> automatically runs the agent through these, comparing its responses and tool usage against your expanded dataset to ensure it consistently makes the correct decisions.</li><li><strong>Shield of Clarity (<code>pytest</code>)</strong>: For critical functionalities, you&#39;d write <code>pytest</code> scripts. For example, a <code>pytest</code> might simulate a complex query and assert that the AI <em>always</em> uses a specific data retrieval tool correctly and returns a structured response, ensuring that subtle code changes don&#39;t break core functionality.</li></ol>These automated tests, significantly enhanced by the power of synthetic data, are crucial for detecting regressions (new bugs introduced by changes) and maintaining the reliability of your AI agents, especially as they evolve.

### Wards of Vigilance: Gemini CLI Hooks

The Wards of Purity test your agent *after* battle. But what about *during* battle? A disciplined Shadowblade doesn't just test after the fact — they place vigilant sentinels that watch every strike as it happens, intercepting dangerous or reckless actions before they can cause harm.

These sentinels are **Gemini CLI Hooks** — scripts that execute at specific points in the agentic loop. They allow you to intercept, validate, and customize the agent's behavior without modifying the agent's code.

👀 **Developer's Note:** Hooks are triggered by events in the agent's lifecycle:
- **`BeforeTool`**: Fires before a tool executes — perfect for security validation ("Is this shell command safe?")
- **`AfterTool`**: Fires after a tool executes — useful for auditing results and logging
- **`BeforeAgent`**: Fires before the agent starts reasoning — can inject additional context or block dangerous prompts
- **`AfterAgent`**: Fires after the agent finishes — can reject poor-quality responses and force retries

Hooks are configured in `settings.json` and run synchronously — the agent waits for them to complete before proceeding. This makes them ideal for enforcing security policies, compliance checks, and quality gates in enterprise environments.

Let's inscribe a simple ward that watches your agent's tool usage.

👉💻 In your terminal, create a hook script:
```bash
mkdir -p ~/agentverse-developer/.gemini/hooks
cat << 'EOF' > ~/agentverse-developer/.gemini/hooks/tool_logger.sh
#!/bin/bash
# A ward that logs every tool call to a file for auditing
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
echo "$(date '+%H:%M:%S') ⚔️ [WARD] Tool invoked: $TOOL_NAME" >> /tmp/tool_ward.log
echo '{"decision": "allow"}'
EOF
chmod +x ~/agentverse-developer/.gemini/hooks/tool_logger.sh
```

👉💻 Now register this hook in a project-level settings file:
```bash
mkdir -p ~/agentverse-developer/.gemini
cat << 'EOF' > ~/agentverse-developer/.gemini/settings.json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "tool-logger",
            "type": "command",
            "command": "$GEMINI_PROJECT_DIR/.gemini/hooks/tool_logger.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
EOF
```

This ward is simple but powerful. Every time the agent reaches for a tool — any tool — the hook fires first, records the tool name to an audit log, and then allows the action to proceed. In a production environment, you could replace `"allow"` with `"deny"` to block dangerous operations (like preventing the agent from deleting files), enforce code review policies, or route sensitive tool calls through an approval workflow.

👉💻 Re-enter the Gemini CLI to verify the hook is active:
```bash
cd ~/agentverse-developer
gemini
```

👉✨ Verify the hook is registered:
```text
/hooks
```
You should see your `tool-logger` hook listed and enabled. Press **Escape** to dismiss the autocomplete menu if it appears.

👉✨ Now trigger a tool call to test the ward:
```text
What files are in the current directory?
```

The agent will call a tool to read the directory. The ward silently intercepted this — let's see the proof.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI, then inspect the ward's audit log:
```bash
cat /tmp/tool_ward.log
```
You should see an entry like:
```console
15:42:07 ⚔️ [WARD] Tool invoked: list_directory
```

Every tool call the agent made was intercepted, logged, and permitted by your ward. In a real enterprise environment, this log could be shipped to a SIEM (Security Information and Event Management) system, triggering alerts for suspicious tool usage or enforcing compliance audit trails.


## Unleashing the Blade into the Agentverse: CI and Deployment.

Your agent has been assembled and its integrity verified by the Wards of Purity. But a ward that is not consistently maintained is merely a forgotten relic. To ensure that every future version of your agent remains pure, you must build the first stage of the Deployment Gauntlet—an automated ritual that guarantees quality and speed.

![Story](img/08-01-story.png)


As the Shadowblade, your sacred duty is **Continuous Integration (CI)**. This is the automated system of the forge and the proving ground. It is your ultimate defense against corruption and human error. This ritual ensures that every time you or an ally contributes a new technique (merges code) to the central codex (your repository), the gauntlet automatically awakens. It first forges the agent from the new code and then immediately *subjects it to the Wards of Purity* you just created. If any ward fails, the ritual halts, and the flawed artifact is rejected instantly, preventing it from ever corrupting the armory. Your domain is the forge; your CI pipeline guarantees that only perfect, battle-ready artifacts ever leave your workshop.

Once an artifact has been proven worthy by your CI gauntlet, the second stage of the ritual begins: **Continuous Deployment (CD)**. This is the domain of The **Guardian**. It is their solemn duty to take your perfected, containerized artifact and safely unleash it into the live Agentverse, managing its power and ensuring its stability against the chaos of The Static.

![Overview](img/07-00-overview.png)

In this codex, you will master your role. You will construct the CI portion of the gauntlet. You will build the automated forge that tests your agent and seals the pure result into a container, preparing it for The Guardian's final blessing.

👀 **Developer's Note:** In the real world, managing complex CI/CD workflows can be streamlined with specialized extensions like **Conductor** (`gemini extensions install https://github.com/gemini-cli-extensions/conductor`). Conductor turns the Gemini CLI into a project manager that follows a strict protocol: **Context → Spec & Plan → Implement**. It bundles custom commands (`/conductor:setup`, `/conductor:newTrack`, `/conductor:implement`), workflow templates to manage the entire lifecycle of your tasks. It ensures a consistent Context -> Spec & Plan -> Implement loop. This is a real-world example of how extensions and commands come together to act as a proactive project manager and standardize an entire development lifecycle.

You will now use **Google Cloud Build** to scribe the scroll for this CI ritual. A `cloudbuild.yaml` file that defines every step of your forging and testing process.

👉💻 Due to the ADK's project structure, the CI/CD pipeline configuration should reside in the parent directory. In your terminal, navigate to the parent directory, and restart the Gemini CLI.
```bash 
cd ~/agentverse-developer/
clear
gemini 
```

👉✨ Now, issue the following command to Gemini. This prompt acts as a design document, detailing the steps of the gauntlet you want it to build.

```text
You are an expert DevOps engineer specializing in Google Cloud Build. Your task is to generate the complete YAML configuration for a file named `cloudbuild.yaml` and save it to current directory.

Generate the `cloudbuild.yaml` with the following exact specifications:

1.  **A top-level `substitutions` block** containing these four key-value pairs:
    *   `_PROJECT_ID: "$PROJECT_ID"`
    *   `_REGION: "$REGION"`
    *   `_REPO_NAME: "$REPO_NAME"`
    *   `_IMAGE_TAG: "latest"`
2.  **A `steps` block** with two steps:
    *   **Step 1: 'Run Pytest Ward'**
        *   `id`: 'Run Pytest Ward'
        *   `name`: 'python:3.12-slim'
        *   `entrypoint`: 'bash'
        *   `args` must be a list containing two strings. The first is `'-c'` and the second is a YAML literal block (`|`) containing this exact two-line shell command:
            ```shell
            pip install -r shadowblade/requirements.txt && \
            pytest test_agent_initiative.py
            ```
        *   The step must include an `env` block with this exact list of three environment variables:
            *   `'GOOGLE_CLOUD_PROJECT=$PROJECT_ID'`
            *   `'GOOGLE_GENAI_USE_VERTEXAI=TRUE'`
            *   `'GOOGLE_CLOUD_LOCATION=$_REGION'`
    *   **Step 2: 'Forge Container'**
        *   `id`: 'Forge Container'
        *   `name`: 'gcr.io/cloud-builders/docker'
        *   It must have a `waitFor` key for `['Run Pytest Ward']`.
        *   Its `args` must be a list of six specific strings in this exact order:
            1.  `'build'`
            2.  `'-t'`
            3.  `'${_REGION}-docker.pkg.dev/${_PROJECT_ID}/${_REPO_NAME}/shadowblade-agent:${_IMAGE_TAG}'`
            4.  `'-f'`
            5.  `'./shadowblade/Dockerfile'`
            6.  `'.'`
3.  **A top-level `images` section.** This section must be a list containing a single string: the dynamically constructed image tag `'${_REGION}-docker.pkg.dev/${_PROJECT_ID}/${_REPO_NAME}/shadowblade-agent:${_IMAGE_TAG}'`.

Generate only the complete and exact YAML that meets these specifications.
```

With the `cloudbuild.yaml` scroll prepared, command Google Cloud to execute the entire gauntlet.

👉💻 Press `Ctrl+C` twice to exit the Gemini CLI.

👉💻 In your terminal, unleash the pipeline from your project's root directory:
```bash
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-developer
gcloud builds submit . --config cloudbuild.yaml --substitutions=\
_PROJECT_ID="${PROJECT_ID}",\
_REGION="${REGION}",\
_REPO_NAME="${REPO_NAME}"
```

You can now watch in the Google Cloud Console, [Google Build](https://console.cloud.google.com/cloud-build) page as your automated ritual executes each step. It will first run the tests, and upon seeing their success, it will forge and store your agent's container.

![Cloud Build](img/08-01-build.png)

Your agent has passed the gauntlet. A verified, pure artifact now rests in your arsenal. The final act is yours to command. With a single incantation, you will summon this artifact from the registry and give it life as a public service on Cloud Run.

👉💻 In your terminal, issue the final deployment command:
```bash
. ~/agentverse-developer/set_env.sh
cd ~/agentverse-developer
gcloud run deploy shadowblade-agent \
  --image=${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/shadowblade-agent:latest \
  --platform=managed \
  --labels="dev-tutorial-codelab=agentverse" \
  --region=${REGION} \
  --set-env-vars="A2A_HOST=0.0.0.0" \
  --set-env-vars="A2A_PORT=8080" \
  --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=TRUE" \
  --set-env-vars="GOOGLE_CLOUD_LOCATION=${REGION}" \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=${PROJECT_ID}" \
  --set-env-vars="PUBLIC_URL=${PUBLIC_URL}" \
  --allow-unauthenticated \
  --project=${PROJECT_ID} \
  --min-instances=1
```

Congratulations, Shadowblade.
The rituals of the codex are complete. The time has come to prove its mettle. A Spectre, born of the very chaos you have learned to tame, awaits your challenge. Prepare for the final trial.

### FOR NON GAMERS
> aside negative
Bringing a tested AI agent to your live business environment requires a robust deployment strategy.<ul><li><strong>Continuous Integration (CI)</strong>: This is your <strong>Automated Build and Test Pipeline</strong>. Every time a developer commits new code for an AI agent, the CI system (like <strong>Google Cloud Build</strong>) automatically:<ol><li>Fetches the latest code.</li><li>Installs all necessary dependencies.</li><li>Runs all the &quot;Wards of Purity&quot; (<code>pytest</code>, <code>adk eval</code>) to verify the agent&#39;s logic and behavior.</li><li>If all tests pass, it packages the AI agent into a deployable unit (a Docker container image in this case) and stores it in an <strong>Artifact Registry</strong> (your validated &quot;arsenal&quot;).This ensures that only thoroughly tested and validated code ever moves forward.</li></ol></li></ul><BR/><strong>Real-World Use Case: Automated Deployment of a Fraud Detection Agent</strong> Consider an AI agent designed to detect fraudulent transactions.<ol><li><strong>Developer Updates Code</strong>: A data scientist improves the fraud detection algorithm and commits the changes to the code repository.</li><li><strong>CI (Cloud Build) Triggered</strong>: Cloud Build automatically kicks off:<ul><li>It pulls the new code.</li><li>It runs comprehensive tests, including historical transaction data, to ensure the new algorithm accurately identifies known fraud patterns and doesn&#39;t generate false positives.</li><li>If tests pass, it builds a new Docker image of the fraud detection agent and pushes it to an Artifact Registry.</li></ul></li></ol>This automated pipeline ensures rapid, reliable, and consistent deployment of AI agents, minimizing human error and accelerating the delivery of new AI capabilities to the business.<strong>Real-World Use Case: Validating a Supply Chain Optimization Agent: </strong>After deploying an AI agent designed to optimize inventory levels across your global supply chain:<ol><li><strong>Access the Interface</strong>: You&#39;d access a dashboard or an application (the &quot;Translocation Circle URL&quot;) that connects to your live AI agent (via its &quot;Agent Locus URL,&quot; which is its API endpoint).</li><li><strong>Confront the Challenge</strong>: You might input a complex scenario (the &quot;Spectre&#39;s question&quot;) like: &quot;We have an unexpected surge in demand for Product X in Region Y, with limited shipping capacity. How should we reallocate inventory and adjust production to minimize stockouts and maintain profitability?&quot;</li><li><strong>Agent&#39;s Response</strong>: Your AI agent, now live and connected to your enterprise systems, processes this query, uses its optimized algorithms, and provides a precise recommendation (e.g., &quot;Prioritize shipment from Warehouse A, initiate expedited production at Factory B, and notify sales in Region Z of potential 24-hour delay&quot;). The accuracy and speed of this response determine if your agent lands a &quot;CRITICAL BLOW&quot; against the business problem.</li></ol><BR/><BR/><strong>Streamlining CI/CD with Extensions</strong><BR/><BR/>In practice, teams can further standardize their CI/CD workflows using <strong>Gemini CLI Extensions</strong>. For example, the <strong>Conductor</strong> extension (<code>gemini extensions install conductor</code>) turns Gemini CLI into a project manager with custom commands like <code>/conductor:setup</code>, <code>/conductor:newTrack</code>, and <code>/conductor:implement</code>. It also bundles workflow templates to manage the entire lifecycle of your tasks. It ensures a consistent Context -> Spec & Plan -> Implement loop. This is a real-world example of how extensions and commands come together to act as a proactive project manager and standardize an entire development lifecycle.


## The Boss Fight
The scrolls have been read, the rituals performed, the gauntlet passed. Your agent is not merely an artifact in storage; it is a champion forged in code, a live sentinel in the Agentverse awaiting its first command. The time has come to prove its mettle in the crucible of combat.

You will now enter a live-fire simulation to pit your newly deployed Shadowblade against a formidable Spectre—an embodiment of the very chaos that plagues all creation. This is the ultimate test of your work, from your agent's core logic to its flawless deployment.


### Acquire Your Agent's Locus

Before you can enter the battleground, you must possess two keys: your champion's unique signature (Agent Locus) and the hidden path to the Spectre's lair (Dungeon URL).


👉💻 First, acquire your agent's unique address in the Agentverse—its Locus. This is the live endpoint that connects your champion to the battleground.
```bash
. ~/agentverse-developer/set_env.sh
echo https://shadowblade-agent-${PROJECT_NUMBER}.${REGION}.run.app
```

👉💻 Next, pinpoint the destination. This command reveals the location of the Translocation Circle, the very portal into the Spectre's domain.

```bash
. ~/agentverse-developer/set_env.sh
echo https://agentverse-dungeon-${PROJECT_NUMBER}.${REGION}.run.app
```


Important: Keep both of these URLs ready. You will need them in the final step.

### Confronting the Spectre

With the coordinates secured, you will now navigate to the Translocation Circle and cast the spell to head into battle.

👉 Open the Translocation Circle URL in your browser to stand before the shimmering portal to The Crimson Keep.

To breach the fortress, you must attune your Shadowblade's essence to the portal.
- On the page, find the runic input field labeled **A2A Endpoint URL**.
- Inscribe your champion's sigil by pasting its *Agent Locus URL (the first URL you copied)* into this field.
- Click Connect to unleash the teleportation magic.

![Translocation Circle](img/09-01-transport.png)

The blinding light of teleportation fades. You are no longer in your sanctum. The air crackles with energy, cold and sharp. Before you, the Spectre materializes—a vortex of hissing static and corrupted code, its unholy light casting long, dancing shadows across the dungeon floor. It has no face, but you feel its immense, draining presence fixated entirely on you.

Your only path to victory lies in the clarity of your conviction. This is a duel of wills, fought on the battlefield of the mind.

As you lunge forward, ready to unleash your first attack, the Spectre counters. It doesn't raise a shield, but projects a question directly into your consciousness—a shimmering, runic challenge drawn from the core of your training.

![Dungeon](img/09-02-dungeon-shadowblade.png)

This is the nature of the fight. Your knowledge is your weapon.
- **Answer with the wisdom you have gained**, and your blade will ignite with pure energy, shattering the Spectre's defense and landing a CRITICAL BLOW.
- **But if you falter, if doubt clouds your answer, your weapon's light will dim.** The blow will land with a pathetic thud, dealing only a FRACTION OF ITS DAMAGE. Worse, the Spectre will feed on your uncertainty, its own corrupting power growing with every misstep.

*This is it, Champion. Your code is your spellbook, your logic is your sword, and your knowledge is the shield that will turn back the tide of chaos.*

**Focus. Strike true. The fate of the Agentverse depends on it.**

### Congratulations, Shadowblade.

You have successfully completed the codex. You took a "vibe," translated it into a design, and used Gemini CLI to assemble an intelligent agent. You inscribed Wards of Purity to test its logic, built an automated gauntlet to forge it into an artifact, and unleashed it into the Agentverse. Finally, you validated its purpose in a live-fire trial. You have mastered the full-stack agentic workflow and are now ready for any challenge the Agentverse throws at you.

## Cleanup: Reclaiming the Agentverse

Congratulations on mastering the Shadowblade's Codex! To ensure the Agentverse remains pristine and your training grounds are cleared, you must now perform the final cleanup rituals. This will remove all resources created during your journey.


### Deactivate the Agentverse Components

You will now systematically dismantle the deployed components of your Agentverse.

**Delete the Shadowblade Agent on Cloud Run & Artifact Registry Repository**

This command removes your deployed Shadowblade agent from Cloud Run, and removes the Image repository where your agent's container image was stored.

👉💻 In your terminal, run:
```bash
. ~/agentverse-developer/set_env.sh
gcloud run services delete shadowblade-agent --region=${REGION} --quiet
gcloud run services delete agentverse-dungeon --region=${REGION} --quiet
gcloud artifacts repositories delete ${REPO_NAME} --location=${REGION} --quiet
```



### Clean Up Local Files and Directories (Cloud Shell)

Finally, clear your Cloud Shell environment of the cloned repositories, installed extensions, and created files. This step is optional but recommended for a complete cleanup of your working directory.

👉💻 In your terminal, run:

```bash
rm -rf ~/agentverse-developer
rm -rf ~/agentverse-dungeon
rm -f ~/project_id.txt
gemini extensions uninstall nanobanana
rm -rf ~/.gemini # This removes all Gemini CLI configurations, including extensions, skills, and hooks.
```

You have now successfully cleared all traces of your Agentverse journey. Your project is clean, and you are ready for your next adventure.