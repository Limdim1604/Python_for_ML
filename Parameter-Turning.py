1, Tại sao phải tinh chỉnh tham số
    tham số trong máy học là gì ?
        -Tham số mô hình (parameter) là các biến số mô hình học từ dữ liệu train, vd: trọng số, bias của một Neural Network
        -Siêu tham số (hyperparameter) là các cấu hình của mô hình trước khi train, vd: số lượng layer `(lớp)`, số neuron(nơ ron) của một lớp trong Neural Network, 
            +được thiết lập thủ công hoặc thông qua quá trình tinh chỉnh siêu tham số
            vd: với KNN classifier thì K là một siêu tham số, với logistic regression thì cái learning rate cùng là một siêu tham số,...
            còn với Naive Bayes classifier thì không có siêu tham số cũng như tham số nào cả
            
            
        tinh chỉnh siêu tham số giúp mô hình đạt được độ chính xác cao hơn, hiệu quả hơn
        overfitting và underfitting: việc chọn siêu tham số ko hợp lý có thể dẫn đến overfitting (quá khớp) hoặc underfitting (thiếu khớp)
        tài nguyên tính toán: siêu tham số ảnh hưởng đến thời gian và tài nguyên tính toán cần thiết để huấn luyện mô hình
        thích ứng với dữ liệu: tinh chỉnh siêu tham số giúp mô hình đc tinh chỉnh để phù hợp nhất với đặc trưng riêng của từng dữ liệu

2, Phương pháp Grid Search (tìm kiếm theo kiểu vét cạn)
    ý tưởng: "vét cạn" tất cả các tổ hợp tham số (siêu tham số) có thể có để tiến hành thử và chọn ra tổ hợp cho kết quả tốt nhất

    ưu nhược: tóm lại là tốn thời gian và tài nguyên tính toán, nhưng lại cho ra kết quả chính xác nhất (nếu có thể), ko kế thừa được các kết quả trước đó,
    
3, Phương pháp Random Search (tìm kiếm theo kiểu ngẫu nhiên)
    ý tưởng: chọn ngẫu nhiên các tổ hợp tham số (siêu tham số) để thử nghiệm, thay vì lấy mẫu đều, sau đó thử nghiệm và chọn ra tổ hợp cho kết quả tốt nhất
    ưu nhược: hiệu quả với ko gian tìm kiếm lớn, bit nếu ko gian tìm kiếm lớn thì khó tìm được điểm tối ưu toàn cục, ko kế thừa được các kết quả trước đó, kết quả ko nhất quán do yếu tố ngẫu nhiên,

4, Phương pháp Bayesian Optimization (tối ưu hóa Bayes)
    Ý tưởng: chiến lược tuần tự (khác độc lập, cóa tính kế thừa) để tìm điểm tối ưu toàn cục của các mô hình dạng black-box
    ưu nhược: kế thừa => giảm số lần thử nghiệm => hiệu quả với ko gian tìm kiếm lớn, có thể kế thừa các kết quả trước đó, pp phức tạp hơn so với 2 pp trước, việc chọn hàm acquistition (hàm thu thập thông tin) ảnh hưởng lớn đến hiệu quả của pp này