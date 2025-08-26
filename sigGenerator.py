import sys

if len(sys.argv) != 2:
    print("Usage: python sig_builder.py <king_sig_hex>")
    print("Exemple : python sig_builder.py 0x845d26af2bf391f13bf73290e7f07c2a3e48f495d57765efe1ac8292a723b2782db86e5fc7235ebee11c84d484cd0b801e71b9f46091b")
    sys.exit(1)

king_sig_hex = sys.argv[1]

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

r_hex = king_sig_hex[2:66]
s_hex = king_sig_hex[66:130]
v_hex = king_sig_hex[130:]

s_int = int(s_hex, 16)
v_int = int(v_hex, 16)

s_new = N - s_int
v_new = 27 if v_int == 28 else 28

malleable_sig_hex = f"0x{r_hex}{hex(s_new)[2:]}{hex(v_new)[2:]}"

print(f"Second valid sig : {malleable_sig_hex}")
