rice = imread("rice.png");
rice_his = imhist(rice);





figure;
bar(rice_his);
title('Histogram of rice');
xlim([0 255]);