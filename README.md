# Haptic Map Conflict Checker

A Python-based tool designed to streamline the process of testing and resolving duplicate stream files in new maps for your FiveM server. While it doesn't solve every issue (some maps require manual editing), this script handles 90% of use cases efficiently, helping you identify and remove duplicate files from conflicting maps.

## Features
- **Automated Duplicate Detection:** Scans for duplicate stream files in newly added maps.
- **Conflict Resolution:** Moves conflicting files to a temporary folder for review.
- **Restore Functionality:** Allows you to restore files if needed and try alternative resolutions.
- **Streamlined Workflow:** Works with an organized folder structure to keep your map testing process clean and efficient.

## Prerequisites
1. **Folder Setup:**
   - `[Test]`: Place the map you want to check for conflicts here.
   - `[Temp]`: Files identified as conflicts will be moved here.
   - `[Tested]`: Store maps that have been verified and contain no duplicate stream files.

2. **Python Installation:** Ensure Python is installed on your system to run the script.

## How to Use
1. **Setup the Folders:**
   - Create the `[Test]`, `[Temp]`, and `[Tested]` folders in the same directory as the script.

2. **Prepare Your Maps:**
   - Add your existing, conflict-free maps to the `[Tested]` folder.
   - Place the new map you want to test in the `[Test]` folder.

3. **Run the Script:**
   - Execute the script with Python:
     ```bash
     python map_conflict_checker.py
     ```

4. **Resolve Conflicts:**
   - The script will scan for duplicate stream files.
   - Conflicting files will be moved to the `[Temp]` folder for your review.

5. **Testing & Iteration:**
   - Test the map in your server after using the tool. 
   - If issues persist:
     - Use the restore function to revert changes.
     - Re-run the script, select a different resolution option, and test again.

## Limitations
- While this tool covers most cases, some maps may still require manual editing.
- Ensure you back up your files before running the script to avoid accidental data loss.

## Example Workflow
1. Add a map to `[Test]` and verified maps to `[Tested]`.
2. Run the script to check for conflicts.
3. Review files in `[Temp]` and decide how to proceed.
4. If the map works, move it to `[Tested]`.

## Notes
- Always test your maps on a staging server after resolving conflicts.
- If an issue arises, the restore function can help you retry with alternative options.

---

This tool aims to save time and simplify your map management process. Feel free to contribute, suggest improvements, or report issues via GitHub! 🌍�
