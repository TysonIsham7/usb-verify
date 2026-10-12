# First run (planned)

1. Use an empty device if possible. Never type a seed phrase into a computer.
2. Plug the device into the computer and unlock it as normal.
3. Run `usb-verify check`. Explain each check as it runs (see CHECKS.md).
4. Optionally run `usb-verify watch --seconds 30` while opening the Ledger app normally.
5. Read the result with the user using RESULTS.md.

If you see a permission error, it is a warning, not a pass. Help the user fix permissions and rerun.
Today only `python -m usb_verify` works, and it prints "not implemented".
