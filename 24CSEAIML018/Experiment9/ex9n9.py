def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(name="Kiran",id=101,dept="IT")