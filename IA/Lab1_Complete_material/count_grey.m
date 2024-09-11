function num = count_grey(I)
    num = zeros(1,256);
    for i = 1 : size(I,1)
        for j = 1 : size(I,2)
            value = I(i,j);
            num(value+1) = num(value+1)+1;
        end
    end
    num = num/(size(I,1)*size(I,2));
end