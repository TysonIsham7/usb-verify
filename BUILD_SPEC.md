# usb-verify BUILD SPEC

Spec sheet for cloud agents building usb-verify. Read the README disclosure contract first.

## Goal

An offline Python CLI that runs preliminary checks on a USB hardware wallet (Ledger first) and returns one of three results: clean pass, pass with conditions, or red light.

## Trust and intent

This project is skeptically optimistic: it is trying to help, and it is honest about its limits.

1. **No guarantees.** This is an attempt to help, not a security promise.
2. **You don't have to trust it.** Skepticism is expected and welcome. Read the code before you run it.
3. **Test with an empty Ledger**, or one holding very little money.
4. **Tyson Isham has no crypto wallet or address connected to this project or its code. Nothing in this repo sends anything to him or anyone else.**
5. **It isn't another attack surface.** It is just a checker you run on your own device, at your own risk. It makes no network calls.
6. **The code contains no attacks.**
7. **Tyson isn't seeking anyone's crypto.**

## Core design principles (equal weight)

1. **False-negative bias.** Anything ambiguous is flagged as a warning, never swallowed. A false negative is the one failure that matters. Unknown models, missing profile fields, read errors, permission errors, and timeouts all produce warnings, not passes.
2. **Output modes are first-class.** Three results:
   - **Clean pass:** framed as "passed N checks," never "device is secure." Always suggests a second source of verification (e.g. the vendor's genuine check, HWI address cross-check).
   - **Pass with conditions:** lists specific next steps the user should take to actually be safe.
   - **Red light:** something was caught. Says what, and tells the user to stop using the device for funds.
   Output is available as human text and as JSON (`--json`) so agents can read it.
3. **Agent-readable docs.** Multiple READMEs in `docs/agents/` let a user's AI agent walk them through install, first run, and each check one by one, answer follow-up questions, and advise on out-of-scope threats (side-channel, fault injection, relay, social engineering), including hardware a typical person already owns (a Mac, a Flipper) and where to take a device.

## Hard constraint: disclosure contract

The tool must never claim more than the README contract. CAN: descriptor mismatch vs vendor profile; traffic anomalies in a short watch window. CANNOT: side-channel, fault injection, Bluetooth relay/distance, social engineering, perfect-descriptor implants. Every result output includes a one-line pointer to these limits.

## Requirements

- **Language/stack:** Python 3.10+, native USB via pyusb on libusb. No vendor SDK required.
- **One-command install:** `pipx install usb-verify` (or `pip install .` from a clone). libusb install notes per OS in docs.
- **Offline-first:** no network calls at runtime, ever. Profiles ship in the repo. A test asserts no socket use.
- **Descriptor dump:** `usb-verify dump` prints device, configuration, interface, and endpoint descriptors (text and JSON).
- **Profile check:** `usb-verify check` compares descriptors to `profiles/<vendor>/<model>.json`. Any mismatch is red or warning per field rules in the profile. Profile values must cite their source; unverified values are marked `"verified": false` and can only produce warnings.
- **Traffic watch:** `usb-verify watch --seconds 30` observes enumeration and traffic for a short window during a normal session and flags anomalies (re-enumeration, unexpected interfaces like HID keyboard, unexpected endpoints, unexpected volume). Read-only.
- **Emulated peripheral:** a pure-software fake USB device (descriptor fixtures, plus later a virtual device such as via speculos or Linux gadget/USB-IP) powers happy-path and tamper-path tests. No real hardware needed in CI.
- **Signed releases:** release tags signed with Sigstore (preferred) or GPG; SHA-256 checksums published with each release; `docs/agents/INSTALL.md` explains how to verify both.
- **Community testing call:** issue template for contributors with empty or suspected-compromised Ledgers. Never ask for seeds, PINs, or personal data.

## Milestones and acceptance criteria

### Standing acceptance criteria (every milestone)
- The code makes no network calls (test asserts no socket use).
- The repo contains no wallet addresses (CI grep for address patterns fails the build).
- Trust and intent section stays in README and this spec.

### M0: Skeleton (done)
- Stub `python -m usb_verify` prints version and "not implemented". No USB access.
- `pytest` passes the fake-descriptor test.

### M1: Results model
- Result types: PASS, PASS_WITH_CONDITIONS, RED. Each check returns pass / warn / fail with a reason and next steps.
- Aggregation: any fail -> RED; any warn -> PASS_WITH_CONDITIONS; else PASS ("passed N checks" + second-source suggestion).
- Tests prove ambiguous inputs never yield PASS.

### M2: Profiles
- JSON schema for profiles; at least one Ledger model profile with sourced values (unverified values flagged).
- Tests: matching fixture -> PASS; altered fixture (extra HID interface, wrong VID/PID, extra endpoint) -> RED or warn.

### M3: Descriptor dump + check on real USB
- `dump` and `check` via pyusb. Permission errors give clear guidance and count as warnings.
- Works on macOS and Linux (Windows best effort).

### M4: Traffic watch
- Short-window watch; enumeration events and anomaly heuristics. All heuristics documented in CHECKS.md.

### M5: Agent docs complete
- Every check in CHECKS.md, every result in RESULTS.md, with plain-language explanations.

### M6: Release
- Signed tag, checksums, install verification steps. No network at runtime confirmed by test.

### M7: Community testing
- Issue template live; first external reports folded into profiles.

## Out of scope
GUI, Mac app (see related idea), cloud services, telemetry, anything that writes to the device.

## Background
Oct 12, 2026 GitHub scan: no tool decodes Ledger USB traffic or checks returned units for implants. Building blocks: LedgerHQ/speculos, LedgerHQ/ragger, LedgerHQ/ledgerctl, bitcoin-core/HWI, newaetech/chipwhisperer, Ledger-Donjon/scaffold, WalletScrutiny. Motivation: a user in Japan found his Ledger about 2 g heavier than documented and had no tool to act on it.
