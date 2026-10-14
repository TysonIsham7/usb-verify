# usb-verify

> **⚠️ Untested on a real Ledger.** This CLI has only been run against an emulated device. It has never been tested on real Ledger hardware, and the maintainer does not own a Ledger. This is a goodwill project built to help people, and it may grow into something broader.
>
> **Can you help?** If you have a Ledger with **no crypto on it** (empty, never holding funds), running this CLI on it would give the project its first real-world test. See [Call for contributors](#call-for-contributors).

> **User story:** Someone should be able to install this CLI, tell their agent to run it or run it themselves, and get a round of preliminary checks yielding either a true negative or a pass-with-conditions with next steps.

usb-verify is an offline command-line tool that runs a round of preliminary checks on a USB hardware wallet (Ledger first) using hardware you already own. It is built in good faith to give people some peace of mind and to help prevent crypto theft. It is **not** a guarantee.

## Trust and intent

This project is skeptically optimistic: it is trying to help, and it is honest about its limits.

1. **No guarantees.** This is an attempt to help, not a security promise.
2. **You don't have to trust it.** Skepticism is expected and welcome. Read the code before you run it.
3. **Test with an empty Ledger**, or one holding very little money.
4. **Tyson Isham has no crypto wallet or address connected to this project or its code. Nothing in this repo sends anything to him or anyone else.**
5. **It isn't another attack surface.** It is just a checker you run on your own device, at your own risk. It makes no network calls.
6. **The code contains no attacks.**
7. **Tyson isn't seeking anyone's crypto.**

## Why

A user in Japan weighed his Ledger, found it about 2 g heavier than the documentation said, and concluded it was unsafe. He had no tool to act on that worry. An Oct 12, 2026 scan of GitHub found no tool that decodes Ledger USB traffic or checks a returned unit for implants. This project aims to fill a small, honest part of that gap.

## Radar-detector disclosure contract

Like a radar detector, this tool tells you what it listens for and what it cannot hear. This contract is a hard constraint on the project.

**What it CAN detect (once implemented):**
- Supply-chain implants or swaps that change the USB descriptors, flagged as a mismatch against the vendor's published profile (stored as JSON in `profiles/`).
- Traffic anomalies during a short watch window: unexpected interfaces, endpoints, re-enumeration, or traffic patterns that don't fit the profile.

**What it CANNOT detect:**
- Side-channel attacks (power, EM, timing).
- Fault injection / glitching.
- Bluetooth relay or distance attacks.
- Social engineering (fake support, phishing, seed-phrase scams).
- Implants that present a perfect, matching descriptor and behave normally during the watch window.

**Cable caveat (Phase 4):**
- It CAN detect cables that enumerate hidden devices, for example an unexpected HID keyboard appearing when a cable is plugged in (as with O.MG-style cables).
- It CANNOT detect passive or non-enumerating implants: a cable or device that never announces itself over USB is invisible to this tool.

## Vision and roadmap

Ledger is the starting point. The longer-term goal is a "danger sniffer" across many device surfaces, eventually all of them. Profiles are pluggable per device class, so each phase adds profiles without changing the core.

1. **Ledger** hardware wallets.
2. **Trezor and other hardware wallets.**
3. **Everyday USB peripherals:** keyboards, drives, hubs.
4. **Charging and data cables** (see the cable caveat above).

Each phase keeps the same disclosure contract: what it can detect, what it can't.

## Results, honestly

- **Clean pass:** "Passed N of N checks." Never "device is secure." Always suggests a second source of verification.
- **Pass with conditions:** something was ambiguous. You get specific next steps.
- **Red light:** something was caught. Stop using the device for funds.

Anything ambiguous is a warning, never silently passed. A false negative is the one failure that matters.

## No guarantees

This software is provided as-is under the MIT License. Passing every check means only that those checks found nothing. It does not prove a device is untampered. Do not treat it as your only line of defense.

## For AI agents

If you are an agent helping a user, start at [docs/agents/AGENT_GUIDE.md](docs/agents/AGENT_GUIDE.md).

## Building it

See [BUILD_SPEC.md](BUILD_SPEC.md) for the build spec, milestones, and acceptance criteria.

## Call for contributors

We need people with **empty** or **suspected-compromised** Ledgers (never one holding funds) to run captures and report results. Open an issue with your device model, firmware version, and descriptor dump once the dump command exists. Never share a seed phrase, PIN, or anything that identifies you.

**Reporting:** normal reports go in GitHub issues. For serious findings (a suspected compromised device, or a flaw in this tool), use GitHub's private vulnerability reporting instead. See [SECURITY.md](SECURITY.md). There is no email contact.

## Releases (proposed, awaiting Tyson's OK)

Nothing is published yet. The proposed setup:
- Sigstore keyless signing via GitHub Actions, plus a `SHA256SUMS` file on every release.
- PyPI publishing via trusted publishing (no stored tokens), plus GitHub releases. Once published, install would be `pipx install usb-verify`; until then, install from a clone.

## Possible building blocks (not dependencies yet)

- [LedgerHQ/speculos](https://github.com/LedgerHQ/speculos): Ledger app emulator
- [LedgerHQ/ragger](https://github.com/LedgerHQ/ragger): run sessions on emulator or real device
- [LedgerHQ/ledgerctl](https://github.com/LedgerHQ/ledgerctl): talk to a Ledger over USB, genuine check
- [bitcoin-core/HWI](https://github.com/bitcoin-core/HWI): multi-wallet CLI, address cross-checks
- [newaetech/chipwhisperer](https://github.com/newaetech/chipwhisperer): side-channel and glitching research
- [Ledger-Donjon/scaffold](https://github.com/Ledger-Donjon/scaffold): chip attack research board
- [WalletScrutiny](https://github.com/WalletScrutiny/WalletScrutinyCom): reproducible-build checks

## Related ideas

- [Consumer hardware verification kit](https://app.notion.com/p/3f71f8483ef381b1aff9d0a7a20d652f)
- [Mac USB verification app](https://app.notion.com/p/3f71f8483ef3813b8aaaea6f69c9c632)
- [The iPhone Moment for Agentic AI: trust layer](https://app.notion.com/p/3ef1f8483ef3810bb13beb5bd07df3a9)
- [Family Box](https://app.notion.com/p/3d21f8483ef38107bfa8fa6fcb371d95)

## License

MIT. Copyright (c) 2026 Tyson Isham.
