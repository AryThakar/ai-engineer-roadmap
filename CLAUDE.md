# Handoff: Ary's AI engineer interview prep

> **Ary, to continue in a new Claude account:** start a new chat and send this, with your backup pasted at the end:
>
> *Read https://raw.githubusercontent.com/AryThakar/ai-engineer-roadmap/main/CLAUDE.md fully and continue as my AI engineer interview prep coach from my old account. My progress backup:* (paste it from the app: "Back up or move progress", then Copy)
>
> If the link doesn't open for that Claude, attach this file to the chat instead.

**Claude, read this first.** Ary has moved to a new Claude account, and a chat can't be carried from one account to another. This file carries over a long conversation from 4 and 5 November 2026 so you can continue as the same assistant. It's a summary written by the Claude he worked with, not a word-for-word transcript. Treat it as what you already know: don't start over, don't ask again what is answered here, and don't redo work listed as done.

When he opens a chat with this file:
1. Read all of it, including the roadmap reference in section 7.
2. If he pasted a progress backup (JSON that starts with `{"app":"ai-engineer-roadmap"`), decode it using section 6. Tell him in a few lines which stage he is in, what's done, and the next topics in each lane. If he didn't paste one, ask for it once.
3. Then do what he asks, the way section 2 describes.

## 1. Who you're helping

