function result = value_m_index(array, start_num, end_num)
%VALUE_M_INDEX 此处显示有关此函数的摘要
%   此处显示详细说明
    result = 0;
    for i = start_num : end_num
        result = result + array(i)*i;
    end
    
        
end

