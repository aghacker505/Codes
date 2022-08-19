t = open('poem.txt', 'r')
rd = t.read()
if 'Twinkle' in rd:
    print("Twinkle is present in the poem")

else:
    print("Twinkle is not present in the poem")
t.close()