- **Ary Thakar**, GitHub `AryThakar`. He is preparing for AI engineer and ML engineer fresher roles in India, mainly through Internshala.
- He already has his Internshala and other job-site accounts and a resume. Don't suggest creating them, and don't guess about them.
- Goal: a job around ₹6 LPA first. He has asked whether about ₹12 LPA is reachable (section 5).
- Time: he said he can study full time, starting over the Diwali break.
- He uses the Claude mobile app and the desktop app, and has the roadmap app installed on his phone.
- He writes short, casual English. Reply in simple, plain English. On mobile, keep answers to about one screen.
- His two public projects (use them as examples when teaching, and for topic 70, project discussion):
  - **zen** (github.com/AryThakar/zen): a private voice assistant that runs entirely on the user's own PC (Windows 11). Rust on Tauri 2 with a hand-written HTML/CSS/JS interface. Pipeline: Silero VAD (voice activity) → Qwen3-ASR 1.7B (speech to text) → Gemma 4 E2B on llama.cpp `llama-server` with an MTP drafter (transcript repair and reply) → Qwen3-TTS 0.6B (speech, voice cloned from a reference clip). Quantised models (Q4_K, Q8_0), aimed at a 4 GB GPU.
  - **Zen-harness** (github.com/AryThakar/Zen-harness): a Python 3.13 personal assistant that gets real work out of an open model you run yourself (Qwen 3.6 35B-A3B through llama.cpp, free on a Kaggle notebook's two T4 GPUs, or any OpenAI-style API). It hands work to three helpers (web; documents and earlier chats; an analyst-programmer for tables and programs) inside a project folder, and checks facts, numbers and files with code before showing them.
  - These overlap with roadmap topics 47 (LLM APIs, local models), 51 (agents and tools), 53 (quantisation, GGUF), 29 and 47 (streaming) and 55 (LLMOps). He still has to be able to explain them at interview depth.

## 2. How he wants you to work

These come from his direct feedback during the chat. Follow them.

- Answer directly in the chat. Short lists, not long essays. He said he has no time to read long documents.
- Before building anything (a plan, a file, a change to the app), lay out the plan in the chat and wait for his OK.
- **Teach each topic yourself** (his request, 5 Nov 2026). He built the roadmap and resources for you to use together with your own knowledge. Don't hand him a list of chapters and links to study; resources are only for extra practice.
- **How he learns best** (his feedback on the Topic 1 lessons):
  - One connected story per topic, in simple words, with everyday analogies (for Python: recipe, step cards, cook, boxes and labels, one knife).
  - Understanding first, then the interview word in brackets. Heavy jargon and long definition lists don't stick for him.
  - Short memory hooks ("Python checks every time; C checks once"), small proofs he can try himself, and a 30-second interview answer at the end.
  - Link to his own projects where it fits (zen, Zen-harness).
  - **Fast pass doesn't mean skipping** (his feedback on Topic 4, 8 Nov):
    - Cover every subtopic fully, with a runnable example and its real output for each. He noticed the `while` loop had no example.
    - Go deep on anything with rules or traps (ternary, changing a list while looping), with step-by-step traces when the behaviour is surprising.
    - Fast means no filler, not less content. The lessons are his future reference material.
- **He checks himself by writing his own summary.** Mark it point by point (correct, wrong, small fix), then give a fixed version for him to memorise.
- Don't quiz him until he asks ("quiz 1"). Don't test him on something before he has revised it.
- Run every code example (Python 3.15) before you show its output.
- After each topic, add its flashcards and MCQs to `flashcards.json` and run the checker (section 6).
- Also save the full lesson as `lessons/<topic id>.md` (section 6), including any follow-up answers he asked for, and run `tools/check-lessons.py`. He asked for this on 8 Nov so he can re-read lessons later.
  - **Flashcards are only for questions an interviewer asks you to explain out loud.** Keep one only if it appears in real question lists (InterviewBit, GeeksforGeeks, PYnative), or if it's a common question for AI roles.
  - **No trivia flashcards** (he rejected these on 6 Nov): PEP numbers, version history, Python 2 vs 3, lists of other implementations.
  - **MCQs** are for what online tests ask: predict the output, find the error, pick the valid option. Syntax rules and trap questions go here.
- **What he prepares, and to what level** (agreed 7 Nov; his own summary, corrected):
  - **Core, all levels:** Python, SQL, DSA (Solve + Explain), REST APIs, data/ML tools (NumPy, pandas, matplotlib, sklearn) plus ML theory, and OOP (concept, MCQ and writing small classes).
  - **Concept + MCQ:** OS, networks, DBMS, system design, security (for us, API auth and prompt injection).
  - **Project + Explain:** GenAI, Docker, cloud deployment.
  - **Daily habits:** aptitude, Git, Linux.
  - The four ways skills are tested:
    - **Build:** a take-home assignment or project round
    - **Solve:** live or online coding, timed
    - **Explain:** the technical interview
    - **Recognise:** MCQ tests
- **DSA is equal-first with Python** (corrected 7 Nov).
  - Section 4's "0 of 13 AI listings ask DSA" counts skill tags, not interview rounds.
  - 2025–26 interview reports (Navi, SarvM.ai, Eightfold, Cognizant GenC, Infosys DSE) show DSA rounds, often 2 LeetCode Mediums.
  - Targets: at least about 110 problems, and all the free NeetCode 150 problems by Stage 6.
  - Level: 2 Mediums in about an hour, explaining out loud.
  - The 2 DSA hours a day are never skipped.
- **The map (his plan, 7 Nov; he considers it final, so don't reshuffle it without his say):**
  - **Stage 1, core Python, fast:**
    - Topics 4–9 are taught quickly, at explain and syntax (MCQ) level, with flashcards and MCQs after each one. He revises them every day.
    - No DSA, SQL or coding practice in Stage 1, only aptitude.
  - **Stage 2, everything together:**
    - Advanced Python and OOP (10–15, 58)
    - REST APIs (28–30)
    - DSA: 16–21, starting with the warm-ups on Topic 16
    - SQL (56)
    - The practical Python programs
  - **Stages 3–6:** Stage 3 maths and data (plus DBMS, OS, networks), Stage 4 ML, Stage 5 GenAI, Stage 6 ship and design.
- **Frozen decks:** Topics 1–3 are final (`"frozen"` in `flashcards.json`, shown as "final set ✓"). Change them only to fix a real mistake.
- **Python vs DSA split** (agreed 7 Nov). Algorithm-style problems (strings, arrays, counting, two pointers) are DSA. They go in the app as LeetCode lists on the DSA topics (the warm-ups are on Topic 16), not as in-app tasks.
  - **MCQ and concept only:** topics 1–5, 11 and 12.
  - **In-app practice tasks** (section 6), only for Python skills LeetCode doesn't test:
    - 6: a decorator and a closure
    - 7: a batching generator
    - 8: a custom exception
    - 9: reading and writing JSON/CSV
    - 10: class design
    - Also planned for the start of Stage 2 (confirm with him before building):
      - a Topic 4 basics pack of 8 classic programs for mass-recruiter tests: prime, GCD, Armstrong number, reverse a number, digit sum, factorial, star pattern, leap year
      - 5 Topic 5 data tasks: grouping and counting lists of dicts
    - Each task gets a time and space target and a speed check. Run `tools/check-practice.py`.
  - **On his laptop:** 13 (`asyncio.gather` with a Semaphore), 14 (a pydantic model) and 15 (pytest). The app's Python has only the standard library.
- **DSA order** (Stage 2, after all of core Python):
  - 16 (Big-O + warm-ups) → 17 → 18 → 19 → 20 → 21, Easy then Medium
  - `Node` classes (topic 10) come just before 21
  - Later: recursion leads to 25 and 26, and `heapq` to 23
- **Daily rhythm** (his request, 7 Nov). Hours are a guide; the stage checks decide when he moves on.
  - Stage 1: Python lessons (typing and running the small examples), cards and MCQs, revision of earlier topics, and 10 aptitude questions.
  - From Stage 2:
    - Python and APIs, about 4 h
    - DSA, about 2 h: 1–2 LeetCode problems
    - SQL, about 1 h
    - Revision, 30–60 min: flashcards plus 10 aptitude questions
- **LeetCode reviews:**
  - He solves on LeetCode (laptop) and pastes his code. Review it like an interviewer: correctness, edge cases, Big-O, cleaner Python.
  - Don't give full answers before he tries.
  - Add a problem to `LC` only after confirming it's free (not Premium).
- Use the same three levels everywhere:
  - **Coding**: he writes it live in an editor, with no AI help.
  - **Concept**: he explains it clearly and reasons about code he is shown.
  - **MCQ**: he recognises it and answers quick questions correctly.
- Don't give ideas about things you don't know about him. Do what he asked, in the order he asked.
- No fixed day-by-day schedule. His pace depends on how fast he learns, so use the stage checks ("Move on when") instead of day counts.
- Quality over speed. Check facts and links before stating them, don't make things up, and work step by step. If you're not sure, say so.
- Change his GitHub repo only when he asks.

## 3. Where things stand (7 Nov 2026)

Done, in order:
1. Read 23 fresher listings on Internshala (13 AI engineer, 10 ML) and counted the skills they ask for (section 4).
2. Agreed the full topic list: 71 topics in 13 sections, A to M, each tagged Coding, Concept or MCQ. Earlier chat answers (Python topics by level, whether the list is enough, which topics are tested as MCQ, concept or live coding) are all folded into this list. Treat the roadmap as the source of truth.
3. Built a parallel study plan: 6 stages, each with 4 lanes studied side by side (Core, Coding, Light, Build) and a "Move on when" check. No day counts.
4. Collected 84 learning and practice resources and checked every link on 5 Nov 2026. Left out repos whose answers are paywalled or mostly missing (the Devinterview repos show only about 15 free answers; llmgenai's answers are paywalled).
5. Built the roadmap as an installable phone app on GitHub Pages that works offline (section 6).
6. Answered whether about ₹12 LPA is reachable, and whether a chat can move to another account (section 5).
7. Started Stage 1. Read every Stage 1 resource and gave exact chapters and problem lists (notes in section 5). He then asked to be taught directly instead.
8. **Taught Topic 1 (Basics and setup)**: the theory as one story (what Python is, how it runs, typing, memory, speed, GIL, why AI uses it) plus the basics (REPL, `-m`, indentation, comments, naming, `print`/`input`, keywords, `None`). He wrote his own summary and it was corrected (section 5).
9. Added a flashcard viewer to the app. Seven zen/Rust cards for topic 70 were made, then removed at his request on 6 Nov; he wants the project work done when we reach the projects (topic 70), and the notes are kept in section 5.
10. **Rebuilt the Topic 1 revision set** (6 Nov). He said the first 39 cards were mostly not useful (PEP and similar trivia). The set is now 10 flashcards for real interview questions, plus 25 MCQs (predict the output, find the error, concept checks), in a new MCQ mode in the app.
    - The 10 flashcards cover: what Python is and why it's popular, compiled vs interpreted, what happens when you run a file, dynamic and strong typing, how variables work, memory management, the GIL, why Python is slow but used for AI, docstrings, and indentation.
    - These are the questions that appear across InterviewBit, GeeksforGeeks and PYnative. PEP 8 appeared in only 1 of the 3 lists.

11. **Taught Topic 2 (Data types and operators)** on 6 Nov, as one story: "the kinds of boxes" (types, sealed vs open, `type` vs `isinstance`, conversion, truthy/falsy), then "the machines" (arithmetic, comparison, `and`/`or`, bits, `is` vs `==`, `in`, precedence), then "the float surprise". He then got 7 flashcards and 39 MCQs for it.

12. **Taught Topic 3 (Strings)** on 6 Nov. He said "continue" without sending a Topic 2 summary.
    - The story was "a train of letter carriages": seat numbers and slicing, the welded train (immutable), the toolbox (split/join, strip/replace/count, in/find/index, checks and case), f-strings, escapes and raw strings, str vs bytes, and join vs `+=`.
    - Measured: `+=` 3.2 ms vs join 2.5 ms for 100k pieces, but 128 ms when a second reference breaks CPython's shortcut.
    - He then got 8 flashcards and 37 MCQs.
    - He was given 6 coding tasks to write himself, with expected outputs and hints but no answers: reverse_words, is_palindrome, is_anagram, first_unique, count_vowels, compress ("aaabbc" → "a3b2c1").

13. **Added in-app code practice** (6 Nov, his request). A "Code practice" screen runs real Python on his phone, offline after the first use (section 6).
    - The 6 Topic 3 tasks are in it. Each task shows its time and space target ("Time O(n) · Space O(1)").
    - Check runs hidden tests, then a speed check on a big input. An O(n²) answer gets "Too slow", and the reason for the target appears only after he passes.
    - The reference answers are in `tools/practice_solutions.py` in the public repo. Never show or quote them to him before he has tried.
    - On 7 Nov the 6 string tasks were removed (see 15). The screen stays, hidden, until tasks for topics 6–10 are added.

14. **Reviewed his first task** (reverse_words). His logic was right, but he wrote `return print(...)`, so the function returned `None` and failed 0/6. He was taught print vs return ("print = saying it out loud; return = handing it back") and told not to reuse `s` for a list.

15. **Python vs DSA split** (7 Nov; the rules are in section 2). He pointed out that the in-app string tasks were really DSA.
    - Topics 3 and 4 are now MCQ level and Topic 5 is Concept, with new checks. Stage 1's "Move on when" was updated.
    - The 6 string tasks were removed. Their LeetCode versions are in the lists below.
    - Each topic panel now has a "LeetCode problems" box with links and ticks; the ticks are saved in the backup. 29 free problems, all confirmed on 7 Nov:
      - Topic 4: 7 warm-ups (moved to Topic 16 on 7 Nov, where DSA starts)
      - Topic 17: 10 hashing problems
      - Topic 18: 12 two-pointer and sliding-window problems

16. **Topics 1–3 count as done** at learning and MCQ level (his call, 7 Nov). He marks them done in the app himself.

17. **Market check and corrections (7 Nov).** He found it odd that videos say DSA, CS fundamentals and system design are needed. Real 2025–26 interview reports agreed with the videos, so DSA was raised to equal-first (section 2). Nothing was missing from the roadmap; only the priorities changed. OOP was moved into the core: interviewers ask it as concept, MCQ and "write a small class".

18. **Topics 1–3 decks reviewed and frozen (7 Nov).**
    - 2 MCQs that repeated another topic were replaced: "is None" and string immutability.
    - 5 MCQs were added for gaps: `python -m pip`, `^` and `>>`, `7.0 // 2`, triple-quoted strings, `ord`/`chr`.
    - Now 25 flashcards and 106 MCQs, all checked.

20. **New map (7 Nov, his plan; section 2).**
    - Stage 1 is now core Python only (1–9), fast. DSA (16–18) and SQL (56) moved to Stage 2, and so did REST APIs (28–30).
    - OS (59) moved to Stage 3, next to DBMS and networks.
    - The Topic 4 warm-ups moved to Topic 16, and the Topic 4 check no longer mentions them.
    - Stage 1's "Move on when" is now: 80% on the Topics 1–9 MCQs and the flashcards answered out loud.
    - The Build lane now adds features to Zen-harness (Stages 3–6).

19. **His projects (7 Nov).**
    - He says he built zen and Zen-harness with AI help.
    - Instead of a new Build-lane project, he'll add features he writes himself to Zen-harness, chosen to cover what AI jobs ask: a FastAPI endpoint, RAG with a vector database, an eval set, Docker, deployment, CI.
    - At Stage 3, read its code together first, see what it already has, then pick the features. Don't guess what it contains.
    - At topic 70, go through both projects until he can explain and change every part.

21. **Taught Topic 4 (Control flow and loops)** on 8 Nov, the first fast-pass lesson.
    - The story: the cook "choosing" (if/elif, ternary, match) and "repeating" (for as a conveyor belt, range, while, break/continue/pass, loop else, enumerate/zip).
    - Traps covered: changing `i`, removing items while looping, nested loops multiply.
    - He then got 7 flashcards and 36 MCQs.

22. **Topic 4 redone in depth, and lesson notes added (8 Nov).**
    - He said the first Topic 4 lesson skipped too much: no `while` example, a thin ternary section, and unclear traps. They were retaught fully.
    - His follow-up questions:
      - Why did `remove` delete only one 2? `remove` deletes the first match only, one per call, and the loop skipped the second 2, so `remove` ran just once.
      - Why fix it if it "works"? It only works by luck: `[2, 4, 6, 8]` with evens removed gives `[4, 8]`.
    - Topic 4 now has 8 flashcards and 53 MCQs.
    - The app now has a **Lesson** reader (section 6). The complete Topic 4 lesson is in `lessons/4.md`, with 36 code examples checked.
    - Topics 1–3 were taught before notes existed, so they have no lesson file yet. Offer to write them from the same stories.

23. **Taught Topic 5 (Data structures)** on 8 Nov, in the complete format from the start.
    - The story: four kinds of storage (list = numbered shelf, tuple = sealed lunchbox, set = bag of unique tokens, dict = labelled spice rack), then the `collections` toolbox, `heapq`/`bisect`, Big-O and the shared-list traps.
    - Measured: 1000 searches in 100,000 items took about 0.6 s in a list and 0.00005 s in a set; emptying 100,000 items from the front took 0.75 s with `list.pop(0)` and 0.004 s with `deque.popleft()`.
    - Python 3.15 wording to remember: `list.index` says "list.index(x): x not in list", and unhashable keys say "cannot use 'list' as a dict key (unhashable type: 'list')".
    - He got 13 flashcards and 63 MCQs. The lesson is in `lessons/5.md`, with 34 code examples checked.

Next:
- **Stage 1 fast pass, continuing with Topic 6** (functions): a complete lesson (every subtopic with runnable examples), then flashcards, MCQs and the lesson file. Then Topics 7, 8, 9 in the same way. He revises every day.
- **Then Stage 2:**
  - Start by building the basics pack and data tasks (with his OK).
  - DSA from Topic 16's warm-ups.
  - SQL: LeetCode SQL 50 in order (Select, Basic Joins, Basic Aggregate Functions, Sorting and Grouping first).
- **Review any LeetCode code he pastes** (section 2).
- If he sends a Topic 2 or Topic 3 summary, check it point by point.
- He revises Topics 1–3 with the flashcards and MCQs.
- **GitHub Pages publishing failed on 5–6 Nov.** The deploy step timed out at "updating_pages", and a stuck queued re-run of cbdc44c couldn't be cancelled ("has not yet queued"). Each push to gh-pages starts a new deploy. If the live `flashcards.json` lacks the newest topics, check the runs with `gh api repos/AryThakar/ai-engineer-roadmap/actions/runs` and re-run or push again. Check the live file with a cache-busting query (`?check=...`), because the fetch tool caches URLs for 15 minutes. His real progress is in the app's backup (section 6).
- Project work (zen, Zen-harness) waits until the Build lane in Stage 3 (adding features to Zen-harness) and topic 70 (explaining both). Don't bring it up before then. For topic 70, start from the zen notes in section 5.

## 4. Internshala research (4 Nov 2026)

23 Internshala listings: fresher jobs, and internships that lead to a job offer. Each number is how many listings ask for the skill, counting the "Skills required" tags and skills named in the description.

| Skill | All (23) | AI engineer (13) | ML (10) |
| --- | --- | --- | --- |
| Python | 23 | 13 | 10 |
| ML fundamentals | 15 | 7 | 8 |
| NLP | 11 | 5 | 6 |
| REST APIs | 10 | 9 | 1 |
| LLM APIs | 9 | 6 | 3 |
| Deep learning | 8 | 1 | 7 |
| Prompt engineering | 7 | 6 | 1 |
| SQL | 7 | 4 | 3 |
| Agents | 6 | 6 | 0 |
| LLM evaluation | 6 | 6 | 0 |
| Cloud | 6 | 5 | 1 |
| EDA | 6 | 0 | 6 |
| RAG, FastAPI, LangChain, JS/TS, frontend | 5 each | 5 each | 0 |
| DSA | 5 | 0 | 5 |
| Git, vector databases | 4 each | 4 each | 0 |

- Python is in every listing.
- AI engineer roles lean on REST APIs, LLM APIs, prompts, agents, evals, RAG and FastAPI.
- ML roles lean on ML fundamentals, deep learning, EDA, NLP and DSA.
- Listed pay ran from about ₹2 LPA to ₹22 LPA, and 15 of the 23 topped out at ₹8 LPA or less. For internships this is the pay after the job offer.

## 5. Answers already given

- **Can he reach about ₹12 LPA?** Answered with 2026 figures: most freshers get ₹6–9 LPA, and GenAI freshers with a strong portfolio get ₹12–22 LPA (Instahyre). So ₹12 LPA is possible but above the usual fresher range. Check current figures again before quoting them.
- **Can this chat move to another account?** No. Shared chats are view-only, and exported data can't be imported into another personal account. That is why this file exists.
- **Topic 1, his own summary (6 Nov):** mostly right. The mistakes he made, worth re-checking later:
  - He said Python "runs on a C compiler". Correct: CPython is written in C; his code never goes through a C compiler.
  - He said the PVM converts bytecode to machine code. Correct: the PVM carries out each instruction directly; only a JIT makes machine code.
  - He said 3.14 is the latest. Correct: 3.15 (October 2026).
  - "You can never mix types" was too strong. `3 + 2.5`, `True + 1` and `"ab" * 3` work; only guessing mixes like `"1" + 1` fail.
  - "Python checks the value each time" should be "checks the type each time".
- **Is Python compiled or interpreted?** Both: compiled to bytecode, then the PVM interprets it. Officially called interpreted.
- **Small-int caching (checked 6 Nov):** the textbook range is -5 to 256, which is true on 3.11–3.13. On the 3.15 build tested here (3.15.0b4), CPython reuses ints from -5 to 1024. Teach it in a version-proof way: "CPython reuses small ints, classically -5 to 256; it's an implementation detail, so never use `is` for values." Also, `5.0 / 0` says "division by zero" on 3.15 but "float division by zero" on 3.13; it's the same error.
- **Why zen uses Rust (for topic 70 later; the cards were removed for now):** he measured a Python prototype at ~12 s per reply and the Rust version at ~3 s, with the same models on the same machine. The reasons found in the zen code:
  - The TTS library calls back into Rust with each audio chunk and polls a Rust cancel flag (`tts.rs`), and Python callbacks would need the GIL.
  - Capture, transcription, LLM and speech run in parallel, and data races are compile errors in Rust.
  - Generation numbers drop stale replies (`session.rs`), and slot IDs are checked by the type system (`engine.rs`).
  - It ships as one exe.
  - Still open, for topic 70: ask him what the 12 s measured. The gain probably came from orchestration (streaming, overlap, models staying loaded), not raw speed, but don't claim that until it's confirmed.
- **PYnative "Top 100 Basic Python Interview Questions"** (pynative.com/beginner-python-interview-questions, updated April 2025): good for revision, not as the only source.
  - Weak points: Q2 skips bytecode and the PVM; Q18 says `PYTHONCASEOK` is Windows-only (docs: Windows and macOS); Q68 skips negative floor division.
  - Question map by topic: 1: Q1–5, 16–18, 24–25 · 2: Q19–23, 68 · 3: Q26–38 · 4: Q6–15 · 5: Q53–67 · 6: Q39–47, 84 · 7: Q85–88 · 8: Q69–73, 93 · 9: Q89–93 · 10: Q74–83.
- **Stage 1 resource notes (5 Nov):**
  - The Chanda-Abdul patterns repo has JavaScript solutions; leetcode-patterns has Java solutions and some Premium problems. Use NeetCode 150 for topics 17–18.
  - PYnative has no quiz on exceptions; CS50P doesn't teach decorators (use Real Python's decorator article).
  - The PrepInsta aptitude link led to an LTI-specific page; use IndiaBIX for topic 69.
  - LeetCode SQL 50 has 7 sections; the first 4 (29 problems) cover the Stage 1 check.

## 6. The roadmap app

- Live app: https://arythakar.github.io/ai-engineer-roadmap/ (installs to the home screen, opens full screen, works offline after the first visit).
- Repo: https://github.com/AryThakar/ai-engineer-roadmap (public). This file is `CLAUDE.md` in it.
- An older copy was published as a Claude artifact in his old account. Ignore it; the GitHub Pages app is the main copy.

### Progress backup

- Progress is saved in the phone's browser (localStorage key `aiEngineerRoadmap.v1`), not in any Claude account, so switching Claude accounts doesn't affect it.
- In the app, "Back up or move progress" then Copy gives JSON like this:
  `{"app":"ai-engineer-roadmap","status":{"3":"done","4":"progress"},"subs":{"3:0":true,"3:1":true},"lc":{"412":true,"1":true}}`
  - `status`: topic id → `"done"` or `"progress"`. A missing id means not started.
  - `subs`: `"<topic id>:<subtopic number>"` → `true` for each ticked subtopic. Numbers start at 0, in the order listed in section 7.
  - Ticking every subtopic of a topic marks it done automatically.
  - `lc` (added 7 Nov; older backups don't have it): LeetCode problem number → `true` for each problem he ticked as solved. Map the numbers to topics with the LeetCode lines in section 7. Ticking one marks a not-started topic "in progress".
- To read it: map the ids to section 7. His current stage is normally the lowest stage that still has unfinished topics. The "Move on when" check is his own judgement, so ask him if it's unclear.
- He can paste a backup into the same box and press "Load pasted progress" to restore it on another device.

### Changing the app (only when he asks)

- `index.html` is the whole app: HTML, CSS and JavaScript in one file, with no build step. It already contains the install and offline pieces.
- The data is in JavaScript constants near the top of the script:
  - `SECTIONS`: the 13 sections, A to M.
  - `LEVELS`: Coding, Concept, MCQ.
  - `T`: topics, `[id, section, title, level, stage, lane, check, [subtopics]]`. Level is `code`, `concept` or `mcq`. Stage is `"1"` to `"6"`, `"Daily"` or `"Optional"`.
  - `PAIRS`: topics that go well together.
  - `LANES`, `STAGES`: the parallel plan and each stage's "Move on when" check.
  - `KINDS`, `RES`: resources, `[name, url, kind, note, [topic ids]]`. Kind is `Learn`, `Practice`, `MCQ` or `QA`.
  - `LC`: LeetCode problems by topic id, `[number, slug, title, difficulty, note]`. The link is `https://leetcode.com/problems/<slug>/`.
    - The number is the backup key, so never reuse it for another problem.
    - Free problems only: confirm a problem isn't Premium before adding it.
    - Lists exist for topics 16 (warm-ups), 17 and 18. Add the next DSA topic's list when he reaches it (19, 20, 21, all in Stage 2).
- Don't renumber topics or reorder subtopics. Progress keys depend on topic ids and subtopic order, so add new subtopics at the end.
- `sw.js` (offline support, `VERSION` is `air-v4`): the page, `flashcards.json`, the `lessons/` files and the `practice/` files load network-first, so changes to them show up on their own. Other files (manifest, icons) are served from the cache first, so raise `VERSION` in `sw.js` when you change them. The Pyodide files are cached on first use in their own cache (`PYODIDE_CACHE`), which survives app updates.
- Deploying: GitHub Pages serves the `gh-pages` branch. Keep `main` and `gh-pages` the same: commit on `main`, then run `git push origin main main:gh-pages`.
- Section 7 below is generated from `index.html`, `flashcards.json`, `lessons/index.json` and `practice/tasks.json`. After changing any of them, run `node tools/update-claude-md.js` from the repo root to bring it up to date.

### Flashcards and MCQs

- In the app, the yellow "Flashcards & MCQs" button opens the deck, and a switch at the top changes between Flashcards and MCQ. Each topic's panel shows "Cards" and "MCQ" buttons when that topic has them.
- **Flashcards** work as a queue: "Got it" removes the card, and "Again" sends it to the back. On a laptop, Space flips, ← means again and → means got it.
- **MCQs** are one pass with a score:
  - The order of the options is shuffled every time.
  - After you answer, the right option turns green, a wrong pick turns red, and the real output and the explanation appear.
  - At the end you can retry the ones you got wrong.
  - On a laptop, keys 1–4 answer and Enter moves to the next question.
- Nothing about cards or scores is saved in the progress backup.
- Both live in `flashcards.json`: `{"version": 2, "updated": "YYYY-MM-DD", "topics": {"<topic id>": [card, ...]}, "mcq": {"<topic id>": [question, ...]}, "notes": {...}}`.
- An MCQ has these fields:
  - `kind`: `output` (predict the output), `error` (find the error) or `concept`.
  - `q`.
  - `options`: 3–4 different strings; backticks become code.
  - `answer`: the index of the right option in `options`.
  - `why`: the explanation.
  - `trap` (optional).
  - `code` and `out` (optional, always together).
- For `error` questions the right option must be the error's name, like `` `TypeError` ``. The checker verifies this.
- A card has these fields:
  - `q` and `a` (both required). Backticks become inline code.
  - `hook` (optional): a memory line.
  - `code` and `out` (optional, always together): the front shows the code, and the back shows its exact output. If the code ends in an error, the last line of `out` is `ErrorName: message`.
  - `trap: true` (optional): shows a red "Trap" badge.
- Write cards like the lessons: simple words, one idea per card, short answers.
- Add new items to the end of a topic's list, then run `python tools/check-flashcards.py` with Python 3.15.
  - It checks every item's shape and runs every `code` to confirm `out` matches exactly. Syntax errors are shown the way a terminal shows them.
  - It also confirms each MCQ's marked answer matches what the code really does.

### Lesson notes

- A topic with a lesson shows "Lesson notes" and a **Lesson** button in its panel. The button opens a full-screen reader; Esc or Close closes it.
- `lessons/index.json`: `{"version": 1, "topics": {"<topic id>": {"title": ..., "updated": "YYYY-MM-DD"}}}`. Each listed topic has `lessons/<topic id>.md`.
- The app fetches every lesson once in the background, so they can be read offline after one visit online.
- The Markdown is a small subset, rendered by `mdRender` in `index.html`:
  - `#` title, `##` parts, `###` sections, `####` sub-sections
  - paragraphs, `-` and `1.` lists (nested by indenting), `| tables |`
  - `> Hook: ...` lines become yellow hook boxes
  - `` `code` `` and `**bold**`
  - fenced blocks: `` ```python `` for code, and a `` ```output `` block straight after it for that code's output
- Write lessons like the chat lessons: the story, every subtopic with an example, the traps, the 30-second answers, and a "Memory hooks" list at the end.
- `python tools/check-lessons.py` (Python 3.15):
  - It runs every python block that has an output block under it and checks that the output matches exactly. Errors end with `ErrorName: message`, as in `flashcards.json`.
  - Python blocks without an output block are shown as they are and not run (use them for fragments like a lone `return`).

### Code practice

- **No tasks right now** (the 6 string tasks were removed on 7 Nov). The "Code practice" button and the topic's "Code" button appear by themselves once `practice/tasks.json` has tasks. Add tasks only for topics 6–10 (section 2).
- The yellow "Code practice" button, or "Code" in a topic's panel, opens the screen: the task (examples, the time and space target, a hint) on one side, and an editor with Run, Check, Stop and Reset on the other.
- **Python runs in the browser**: Pyodide 314.0.7 (Python 3.14.2) in `pyodide/314.0.7/`, about 13 MB, downloaded on first use and then kept for offline use.
  - It runs inside a Web Worker (`practice/worker.js`), so Stop and the time limits end a stuck loop by ending the worker; a fresh one starts by itself.
  - It's Python 3.14, not 3.15, so a few error messages can differ slightly from his laptop.
  - License notes are in `pyodide/README.md`.
- **Run** runs the code as a script and shows its prints (10 s limit; `input()` is blocked with a clear message).
- **Check** calls the function on every test and shows ✅/❌ with expected vs got, or the error and its line. If all pass, it runs the speed check:
  - It times the function on the task's big input, with a 4 s limit.
  - Pass: "⚡ Fast enough", the task is marked solved, and the "why" of the target appears.
  - Fail: "🐢 Too slow… probably O(n²)", with common causes to look for.
  - Space isn't measured; the screen tells him to compare his answer with the target.
- Editor keys:
  - Tab gives 4 spaces and Shift+Tab removes them, also on a selection of lines.
  - Enter keeps the indent and adds 4 after a colon; Backspace in the indent removes 4.
  - Ctrl+Enter runs, Ctrl+Shift+Enter checks, and Esc leaves the editor.
  - Touch screens get Tab → and ← Tab buttons.
- His code and solved tasks are saved in the browser (localStorage key `aiEngineerRoadmap.practice.v1`), not in the progress backup.
- `practice/harness.py` judges the code, in both the browser and the checker, so they always agree. Comparisons are strict: `True` isn't accepted for `1`, and `None` must be `None`.
- Tasks are in `practice/tasks.json`: `{"version": 1, "updated": ..., "python": ..., "topics": {"<topic id>": [task, ...]}}`. A task has:
  - `id` (like `t3-compress`), `title` and `func` (the function name he must write).
  - `prompt`: backticks become code.
  - `starter`: a function stub plus a couple of example prints. It must not pass the tests.
  - `tests`: `[{"args": [...], "expect": ..., "show": true}]`. `show` marks the examples shown on the task. Don't use whole-number floats like `3.0`, because the app would show them as `3`.
  - `target`: `{"time": "O(n)", "space": "O(1)", "why": "..."}`.
  - `speed`: `{"setup": "args = (...)", "label": "1,200,000 letters", "limit": 4}`. `setup` is Python that builds `args`.
  - `hint`.
- To add tasks:
  1. Add them to `practice/tasks.json`.
  2. Put a correct answer in `SOLUTIONS` and a correct but O(n²) answer in `SLOW` in `tools/practice_solutions.py`.
  3. Run `python tools/check-practice.py` with Python 3.15. It checks that the reference passes and takes under a tenth of the limit, and that the starter fails. It also checks that the slow answer still passes the tests but takes over twice the limit.
  4. Size the speed input so this holds.
- On 6 Nov 2026 in browser Python, the references took 0.01–0.18 s and the slow answers 13–45+ s.

## 7. Roadmap reference (generated from the app's data, do not edit by hand)

Totals: 71 topics in 13 sections, 6 stages, 84 resources. Levels: 27 Coding, 30 Concept, 14 MCQ. Flashcards: 46, MCQs: 222 (topics 1, 2, 3, 4, 5). Coding tasks: 0. Lesson notes: 2 (topics 4, 5). LeetCode problems: 29 (topics 16, 17, 18).

### Levels
- **Coding**: You write it live in an editor, with no AI help.
- **Concept**: You explain it clearly and reason about code you are shown.
- **MCQ**: You recognise it and answer quick questions correctly.

### Lanes (studied side by side inside each stage)
- **Core**: About half of each study day. The main subject; moves only after the stage check.
- **Coding**: About a quarter. DSA problems every day, in pattern order.
- **Light**: A small daily dose of one CS or tools subject.
- **Build**: One project that grows as the Core lane reaches each part.
- Topic 69 (aptitude) runs every day from the start. Topic 71 (frontend) is optional.

### Stages
Move to the next stage only when its "Move on when" check is true. There is no fixed number of days.

**Stage 1: Python core, fast**
- Core: 1 Basics and setup, 2 Data types and operators, 3 Strings, 4 Control flow and loops, 5 Data structures, 6 Functions, 7 Iterators and generators, 8 Error handling, 9 Files and data formats
- Coding: None yet: DSA starts in Stage 2, once you know all of core Python.
- Light: none
- Build: On your laptop: set up Git, a virtual environment and one repo for all your practice code.
- Move on when: you score 80% or more on the MCQs for Topics 1–9 and can answer their flashcards out loud without notes.

**Stage 2: Python depth, APIs and coding**
- Core: 10 Classes and objects, 11 Modules, packages and environment, 12 Memory and internals, 13 Concurrency and async, 14 Type hints, 15 Testing and code quality, 58 OOP principles, 28 HTTP and REST concepts, 29 FastAPI and pydantic, 30 Calling APIs (requests, httpx)
- Coding: 16 Big-O complexity, 17 Arrays and hashing, 18 Two pointers and sliding window, 19 Stack and queue, 20 Binary search, 21 Linked list
- Light: 56 SQL queries
- Build: Practical Python programs (basics, data tasks, decorators, generators, files, classes), saved with pytest tests in your practice repo.
- Move on when: you can write a decorator, a generator, a JSON/CSV script and a small class from a blank file; build a validated FastAPI endpoint and call an API with retries; explain copying, scope, the GIL and async; solve Easy and Medium hashing, two-pointer, stack, binary search and linked-list problems alone; and write a JOIN with GROUP BY.

**Stage 3: Maths and data**
- Core: 31 Linear algebra basics, 32 Probability and statistics, 33 NumPy, 34 pandas, 35 Data visualisation
- Coding: 22 Trees, 23 Heap
- Light: 57 DBMS concepts, 59 Operating systems, 60 Computer networks
- Build: 47 LLM APIs. Read Zen-harness's code with Claude, then add a FastAPI endpoint to it that calls the LLM.
- Move on when: you can clean a dataset in pandas, vectorise a loop in NumPy, and explain dot product and p-values; solve tree and heap problems; do well on DBMS, OS and networks quizzes; and Zen-harness has a FastAPI endpoint you wrote.

**Stage 4: ML and deep learning**
- Core: 36 ML fundamentals, 37 ML algorithms, 38 Evaluation metrics, 39 scikit-learn workflow, 40 Neural network basics, 41 CNN, RNN and LSTM, 42 PyTorch basics
- Coding: 24 Graphs (BFS, DFS), 25 Recursion and backtracking
- Light: 61 Git and GitHub, 62 Linux and the shell
- Build: 43 NLP basics (tokens, embeddings), 49 Vector databases. Add embeddings and similarity search to Zen-harness.
- Move on when: you can train and evaluate an sklearn pipeline without leakage, explain the metrics and bias vs variance, and write a PyTorch training loop; and solve BFS/DFS and backtracking basics.

**Stage 5: GenAI**
- Core: 43 NLP basics (tokens, embeddings), 44 Transformers and attention, 45 How LLMs generate, 46 Prompt engineering and structured output, 47 LLM APIs, 48 RAG, 49 Vector databases, 50 LangChain, LangGraph, LlamaIndex, 51 Agents and tool calling, 52 Evaluating LLM apps, 53 Fine-tuning and quantisation, 54 Guardrails and prompt injection, 55 LLMOps
- Coding: 26 Dynamic programming basics, 27 Sorting algorithms
- Light: 63 Docker
- Build: 48 RAG, 51 Agents and tool calling, 52 Evaluating LLM apps, 63 Docker. Add the GenAI features Zen-harness doesn't have yet (such as RAG and an eval set) and a Dockerfile.
- Move on when: Zen-harness runs in Docker with eval numbers you can explain, and you answer LLM, RAG and agent questions without notes.

**Stage 6: Ship and design**
- Core: 67 System design basics, 68 Designing an LLM app, 70 Project discussion and HR
- Coding: Timed, mixed problems from every pattern, as in a real round.
- Light: 64 Kubernetes basics
- Build: 65 Cloud basics (AWS), 66 CI/CD basics. Deploy Zen-harness and add CI.
- Move on when: Zen-harness is deployed with CI, you can design an LLM app in 30 minutes, and you can tell each project's story in 2 minutes.

### All topics
Format: **id. title** [level, where]. Check = what he must be able to do. Subtopic numbers start at 0 and match the progress backup keys.

#### A. Python
- **1. Basics and setup** [MCQ, stage 1, Core lane, 10 flashcards, 26 MCQs]
  - Check: Explain how Python runs your code and answer basic syntax questions.
  - Subtopics: (0) What Python is: interpreted, dynamically typed, high-level; (1) Installing Python; versions 3.14 and 3.15; (2) REPL vs running a `.py` script; `python -m module`; (3) Indentation defines blocks; (4) Comments and docstrings; (5) Variables and naming rules (PEP 8 style); (6) `print()` and `input()`; (7) Keywords and `None`
- **2. Data types and operators** [MCQ, stage 1, Core lane, 7 flashcards, 41 MCQs]
  - Check: Predict results like `-7 // 2`, `0.1 + 0.2`, `'a' or 'b'` and `1 < x < 5`.
  - Subtopics: (0) `int`, `float`, `complex`, `bool`, `str`, `None`; (1) `type()` vs `isinstance()`; (2) Type conversion: `int()`, `float()`, `str()`, `bool()`; (3) Truthy and falsy values; (4) Arithmetic: `/`, `//`, `%`, `**`; floor division with negatives; (5) Comparison and chained comparison; (6) `and` / `or` / `not`: short-circuiting and returning operands; (7) Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`; (8) Identity (`is`) vs equality (`==`); membership (`in`); (9) Operator precedence; (10) Float precision: why `0.1 + 0.2 != 0.3`
- **3. Strings** [MCQ, stage 1, Core lane, 8 flashcards, 39 MCQs]
  - Check: Predict string results (slicing, `find` vs `index`, f-strings), and explain why strings are immutable and why `join` beats `+=`.
  - Subtopics: (0) Indexing and negative indexing; (1) Slicing with a step; `s[::-1]`; (2) Strings are immutable; (3) Methods: `split`, `join`, `strip`, `replace`, `count`; (4) `find` (returns -1) vs `index` (raises an error); (5) `startswith`, `endswith`, `upper`, `lower`, `isdigit`, `isalpha`; (6) f-strings and format specs: `{x:.2f}`, `{x:>10}`; (7) Escape sequences and raw strings `r'...'`; (8) Multiline strings; (9) Unicode, `encode` / `decode`, `bytes`; (10) Build strings with `''.join(parts)`, not `+=` in a loop
- **4. Control flow and loops** [MCQ, stage 1, Core lane, lesson notes, 8 flashcards, 53 MCQs]
  - Check: Predict what loops print, use `range`, `enumerate` and `zip`, and say when a loop's `else` runs.
  - Subtopics: (0) `if` / `elif` / `else`; (1) Conditional expression: `a if cond else b`; (2) `match` / `case` (3.10+); (3) `for` over any iterable; (4) `while` loops; (5) `range(start, stop, step)`; (6) `break`, `continue`, `pass`; (7) `else` on `for` and `while`; (8) `enumerate` and `zip`; (9) Nested loops and their cost
- **5. Data structures** [Concept, stage 1, Core lane, lesson notes, 13 flashcards, 63 MCQs]
  - Check: Pick the right structure for a job, state the Big-O of its operations (`x in list` vs `x in set`), and spot traps like `[[0]*3]*3`.
  - Subtopics: (0) list: `append` vs `extend`, `insert`, `pop`, `remove`; (1) `sort()` vs `sorted()`; sorting with `key=`; (2) tuple: `(1,)`, unpacking, `first, *rest = items`; (3) set: `&`, `|`, `-`, `^`; `add`, `discard` vs `remove`; (4) dict: `get`, `setdefault`, `items`, `update`, merge with `|`; (5) dict keeps insertion order; keys must be hashable; (6) List, dict and set comprehensions; (7) `collections`: `Counter`, `defaultdict`, `deque`, `namedtuple`; (8) `heapq` and `bisect`; (9) Big-O of each operation (`x in list` vs `x in set`); (10) Trap: `[[0]*3]*3` shares one inner list
- **6. Functions** [Coding, stage 1, Core lane]
  - Check: Write a retry decorator, and explain closures and the mutable default trap.
  - Subtopics: (0) `def`, `return`, returning several values; (1) Positional, keyword and default arguments; (2) Mutable default argument trap; (3) `*args` and `**kwargs`; unpacking at the call site; (4) Keyword-only (`*`) and positional-only (`/`) parameters; (5) Scope rules (LEGB), `global`, `nonlocal`; (6) `lambda`; (7) Functions as objects; higher-order functions; (8) `map`, `filter`, `functools.reduce`; (9) Recursion and the recursion limit; (10) Closures; (11) Decorators, `functools.wraps`, decorators with arguments; (12) `functools.partial` and `lru_cache`
- **7. Iterators and generators** [Coding, stage 1, Core lane]
  - Check: Write a batching generator and explain why generators save memory.
  - Subtopics: (0) Iterable vs iterator; (1) `iter()`, `next()`, `StopIteration`; (2) `__iter__` and `__next__`; (3) How a `for` loop works underneath; (4) Generators with `yield`; (5) Generator expressions vs list comprehensions; (6) A used-up generator returns nothing; (7) `yield from`; (8) `itertools`: `chain`, `islice`, `groupby`, `product`, `permutations`, `combinations`
- **8. Error handling** [Coding, stage 1, Core lane]
  - Check: Handle errors cleanly and write a custom exception.
  - Subtopics: (0) `try` / `except` / `else` / `finally`; (1) Catch specific exceptions; several `except` blocks; (2) `raise` and re-raise; (3) Chaining: `raise ... from err`; (4) Custom exception classes; (5) Hierarchy: `BaseException` vs `Exception`; (6) `assert`; (7) Common errors: `KeyError`, `IndexError`, `TypeError`, `ValueError`, `AttributeError`; (8) EAFP vs LBYL style; (9) `ExceptionGroup` and `except*` (3.11+)
- **9. Files and data formats** [Coding, stage 1, Core lane]
  - Check: Read a JSON or CSV file, transform it, and write the result safely with `with`.
  - Subtopics: (0) `open()` modes: `r`, `w`, `a`, `rb`, `wb`; (1) The `with` statement; (2) `read`, `readline`, looping over lines; (3) Text vs binary; encodings; (4) `pathlib.Path` and `os.path`; (5) `json`: `load`, `loads`, `dump`, `dumps`; (6) `csv`: `reader`, `writer`, `DictReader`; (7) `pickle`, and why you never unpickle untrusted data; (8) Context managers: `__enter__` / `__exit__`, `contextlib.contextmanager`
- **10. Classes and objects** [Coding, stage 2, Core lane]
  - Check: Design a small class (stack, LRU cache, bank account) and explain classmethod vs staticmethod.
  - Subtopics: (0) `class`, objects, `__init__`, `self`; (1) Instance vs class attributes; (2) Instance methods, `@classmethod`, `@staticmethod`; (3) `@property` getters and setters; (4) Inheritance, `super()`, overriding; (5) Multiple inheritance and MRO; (6) Polymorphism and duck typing; (7) `_protected` and `__name` mangling; (8) Dunder methods: `__str__`, `__repr__`, `__eq__`, `__hash__`, `__len__`, `__getitem__`, `__iter__`, `__call__`; (9) Operator overloading; (10) Abstract classes with `abc`; (11) `@dataclass` and `Enum`; (12) Composition vs inheritance
- **11. Modules, packages and environment** [Concept, stage 2, Core lane]
  - Check: Explain how imports work, what `__main__` does, and how you manage dependencies.
  - Subtopics: (0) `import`, `from ... import`, aliases; (1) Modules vs packages; `__init__.py`; (2) `if __name__ == '__main__':`; (3) How Python finds imports (`sys.path`); (4) Standard library: `os`, `sys`, `math`, `random`, `datetime`, `time`, `re`, `logging`, `argparse`, `subprocess`; (5) `pip` and `requirements.txt`; (6) Virtual environments with `venv`; (7) `uv` and `conda`; (8) `pyproject.toml`
- **12. Memory and internals** [Concept, stage 2, Core lane]
  - Check: Explain shallow vs deep copy, `is` vs `==`, and what the GIL means.
  - Subtopics: (0) Everything is an object; names are references; (1) Mutable vs immutable; (2) `is` vs `==`; `id()`; (3) Shallow vs deep copy (`copy` module); (4) Reference counting; (5) Garbage collector and reference cycles; (6) Small int and string interning; (7) CPython, bytecode, the `dis` module; (8) The GIL; (9) Free-threaded (no-GIL) build and the experimental JIT
- **13. Concurrency and async** [Concept, stage 2, Core lane]
  - Check: Say when to use threads, processes or asyncio, and write `asyncio.gather` with a Semaphore.
  - Subtopics: (0) Concurrency vs parallelism; (1) I/O-bound vs CPU-bound work; (2) `threading`: `Thread`, `Lock`; (3) `multiprocessing`: `Process`, `Pool`; (4) `concurrent.futures`: thread and process pools; (5) How the GIL affects each; (6) The asyncio event loop; (7) `async def` and `await`; (8) `asyncio.gather` and `create_task`; (9) `asyncio.Semaphore` to cap concurrent calls; (10) `time.sleep` blocks the loop; use `asyncio.sleep`; (11) Race conditions and deadlocks
- **14. Type hints** [MCQ, stage 2, Core lane]
  - Check: Read type hints fluently and write a pydantic model (you use it again in topic 29).
  - Subtopics: (0) Annotating variables, parameters and returns; (1) `list[int]`, `dict[str, int]`; (2) `Optional` and `X | None`; `Union`; `Any`; (3) `Callable` and `TypedDict`; (4) `Protocol`, `TypeVar` and generics; (5) Checking with `mypy`; (6) pydantic models and validation
- **15. Testing and code quality** [Concept, stage 2, Core lane]
  - Check: Write a few pytest tests and use logging instead of print.
  - Subtopics: (0) `unittest` basics; (1) pytest: test functions, `assert`, fixtures, `parametrize`; (2) Mocking with `unittest.mock`; (3) Debugging with `pdb` / `breakpoint()`; (4) `logging` vs `print`; (5) PEP 8 style; (6) `ruff` for linting and formatting; (7) `timeit` and `cProfile`

#### B. DSA
- **16. Big-O complexity** [Concept, stage 2, Coding lane]
  - Check: State the time and space complexity of any solution you write.
  - Subtopics: (0) Time vs space complexity; (1) O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ); (2) Best, average and worst case; (3) Counting loops and nested loops; (4) Complexity of recursion; (5) Amortised O(1): `list.append`; (6) Big-O of Python built-ins
  - LeetCode (backup key = number): 412 Fizz Buzz (Easy); 509 Fibonacci Number (Easy); 9 Palindrome Number (Easy); 1342 Number of Steps to Reduce a Number to Zero (Easy); 1480 Running Sum of 1d Array (Easy); 1672 Richest Customer Wealth (Easy); 151 Reverse Words in a String (Medium)
- **17. Arrays and hashing** [Coding, stage 2, Coding lane]
  - Check: Solve two-sum, group anagrams and top-k frequent in one pass with a hash map.
  - Subtopics: (0) Frequency counting with a dict or `Counter`; (1) Two-sum with a hash map; (2) Contains duplicate; (3) Group anagrams; (4) Top-k frequent elements; (5) Prefix sums; (6) Product of array except self; (7) Longest consecutive sequence
  - LeetCode (backup key = number): 217 Contains Duplicate (Easy); 242 Valid Anagram (Easy); 387 First Unique Character in a String (Easy); 1 Two Sum (Easy); 724 Find Pivot Index (Easy); 49 Group Anagrams (Medium); 347 Top K Frequent Elements (Medium); 238 Product of Array Except Self (Medium); 128 Longest Consecutive Sequence (Medium); 560 Subarray Sum Equals K (Medium)
- **18. Two pointers and sliding window** [Coding, stage 2, Coding lane]
  - Check: Spot when a sorted-array or substring problem needs two pointers or a window.
  - Subtopics: (0) Two pointers on a sorted array; (1) Valid palindrome; (2) 3-sum; (3) Container with most water; (4) Fixed-size sliding window; (5) Variable-size sliding window; (6) Longest substring without repeating characters; (7) Best time to buy and sell stock
  - LeetCode (backup key = number): 125 Valid Palindrome (Easy); 283 Move Zeroes (Easy); 167 Two Sum II - Input Array Is Sorted (Medium); 15 3Sum (Medium); 11 Container With Most Water (Medium); 443 String Compression (Medium); 121 Best Time to Buy and Sell Stock (Easy); 643 Maximum Average Subarray I (Easy); 3 Longest Substring Without Repeating Characters (Medium); 1456 Maximum Number of Vowels in a Substring of Given Length (Medium); 424 Longest Repeating Character Replacement (Medium); 567 Permutation in String (Medium)
- **19. Stack and queue** [Coding, stage 2, Coding lane]
  - Check: Solve valid parentheses and next-greater-element with a stack.
  - Subtopics: (0) Stack with a list; (1) Queue with `collections.deque`; (2) Valid parentheses; (3) Min stack; (4) Monotonic stack: next greater element, daily temperatures; (5) Evaluate reverse Polish notation; (6) Queue using two stacks
- **20. Binary search** [Coding, stage 2, Coding lane]
  - Check: Write bug-free binary search, including the boundary cases.
  - Subtopics: (0) Classic binary search; (1) Lower and upper bound; (2) The `bisect` module; (3) Search in a rotated sorted array; (4) Minimum of a rotated array; (5) Binary search on the answer (e.g. Koko eating bananas)
- **21. Linked list** [Coding, stage 2, Coding lane]
  - Check: Reverse a linked list and detect a cycle.
  - Subtopics: (0) Node class; traversal, insert, delete; (1) Reverse a linked list; (2) Merge two sorted lists; (3) Detect a cycle (fast and slow pointers); (4) Middle of the list; (5) Remove the nth node from the end
- **22. Trees** [Coding, stage 3, Coding lane]
  - Check: Write DFS and BFS traversals and validate a BST.
  - Subtopics: (0) Binary tree node; (1) DFS: preorder, inorder, postorder; (2) BFS level-order traversal; (3) Maximum depth; (4) Invert a tree; (5) Same tree and subtree; (6) BST: search, insert, validate; (7) Lowest common ancestor
- **23. Heap** [Coding, stage 3, Coding lane]
  - Check: Find the kth largest element and the top-k items with `heapq`.
  - Subtopics: (0) `heapq`: `heappush`, `heappop`, `heapify`; (1) Min-heap vs max-heap (negate values); (2) Kth largest element; (3) Top-k frequent; (4) Merge k sorted lists; (5) Median of a data stream (two heaps)
- **24. Graphs (BFS, DFS)** [Coding, stage 4, Coding lane]
  - Check: Count islands with BFS or DFS and explain topological sort.
  - Subtopics: (0) Adjacency list vs matrix; (1) BFS with `deque`; (2) DFS, recursive and iterative; (3) Visited sets; (4) Number of islands; (5) Shortest path in an unweighted graph; (6) Topological sort; (7) Cycle detection; (8) Dijkstra (the idea)
- **25. Recursion and backtracking** [Coding, stage 4, Coding lane]
  - Check: Generate subsets and permutations with backtracking.
  - Subtopics: (0) Base case and recursive case; (1) Drawing the recursion tree; (2) Subsets; (3) Permutations; (4) Combination sum; (5) Word search; (6) N-Queens (the idea)
- **26. Dynamic programming basics** [Coding, stage 5, Coding lane]
  - Check: Solve climbing stairs, house robber and coin change, top-down and bottom-up.
  - Subtopics: (0) Overlapping subproblems and optimal substructure; (1) Memoisation (`lru_cache`) vs tabulation; (2) Climbing stairs; (3) House robber; (4) Coin change; (5) Longest common subsequence; (6) 0/1 knapsack (the idea)
- **27. Sorting algorithms** [Concept, stage 5, Coding lane]
  - Check: Explain merge sort and quick sort, their complexities, and stability.
  - Subtopics: (0) Bubble, selection and insertion sort; (1) Merge sort; (2) Quick sort; (3) Time and space complexity of each; (4) Stable vs unstable sorts; (5) Python's `sorted`: Timsort (merge policy updated to Powersort in 3.11), and `key=`; (6) Counting sort (the idea)

#### C. REST API
- **28. HTTP and REST concepts** [Concept, stage 2, Core lane]
  - Check: Explain HTTP methods, status codes, idempotency and API authentication.
  - Subtopics: (0) Client and server; request and response; (1) Methods: GET, POST, PUT, PATCH, DELETE; (2) Status codes: 200, 201, 204, 400, 401, 403, 404, 422, 429, 500; (3) Headers, path params, query params, body; (4) JSON payloads; (5) REST principles: resources, statelessness; (6) Idempotency; (7) Auth: API keys, Bearer tokens, JWT, OAuth (the idea); (8) CORS; (9) Rate limiting; (10) Streaming: Server-Sent Events vs WebSockets
- **29. FastAPI and pydantic** [Coding, stage 2, Core lane]
  - Check: Build a POST endpoint with a pydantic body, validation and a response model.
  - Subtopics: (0) Create an app; path operations; (1) Path and query parameters; (2) Request bodies with pydantic models; (3) `response_model`; (4) Validation errors (422); (5) Dependencies with `Depends`; (6) `async` endpoints; (7) Streaming responses; (8) `HTTPException` and error handling; (9) Background tasks; (10) Automatic docs at `/docs`; (11) Running with `uvicorn`
- **30. Calling APIs (requests, httpx)** [Coding, stage 2, Core lane]
  - Check: Call an API with a timeout, retries with backoff, and JSON parsing.
  - Subtopics: (0) `requests.get` / `requests.post`; (1) `httpx` sync and async clients; (2) Headers and auth; (3) Timeouts; (4) `raise_for_status()`; (5) Retries with exponential backoff; (6) Parsing JSON responses; (7) Handling 429 rate limits; (8) Many calls at once: `asyncio.gather` + Semaphore

#### D. Maths
- **31. Linear algebra basics** [Concept, stage 3, Core lane]
  - Check: Explain dot product, cosine similarity and matrix shapes.
  - Subtopics: (0) Scalars, vectors, matrices, tensors; (1) Vector operations; (2) Dot product and cosine similarity; (3) Matrix multiplication and shape rules; (4) Transpose; (5) Norms: L1 and L2; (6) Identity and inverse (the idea); (7) Eigenvalues and eigenvectors (the idea, for PCA)
- **32. Probability and statistics** [Concept, stage 3, Core lane]
  - Check: Explain mean vs median, a p-value, Bayes' theorem and an A/B test.
  - Subtopics: (0) Mean, median, mode; (1) Variance and standard deviation; (2) Probability and conditional probability; (3) Bayes' theorem; (4) Distributions: normal, binomial, uniform; (5) Central limit theorem; (6) Correlation vs causation; (7) Hypothesis testing and p-values; (8) A/B testing; (9) Confidence intervals (the idea)

#### E. Data
- **33. NumPy** [Coding, stage 3, Core lane]
  - Check: Vectorise a loop and predict the shape of a broadcast result.
  - Subtopics: (0) `ndarray`, `dtype`, `shape`; (1) Creating arrays: `array`, `zeros`, `ones`, `arange`, `linspace`; (2) Indexing, slicing, boolean masks; (3) `reshape`, `flatten`, transpose; (4) Broadcasting rules; (5) Vectorised operations vs loops; (6) Aggregations with `axis`; (7) Matrix multiply with `@`; (8) `np.random`
- **34. pandas** [Coding, stage 3, Core lane]
  - Check: Clean a dataset: fix types, fill nulls, filter, group and merge.
  - Subtopics: (0) Series and DataFrame; (1) `read_csv` and `to_csv`; (2) `head`, `info`, `describe`; (3) Selecting with `loc` and `iloc`; (4) Boolean filtering; (5) Missing values: `isna`, `fillna`, `dropna`; (6) `groupby` and `agg`; (7) `merge`, `join`, `concat`; (8) `apply` vs vectorised operations; (9) Sorting and `value_counts`; (10) Dates and times
- **35. Data visualisation** [MCQ, stage 3, Core lane]
  - Check: Pick the right chart for a comparison, a trend or a distribution.
  - Subtopics: (0) matplotlib: line, bar, scatter, histogram; (1) Subplots; (2) seaborn (the idea); (3) Choosing the right chart

#### F. Machine learning
- **36. ML fundamentals** [Concept, stage 4, Core lane]
  - Check: Explain overfitting, bias vs variance, cross-validation and data leakage.
  - Subtopics: (0) Supervised, unsupervised, reinforcement learning; (1) Features and labels; (2) Train, validation and test splits; (3) Overfitting and underfitting; (4) Bias–variance trade-off; (5) Cross-validation; (6) Data leakage; (7) Regularisation: L1 and L2; (8) Gradient descent: batch, SGD, mini-batch; (9) Feature scaling; (10) Class imbalance
- **37. ML algorithms** [Concept, stage 4, Core lane]
  - Check: Explain how each algorithm works and when to use it; code one from scratch.
  - Subtopics: (0) Linear regression; (1) Logistic regression; (2) K-nearest neighbours; (3) Decision trees; (4) Random forest (bagging); (5) Gradient boosting, XGBoost (boosting); (6) SVM (the idea); (7) Naive Bayes; (8) K-means clustering; (9) PCA; (10) From scratch in NumPy: logistic regression or k-means
- **38. Evaluation metrics** [Concept, stage 4, Core lane]
  - Check: Choose a metric for an imbalanced problem and read a confusion matrix.
  - Subtopics: (0) Confusion matrix; (1) Accuracy, precision, recall, F1; (2) ROC curve and AUC; (3) PR-AUC for imbalanced data; (4) MAE, MSE, RMSE, R²; (5) Threshold tuning; (6) Choosing the metric for the problem
- **39. scikit-learn workflow** [Coding, stage 4, Core lane]
  - Check: Build a Pipeline with preprocessing, train it, and report F1 on a test set.
  - Subtopics: (0) `train_test_split`; (1) `fit`, `predict`, `predict_proba`; (2) `StandardScaler`, `OneHotEncoder`; (3) `Pipeline` and `ColumnTransformer`; (4) `cross_val_score`; (5) `GridSearchCV`; (6) Feature importance; (7) Saving models with `joblib`

#### G. Deep learning
- **40. Neural network basics** [Concept, stage 4, Core lane]
  - Check: Explain backpropagation, activations, loss functions and optimisers.
  - Subtopics: (0) Neuron: weights and bias; (1) Activations: ReLU, sigmoid, tanh, softmax; (2) Forward pass; (3) Loss: MSE, cross-entropy; (4) Backpropagation and the chain rule; (5) Optimisers: SGD, Adam; (6) Learning rate, epochs, batch size; (7) Vanishing and exploding gradients; (8) Dropout and batch normalisation; (9) Early stopping
- **41. CNN, RNN and LSTM** [Concept, stage 4, Core lane]
  - Check: Explain what CNNs and RNNs are good at, and why transformers replaced RNNs.
  - Subtopics: (0) Convolution, filters, pooling; (1) CNN use cases: images; (2) RNNs and sequence data; (3) LSTM and GRU gates (the idea); (4) Why transformers replaced RNNs; (5) Transfer learning
- **42. PyTorch basics** [Coding, stage 4, Core lane]
  - Check: Write a minimal PyTorch training loop.
  - Subtopics: (0) Tensors and devices (CPU / GPU); (1) Autograd; (2) `nn.Module`; (3) `Dataset` and `DataLoader`; (4) Training loop: `zero_grad`, forward, loss, `backward`, `step`; (5) `model.train()` vs `model.eval()`; `torch.no_grad()`; (6) Saving and loading a `state_dict`

#### H. GenAI and LLMs
- **43. NLP basics (tokens, embeddings)** [Concept, stage 5, Core lane]
  - Check: Explain tokens, embeddings, and how cosine similarity finds similar text.
  - Subtopics: (0) Text preprocessing; (1) Tokenisation: word vs subword (BPE); (2) Bag of words and TF-IDF; (3) Word embeddings (word2vec, the idea); (4) Sentence embeddings; (5) Cosine similarity; (6) Tasks: classification, NER, summarisation
- **44. Transformers and attention** [Concept, stage 5, Core lane]
  - Check: Explain self-attention with query, key and value, and encoder vs decoder.
  - Subtopics: (0) Self-attention: query, key, value; (1) Multi-head attention; (2) Positional encoding; (3) Encoder vs decoder; (4) BERT vs GPT vs T5; (5) Why attention cost grows with length squared; (6) Pretraining vs fine-tuning
- **45. How LLMs generate** [Concept, stage 5, Core lane]
  - Check: Explain temperature, top-p, context windows, and why LLMs hallucinate.
  - Subtopics: (0) Next-token prediction; (1) Context window and its limits; (2) Tokens, cost and latency; (3) Temperature, top-p, top-k; (4) Greedy decoding vs sampling; (5) KV cache (the idea); (6) Hallucination: causes and fixes; (7) Mixture of experts (the idea); (8) Reasoning models (the idea)
- **46. Prompt engineering and structured output** [Concept, stage 5, Core lane]
  - Check: Write a prompt that returns valid JSON, and recover when it doesn't.
  - Subtopics: (0) System vs user prompts; (1) Zero-shot and few-shot; (2) Chain-of-thought; (3) Roles and constraints; (4) Structured output: JSON with a schema; (5) Validating output and retrying; (6) Prompt templates and versioning
- **47. LLM APIs** [Coding, stage 5, Core lane]
  - Check: Call an LLM API with streaming, retries and token counting.
  - Subtopics: (0) OpenAI, Anthropic and Gemini Python SDKs; (1) The messages format; (2) Streaming responses; (3) Token usage and cost tracking; (4) Errors, retries, rate limits; (5) OpenAI-compatible endpoints; local models (Ollama, llama.cpp); (6) API keys in environment variables
- **48. RAG** [Coding, stage 5, Core lane]
  - Check: Build a RAG pipeline end to end and explain your chunking and retrieval choices.
  - Subtopics: (0) Why RAG; (1) Load → chunk → embed → index → retrieve → generate; (2) Chunk size and overlap; (3) Choosing an embedding model; (4) Top-k similarity search; (5) Hybrid search: BM25 + vectors; (6) Reranking; (7) Citations and grounding; (8) PDFs and tables; (9) Failure modes: bad retrieval, lost in the middle
- **49. Vector databases** [Concept, stage 5, Core lane]
  - Check: Explain approximate nearest-neighbour search and compare vector databases.
  - Subtopics: (0) What a vector database stores; (1) Exact vs approximate nearest neighbour; (2) HNSW and IVF (the idea); (3) FAISS, Chroma, Qdrant, Pinecone, pgvector; (4) Metadata filtering; (5) Vector DB vs SQL database
- **50. LangChain, LangGraph, LlamaIndex** [Concept, stage 5, Core lane]
  - Check: Explain what each framework adds and when plain Python is better.
  - Subtopics: (0) What each framework is for; (1) LangChain: models, prompts, chains, retrievers; (2) LangGraph: state, nodes and edges for agents; (3) LlamaIndex: indexes and query engines; (4) Framework vs plain code
- **51. Agents and tool calling** [Coding, stage 5, Core lane]
  - Check: Write a tool-calling agent loop with a step limit and error handling.
  - Subtopics: (0) Agent = LLM + tools + loop; (1) Function / tool calling with JSON schemas; (2) ReAct pattern; (3) Step limits and stopping; (4) Short-term and long-term memory; (5) Multi-agent setups; (6) MCP (Model Context Protocol), the idea; (7) Handling bad tool calls
- **52. Evaluating LLM apps** [Coding, stage 5, Core lane]
  - Check: Build a small eval set and measure retrieval recall and answer faithfulness.
  - Subtopics: (0) Golden test sets; (1) Retrieval metrics: recall@k, MRR; (2) Answer quality: faithfulness, relevance, correctness; (3) LLM-as-judge and its pitfalls; (4) Latency and cost per query; (5) Regression tests for prompt changes; (6) Tools: RAGAS, DeepEval (the idea)
- **53. Fine-tuning and quantisation** [Concept, stage 5, Core lane]
  - Check: Explain LoRA and quantisation, and when fine-tuning beats RAG.
  - Subtopics: (0) Fine-tuning vs RAG vs prompting; (1) Full fine-tuning vs LoRA / QLoRA; (2) Instruction tuning; RLHF and DPO (the idea); (3) Quantisation: 8-bit, 4-bit, GGUF; (4) Trade-offs: memory, speed, quality
- **54. Guardrails and prompt injection** [Concept, stage 5, Core lane]
  - Check: Explain prompt injection and how you'd defend an agent that reads web pages.
  - Subtopics: (0) Direct and indirect prompt injection; (1) Jailbreaks; (2) Input and output filtering; (3) Tool permissions and human approval; (4) PII handling; (5) AI ethics: bias and fairness
- **55. LLMOps** [Concept, stage 5, Core lane]
  - Check: Explain how you'd monitor the quality, latency and cost of an LLM app.
  - Subtopics: (0) Logging prompts and responses; (1) Monitoring quality, latency and cost; (2) Caching; (3) Fallbacks and model routing; (4) Versioning prompts and models; (5) Deploying LLM apps

#### I. Databases
- **56. SQL queries** [Coding, stage 2, Light lane]
  - Check: Write joins, GROUP BY with HAVING, and top-N per group with window functions.
  - Subtopics: (0) `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; (1) `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`; (2) `GROUP BY` and `HAVING`; (3) Joins: inner, left, right, full, self; (4) Subqueries and CTEs (`WITH`); (5) Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`; (6) `CASE WHEN`; (7) `NULL` handling; (8) `INSERT`, `UPDATE`, `DELETE`; (9) Classics: second-highest salary, duplicates, top-N per group
- **57. DBMS concepts** [Concept, stage 3, Light lane]
  - Check: Explain ACID, normalisation up to 3NF, and how an index speeds up queries.
  - Subtopics: (0) Keys: primary, foreign, candidate, composite; (1) Normalisation: 1NF, 2NF, 3NF, BCNF; (2) ACID properties; (3) Transactions: commit and rollback; (4) Isolation levels (the idea); (5) Indexes and B-trees; (6) SQL vs NoSQL; (7) ER diagrams (the idea)

#### J. CS fundamentals
- **58. OOP principles** [Concept, stage 2, Core lane]
  - Check: Explain the four OOP pillars with examples from your own code.
  - Subtopics: (0) Encapsulation, abstraction, inheritance, polymorphism; (1) Class vs object; (2) Overloading vs overriding; (3) Composition vs inheritance; (4) SOLID principles (basic); (5) Design patterns: singleton, factory (the idea)
- **59. Operating systems** [MCQ, stage 3, Light lane]
  - Check: Answer MCQs on processes, threads, scheduling, deadlock and paging.
  - Subtopics: (0) Process vs thread; (1) Process states; (2) CPU scheduling: FCFS, SJF, round robin, priority; (3) Context switching; (4) Deadlock: four conditions, prevention; (5) Mutex and semaphore; (6) Paging, segmentation, virtual memory; (7) Thrashing
- **60. Computer networks** [MCQ, stage 3, Light lane]
  - Check: Answer MCQs on OSI and TCP/IP layers, TCP vs UDP, DNS and HTTPS.
  - Subtopics: (0) OSI model (7 layers) vs TCP/IP model; (1) TCP vs UDP; (2) Three-way handshake; (3) IP addresses; subnetting (the idea); (4) How a DNS lookup works; (5) HTTP vs HTTPS; TLS; (6) Common ports: 22, 80, 443; (7) What happens when you type a URL

#### K. Tools and deployment
- **61. Git and GitHub** [MCQ, stage 4, Light lane]
  - Check: Know merge vs rebase, reset vs revert, stash, and how to resolve conflicts.
  - Subtopics: (0) `init`, `clone`, `add`, `commit`, `push`, `pull`; (1) Branches; merge vs rebase; (2) Merge conflicts; (3) `stash`; (4) `reset` vs `revert`; (5) `.gitignore`; (6) Pull requests and code review; (7) A clean README and repo
- **62. Linux and the shell** [MCQ, stage 4, Light lane]
  - Check: Use common shell commands for files, search, permissions and processes.
  - Subtopics: (0) Navigation: `ls`, `cd`, `pwd`; (1) Files: `cp`, `mv`, `rm`, `mkdir`, `cat`, `less`; (2) Search: `grep`, `find`; (3) Permissions: `chmod`, `chown`; (4) Processes: `ps`, `top`, `kill`; (5) Pipes and redirection; (6) Environment variables; (7) `ssh` and `scp`
- **63. Docker** [Coding, stage 5, Build lane]
  - Check: Write a Dockerfile for a FastAPI app and run it on the right port.
  - Subtopics: (0) Image vs container; (1) Dockerfile: `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`, `EXPOSE`; (2) `docker build` and `docker run`; (3) Ports and volumes; (4) Environment variables; (5) Docker Compose; (6) Small images; `.dockerignore`; (7) Containerising a FastAPI app
- **64. Kubernetes basics** [MCQ, stage 6, Light lane]
  - Check: Explain pod, deployment and service, and why orchestration exists.
  - Subtopics: (0) Why orchestration; (1) Pod, Deployment, Service; (2) ReplicaSets and scaling; (3) ConfigMap and Secret; (4) Ingress (the idea); (5) `kubectl` basics
- **65. Cloud basics (AWS)** [Concept, stage 6, Build lane]
  - Check: Explain EC2, S3, Lambda and IAM, and how you'd deploy a container.
  - Subtopics: (0) IaaS, PaaS, SaaS; (1) Regions and availability zones; (2) EC2, S3, Lambda, RDS; (3) IAM roles and permissions; (4) Deploying a container (ECS, App Runner, Cloud Run), the idea; (5) GPU instances for AI; (6) Managed AI: Bedrock, SageMaker (the idea)
- **66. CI/CD basics** [MCQ, stage 6, Build lane]
  - Check: Read a GitHub Actions workflow that runs tests on every push.
  - Subtopics: (0) Continuous integration vs delivery vs deployment; (1) GitHub Actions workflow files; (2) Running tests and lint on push; (3) Building and pushing Docker images; (4) Secrets in CI

#### L. System design
- **67. System design basics** [Concept, stage 6, Core lane]
  - Check: Explain load balancing, caching, scaling, and SQL vs NoSQL choices.
  - Subtopics: (0) Client–server architecture; (1) Vertical vs horizontal scaling; (2) Load balancers; (3) Caching (Redis); (4) Replication and sharding (the idea); (5) Message queues (the idea); (6) CAP theorem (the idea); (7) Rate limiting; (8) API design
- **68. Designing an LLM app** [Concept, stage 6, Core lane]
  - Check: Design a chatbot over company documents: ingestion, retrieval, cost, latency and evaluation.
  - Subtopics: (0) Chatbot over company documents, end to end; (1) Ingestion pipeline; (2) Retrieval and generation; (3) Streaming responses; (4) Caching and cost control; (5) Latency budget; (6) Evaluation and monitoring; (7) Guardrails; (8) Scaling to many users

#### M. Others
- **69. Aptitude and reasoning** [MCQ, every day]
  - Check: Solve aptitude and reasoning questions quickly and accurately.
  - Subtopics: (0) Percentages, ratios, averages; (1) Profit and loss; (2) Time, speed and distance; (3) Time and work; (4) Probability, permutations and combinations; (5) Number series; (6) Logical reasoning: blood relations, seating, syllogisms; (7) Data interpretation
- **70. Project discussion and HR** [Concept, stage 6, Core lane]
  - Check: Explain each project in 2 minutes, then handle deep follow-up questions.
  - Subtopics: (0) Each project end to end in 2 minutes; (1) Architecture and design choices; (2) Hardest bug and how you fixed it; (3) Metrics and results; (4) What you'd improve next; (5) Tell me about yourself; (6) Strengths and weaknesses; (7) Why this company
- **71. Frontend basics (optional)** [MCQ, optional]
  - Check: Answer basics on JavaScript and React, and read simple component code.
  - Subtopics: (0) HTML and CSS basics; (1) JavaScript: `let` / `const`, functions, `async` / `await`, `fetch`; (2) DOM basics; (3) React: components, props, state; (4) Hooks: `useState`, `useEffect`; (5) Calling your own API from React

### Resources
All links were opened and checked on 5 Nov 2026. "Topics" lists the topic ids each one covers.

#### Learn
- [Python official tutorial](https://docs.python.org/3/tutorial/): The official tutorial, free. Topics: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
- [Real Python](https://realpython.com/): In-depth articles on decorators, generators, asyncio and more. Topics: 6, 7, 10, 12, 13, 15, 30.
- [CS50P (Harvard)](https://cs50.harvard.edu/python/): Free Python course with problem sets. Topics: 1, 2, 3, 4, 5, 6, 8, 9, 10, 15.
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python): Runnable example scripts for each topic. Topics: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
- [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook): Coding-interview cheatsheets, study plans and behavioural prep. Topics: 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 70.
- [Coding patterns (Chanda-Abdul)](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews): Each DSA pattern explained with worked problems. Topics: 17, 18, 19, 20, 23, 24, 25, 26.
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python): Reference implementations: sorting, graphs, DP, ML basics. Topics: 21, 22, 24, 26, 27, 37.
- [MDN: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP): HTTP methods, status codes, headers and CORS. Topics: 28, 60.
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/): The official step-by-step tutorial. Topics: 29, 14.
- [HTTPX docs](https://www.python-httpx.org/): Sync and async HTTP client for Python. Topics: 30, 13.
- [3Blue1Brown](https://www.3blue1brown.com/): Visual series on linear algebra and neural networks. Topics: 31, 40.
- [StatQuest: machine learning playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF): Statistics and ML algorithms explained step by step. Topics: 32, 36, 37, 38, 40.
- [Khan Academy: statistics and probability](https://www.khanacademy.org/math/statistics-probability): Free lessons with practice questions. Topics: 32.
- [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas): Six short lessons with exercises, free. Topics: 34.
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course): Free, about 15 hours, with interactive exercises. Topics: 36, 37, 38.
- [Kaggle Learn: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning): Short hands-on course, free. Topics: 36, 39.
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html): Official docs for every model, metric and pipeline tool. Topics: 37, 38, 39.
- [ageron/handson-ml3](https://github.com/ageron/handson-ml3): Notebooks for the book Hands-On Machine Learning, 3rd edition. Topics: 36, 37, 39, 40, 42.
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners): Free classic-ML curriculum with lessons and quizzes. Topics: 36, 37, 39.
- [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero): Build backprop and a small GPT from scratch, with videos. Topics: 40, 42, 44, 45.
- [PyTorch tutorials](https://pytorch.org/tutorials/): Official tutorials; start with Learn the Basics. Topics: 42.
- [mrdbourke/pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning): Beginner-friendly PyTorch course materials. Topics: 40, 41, 42.
- [Dive into Deep Learning (d2l-ai/d2l-en)](https://github.com/d2l-ai/d2l-en): Free interactive deep learning textbook. Topics: 40, 41, 44.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): Attention and transformers explained visually. Topics: 43, 44.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course): Free: transformers, tokenizers, fine-tuning. Topics: 43, 44, 45, 53.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course): Free course on building AI agents. Topics: 50, 51.
- [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/): 1–2 hour courses on prompting, RAG, agents; videos are free. Topics: 46, 47, 48, 50, 51, 52.
- [LangChain Academy](https://academy.langchain.com/): Free official LangChain and LangGraph courses. Topics: 50, 51.
- [Prompt Engineering Guide](https://www.promptingguide.ai/): Prompting techniques with examples, plus prompt-injection basics. Topics: 46, 54.
- [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques): RAG techniques as runnable notebooks. Topics: 48, 49.
- [langchain-ai/rag-from-scratch](https://github.com/langchain-ai/rag-from-scratch): RAG built step by step, with a video series. Topics: 48, 49.
- [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents): Agent patterns as runnable notebooks. Topics: 51.
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch): Build a GPT-style model in PyTorch, step by step. Topics: 44, 45, 53.
- [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners): Free generative-AI lessons with code. Topics: 45, 46, 47, 48.
- [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners): Free lessons on building agents, including safety. Topics: 51, 54.
- [openai/openai-cookbook](https://github.com/openai/openai-cookbook): Working examples for the OpenAI API, including evals. Topics: 46, 47, 48, 52.
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks): Working examples for the Claude API: tools, RAG, agents. Topics: 46, 47, 51.
- [Hamel Husain: Your AI product needs evals](https://hamel.dev/blog/posts/evals/): A practical guide to evaluating LLM apps. Topics: 52, 55.
- [mlabonne/llm-course](https://github.com/mlabonne/llm-course): LLM roadmaps and notebooks: fine-tuning, quantisation, deployment. Topics: 45, 53, 55.
- [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book): Resources from the book AI Engineering. Topics: 52, 55, 68.
- [Gate Smashers: DBMS playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y): Hindi lectures widely used for placement prep. Topics: 57, 56.
- [Gate Smashers: Operating System playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiGz9donHRrE9I3Mwn6XdP8p): Hindi lectures on scheduling, deadlock and paging. Topics: 59.
- [Pro Git book](https://git-scm.com/book/en/v2): The free official Git book. Topics: 61.
- [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line): Command-line essentials on one page. Topics: 62.
- [Docker docs: Get started](https://docs.docker.com/get-started/): The official beginner guide. Topics: 63.
- [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/): Official basics tutorial. Topics: 64.
- [AWS Skill Builder: Cloud Practitioner Essentials](https://skillbuilder.aws/): Free AWS fundamentals course; search for its name after signing in. Topics: 65.
- [GitHub Actions docs](https://docs.github.com/en/actions): Official quickstart and workflow syntax. Topics: 66.
- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer): The classic system design guide. Topics: 67.
- [ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101): Visual explanations of system design and networking topics. Topics: 67, 28, 60.
- [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design): A free system design course. Topics: 67.
- [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources): Curated system design resources. Topics: 67.

#### Coding practice
- [PYnative Python exercises](https://pynative.com/python-exercises-with-solutions/): 570+ topic-wise coding questions with solutions. Topics: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34.
- [Exercism Python track](https://exercism.org/tracks/python): 146 exercises with free mentor feedback. Topics: 3, 4, 5, 6, 7, 8, 10.
- [HackerRank Python](https://www.hackerrank.com/domains/python): Practice track, plus a free Python (Basic) skill certificate test. Topics: 1, 2, 3, 4, 5, 6, 7, 8.
- [NeetCode roadmap](https://neetcode.io/roadmap): The free NeetCode 150 list, ordered by pattern, with video solutions. Topics: 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26.
- [Striver's A2Z DSA sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z): 474 problems from basics to advanced, free, with progress tracking. Topics: 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27.
- [seanprashad/leetcode-patterns](https://github.com/seanprashad/leetcode-patterns): LeetCode problems grouped by pattern. Topics: 17, 18, 19, 20, 22, 23, 24, 25, 26.
- [LeetCode problem set](https://leetcode.com/problemset/): Where you solve the problems from the lists above. Topics: 17, 18, 19, 20, 21, 22, 23, 24, 25, 26.
- [rougier/numpy-100](https://github.com/rougier/numpy-100): 100 NumPy exercises with solutions. Topics: 33, 31.
- [guipsamora/pandas_exercises](https://github.com/guipsamora/pandas_exercises): Pandas exercises on real datasets, including plotting. Topics: 34, 35.
- [ajcr/100-pandas-puzzles](https://github.com/ajcr/100-pandas-puzzles): 100 short pandas puzzles. Topics: 34.
- [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/): Free 50-question SQL study plan. Topics: 56.
- [DataLemur SQL questions](https://datalemur.com/sql-interview-questions): Free tier of real SQL interview questions, plus a free SQL tutorial. Topics: 56.
- [HackerRank SQL](https://www.hackerrank.com/domains/sql): Free SQL track and SQL skill certificate tests. Topics: 56.
- [Learn Git Branching](https://learngitbranching.js.org/): Interactive Git puzzles in the browser. Topics: 61.
- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/): Learn the Linux shell by solving levels. Topics: 62.
- [Play with Docker](https://labs.play-with-docker.com/): Free Docker playground in the browser. Topics: 63.
- [Killercoda](https://killercoda.com/): Free browser labs for Linux, Docker and Kubernetes. Topics: 62, 63, 64.

#### MCQ practice
- [satwikkansal/wtfpython](https://github.com/satwikkansal/wtfpython): Surprising snippets with explanations: predict-the-output practice. Topics: 2, 3, 5, 6, 12.
- [PYnative Python quizzes](https://pynative.com/python/quizzes/): Topic quizzes with 25 MCQs each. Topics: 1, 2, 3, 4, 5, 6, 8, 9.
- [GeeksforGeeks Quiz Corner](https://www.geeksforgeeks.org/quiz-corner-gq/): Topic MCQs on DSA, OS, DBMS, networks, Python and aptitude. Topics: 16, 27, 57, 59, 60, 69.
- [IndiaBIX](https://www.indiabix.com/): Aptitude, reasoning and technical MCQs (networking, databases). Topics: 69, 57, 60.
- [PrepInsta](https://prepinsta.com/): Company-wise placement papers: TCS, Infosys, Accenture and more. Topics: 69.

#### Interview Q&A
- [learning-zone/python-basics](https://github.com/learning-zone/python-basics): About 340 Python interview questions with answers, by topic. Topics: 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 58.
- [Probability interview questions](https://github.com/alexeygrigorev/data-science-interviews/blob/master/contrib/probability.md): Community-answered probability questions. Topics: 32.
- [alexeygrigorev/data-science-interviews](https://github.com/alexeygrigorev/data-science-interviews): Theory and technical (SQL, Python) questions with answers. Topics: 36, 37, 38, 32, 56.
- [andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions): ML and computer-vision interview questions. Topics: 36, 37, 38, 40, 41.
- [AI engineering interview Q&A (amitshekhariitbhu)](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions): LLMs, RAG, agents, fine-tuning, evals and AI system design. Topics: 45, 46, 48, 49, 51, 52, 53, 55, 68.
- [LLM Interview Q&A Hub (KalyanKS-NLP)](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub): 100+ LLM questions with answers. Topics: 43, 44, 45, 53.
- [RAG Interview Q&A Hub (KalyanKS-NLP)](https://github.com/KalyanKS-NLP/RAG-Interview-Questions-and-Answers-Hub): 100+ RAG questions with answers. Topics: 48, 49, 52.
- [IndiaBIX: HR interview](https://www.indiabix.com/hr-interview/questions-and-answers/): Common HR questions with sample answers. Topics: 70.
- [sudheerj/javascript-interview-questions](https://github.com/sudheerj/javascript-interview-questions): JavaScript interview questions with answers. Topics: 71.
- [sudheerj/reactjs-interview-questions](https://github.com/sudheerj/reactjs-interview-questions): React interview questions with answers. Topics: 71.
