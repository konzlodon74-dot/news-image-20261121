#!/usr/bin/env python3
"""Entry for make.fun news-image-20261121.

Copies the front-page image for Saturday 21 November 2026 to the output
path. The image itself is the entry: a one-page newspaper summarising
the day's world news (Russian missiles landing in Poland, the 6.8 quake
in Peru, the UK-EU reset deal in Brussels, the Wall Street AI selloff,
Denmark thwarting an alleged Russian assassination plot, and New York's
plan to close Rikers Island by 2032).

Standard library only. Before copying, the program checks the file is a
whole PNG of at most 1 MiB and exactly 1024 by 1024 pixels, so a damaged
or wrong-sized image fails loudly instead of being submitted.
"""

import hashlib
import os
import shutil
import struct
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
MAX_BYTES = 1_048_576
EXPECT_W = EXPECT_H = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_png_size(data):
    """Return (width, height) from the IHDR chunk of a PNG byte string."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        fail("entry.png is not a PNG file")
    chunk_len = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_len != 13:
        fail("entry.png has no valid IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    bit_depth, color_type = data[24], data[25]
    if bit_depth != 8 or color_type not in (2, 6):
        fail(f"entry.png has unexpected IHDR: {bit_depth}-bit color type {color_type}")
    return width, height


def check_png_whole(data):
    """Walk the PNG chunk list, verifying lengths and CRCs, ending at IEND."""
    offset = 8
    seen_iend = False
    while offset + 8 <= len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        chunk_type = data[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(data):
            fail(f"entry.png is truncated inside {chunk_type!r} chunk")
        body = data[offset + 4:end - 4]
        stored_crc = struct.unpack(">I", data[end - 4:end])[0]
        if zlib.crc32(body) & 0xFFFFFFFF != stored_crc:
            fail(f"entry.png has a bad CRC in {chunk_type!r} chunk")
        offset = end
        if chunk_type == b"IEND":
            seen_iend = True
            break
    if not seen_iend:
        fail("entry.png is truncated: no IEND chunk at the end")
    if offset != len(data):
        fail("entry.png has trailing bytes after the IEND chunk")


def main():
    if not SOURCE.is_file():
        fail("entry.png is missing from the repository")
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    width, height = read_png_size(data)
    if (width, height) != (EXPECT_W, EXPECT_H):
        fail(f"entry.png is {width}x{height}, expected 1024x1024")
    check_png_whole(data)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
