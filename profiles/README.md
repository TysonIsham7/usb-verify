# Vendor profiles

One JSON file per device model at `profiles/<vendor>/<model>.json`, holding the expected USB descriptors.

Every value must cite a source. Values not confirmed against a known-good device must be marked `"verified": false`; they can only produce warnings, never a pass. No profiles exist yet.
