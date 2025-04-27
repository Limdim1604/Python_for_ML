để mà chọn lựa được một cái mô hình tốt, phù hợp thì ta phải hiểu bản chất bài toán mình đang muốn giải là gì,
cũng như biết được cách đánh giá kết quả này tốt hơn kết quả kia ntn.

SLIDE

xác thực tính hiệu quả: mô hình có đang đoán chính xác hay chỉ là nhớ dữ liệu
có bị overfitting hay không

độ đo cho bài toán hồi quy
chọn hàm độ lỗi (hàm loss) (cho mô hình khi huấn luyện) (ý huấn luyện ở đây là làm việc với tập train) vd hàm lỗi MSE, MAE
độ đo đánh giá: (sau huấn luyện) (đánh giá trên tập test)
- MAE: mean absolute error
- MSE: mean squared error
- RMSE: root mean squared error
- RAE : relative absolute error
- RSE : relative squared error

độ đo cho bài toán phân loại
chọn hàm độ lỗi (hàm loss) (cho mô hình khi huấn luyện) vd hàm độ lỗi log loss cho trường hợp có nhiều class chứ ko nhất thiết là 2 class
log loss có công thức tổng quát là :
log loss = -1/n * sum(y_i * log(p_i)) : công thức tổng quát cho bài toán phân loại nhiều lớp
log loss = -1/n * sum(y_i * log(p_i) + (1-y_i) * log(1-p_i)) : công thức đặc biệt dành cho bài toán phân loại nhị phân


độ đo đánh giá: (sau huấn luyện) (đánh giá trên tập test)
tại sao ko dùng hàm log loss để làm độ đo đánh giá, tại vì hàm log loss là hàm độ lỗi, không nhất thiết phải dùng để đánh giá tại vì nó khó hiểu với người dùng hoặc khách hàng
mặc dù nó nhanh và hiệu quả

Một giải pháp khác là dùng Jaccard index với công thức: J(Y, Y~) = |Y ∩ Y~| / |Y ∪ Y~| = | Y ∩ Y~| / (|Y| + |Y~| - |Y ∩ Y~|)
VD: Y = [1, 0, 1, 0, 1], Y~ = [1, 1, 0, 0, 1]
J(Y, Y~) = 3 / 5 + 5 - 3 = 3 / 7 = 0.42857
ngoài ra còn có
- accuracy: độ chính xác
- precision: độ chính xác
- recall: độ nhạy
- f1 score: độ chính xác hài hòa

các độ đo đánh giá, hàm độ lỗi trên là cách tính trung bình, thực tế có thể có tính thiên lệch (cái này quan trọng hơn (có trọng số lớn hơn) cái kia)




QUY TRÌNH ĐÁNH GIÁ MÔ HÌNH MÁY HỌC  
1, Tập test là một phần của tập train : ko khách quan, ko có tính tổng quát, dễ overfit
2, Train-Test Split: chia tập dữ liệu thành 2 phần, 1 phần train, 1 phần test : khách quan 1 phần, lỡ tập test tách ra quá dễ hoặc quá khó thì...,
phù hợp với dữ liệu lớn hoặc mô hình quá nặng (vd các deep learning model)
3, K-fold cross validation: chia tập dữ liệu thành k phần, mỗi lần lấy 1 phần làm tập test, còn lại làm tập train, rồi lấy trung bình: khách quan hơn, nhưng tốn thời gian
phù hợp với dữ liệu ít hoặc huấn luyện nhanh