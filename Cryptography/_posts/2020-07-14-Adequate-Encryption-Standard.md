---
layout: post
title: "Adequate Encryption Standard"
author: "raghul-rajasekar"
---
I wrote my own AES! Can you break it?  
  
hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg==

**Files:**
- [adequate_encryption_standard.py]({{site.baseurl}}/assets/Adequate-Encryption-Standard/adequate_encryption_standard.py)

## Solution

The encryption is done as follows:
```python
def encrypt(plain: bytes, key: bytes) -> bytes:
    blocks = to_blocks(plain)
    out = bytearray()
    key = expand_key(key, len(blocks))
    for idx, block in enumerate(blocks):
        block = pad(block)
        assert len(block) == BLOCK_SIZE
        for _ in range(ROUNDS):
            block = enc_sub(block)
            block = enc_perm(block)
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
        out.extend(block)
    return bytes(out)
```
`enc_sub` substitutes each byte of the block with another byte determined by an internal mapping (which is available to us as the `sbox` list) while `enc_perm` permutes the bits in the block according to a preset permutation in `pbox`. Clearly, both these operations are easily reversible. Now, all we need to do is bypass the "XOR with key" step.

This is also easy, since only one byte of the key is used to encrypt each block. Moreover, the encryption happens in ECB mode, meaning that each block is encrypted independent of the others. Thus, for each block, we can enumerate through 256 possibilities for `key[idx]` corresponding to that block and check which decrypted blocks have all printable characters only. Thus, the total number of decryptions we attempt is at most `256*len(blocks)`. The code to achieve this would go something like this:

```python
for block in blocks: 
    for key in range(256): 
        _block = block 
        for _ in range(8): 
            _block = bytearray(_block) 
            for i in range(len(_block)): 
                _block[i] ^= key 
            _block = rev_perm(_block)	# reverses bit permutation
            _block = rev_sub(_block)	# reverses byte substitution
        try: 
            _block = _block.decode() 
            if all([(c in string.printable) for c in _block]): 
                print(block, _block) 
        except Exception: 
            continue
```

## Flag

`rgbCTF{brut3_f0rc3_is_4LW4YS_th3_4nsw3r(but_with_0ptimiz4ti0ns)}`

