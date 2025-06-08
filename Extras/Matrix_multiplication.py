def matrix_multiplication(mat1,mat2):
    r1,c1=len(mat1),len(mat1[0])
    r2,c2=len(mat2),len(mat2[0])
    result= [[0]*c1 for _ in range(r2)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j]+=mat1[i][k]*mat2[k][j]
    return result


mat1=[[1,2],[5,3]]
mat2=[[2,3],[4,1]]

if len(mat1)!=len(mat2[0]):
    print("Give valid input!")

print(f"Matrix Maltiplication{matrix_multiplication(mat1,mat2)}")


