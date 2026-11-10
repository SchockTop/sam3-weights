"""Download the weight files of this repo from its GitHub release and verify them.

    python download.py                 # everything
    python download.py --only <folder> # one variant folder
Standard library only. Honors HTTP(S)_PROXY environment variables.
"""
import argparse, hashlib, json, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAN = json.loads((HERE / "manifest.json").read_text())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="variant folder to download")
    a = ap.parse_args()
    bad = 0
    for e in MAN["files"]:
        if a.only and not e["path"].startswith(a.only.rstrip("/") + "/"):
            continue
        dst = HERE / e["path"]
        if dst.exists() and dst.stat().st_size == e["size"] and sha256(dst) == e["sha256"]:
            print("ok (already there):", e["path"])
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_name(dst.name + ".download")
        h, done = hashlib.sha256(), 0
        with open(tmp, "wb") as out:
            for part in e["parts"]:
                with urllib.request.urlopen(MAN["base_url"] + part) as r:
                    for b in iter(lambda: r.read(1 << 22), b""):
                        out.write(b); h.update(b); done += len(b)
                        print("\r%s  %5.1f%%" % (e["path"], 100 * done / e["size"]), end="", flush=True)
        print()
        if h.hexdigest() != e["sha256"]:
            print("SHA256 MISMATCH:", e["path"]); bad += 1
            continue
        tmp.replace(dst)
        print("ok:", e["path"])
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
