def fake_bin(x):
    trans = "";
    for c in x:
        i = c.int();
        if i < 5:
            trans += "0";
        else:
            trans += "1";
    return trans;