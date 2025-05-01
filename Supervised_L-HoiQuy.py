Học có giám sát- Mô hình Hồi Quy (Regression)

1, mô hình hồi quy tuyến tính (Linear Regression)
    mô hình thực tế y = epsilon + beta*x, với nhiễu tuân theo phân phối chuẩn N (0,1). phải hiểu ở đây x dạng như một vector [1    beta = [b0
                                                                                                                             xi],          b1]
   hàm mô hình dự đoán: y_ = b_ x
   
2, bias và variance

3, Các biến thể khác của linear regression như
3, Mô hình LASSO (L1 regularization), Ridge (L2 regularization), ElasticNet (L1+L2 regularization)
    LASSO: L1 regularization, cố gắng đưa các hệ số tương ứng cho các đặc trưng không quan trọng về 0,
    Ridge: L2 regularization, cố gắng trải đều và dùng hết các đặc trưng chứ ko cố gắng loại bỏ đặc trưng
    ElasticNet: kết hợp cả L1 và L2 regularization,

    lamda: tham số điều chỉnh độ mạnh của regularization, giúp cho argmin nên nghiêng về MSE hay regularization (lamda lớn thì nghiêng về regularization, lamda nhỏ thì nghiêng về MSE)
    
    
    
    ở trên là dùng với bài toán có quan hệ tuyến tính (Linear regression) 
4, mô hình với dữ liệu có quan hệ phi tuyến (Non-linear regression)
    - một số mô hình hồi quy khác
        +vẫn dùng linear regression nhưng với feature engineer (thêm các đặc trưng) 
        (vd đoán được mô hình cần dự đoán làm hàm số bậc 3 thì thay vì trước là X với [1 x]T, giờ là X new [1 x1 x^2 x^3 ]T,
         còn B thì [bo b1 b2 b3]T)
        
        + KNN regressor: dự đoán giá trị của điểm mới bằng cách tìm k điểm gần nhất với nó trong tập huấn luyện, 
         sau đó áp dụng với 2 cách là tính trung bình các giá trị của k điểm đó hoặc tính trung bình trọng số theo khoảng cách (khoảng cách nào mà càng nhỏ thì trọng số càng lớn và ngược lại)
         mô hình này là mô hình học lười ( lazy learning) vì nó ko học gì cả mà chỉ lưu lại các điểm trong tập huấn luyện và khi cần dự đoán thì tìm k điểm gần nhất với nó trong tập huấn luyện,
         vì thế nó rất tốn tài nguyên
         
        + Mạng neutral network (hay multi layer perceptron)
            trong sklearn với bài toán hồi quy thì dùng MLPRegressor, còn với bài toán phân loại thì dùng MLPClassifier
            ngoài ra còn có các mô hình có nguồn gốc từ mô hình phân lớp để phục vụ cho bài toán hồi quy như
            Support Vector Regression (SVR) (gốc là SVM)
            Decision Tree Regressor, 
            Random Forest Regressor, 
            Gradient Boosting Regressor, XGBoost Regressor, LightGBM Regressor, CatBoost Regressor
            chi tiết bài này: https://www.youtube.com/watch?v=B5cpY9SY7CY
            