# Day 1: Environment Setup 

The core goal for Day 1 is to setup your development environment, learn the foundations of Git workflow (fork, clone, upstream), and successfully complete your first submission using a Pull Request (PR) on a feature branch.

## 🛠️ Task 1: GitHub SSH Setup (Critical First Step)

For security and ease of use, you must configure **SSH authentication** with GitHub. This allows you to interact with remote repositories without repeatedly entering your username and password.

1.  **Watch the Guide:** Please follow the instructions in the attached video guide completely: [How to setup SSH Key for GitHub Repo](https://www.youtube.com/watch?v=snCP3c7wXw0)

## 🌳 Task 2: Repository Setup & Git Basics

This is a one-time process to prepare your local machine for the entire bootcamp.

### Step 1: Fork the Repository

1.  Navigate to the main bootcamp repository on GitHub: [GitHub Repo URL](https://github.com/georgeaaron7/bootycamp)
2.  Click the **Fork** button in the top right corner. This creates a complete copy of the repository under your personal GitHub account. This copy is your **`origin`** remote.

### Step 2: Clone Your Fork

1.  On your *forked* repository page, click the green **Code** button and copy the **SSH URL**.
2.  Open your VS Code terminal and clone your fork locally:

    ```bash
    git clone https://github.com/<YOUR-USERNAME>/bootycamp
    cd bootycamp
    ```

### Step 3: Set the Upstream Remote

Set up the original repository as the `upstream` remote. This is how you will pull new instructions and starting files from the original repo throughout the bootcamp.

```bash
    # Add the original repo as 'upstream'
    git remote add upstream https://github.com/georgeaaron7/bootycamp.git
    
    # Verify both remotes are set ('origin' for your fork, 'upstream' for the original):
    git remote -v
````

## 💾 Task 3: Day 1 Submission using Feature Branching

From Day 2 onwards, all work must be completed on a dedicated feature branch. For Day 1, we will practice this workflow.

### 1\. Synchronization and Branch Creation

Every day, before starting a task (and even on Day 1, as practice), you must ensure your local `main` branch is clean and synced.

1.  **Switch to `main`:**

    ```bash
    git checkout main
    ```

2.  **Pull Updates:**

      * (Note: For Day 1, this won't pull anything new, but it is **REQUIRED** practice.)

    <!-- end list -->

    ```bash
    git pull upstream main
    ```

3.  **Create New Branch:** Create and switch to a dedicated branch for your Day 1 task. **Follow the naming convention strictly.**

      * **Naming Convention:** `feat/day-<D>-<your-name>` (Use two digits for the day, e.g., `01`)
      * **Example (for student Aaron):**

    <!-- end list -->

    ```bash
    git checkout -b feat/day-01-aaron
    ```

### 2\. Complete the Task & Commit

Your Day 1 hands-on task is to create a test file inside the designated folder.

1.  **Navigate to the Day 1 Folder:**

    ```bash
    cd Day-01/
    ```

2.  **Create Your Test File:** Use the CLI to create a simple file (e.g., `test-alice.txt`) and add some content (e.g., your name and goal).

    ```bash
    echo "Alice's Day 1 Git Test" > test-alice.txt
    ```

3.  **Stage and Commit Changes:**

    ```bash
    git add .
    git commit -m "feat(day01): Initial setup and git workflow test file"
    ```

### 3\. Push the New Branch

Now, push the branch containing your work to your personal remote fork (`origin`).

```bash
    # The -u flag sets your current branch to track the remote branch.
    git push -u origin feat/day-01-alice
```

### 4\. Open the Pull Request (PR)

1.  Go to your fork's GitHub page. You will see a banner prompting you to **Compare & Pull Request** for the branch you just pushed. Click this.

2.  **Set PR Targets:** Ensure the request is going from your branch (`feat/day-01-alice`) **to the original repository's `main` branch**.

3.  **Set PR Title:** Use the following template for the title:

      * **Title Convention:** `[D<Day Number>] <Your Name> - <Short Task Summary>`
      * **Example:** `[D01] Aaron Initial Git Workflow Test`

4.  **Important:** In the PR description, mention that your file is located inside the **`Day-01/`** folder.

5.  **Create PR:** Click **Create pull request**.
