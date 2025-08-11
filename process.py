readings = open ("Unihan_Readings.txt").readlines ()
outputs = {}
def numberize (pinyin):
    for r, k in (("a", "āáǎà"), ("o", "ōóǒò"), ("e", "ēéěè"), ("i", "īíǐì"), ("u", "ūúǔù"), ("v", "ǖǘǚǜ")):
        for j, i in enumerate (k):
            if i in pinyin:
                pinyin = pinyin.replace (i, r) + str (j + 1)
    return pinyin.replace ("ü", "v")

chars = {}
pinlu = {}
for i in readings:
    line = i.strip ().split ()
    point = int (line [0] [2 : ], 16)
    if line [1] == "kHanyuPinyin":
        for i in line [2].split (":") [1].split (","):
            chars.setdefault (point, set ()).add (i.strip ())
    elif line [1] == "kMandarin":
        chars.setdefault (point, set ()).add (line [2].strip ())
    elif line [1] == "kHanyuPinlu":
        pinlu.setdefault (point, {})
        for j in line [2 : ]:
            p = j.split ("(") [0].strip ()
            chars.setdefault (point, set ()).add (p)
            pinlu [point] [p] = j.split ("(") [1].split (")") [0].strip ()
for k, v in chars.items ():
    for i in v:
        outputs.setdefault (numberize (i), []).append ((chr (k), int (pinlu [k] [i]) if k in pinlu and i in pinlu [k] else -1))
outputstr = []
for k, v in outputs.items ():
    outputstr.append (k + " " + "".join ([j [0] for j in reversed (sorted (v, key = lambda x: x [1]))]))
with open ("pinyin.txt", "w") as f:
    f.write ("\n".join (outputstr))
