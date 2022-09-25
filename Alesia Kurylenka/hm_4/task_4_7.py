a = "sklskdaskdlasld, 988.  adkahiuwjbzxbjhhjLHh JJSYUBNMNV Hlk>>'??Km asdTTYGV"

a1 = (''.join(filter(str.isalpha, a)))
a1_low = a1.lower()
a1_low_sorted = sorted(a1_low)

a2 = max(a1_low_sorted, key = a1_low_sorted.count)
print(a2)
