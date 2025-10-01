[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wSmf0KE5)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20697592)

# Assignment 02: Git Workflow, CLI Automation, and Python Data Processing

**Due Date**: October 1, 2025
**Points**: 20 total
**Estimated Time**: 3-4 hours

## Project Overview

For this project we were assigned to do 4 tasks: 
   1) Creation of 2 branches: `feature/project-scaffold` & `feature/data-processing`
   2) Development of an automated project setup shell file, `setup_project.sh`, in branch `feature/project-scaffold`
   3) Development of 2 data processing scripts: `data_analysis.py` & `data_analysis_functions.py`, in branch `feature/data-processing`
   4) Merge `feature/project-scaffold` & `feature/data-processing` with `main`.

Successful completion of these tasks allows us to create `analysis_report.txt`, a .txt file which contains:
   - Total number of students
   - Average grade (formatted to 1 decimal place)
   - Subject counts
   - For the `data_analysis_functions.py` generated script: grade distribution with percentages

## Development Documentation

Initial versions of this project, commits made on September 24, 2025, were made to allow me to get a feel for merging and developing features on separate branches. 

Changes pushed on October 1, 2025, were those following internal development of the features over the week. Many of the commits were minor adjustments to comply with the auto-checker. For instance, the auto-checker checks to make sure 'Alice' was included in a .csv developed by setup_project.sh.

This project is fully completed as of October 1, 2025, based on the criteria Professor Seaman originally provided as well as the auto-checker verification.

## Features

1) `setup_project.sh:`
   - Create directory structure (src, data, output)
   - Generate initial files (.gitignore, requirements.txt)
   - Create sample data files (students.csv with at least 8 records)
   - Set up Python template files with TODO placeholders

2) `data_analysis.py:`
   - Reads CSV file 
   - Calculate basic statistics (total students, average grade)
   - Count students by subject (Math)
   - Writes results to `output/analysis_report.txt`

3) `data_analysis_functions.py:`
- Reads CSV file
- Provide more detailed analysis (highest/lowest grades, grade distribution)
- Generate a more comprehensive report
- Writes results to `output/analysis_report.txt`

## Usage

1) Run `./setup_project.sh` to create project structure
2) Execute `python src/data_analysis.py` for basic analysis
3) Run `python src/data_analysis_functions.py` for advanced analysis 

## Status

| Branch | Purpose | Status |
|--------|---------|--------|
| main | Production code | Active |
| feature/project-scaffold | CLI automation | Merged |
| feature/data-processing | Python analysis | Merged |