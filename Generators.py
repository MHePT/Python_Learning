# Recommended:
def f(x): return 3*x


# Not recommended:
f = lambda x: 3*x

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))



class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Yes, we know that y is not always considered a vowel.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
    


short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

