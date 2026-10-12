"""Stub entrypoint. Prints version only. No USB access."""

from usb_verify import __version__


def main() -> None:
    print(f"usb-verify {__version__}")
    print("not implemented")


if __name__ == "__main__":
    main()
