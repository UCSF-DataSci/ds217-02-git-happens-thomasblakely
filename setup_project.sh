#!/bin/bash
echo "Creating Directory Structure"
mkdir -p src data output

echo "Generating Initial Files"
# git.ignore | From class notes
cat > .gitignore << 'EOF'
# Python cache files
__pycache__/
*.pyc
# Data and secrets
data/raw/*.csv
.env
*.key
# IDE files
.vscode/
.idea/
# Track important files
!data/processed/important_results.csv
EOF

# Requirements.txt
## Modifies requirements.txt initially provided
cat > requirements.txt << 'EOF'
# Update Testing Framework
pytest>=8.0.0
EOF

echo "Creating CSV w/ 8 Records"
cat > data/students.csv << 'EOF'
name,age,grade,subject
Mikey,14,74,Science 
Brandon,12,89,History
Mouth,13,59,English
Chunk,13,67,Science
Data,14,94,Math
Stef,15,96,History
Andy,16,78,English
Francis,12,82,English
EOF

echo "Setting up Python template files with TODO placeholders"
# data_analysis.py
cat > src/data_analysis.py 