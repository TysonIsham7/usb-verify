# Install (planned)

1. Install Python 3.10+ and libusb (macOS: `brew install libusb`; Debian/Ubuntu: `sudo apt install libusb-1.0-0`).
2. Install: `pipx install usb-verify` (not yet published; for now `pip install -r requirements.txt` from a clone).
3. Verify the release (once releases exist): check the SHA-256 checksum against the published file, and verify the Sigstore or GPG signature on the tag. If either fails, stop.
4. The tool needs no internet. You can disconnect before running it.
