# SAM 3 weights

Unmodified copies of Meta's model weights, mirrored for easy download. Upstream: https://github.com/facebookresearch/sam3

**License:** these files are distributed under Meta's SAM License, see [LICENSE](LICENSE).
By downloading or using them you agree to those terms. This mirror does not relicense anything.

## Get the weights

The large files are GitHub release assets (split into parts below 2 GB); small config files are in the repo.

```
git clone https://github.com/SchockTop/sam3-weights.git
cd sam3-weights
python download.py
```

`download.py` (standard library only) fetches the parts, joins them into the folders below and checks the SHA256.
Use `python download.py --only <folder>` for a single variant.

## Contents

- `sam3/`: original `sam3.pt` checkpoint for the Meta `sam3` repo
- `sam3-hf/`: Hugging Face `transformers` format (`model.safetensors` + configs)

| File | Size | SHA256 |
|---|---|---|
| `sam3/sam3.pt` | 3.45 GB | `9999e2341ceef5e136daa386eecb55cb414446a00ac2b55eb2dfd2f7c3cf8c9e` |
| `sam3-hf/model.safetensors` | 3.36 GB | `fb88a9ae6053003f1b7e737170cf2b2158e5cad5ba29ec529c83f25393258774` |

`.pt` / `.pth` files are pickle based: load them with `torch.load(..., weights_only=True)`.
