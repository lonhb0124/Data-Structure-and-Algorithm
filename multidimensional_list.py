


if __name__ == "__main__":
    
    c = 6
    r = 3

    data = ([0] * c) * r        # mistake multidimension list       
    print("data: ", data) 


    data2 = [[0] * c] * r        # still mistake multidimension list
    print(data2) 
    data2[2][0] = 100            #  aliasing
    print(data2)

    correct_data = [[0] * c for j in range(r)]      # multidimension list 
    print(correct_data) 
    correct_data[2][0] = 100
    print(correct_data)

