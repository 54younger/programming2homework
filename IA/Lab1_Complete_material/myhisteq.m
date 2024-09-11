    
I0 = imread("images\greytoys.png");
I0 = imread("rice.png");
h0 = imhist(I0);
P0 = count_grey(I0);
Pcdf0 = cumsum(P0);
maplist = round(Pcdf0*255);
I1 = remap(I0, maplist);
h1 = imhist(I1);
P1 = count_grey(I1);
Pcdf1 = cumsum(P1);

figure;
subplot(3, 2, 1);
imshow(I0);
title('Image I0');

subplot(3, 2, 2);
imshow(I1);
title('Image I1');

subplot(3, 2, 3);
bar(h0);
title('Histogram of I0');
xlim([0 255]);

subplot(3, 2, 4);
bar(h1);
title('Histogram of I1');
xlim([0 255]);
subplot;

subplot(3, 2, 5);
bar(Pcdf0);
title('CDF of I0');
xlim([0 255]);
subplot;

subplot(3, 2, 6);
bar(Pcdf1);
title('CDF of I1');
xlim([0 255]);
subplot;