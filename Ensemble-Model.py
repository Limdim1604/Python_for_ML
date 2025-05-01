mô hình tổ hợp là cách nói ví von nhưng nó chưa lột tả được hết nên ta vẫn gọi là ensemble model

1, Tại sao cần có ensemble model?
    giới thiệu về ensemble learning
       mục tiêu máy học: xây dựng mô hình có tính tổng quát cao từ dữ liệu huấn luyện (làm sao cho với 1 tập con dữ liệu vẫn có tính tổng quát cao thay vì làm với toàn bộ dữ liệu)
       
       có hai cách chính để cải thiện tính tổng quát hóa:
           +cải thiện hiệu suất của một máy học (model)
           +kết hợp nhiều mô hình và tổng hợp kết quả dự đoán => ensemble Learning

    tại sao ensemble learning lại hiệu quả?
        +Vấn đề giảm Variance(phương sai): sử dụng nhiều mô hình có thể trung bình giá trị dự đoán gần với giá trị thực tế-> giảm variance -> tránh hiện tượng overfitting
        vd: Thuật toán Random Forest kết hợp nhiều cây quyết định (Decision Tree) để giảm variance của mô hình.(nó cũng có thể coi là một dạng ensemble model)

        +Vấn đề giảm Bias: mỗi mô hình yếu chỉ đoán đúng cho một số tình huống dữ lieeuk, kết hợp nhiều mô hình yếu lại với nhau để tận dụng điểm mạnh của mỗi mô hình, khắc phục những trường hợp mà từng mô hình đoán sai => giảm overfitting
        
2, Kĩ thuật cơ bản: Voting (lấy phiếu bầu), Averaging (trung bình), Weighted Averaging (trung bình có trọng số)
    2.1, Voting: thường dùng cho bài toán phân loại, mỗi mô hình như một "cử tri", quyết định cuối cùng thuộc về số đông
    2.2, Averaging: thường dùng cho bài toán hồi quy, tính trung bình cộng kết quả của từng mô hình để tổng hợp
    2.3, Weighted Averaging: mõi mô hình có hiệu quả/trọng số khác nhau nên có trọng số khác nhau, trọng số được tính dựa trên độ chính xác trên tập train/validation của từng mô hình




3, Kĩ thuật nâng cao: Stacking (xếp chồng), Blending (trộn), Bagging (Bootstrap Aggregating), Boosting
    3.1, Stacking: sử dụng kết quả dự đoán của tập train làm đặc trưng để huấn luyện mô hình tổng hợp (mega learner)
    3.2, Blending: Sử dụng (đặc trưng + kết quả dự đoán của tập validation) hòa trộn lại với nhau để làm đặc trưng huấn luyện mô hình tổng hợp
    3.3, Bagging: Khác với 2 thuật toán trên, Bagging sử dụng cùng một thuật toán cho tất cả các mô hình con 
         bagging huấn luyện độc lập các mô hình con trên các tập con khác nhau của dữ liệu huấn luyện
         điển hình của kĩ thuật này chính là Random Forest
         ưu điểm: tổng quát hóa cao, có thể thực hiện được trên 1 số đặc trưng lớn mà ko cần phân tích đặc trưng,
         linh hoạt dùng cho cả hồi quy và phân lớp, ít bị ảnh hưởng bởi outlier
         nhược: khó giải thích, độ phức tạp tính toán cao, Bias với dữ liệu không cân bằng
    các mô hình điển hình: Random Forest, Bagging SVM, Bagging KNN,...
    
    3.4, Kĩ thuật Boosting: là kĩ thuật mà các mô hình con được huấn luyện tuần tự, mô hình sau sẽ được train dựa theo kết quả của mô hình trước đó để cố gắng sửa các lỗi sai còn lại
    vd: kĩ thuật gradient boost
        ý tưởng: xây dựng chuỗi cây quyết định liên tiếp, cây sau làm giảm sai số dự đoán của các cây trước
        
    Một số thuật toán Boosting phổ biến, đạt giải cao trong các cuộc thi Kaggle đặc biệt là 3 cái cuối:
        + AdaBoost: là thuật toán boosting đầu tiên, nó sử dụng các trọng số để điều chỉnh độ quan trọng của các mẫu trong tập huấn luyện, các mẫu khó dự đoán sẽ có trọng số lớn hơn.
        + Gradient Boosting: là thuật toán boosting phổ biến nhất hiện nay, nó sử dụng gradient descent để tối ưu hóa hàm mất mát của mô hình.
        + XGBoost: là một phiên bản cải tiến của Gradient Boosting, nó sử dụng các kỹ thuật tối ưu hóa để tăng tốc độ huấn luyện và giảm thiểu overfitting.
        + LightGBM: là một phiên bản khác của Gradient Boosting, nó sử dụng cây quyết định theo chiều rộng (leaf-wise) thay vì chiều sâu (depth-wise) để tăng tốc độ huấn luyện và giảm thiểu overfitting.
        + CatBoost: là một phiên bản khác của Gradient Boosting, nó sử dụng các kỹ thuật xử lý dữ liệu phân loại để tăng tốc độ huấn luyện và giảm thiểu overfitting.
        
        tóm lại: Ensemble learning là kĩ thuật quan trọng để mô hình có tính tổng quát cao
          Bagging và Boosting là 2 kĩ thuật nâng cao có tính hiệu quả cao
          trong quá trình sử dụng cần chọn các siêu tham số cho phù hợp bằng pp tinh chỉnh tham số (hyperparameter tuning) như Grid Search, Random Search, Bayesian Optimization,...