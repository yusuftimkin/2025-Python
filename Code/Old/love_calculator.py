def calculate_love_score(name1, name2):

    combine_names = name1 + name2
    
    lower_names = combine_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    
    print(f"Total = {t+r+u+e}")
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    
    print(f"Total = {l+o+v+e}")
    
    love_score = str(t+r+u+e) + str(l+o+v+e)
    
    print(f"Love Score = {love_score}")
    
    
calculate_love_score("Kanye West", "Kim Kardashian")