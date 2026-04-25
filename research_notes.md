# Research Notes: Prompt Engineering Paper Origins

## Historical Papers and Key Dates

### GPT-2
- **Paper Title:** "Language Models are Unsupervised Multitask Learners"
- **Authors:** Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever
- **Publication Date:** February 14, 2019 (initial release); full 1.5B parameter model November 5, 2019
- **Institution:** OpenAI
- **Key Contribution:** Demonstrated that language models could perform multiple NLP tasks without task-specific training, using zero-shot transfer via task conditioning

### GPT-3
- **Paper Title:** "Language Models are Few-Shot Learners"
- **Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen M. Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei
- **Publication Date:** May 28, 2020
- **Institution:** OpenAI
- **Key Contribution:** Showed that scaling language models to 175B parameters enabled few-shot learning (in-context learning) without gradient updates

### Chain-of-Thought (CoT)
- **Paper Title:** "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- **Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- **Publication Date:** January 28, 2022
- **arXiv ID:** arXiv:2201.11903
- **Institution:** Google Research
- **Key Contribution:** Introduced chain-of-thought prompting, showing that generating intermediate reasoning steps significantly improves LLM performance on complex reasoning tasks (arithmetic, commonsense, symbolic)
- **Key Finding:** A 540B-parameter LLM achieved state-of-the-art on GSM8K math word problems using only eight CoT exemplars

### ReAct
- **Paper Title:** "ReAct: Synergizing Reasoning and Acting in Language Models"
- **Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Publication Date:** October 6, 2022
- **arXiv ID:** arXiv:2210.03629
- **Institution:** Princeton University, Google Research
- **Key Contribution:** Framework enabling LLMs to interleave reasoning traces and task-specific actions, improving synergy between reasoning and acting
- **Key Finding:** ReAct reduced hallucination in question answering (HotpotQA) and fact verification (Fever), and outperformed imitation/RL by 34% and 10% on interactive decision-making tasks

### Tree-of-Thoughts (ToT)
- **Paper Title:** "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
- **Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Publication Date:** May 17, 2023
- **arXiv ID:** arXiv:2305.10601
- **Institution:** Princeton University, Google DeepMind
- **Key Contribution:** Generalized CoT by enabling LLMs to explore multiple reasoning paths, self-evaluate choices, and look ahead or backtrack
- **Key Finding:** On Game of 24, GPT-4 with CoT solved 4% of tasks, while ToT achieved 74% success rate

### The Prompt Report
- **Paper Title:** "The Prompt Report: A Systematic Survey of Prompting Techniques"
- **Authors:** Sander Schulhoff, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, Chenglei Si, Yinheng Li, Aayush Gupta, HyoJung Han, Sevien Schulhoff, Pranav Sandeep Dulepet, Saurav Vidyadhara, Dayeon Ki, Sweta Agrawal, Chau Pham, Gerson Kroiz, Feileen Li, Hudson Tao, Ashay Srivastava, Hevander Da Costa, Saloni Gupta, Megan L. Rogers, Inna Goncearenco, Giuseppe Sarli, Igor Galynker, Denis Peskoff, Marine Carpuat, Jules White, Shyamal Anadkat, Alexander Hoyle, Philip Resnik
- **Publication Date:** June 6, 2024
- **arXiv ID:** arXiv:2406.06608
- **Institution:** University of Maryland, Princeton University, other institutions
- **Key Contribution:** Most comprehensive survey of prompt engineering to date, establishing structured taxonomy of 58 LLM prompting techniques and 40 techniques for other modalities
- **Key Finding:** Provides unified vocabulary of 33 terms and best practices for state-of-the-art LLMs

## Timeline Summary

| Year | Month | Milestone |
|------|-------|-----------|
| 2019 | Feb | GPT-2 released |
| 2019 | Nov | GPT-2 full model (1.5B params) |
| 2020 | May | GPT-3 released (175B params) |
| 2022 | Jan | Chain-of-Thought paper |
| 2022 | Oct | ReAct paper |
| 2023 | May | Tree-of-Thoughts paper |
| 2024 | Jun | The Prompt Report |
