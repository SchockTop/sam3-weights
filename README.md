# SAM 3 weights

Unmodified copies of Meta's model weights, stored directly in this git repository. Upstream: https://github.com/facebookresearch/sam3

**License:** these files are distributed under Meta's SAM License, see [LICENSE](LICENSE).
By downloading or using them you agree to those terms. This mirror does not relicense anything.

## Get the weights

Everything is in the repo itself (no releases, no Git LFS). GitHub allows at most 100 MB per file,
so each large file is stored as `<name>.part000`, `<name>.part001`, ... next to its config files.

```
git clone --depth 1 https://github.com/SchockTop/sam3-weights.git
cd sam3-weights
python join.py
```

`join.py` works offline (standard library only): it joins the parts into the model files below and checks
the SHA256. `python join.py --only <folder>` joins one variant, `--delete-parts` frees the space afterwards.

Without Python, join by hand and compare the SHA256 with the table:

```
:: Windows (cmd)
copy /b "sam3\sam3.pt.part*" "sam3\sam3.pt"
certutil -hashfile "sam3\sam3.pt" SHA256

# Linux / macOS
cat sam3/sam3.pt.part* > sam3/sam3.pt && sha256sum sam3/sam3.pt
```

## Contents

- `sam3/`: original `sam3.pt` checkpoint for the Meta `sam3` repo
- `sam3-hf/`: Hugging Face `transformers` format (`model.safetensors` + configs)

| File | Size | Parts | SHA256 |
|---|---|---|---|
| `sam3/sam3.pt` | 3.45 GB | 35 | `9999e2341ceef5e136daa386eecb55cb414446a00ac2b55eb2dfd2f7c3cf8c9e` |
| `sam3-hf/model.safetensors` | 3.36 GB | 34 | `fb88a9ae6053003f1b7e737170cf2b2158e5cad5ba29ec529c83f25393258774` |

`.pt` / `.pth` files are pickle based: load them with `torch.load(..., weights_only=True)`.
