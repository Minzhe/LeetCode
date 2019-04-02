def fullJustify(words, maxWidth):
    lines, l, chars = [], [], 0
    for word in words:
        if chars + len(l) + len(word) > maxWidth:
            for i in range(maxWidth - chars - len(l) + 1):
                l[i%(len(l)-1 or 1)] += ' '
            lines.append(' '.join(l))
            l, chars = [], 0
        l.append(word)
        chars += len(word)
    return lines + [' '.join(l) + ' '*(maxWidth-len(l)-chars+1)]

res = fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print(res)