# Merge notes

## Part B - Three-way merge
The second merge could not be a fast-forward because main had moved forward (it received count-rows) after docs-steps was created, so the two histories had diverged and Git had to create a merge commit with two parents.

## Part C - Conflict in README.md
- File: README.md, line 3 (the intro sentence).
- Version from main (intro-short): "Clean CSV files in one command."
- Version from intro-long: "Command-line tool that cleans messy CSV files: empty rows, extra spaces, duplicates."
- Kept: "Clean messy CSV files in one command: empty rows, extra spaces, duplicates."
- Why: I combined both. The short version is punchy but vague, the long one is precise but heavy. The combined sentence keeps the "one command" promise and lists exactly what the tool cleans.
