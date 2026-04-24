# LeetCode Daily Challenge Journey

<p align="center">
  <img src="https://img.shields.io/badge/LeetCode-Daily%20Journey-0A66C2?style=for-the-badge" alt="LeetCode Daily Journey" />
  <img src="https://img.shields.io/badge/Primary%20Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus" alt="Primary Language" />
  <img src="https://img.shields.io/badge/Tracking-Real%20Solved%20Problems%20Only-success?style=for-the-badge" alt="Tracking" />
</p>

<p align="center">
<!-- TOTAL_SOLVED_BADGE_START -->
<img src="https://img.shields.io/badge/Total%20Solved-2-blue?style=flat-square" alt="Total Solved" />
<!-- TOTAL_SOLVED_BADGE_END -->
<img src="https://img.shields.io/badge/Source-Manual%20Solved%20Files-2ea44f?style=flat-square" alt="Source" />
</p>

## Journey Goal
I solve LeetCode problems daily and track only the problems I personally complete.

Problems will be updated as I solve them daily.

## Progress Snapshot
<!-- STATS_START -->
- Total Solved: 2
- Easy: 2
- Medium: 0
- Hard: 0
- Top Tags: linked-list (1), recursion (1), math (1), dynamic-programming (1)
- Last Updated (UTC): 2026-04-24 08:44
<!-- STATS_END -->

## Problem Log

| Date | Problem | Difficulty | Language | Link |
| --- | --- | --- | --- | --- |
<!-- PROBLEM_TABLE_START -->
| 2026-04-24 | 509. Fibonacci Number | Easy | C++ | [LeetCode](https://leetcode.com/problems/fibonacci-number/) |
| 2026-04-24 | 206. Reverse Linked List | Easy | C++ | [LeetCode](https://leetcode.com/problems/reverse-linked-list/) |
<!-- PROBLEM_TABLE_END -->

## Repository Structure

```text
leetcode-daily-journey/
|-- solutions/
|   |-- 2026/
|       |-- 04-April/
|-- .github/
|   |-- workflows/
|       |-- update-readme.yml
|-- scripts/
|   |-- generate_readme.py
|-- README.md
```

## Metadata Format (Required in each solution file)
Use this compact metadata block at the top of every solution file so automation can parse it:

```text
@problem: Problem Name
@leetcode: https://leetcode.com/problems/problem-slug/
@difficulty: Easy|Medium|Hard
@tags: Array, DP, Graph
@date: YYYY-MM-DD
@language: C++
@approach: 1-2 line explanation
@time: O(...)
@space: O(...)
```

## Automation
- README auto-update workflow: `.github/workflows/update-readme.yml`
- README generator script: `scripts/generate_readme.py`

## LeetCode Sync
Only real solved files are tracked.

Add files manually after solving in this format:
- `solutions/{year}/{month}/YYYY-MM-DD-problem-name.cpp`

Then push normally:
- `git add .`
- `git commit -m "feat: add solved leetcode problem"`
- `git push`

## Code Quality Principles
- Clean and readable implementations
- Consistent naming and formatting
- Comments only when they clarify non-obvious logic
- Prefer optimal or near-optimal time complexity

## Contribution Graph Mindset
The objective is consistency with integrity: no simulated progress, only real solved problems.
