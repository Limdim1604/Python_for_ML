mô hình phân lớp

1, Xét với mô hình logistic regression:
    hàm mô hình dự đoán: y_ = sigmoid(b_ x) với sigmoid là hàm logistic sigmoid, b_ là vector hệ số hồi quy, x là vector đặc trưng
    hàm độ lỗi dự đoán BCE (Binary Cross Entropy): -1/n tổng[i = 1 đến n]( -yi*log(yi_) - (1-yi)*log(1-yi_))
    với binary cross entropy là hàm độ lỗi đặc biệt (cho phân loại nhị phân) với 
    trường hợp tổng quát của công thức log loss
    chi tiết hơn: https://www.youtube.com/watch?v=UCmTraNX7QA&t=331s
    
    dễ cài đặt, thậm chí trong sklearn có sẵn hàm LogisticRegression
    cũng như ta có thể mở rộng sang bài toán phân loại nhiều lớp (multiclass classification) bằng cách 
    thay vì dùng hàm sigmoid (y = sigmoid(B_ x) thì dùng softmax (softmax là hàm logistic tổng quát cho bài toán phân loại nhiều lớp)
                              
    khuyết điểm mô hình: ko giải quyết đc với dữ liệu phức tạp vd phi tuyến, cũng như nó rất dễ ảnh hưởng bởi outliers 
    
    
2, Xét với mô hình với dữ liệu có quan hệ phi tuyến (Non-linear classification)
    +KNN classifier: là một mô hình phân loại (ko tham số) dựa trên nhãn của K đặc trưng có khoảng cách gần nhất, với K là siêu tham số của mô hình
     (lazy learning: mô hình chả có tham số gì hết mà chỉ đơn giản là nhớ toàn bộ dữ liệu-> tốn bộ nhớ)
     
    + Mô hình Multi Layer Perceptron (MLP)
     MLPClassifier trong sklearn (với bài toán hồi quy thì dùng MLPRegressor)
     MLP classifier: sử dụng thêm các lớp ẩn để học các đặc trưng trung gian, 
     giúp việc ra quyết định dễ hơn với dữ liệu có mối quan hệ phụ thuộc phi tuyến tính với dữ liệu đầu vào 
     bằng cách học các đặc trưng trung gian
     nếu số phân lớp cần phân loại là K thì output sẽ có K cái nơ ron (nếu xét tới bài toán hồi quy ở trước thì output sẽ có 1 cái nơ ron mà ko có hàm kích hoạt để ép miền giá trị về cái khoảng nào đó)
     => tính linh động của mô hình cao
     
     
     
    + Decision Tree: là một cấu trúc phân cấp ko tham số
     mỗi nút đại diện cho một thuộc tính (đặc trưng) 
     mỗi nhánh từ nút đó tương ứng với 1 trong số khả năng có thể xảy ra của thuộc tính đó
     mỗi nút lá (nút cuối cùng) đưa ra quyết định phân loại cuối cùng dựa trên các thuộc tính đã duyệt trước đó
     
     có thể dựa trên dộ đo information gain (IG) để quyết định xem chọn đặc trưng nào để phân loại cho nút tiếp theo
     muốn tính được IG thì cần tính được entropy của tập dữ liệu, entropy thể hiện mức độ đa dạng của các loại đối tượng trong tập S, nếu S chỉ có một loại đối tượng thì entropy(S) = 0
     Entropy(S) = - tổng[i=1 đến n] (p_i * log(p_i)) với p_i là tỉ lệ của nhãn thứ i trong tập S, với n là số đối tượng(số nhãn) trong tập S
     InfoGain = Entropy(Parent) - Expectation[Entropy(Child)] với Expectation[Entropy(Child)] là trung bình (kỳ vọng) của entropy của các lớp con
     
     ngoài info gain ra thì còn có thể dùng các độ đo khác như Gini,...
     
     ưu điểm thuật toán decision tree:
         có thể làm được trên dữ liệu dạng số và dạng phân loại 
         là mô hình phi tham số
         có thể dùng luôn trong bước feature selection (chọn đặc trưng)
        
    khuyết: 
    -dễ overfitting với dữ liệu khi cây ko đc cắt tỉa (pruning) hoặc cây quá sâu (mô hinh quá phức tạp)
    -ko ổn định: nếu thay đổi một chút dữ liệu thì cây sẽ thay đổi hoàn toàn
    => khắc phục bằng kĩ thuật ensemble với ramdom forest (chọn ra ngẫu nhiên tập con của dữ liệu và huấn luyện trên nhiều cây, nếu có cây nào có vấn đề (overfitting) thì cũng ko sao vì nó chỉ là một trong số nhiều cây, cuối cùng thì cũng tạo ra cây có tổng quát hóa cao nhất)
    -khó tối ưu vì việc tìm cây tốn nhiều chi phí tính toán, còn nếu cây mà dựa vào (có dùng) các hàm heuristic thì lại không đảm bảo tối ưu (đánh đổi giữa tốc độ và độ chính xác)
    bias cũng sẽ khiến cho cây có thể tạo ra nhiều nhánh hơn => tương tự dễ overfitting
    CS116 BAI 7B
    
3, một số mô hình phân lớp khác
Support Vector Machine (SVM)
Naive Bayes Classifier (dựa trên kiến thức về thống kê)
Random Forest (xây nhiều cây trên nhiều tập dữ liệu con khác nhau dựa trên cơ chế bagging (thực hiện độc lập trên các cây độc lập))
#     Bagging: là một kĩ thuật ensemble, trong đó nhiều mô hình được huấn luyện trên các tập dữ liệu con khác nhau và sau đó kết hợp lại để tạo ra một mô hình tổng thể mạnh hơn.
Gradient Boosting Classifier 
XGBoost Classifier 
LightGBM Classifier
CatBoost Classifier
(cũng như các nhóm thuật toán về boosting, các nhóm này cho ra độ chính xác rất cao trong các cuộc thi kaggle hơn các mô hình linear vì dữ liệu có mối quan hệ phức tạp (phi tuyến))