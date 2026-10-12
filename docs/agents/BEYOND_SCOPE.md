# Beyond this tool's scope

Advice here is general and not verified by this project. Mark it that way to the user.

- **Side-channel (power/EM/timing):** needs lab gear (e.g. ChipWhisperer). Most people can't test this; defense is buying from the vendor directly and using a PIN plus passphrase.
- **Fault injection / glitching:** also lab territory. Keep physical control of the device; a strong passphrase adds protection if the device is stolen.
- **Bluetooth relay / distance:** turn Bluetooth off when not needed or use USB; confirm every transaction on the device screen.
- **Social engineering:** no real support will ask for your seed. Ignore unsolicited calls, emails, or mailed "replacement" devices.
- **Perfect-descriptor implants:** physical checks help: compare weight and photos to a known-good unit (a small weight difference alone is not proof; scales and production batches vary, unverified), inspect the packaging.

**Hardware people may already own:** a Mac or Linux laptop (USB descriptor inspection, Wireshark USB capture on Linux), a Flipper Zero (Bluetooth/NFC/RF awareness; limited for USB analysis, unverified), a kitchen scale accurate to 0.1 g, a phone camera for board photos.

**Where to take a device:** the vendor's official support (start here), a reputable hardware security firm, or a local hackerspace with experience in electronics. Never hand over a device holding funds.
