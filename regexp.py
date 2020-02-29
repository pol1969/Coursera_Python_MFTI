def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)=([abc])?([+-]?\d+)?")
    # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches: 
        tmp = data.get(v2, 0) + int(n or 0)
        if s == "-":
            data[v1] -= tmp
        elif s == "+":
            data[v1] += tmp
        else:
            data[v1] = tmp
            
    return data
