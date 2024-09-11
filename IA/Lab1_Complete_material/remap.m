function I1 = remap(I, maplist)
    I1 = zeros(size(I,1),size(I,2));
    I1 = im2uint8(I1);
    for i = 1 : size(I,1)
        for j = 1 : size(I,2)
            I1(i,j) = maplist(I(i,j) + 1);
        end
    end
end