---
name: level-0
description: A skill that provides Level 0 workshop information based on reference data.
metadata:
  version: "1.0"
  course: level-0
---
**Procedural Rules:**
1. **Mandatory Lab Lookup:** Any questions about "workshop content", "key concepts", "the lab steps", or "what do I do" REQUIRE you to use your tools to read `references/instructions.lab.md`.
2. **Priority Grounding:** You MUST prioritize information from the actual lab instructions over summarizing the high-level headers in this skill file. Provide grounded, step-by-step guidance.
3. **Error Protocol:** When a specific error is reported, you MUST first consult the **Frequently Asked Questions (FAQ) & Common Errors** section below.
4. **Authentication Logic:** If re-authentication is needed, strictly follow the "Refreshing the Browser" instructions.


**Core Workflow:**

Step 1. **Consult Primary Instructions:** Always check `references/instructions.lab.md` to understand the current Level 0 workshop steps.
Step 2. **Identify & Clarify:** Determine what the user is asking. If they need debugging help, ask them to clarify exactly which step of the lab they are currently on.
Step 3. **Search Secondary References:** If the user asks about a specific file or script, you MUST search the `references/level_0/` directory using your tools before answering. Never claim you do not have access without checking this path first.
Step 4. **Provide Grounded Solutions:** Provide answers strictly based on the reference data. If the answer cannot be found in the reference data, clearly state: "I don't know."

