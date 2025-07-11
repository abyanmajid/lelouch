# Lelouch 

**Lelouch** is a feedback engine for scanning and evaluating handwritten Java code in terms of correctness and Object-Oriented Programming (OOP) theory. The *scanning part* is implemented by a fine-tuned TrOCR model, and the *evaluation part* is implemented by a fine-tuned LLaMa 3.1:8b model quantized to 8-bits.

This repository dumps all components of the system *(WIP)*:

- [data/](https://github.com/abyanmajid/lelouch/tree/main/data) contains the dataset and relevant source files used for generating and curating the dataset, the overwhelming majority of which is synthetically attained.
- [llm/](https://github.com/abyanmajid/lelouch/tree/main/llm) contains notebooks for fine-tuning the LLaMa 3.1:8b base model
- [ocr/](https://github.com/abyanmajid/lelouch/tree/main/ocr) contains notebooks for fine-tuning the TrOCR base model
- [app/](https://github.com/abyanmajid/lelouch/tree/main/app) contains source files for the web user interface orchestrating the entire engine

**Aside:** This project is named after *Lelouch Lamperouge*, the lead character in the anime *Code Geass*. Wonderful character, one of my favourites of all time!

## Synthetic Data Generation & Curation

WIP.

## Fine-Tuning Microsoft's TrOCR Model

WIP.

## Fine-Tuning 

WIP.

## License

**Lelouch** is GPL-3 licensed.
