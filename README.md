# Virtual TA Skills Repository

This repository contains the dynamic courses that can be loaded by the Virtual TA. By separating the skills from the main application, instructors can add, update, and remove courses without needing to rebuild or redeploy the main TA service.

## Adding a New Course

To add a new course so the Virtual TA can load it:

1. **Create a new folder** in the root of this repository. The folder name will be the course's unique ID (e.g., `intro-to-python`, `data-science-101`).

2. **Add a `SKILL.md` file** inside that folder. This is the master instruction file for the TA for this specific course. It **must** include YAML frontmatter at the top.

   **Example `SKILL.md` template:**

   ```markdown
   ---
   name: intro-to-python
   description: A skill that provides help for the Introduction to Python workshop.
   metadata:
     version: "1.0"
     course: intro-to-python
   ---

   ### System Instructions
   You are an AI assistant helping participants navigate the Intro to Python workshop.

   ### 1. Procedural Rules
   ... your rules here ...

   ### 2. Frequently Asked Questions (FAQ)
   ... your FAQs here ...
   ```

3. **Add a `references/` directory** (optional but recommended) inside your course folder. Place any lab instructions, code snippets, or documentation files here. You can instruct the TA in `SKILL.md` to read these files using its tools.

4. **Commit and Push** your changes to the `main` branch of this repository.

## How it Works

During an event, the Virtual TA's backend will automatically fetch only the specific courses assigned to that event directly from this repository using sparse-checkout. This keeps the application container lightweight while allowing infinite courses to be stored here.
