def print_list(sl:list):
    names = [s.get("name") for s in sl]
    alpha_list = []
    for n in names :
        fl = n.split(" ")
        alpha_list.append(f"{fl[1]}, {fl[0]}")
    alpha_list.sort()
    return "\n".join(alpha_list)

def avg_gpa(sl:list):
    tot_gpa = sum([s.get("gpa") for s in sl])
    return tot_gpa/len(sl)

def high_achievers(sl:list):
    high_gpa = max([s.get("gpa") for s in sl])
    hc = [s.get("name") for s in sl if s.get("gpa") == high_gpa]
    return f"Highest GPA: {high_gpa}\n\n" + "\n".join(hc)