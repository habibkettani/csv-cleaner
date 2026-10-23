# Undo notes

## C1 - Deleted function
- Situation: I deleted remove_duplicates by mistake. The change was only in my working directory, nothing staged.
- Command: git restore cleaner.py
- Why: restore copies the last committed version back over my file. The problem is only on disk, so I don't need to touch staging or history.

## C2 - Debug line
- Situation: print("debug") was staged. I wanted it out of the next commit but still on disk, then gone for good.
- Commands: git restore --staged cleaner.py, then git restore cleaner.py
- Why: --staged only unstages, so my edit stays safe in the file. Plain restore then discards it from the working directory. Two steps for two different intentions.

## C3 - WIP commit
- Situation: one unpushed commit "WIP" mixed a code change and a README change.
- Command: git reset HEAD~1 (mixed, the default), then two separate add + commit.
- Why: mixed reset removes the commit but keeps the changes in my files, unstaged, so I can stage file by file. --soft would keep everything staged and I would have to unstage first. --hard would delete the changes and I would have to retype the code. Safe because nothing was pushed.

## C4 - Bug already pushed
- Situation: a buggy commit is on main and my teammates already pulled it.
- Command: git revert HEAD
- Why: revert adds a new commit with the opposite changes, so history only grows. Reset or amend would rewrite a commit that others already have and break their history.

## C5 - Bad message
- Situation: my last commit (not pushed) had a vague message and was missing this entry.
- Commands: git add UNDO_NOTES.md, then git commit --amend -m "Add notes on undo operations"
- Why: amend replaces the last commit with a new one that includes what is staged and the new message, in one step, without adding a commit. Fine because it was not pushed.

## Bonus - Regretted reset --hard
- Situation: git reset --hard HEAD~3 removed my last three commits from the branch.
- Commands: git reflog, then git reset --hard HEAD@{1}
- Why: reflog records every move of HEAD, so the "lost" commits still exist and I can point main back to them. This would not work for edits that were never committed: Git never stored them, so reset --hard deletes them for good.
