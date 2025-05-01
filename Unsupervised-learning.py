1, giới thiệu
Học không giám sát là một nhánh của ML, 
có nhiệm vụ học phân bố của dữ liệu, từ đó có thể biểu diễn dữ liệu hiệu quả hơn

Dữ liệu cho thuật toán học ko giám sát là dữ liệu ko cần gán nhãn,
chỉ cần dữ liệu đầu vào x

một số chủ đề chính:
- Nhóm dữ liệu (clustering): phân nhóm dữ liệu thành các nhóm khác nhau
- Giảm chiều dữ liệu (dimensionality reduction): giảm số chiều của dữ liệu đầu vào


Khái niệm phân bố dữ liệu: là cách mà dữ liệu được phân bố trong không gian nhiều chiều.
Ví dụ: phân phối chuẩn, phân phối đồng đều, phân phối nhị thức, v.v.

Thực tế, thuật toán UL sẽ mã hóa bằng các cluster ID nào đó




2, Các mô hình gom nhóm dữ liệu (clustering)
Gom nhóm (clustering) là bài toán gom các đối tượng theo từng cụm sao cho các đối tượng
trong cùng một cụm có sự tương đồng với nhau hơn so với những đối tượng thuộc các nhóm khác.

một số thuật toán gom nhóm phổ biến:
- K-means clustering: phân chia dữ liệu thành k cụm khác nhau dựa trên khoảng cách Euclidean.
- Hierarchical clustering: xây dựng cây phân cấp các cụm dữ liệu dựa trên khoảng cách giữa các đối tượng.
- DBSCAN: phân cụm dựa trên mật độ của các điểm dữ liệu trong không gian.
- Gaussian Mixture Model (GMM): mô hình hóa dữ liệu bằng cách sử dụng các phân phối Gaussian.
- Spectral clustering: sử dụng thông tin về cấu trúc đồ thị của dữ liệu để phân cụm

mỗi phương pháp có ưu nhược điểm riêng, sử dụng phương pháp nào tùy vào tính chất dữ liệu và mục tiêu cụ thể

-Thuật toán gom nhóm K-means:
    Ý tưởng: khởi tạo ngẫu nhiên K tâm cụm, sau đó gán các điểm dữ liệu vào trọng tâm gần nhất.
    Qúa trình này được lặp lại cho đến khi không còn sự thay đổi trọng tâm nào nữa.
    
    Ưu điểm:
    - Đơn giản và dễ hiểu.
    - Tính toán nhanh chóng và hiệu quả với dữ liệu lớn. (tuy nhiên nếu lớn quá thì sẽ chậm đi nên sẽ cần biến thể như AK means)
    Khuyết điểm:
        - Cần biết trước số cụm K.
        - Dễ bị rơi vào cực tiểu cục bộ (phụ thuộc nhiều vào việc khởi tạo K cụm ban đầu).
        - Phụ thuộc vào tâm cụm khởi tạo.
        - Ko hoạt động tốt với dữ liệu có phân bố phức tạp, ko phải dạng hình cầu.
        
        
        
- Thuật toán gom nhóm DBSCAN:
    Ý tưởng: phân cụm dựa trên mật độ của các điểm dữ liệu trong không gian. gom các điểm gần nhau (có khoảng cách nhỏ hơn epsilon) và
    có mật độ cao (thường được xác định bằng số điểm lân cận tối thiểu minPts).
    Các điểm nằm trong cụm mật độ thấp sẽ được coi là nhiễu (noise).
    
    Ưu điểm: 
    - Không cần biết trước số cụm.
    - Có thể phát hiện các cụm có hình dạng bất kì.
    - Hiệu quả với dữ liệu mật độ cao.
    
    Khuyết điểm:
    - Nhạy cảm với các tham số epsilon và minPts.
    - Không hoạt động tốt với dữ liệu có mật độ biến động, không đồng nhất.
    
    
    
3, Các mô hình giảm chiều dữ liệu (dimensionality reduction)
Giảm chiều dữ liệu là quá trình chuyển đổi dữ liệu từ không gian đa chiều sang ko gian ít chiều sao cho biểu diễn
ko gian ít chiều vẫn giữ được một số tính chất quan trọng của dữ liệu gốc.

Một số thuật toán giảm chiều dữ liệu phổ biến:
- Principal Component Analysis (PCA): tìm các thành phần chính (principal components) của dữ liệu để giảm chiều.
- t-Distributed Stochastic Neighbor Embedding (t-SNE): giảm chiều dữ liệu bằng cách tối ưu hóa khoảng cách giữa các điểm trong không gian thấp chiều. 
    dùng cho dữ liệu có mối qhe phi tuyến tính, với công dụng chính là trực quan hóa dữ liệu

Mỗi phương pháp có những đặc điểm và ứng dụng riêng, tùy thuộc vào tính chất dữ liệu và mục tiêu cụ thể.

1, Kĩ thuật PCA:
    Ý tưởng: tìm các thành phần chính (principal components) của dữ liệu để giảm chiều. chấp nhận
    ko thể khôi phục lại dữ liệu gốc từ dữ liệu đã giảm chiều, nhưng vẫn giữ được các thông tin quan trọng nhất.
    
2, Kĩ thuật t-SNE: là kĩ thuật giảm chiều dữ liệu phi tuyến tính, thường được sử dụng để trực quan hóa dữ liệu
đa chiều trong ko gian có số chiều thấp hơn (thường là 2 hoặc 3 chiều).
    Ý tưởng: tạo ra một phân phối xác suất tương tự trong ko gian có số chiều thấp hơn
    nếu PCA là kĩ thuật dựa vào các phép biến đổi tuyến tính (đại số tt) thì t-SNE là kĩ thuật dựa vào các phép biến đổi phi tuyến tính (hình học)
    
    
    ưu nhược từng pp: SLIDE 06.CS116
    