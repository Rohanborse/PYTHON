def get_year_dict():
    year_list = []
    with open("movies_data.txt", 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            year = line.split()[-1].split("::")[0].strip()[1:-1]
            year_list.append(int(year))

    year_dict = {}
    unique_list = list(set(year_list))

    for i in unique_list:
        count = 0
        for j in year_list:
            if i == j:
                count +=1
        year_dict[i] = count
    print(year_dict)

    
def movie_name():
    count = 0
    with open("movies_data.txt","r") as file: 
        while True :
            line = file.readline()
            if line == '':
                break
            movie = line.split("::")[1].strip()
            if movie.startswith("T") or movie.startswith("J"):
                count += 1
        print(count)
    
def yeargener():
    comedy,action = 0,0
    with open("movies_data.txt","r") as file:
        while True :
            line = file.readline()
            if line == '':
                break
            year = line.split()[-1].split("::")[0].strip()[1:-1]
            gener = line.split()[-1].split("::")[1].split("|")
            if year == "1995" and ("Comedy" in gener or "Comedy\n"):
                comedy += 1
            if year == "1993" and ("Action" in gener or "Action\n"):
                action += 1
        return (comedy,action)



def batman():
    count = 0
    with open("movies_data.txt","r") as file:
        while True:
            line = file.readline()
            if line == '':
                break
            name = line.split("::")[1]
            if name.startswith("batman") or name.startswith("Batman") or name.startswith("BATMAN"):
                count += 1
        print(count)
