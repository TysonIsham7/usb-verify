# Checks, one by one (planned)

1. **Device identity:** vendor ID and product ID match the profile. Mismatch = red.
2. **Descriptor strings:** manufacturer and product strings match. Mismatch = warning or red per profile.
3. **Configuration and interfaces:** number and class of interfaces match. An extra interface (especially a HID keyboard or mass storage) = red.
4. **Endpoints:** endpoint count, direction, and sizes match. Unexpected endpoint = red.
5. **Profile coverage:** if the model is unknown or the profile has unverified values = warning.
6. **Traffic watch:** re-enumeration, new interfaces appearing, or unexpected traffic during the window = warning or red.
7. **Read problems:** permission errors, timeouts, partial reads = warning, never pass.

Profile values are only as good as their sources. Values not confirmed against a known-good device are marked unverified.
