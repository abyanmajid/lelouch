# Floch

Floch is a feedback engine for handwritten Java code, designed for pen-and-paper programming exams. It combines a fine-tuned TrOCR model — trained on a synthetic dataset of handwritten Java code spanning key OOP concepts — with an AST-based static analysis pipeline to deliver line-level feedback on syntax, structure, and object-oriented design quality.

## Problem Statement

**TO NOTE:** This project is MY OWN, non-professional, implementation of **CS2025/4 Handwritten Code Recognition for Pen-and-Paper based Programming Exam**, a Winter 2025 vacation research project at The University of Sydney. That is, this is a hobby project and I did not formally partake in the research program.

> With the emergence of GenAI, universities are moving towards pen-and-paper exams. However, for programming exams, it creates a lot of issues with marking and feedback. In this work, the aim is to recognize students’ handwritten code using OCR. However, the challenge is that OCR errors, perhaps due to varied handwriting styles and inconsistencies in the quality of the handwritten text, can lead to inaccurate or incomplete recognition of the code.
>
> Therefore, this research focuses on several core challenges. First, we seek to improve the accuracy of OCR in recognizing programming languages by training the model to understand specific programming (e.g. OOP, SQL etc) syntax and structures. Second, we aim to develop a system that can not only recognize the code but also provide meaningful feedback on its correctness and quality.