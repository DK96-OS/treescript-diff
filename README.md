# TreeScript Diff
Find the differences between TreeScript files.

## Introduction
A Command Line app for comparing TreeScript files, similar to `git diff`.

## Usage
This package expects two input files, both must be valid TreeScript.

```bash
treescript-diff <file1> <file2>
```

The first file is considered the original, the second file is updated TreeScript.

### Default Action
The program will return the diff in this structure:
1. newly added files
2. blank line
3. deleted files

### Additions Only
Use the argument: `--add`

### Deletions Only
Use the argument: `--del`
