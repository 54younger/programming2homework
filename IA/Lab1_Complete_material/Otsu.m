rice = imread("rice.png");
rice_p = count_grey(rice);
rice_h = rice_p * size(rice,1) * size(rice,2); 
perfect = 0;
max = 0;
global_mean = sum(rice_p);
record = zeros(1,255);
for threshold = 0:254
    p_a = sum(rice_p(1:threshold+1));
    p_b = sum(rice_p(threshold+2:256));
    cat_a_sum = value_m_index(rice_h, 1, threshold+1);
    cat_b_sum = value_m_index(rice_h, threshold+2, 256);
    mean_a = cat_a_sum / sum(rice_h(1:threshold+1));
    mean_b = cat_b_sum / sum(rice_h(threshold+2:256));
    variance = p_a * (global_mean - mean_a)^2 + p_b * (global_mean - mean_b)^2;
    record(threshold+1) = variance;
    if (variance > max)
        max = variance;
        perfect = threshold;
    end
end
    


