def get_freq(text):
    d = {}
    words = text.lower().replace(',', '').replace('.', '').split()
    
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
            
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

test_text = "Data analysis is the process of inspecting, cleansing, transforming, and modeling data"
print(get_freq(test_text))
